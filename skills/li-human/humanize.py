#!/usr/bin/env python3
"""
humanize.py - tira a impressão digital de máquina de um rascunho.
Versão adaptada para português do Brasil.

Três passadas, nesta ordem:

  1. INVISÍVEIS   apaga ou normaliza caracteres que um teclado humano nunca
                  produz: zero-width joiners, word joiners, hífens suaves,
                  BOMs, caracteres Unicode de tag, espaços rígidos e estreitos.
                  Eles sobrevivem ao copiar e colar e são o sinal mais
                  mecânico de qualquer texto gerado.
  2. TIPOGRAFIA   travessão -> vírgula, meia-risca -> hífen, aspas curvas ->
                  retas, reticências -> três pontos, marcador -> hífen.
  3. LÉXICO       troca o vocabulário batido do slop.json por palavras simples,
                  preservando maiúsculas e sem mexer em URLs.

Estruturas denunciadoras (regra de três, "não é só X, é Y", muro de hashtags)
são APONTADAS, nunca reescritas automaticamente - mudar o formato de uma frase
exige julgamento, então isso é trabalho do modelo, não de uma regex.

Adaptações para pt-BR em relação ao original (MIT, Jake Schincariol):
  - conserto de frases emendadas usa conectivos em português;
  - frase que perde a abertura ("Vale ressaltar que...") volta a começar com
    letra maiúscula;
  - "Também," solto no início de frase (sobra de "Além disso,") é removido;
  - opção --keep-dash para manter o travessão, que é pontuação legítima em
    português;
  - caracteres especiais escritos como escapes Unicode.

Uso
  python3 humanize.py rascunho.txt
  python3 humanize.py rascunho.txt --report
  pbpaste | python3 humanize.py - --report
  python3 humanize.py rascunho.txt --json
  python3 humanize.py rascunho.txt -o limpo.txt
  python3 humanize.py rascunho.txt --keep-dash
"""

import argparse
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

URL_RE = re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+")
SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")

EM_DASH = "\u2014"
EN_DASH = "\u2013"
LOWER = "a-zß-öø-ÿ"


def load_lexicon(path=LEX):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _cp(spec):
    """'U+200B' -> 0x200B;  'U+E0000-U+E007F' -> (inicio, fim)."""
    if "-" in spec:
        a, b = spec.split("-")
        return (int(a[2:], 16), int(b[2:], 16))
    return int(spec[2:], 16)


def protect_urls(text):
    """Troca URLs por marcadores para nenhuma passada mexer dentro de um link."""
    found = []

    def stash(m):
        found.append(m.group(0))
        return f"\x00URL{len(found) - 1}\x00"

    return URL_RE.sub(stash, text), found


def restore_urls(text, found):
    for i, url in enumerate(found):
        text = text.replace(f"\x00URL{i}\x00", url)
    return text


def pass_invisible(text, lex):
    """Apaga ou transforma em espaço os caracteres invisíveis. Retorna (texto, ocorrências)."""
    hits = []
    for entry in lex["invisible"]:
        cp = _cp(entry["cp"])
        if isinstance(cp, tuple):
            pattern = "[" + re.escape(chr(cp[0])) + "-" + re.escape(chr(cp[1])) + "]"
        else:
            pattern = re.escape(chr(cp))
        n = len(re.findall(pattern, text))
        if n:
            hits.append({"name": entry["cp"] + " " + entry["name"], "count": n,
                         "action": entry["action"]})
            text = re.sub(pattern, "" if entry["action"] == "delete" else " ", text)
    # Qualquer caractere de formatação (Cf) restante é invisível por definição.
    stray = [c for c in text if unicodedata.category(c) == "Cf"]
    if stray:
        hits.append({"name": "outros caracteres invisíveis de formatação", "count": len(stray),
                     "action": "delete"})
        text = "".join(c for c in text if unicodedata.category(c) != "Cf")
    return text, hits


def pass_typographic(text, lex, keep_dash=False):
    hits = []
    for entry in lex["typographic"]:
        ch = entry["from"]
        if keep_dash and ch == EM_DASH:
            continue
        n = text.count(ch)
        if not n:
            continue
        hits.append({"name": f"{ch} {entry['name']}", "count": n, "to": entry["to"].strip() or "(espaço)"})
        if ch == EM_DASH:
            # " palavra — palavra " e "palavra—palavra" viram vírgula + espaço.
            text = re.sub(r"\s*" + EM_DASH + r"\s*", ", ", text)
        elif ch == EN_DASH:
            text = re.sub(r"\s*" + EN_DASH + r"\s*(?=\d)", "-", text)   # 5–10 -> 5-10
            text = re.sub(r"\s+" + EN_DASH + r"\s+", ", ", text)         # usada como travessão
            text = text.replace(EN_DASH, "-")
        else:
            text = text.replace(ch, entry["to"])
    # Vírgula inserida antes de outra pontuação fica errada.
    text = re.sub(r",\s*([,.;:!?])", r"\1", text)
    text = re.sub(r",\s*\n", "\n", text)
    return text, hits


def _match_case(src, repl):
    if not repl:
        return repl
    if src.isupper() and len(src) > 1:
        return repl.upper()
    if src[0].isupper():
        return repl[0].upper() + repl[1:]
    return repl


def _capitalize_sentences(text):
    """Volta a maiúscula no início de linha e depois de . ! ? (mas não depois de ...)."""
    text = re.sub(rf"(?m)^([{LOWER}])", lambda m: m.group(1).upper(), text)
    text = re.sub(rf"((?<!\.\.)[.!?]\s+)([{LOWER}])",
                  lambda m: m.group(1) + m.group(2).upper(), text)
    return text


def pass_lexical(text, lex):
    """Troca palavras e expressões batidas. As mais longas primeiro, para as expressões vencerem."""
    hits = []
    entries = sorted(lex["phrases"] + lex["words"],
                     key=lambda e: len(e["find"]), reverse=True)
    for entry in entries:
        find = entry["find"]
        pattern = re.compile(r"\b" + re.escape(find).replace(r"\ ", r"\s+") + r"\b",
                             re.IGNORECASE)
        found = pattern.findall(text)
        if not found:
            continue
        hits.append({"find": find, "replace": entry["replace"] or "(apagado)",
                     "count": len(found), "family": entry["family"]})
        text = pattern.sub(lambda m: _match_case(m.group(0), entry["replace"]), text)
    if not hits:
        return text, hits
    # Limpeza depois das remoções.
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"(?m)^[ \t]*([,.;:])\s*", "", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r"(?m)^[ \t]+$", "", text)
    text = re.sub(r"(?m)^[ \t]+(?=\S)", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Travessão que virou vírgula, seguido de conectivo, deixa a frase emendada
    # ("é importante, assim, os dados..."). Promove a ponto final.
    text = re.sub(r",\s*(também|assim|por isso|no fundo|enfim)\s*,\s*",
                  lambda m: ". " + m.group(1)[0].upper() + m.group(1)[1:] + ", ", text,
                  flags=re.IGNORECASE)
    # "Também," solto no início de frase (sobra de "Além disso,") soa estranho
    # em português: remove.
    text = re.sub(r"(^|[.!?]\s+)Também,\s*", r"\1", text, flags=re.MULTILINE)
    text = _capitalize_sentences(text)
    return text, hits


def scan_structures(text, lex):
    flags = []
    for s in lex["structures"]:
        try:
            pattern = re.compile(s["regex"], re.MULTILINE)
        except re.error:
            continue
        found = pattern.findall(text)
        if found:
            flags.append({"name": s["name"], "count": len(found), "fix": s["fix"]})
    # Uniformidade no tamanho das frases também é estrutural.
    lens = [len(s.split()) for s in SENT_RE.findall(text) if len(s.split()) > 2]
    if len(lens) >= 4:
        mean = sum(lens) / len(lens)
        var = sum((n - mean) ** 2 for n in lens) / len(lens)
        cv = (var ** 0.5) / mean if mean else 0
        if cv < 0.35:
            flags.append({
                "name": f"Frases de tamanho uniforme (variação {cv:.2f})",
                "count": len(lens),
                "fix": "Corte uma frase ao meio. Deixe outra se estender. Máquina escreve tudo igual.",
            })
    return flags


def humanize(text, lex, keep_dash=False):
    text, urls = protect_urls(text)
    text, inv = pass_invisible(text, lex)
    text, typo = pass_typographic(text, lex, keep_dash=keep_dash)
    text, lexi = pass_lexical(text, lex)
    text = restore_urls(text, urls)
    return text.strip() + "\n", {
        "invisible": inv,
        "typographic": typo,
        "lexical": lexi,
        "structures": scan_structures(text, lex),
    }


def render_report(report, out=sys.stderr):
    def head(title):
        print(f"\n{title}\n" + "-" * len(title), file=out)

    total = sum(h["count"] for h in report["invisible"]) \
        + sum(h["count"] for h in report["typographic"]) \
        + sum(h["count"] for h in report["lexical"])

    head("RELATÓRIO DE HUMANIZAÇÃO")
    print(f"{total} marca(s) de máquina removida(s), "
          f"{len(report['structures'])} estrutura(s) denunciadora(s) apontada(s) para reescrita", file=out)

    if report["invisible"]:
        head("1. CARACTERES INVISÍVEIS")
        for h in report["invisible"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['action']}", file=out)
    if report["typographic"]:
        head("2. TIPOGRAFIA")
        for h in report["typographic"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['to']}", file=out)
    if report["lexical"]:
        head("3. LÉXICO BATIDO")
        for h in report["lexical"]:
            print(f"  {h['count']:>3}x  {h['find']}  -> {h['replace']}   [{h['family']}]", file=out)
    if report["structures"]:
        head("4. ESTRUTURAS DENUNCIADORAS  (não corrigidas automaticamente - reescreva você)")
        for h in report["structures"]:
            print(f"  {h['count']:>3}x  {h['name']}\n        {h['fix']}", file=out)
    if not any(report.values()):
        head("LIMPO")
        print("  Nada para remover.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Tira a impressão digital de máquina de um rascunho.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo, ou - para stdin")
    ap.add_argument("-o", "--out", help="grava o texto limpo aqui em vez de mostrar na tela")
    ap.add_argument("--report", action="store_true", help="mostra o que mudou (em stderr)")
    ap.add_argument("--json", action="store_true", help="emite {text, report} em JSON")
    ap.add_argument("--lexicon", default=LEX, help="caminho do slop.json")
    ap.add_argument("--keep-dash", action="store_true", help="mantém o travessão (—) em vez de trocar por vírgula")
    args = ap.parse_args()

    if args.input == "-":
        raw = sys.stdin.read()
    else:
        with open(args.input, encoding="utf-8") as fh:
            raw = fh.read()
    lex = load_lexicon(args.lexicon)
    clean, report = humanize(raw, lex, keep_dash=args.keep_dash)

    if args.json:
        print(json.dumps({"text": clean, "report": report}, indent=2, ensure_ascii=False))
        return
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(clean)
        print(f"gravado em {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(clean)
    if args.report:
        render_report(report)


if __name__ == "__main__":
    main()
