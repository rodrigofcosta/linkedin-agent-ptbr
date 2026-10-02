#!/usr/bin/env python3
"""
detect.py - painel de cinco checagens que pontua o quanto um rascunho parece
escrito por máquina. Versão adaptada para português do Brasil.

O que isto é:  cinco heurísticas locais, modeladas nos sinais que os
detectores públicos de IA de fato medem - variação no tamanho das frases,
concretude, vocabulário batido, impressão digital tipográfica e voz. Toda nota
é calculada na sua máquina, só a partir do texto. Nada é enviado.

O que isto NÃO é:  GPTZero, Originality, Copyleaks, Winston ou Turnitin.
Não chama as APIs deles e não pode prometer o veredito deles. Ele pega o que
todos eles observam, por isso corrigir esses pontos costuma mexer nas notas
deles também - mas a única afirmação honesta é a desta linha.

Cada checagem retorna uma nota HUMANA de 0 a 100. Quanto maior, melhor.

Adaptações para pt-BR em relação ao original (MIT, Jake Schincariol):
  - palavras com acento e hífen são contadas corretamente;
  - nomes próprios com inicial acentuada (Ângela, Éder) e siglas (IBGE,
    ANEEL) contam como marcas concretas;
  - valores em reais (R$ 1.500) contam como números;
  - contrações do inglês foram trocadas por marcas de oralidade do português
    (pra, pro, tá, tô, né, a gente...);
  - pronomes do inglês foram trocados pelos do português, com limites menores,
    porque o português omite o sujeito ("fiz", "aprendi");
  - caracteres especiais escritos como escapes Unicode, para não serem
    confundidos com espaços comuns ao copiar o arquivo.

Uso
  python3 detect.py rascunho.txt
  pbpaste | python3 detect.py -
  python3 detect.py rascunho.txt --json
  python3 detect.py antes.txt depois.txt      # compara dois rascunhos
"""

import argparse
import json
import os
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")

# Qualquer letra (inclusive acentuada), permitindo hífen e apóstrofo internos:
# "trata-se", "guarda-chuva", "d'água".
WORD_RE = re.compile(r"[^\W\d_]+(?:['\-][^\W\d_]+)*")

# Marcas de oralidade: o equivalente, em português, às contrações do inglês.
INFORMAL = re.compile(
    r"\b(?:pra|pras|pro|pros|tá|tô|tava|tavam|né|cê|ocê|a gente|num|numa|"
    r"dum|duma|daí|aí|tipo assim|beleza|valeu|bora)\b",
    re.IGNORECASE,
)

# Pronomes pessoais e possessivos de 1a e 2a pessoa. "nos" ficou de fora porque
# na maioria das vezes é contração (em + os: "nos dias de hoje").
PRONOUNS = re.compile(
    r"\b(?:eu|me|mim|comigo|meu|minha|meus|minhas|nós|conosco|nosso|nossa|"
    r"nossos|nossas|a gente|você|vocês|te|ti|contigo|seu|sua|seus|suas|"
    r"teu|tua|teus|tuas)\b",
    re.IGNORECASE,
)

# Números, percentuais e valores em dinheiro (R$, US$, $).
NUMBERS = re.compile(r"\b\d[\d.,]*%?|(?:R|US)?\$\s?\d")

# Palavras com inicial maiúscula (inclusive acentuada) que não estão no início
# de frase nem de linha: aproximação de nomes próprios.
UPPER = "A-ZÀ-ÖØ-Þ"
LOWER = "a-zß-öø-ÿ"
PROPER = re.compile(
    rf"(?<![.!?]\s)(?<!^)\b[{UPPER}][{LOWER}]{{2,}}\b", re.MULTILINE
)

# Siglas (IBGE, ANEEL, APPs, LT): muito comuns em post técnico brasileiro e tão
# concretas quanto um nome próprio.
ACRONYM = re.compile(rf"\b[{UPPER}]{{2,}}s?\b")

# Caracteres tipográficos, escritos como escapes para não se perderem.
EM_DASH = "\u2014"
CURLY = "\u2018\u2019\u201c\u201d\u00ab\u00bb"
ELLIPSIS = "\u2026"
HARD_SPACES = "\u00a0\u202f\u2009"


def clamp(n):
    return max(0.0, min(100.0, n))


def scale(value, human, machine):
    """Mapeia o valor em 0-100, onde `human` -> 100 e `machine` -> 0."""
    if human == machine:
        return 50.0
    return clamp((value - machine) / (human - machine) * 100)


def sentences(text):
    return [s.strip() for s in SENT_RE.findall(text) if len(s.split()) > 2]


def words(text):
    return WORD_RE.findall(text)


def check_burstiness(text):
    """Humanos variam muito o tamanho das frases. Modelos escrevem por igual."""
    lens = [len(s.split()) for s in sentences(text)]
    if len(lens) < 4:
        return 50.0, "curto demais para avaliar"
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0
    score = scale(cv, human=0.70, machine=0.22)
    return score, f"variação {cv:.2f} em {len(lens)} frases (ideal 0.55+)"


def check_specificity(text):
    """Números, nomes e marcas concretas. Texto genérico é abstrato."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "curto demais para avaliar"
    per100 = 100 / len(w)
    hits = (len(NUMBERS.findall(text))
            + len(set(PROPER.findall(text)))
            + len(set(ACRONYM.findall(text))))
    density = hits * per100
    score = scale(density, human=6.0, machine=0.5)
    return score, f"{hits} marcas concretas, {density:.1f} a cada 100 palavras (ideal 4+)"


def check_slop(text, lex):
    """Densidade de vocabulário batido, segundo o léxico."""
    w = words(text)
    if not w:
        return 50.0, "vazio"
    hits, found = 0, []
    for entry in lex["words"] + lex["phrases"]:
        pattern = re.compile(r"\b" + re.escape(entry["find"]).replace(r"\ ", r"\s+") + r"\b",
                             re.IGNORECASE)
        n = len(pattern.findall(text))
        if n:
            hits += n
            found.append(entry["find"])
    density = hits * 100 / len(w)
    score = scale(density, human=0.0, machine=4.0)
    detail = f"{hits} termos batidos, {density:.1f} a cada 100 palavras"
    if found:
        detail += " (" + ", ".join(sorted(found)[:4]) + (", ..." if len(found) > 4 else "") + ")"
    return score, detail


def check_fingerprint(text):
    """Caracteres que um teclado de celular não produz."""
    invisible = sum(1 for c in text if unicodedata.category(c) == "Cf")
    em = text.count(EM_DASH)
    curly = sum(text.count(c) for c in CURLY)
    ellip = text.count(ELLIPSIS)
    nbsp = sum(text.count(c) for c in HARD_SPACES)
    total = invisible * 4 + em * 2 + curly + ellip + nbsp
    per1k = total * 1000 / max(len(text), 1)
    score = scale(per1k, human=0.0, machine=12.0)
    detail = (f"{invisible} invisível(is), {em} travessão(ões), {curly} aspa(s) curva(s), "
              f"{ellip} reticência(s), {nbsp} espaço(s) rígido(s)")
    return score, detail


def check_voice(text, lex):
    """Oralidade, pessoa e as estruturas que os modelos usam por padrão."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "curto demais para avaliar"
    per100 = 100 / len(w)
    informal = len(INFORMAL.findall(text)) * per100
    person = len(PRONOUNS.findall(text)) * per100
    tells = 0
    names = []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"], re.MULTILINE).findall(text))
        except re.error:
            continue
        if n:
            tells += n
            names.append(s["id"])
    bullets = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*\u2022]\s+(.+)$", text)]
    uniform = (len(bullets) >= 3 and statistics.pstdev(bullets) < 1.6)
    # Pesos ajustados para o português: oralidade pesa menos, porque post
    # profissional em português costuma ser mais formal que em inglês.
    score = (scale(informal, human=1.5, machine=0.0) * 0.20
             + scale(person, human=5.0, machine=0.5) * 0.45
             + clamp(100 - tells * 22) * 0.35)
    if uniform:
        score -= 12
        names.append("bullets-uniformes")
    detail = (f"{informal:.1f} marcas de oralidade, {person:.1f} pronomes pessoais "
              f"a cada 100 palavras, {tells} estrutura(s) denunciadora(s)")
    if names:
        detail += " [" + ", ".join(names[:4]) + "]"
    return clamp(score), detail


CHECKS = ["BURSTINESS", "SPECIFICITY", "SLOP DENSITY", "FINGERPRINT", "VOICE"]


def run(text, lex):
    results = {}
    results["BURSTINESS"] = check_burstiness(text)
    results["SPECIFICITY"] = check_specificity(text)
    results["SLOP DENSITY"] = check_slop(text, lex)
    results["FINGERPRINT"] = check_fingerprint(text)
    results["VOICE"] = check_voice(text, lex)
    scores = [results[c][0] for c in CHECKS]
    # A checagem mais fraca puxa o veredito: um detector só precisa de um sinal.
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4
    verdict = "PASS" if overall >= 70 and min(scores) >= 55 else (
        "REVIEW" if overall >= 50 else "FLAGGED")
    return results, overall, verdict


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render(results, overall, verdict, label=None, out=sys.stdout):
    title = "PAINEL DE DETECÇÃO DE IA" + (f"  -  {label}" if label else "")
    print("\n" + title, file=out)
    print("=" * max(len(title), 62), file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<13} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<13} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'HUMAN SCORE':<13} {bar(overall)} {overall:5.1f}   {verdict}", file=out)
    if verdict != "PASS":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Sinal mais fraco: {weakest}. Corrija esse primeiro.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Pontua o quanto um rascunho parece escrito por máquina.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo, ou - para stdin")
    ap.add_argument("compare", nargs="?", help="segundo arquivo, para comparar antes/depois")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lexicon", default=LEX)
    args = ap.parse_args()

    with open(args.lexicon, encoding="utf-8") as fh:
        lex = json.load(fh)

    def read(p):
        if p == "-":
            return sys.stdin.read()
        with open(p, encoding="utf-8") as fh:
            return fh.read()

    targets = [(args.input, read(args.input))]
    if args.compare:
        targets.append((args.compare, read(args.compare)))

    payload = []
    for name, text in targets:
        results, overall, verdict = run(text, lex)
        payload.append({
            "source": name,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "human_score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if args.compare else payload[0], indent=2, ensure_ascii=False))
        return

    for (name, text), p in zip(targets, payload):
        results, overall, verdict = run(text, lex)
        render(results, overall, verdict, label=os.path.basename(name) if args.compare else None)
    if args.compare:
        a, b = payload
        delta = b["human_score"] - a["human_score"]
        print(f"  {a['human_score']:.1f} {a['verdict']}  ->  "
              f"{b['human_score']:.1f} {b['verdict']}   ({delta:+.1f})\n")

    sys.exit(0 if payload[-1]["verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
