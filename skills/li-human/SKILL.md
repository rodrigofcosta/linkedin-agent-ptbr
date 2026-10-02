---
name: li-human
description: >-
  Tira a impressão digital de máquina de qualquer rascunho em português -
  travessões, vocabulário batido de IA, caracteres invisíveis - e pontua o
  texto num painel de cinco checagens antes de ele sair. Use sempre que um
  texto precisar soar humano, quando o usuário disser "humaniza", "isso parece
  IA?", "tira os travessões", "limpa esse texto", "vai ser detectado?",
  "humanize", "does this sound like AI", ou antes de mostrar ao usuário qualquer
  post, comentário, resposta ou DM do LinkedIn.
---

# li-human

Esta pasta tem duas ferramentas, e as duas rodam de verdade. Use-as. Não
avalie no olho.

```bash
python3 humanize.py rascunho.txt --report        # limpa e mostra o que mudou
python3 detect.py rascunho.txt                   # pontua, cinco checagens
python3 detect.py antes.txt depois.txt           # comprova a diferença
```

As duas leem o `slop.json`, que é o léxico em português do Brasil: mais de
130 palavras e expressões batidas com substituições simples (respeitando
gênero e número), 17 classes de caracteres invisíveis, 13 substituições
tipográficas e 11 estruturas denunciadoras. Ele foi feito para ser editado. Se
o usuário tem uma palavra que sempre usa e que o léxico remove, tire-a do
arquivo.

Alguns termos ficaram fora do léxico de propósito, porque têm uso técnico
legítimo: "ecossistema" e "divisor de águas" (geografia, hidrologia),
"transformador" (setor elétrico), "jornada" sozinha (jornada de trabalho). Não
os trate como vício de IA quando aparecerem no sentido técnico.

## O que é corrigido automaticamente

**1. Caracteres invisíveis.** Zero-width spaces e joiners, word joiners,
hífens suaves, BOMs, caracteres Unicode de tag, espaços rígidos e estreitos.
Teclado não produz esses caracteres. Eles sobrevivem ao copiar e colar, são
invisíveis em qualquer editor e são o sinal mais mecânico de texto gerado. O
`humanize.py` apaga todos, inclusive qualquer caractere de formatação Unicode
que ele não conheça pelo nome.

**2. Tipografia.** Travessão vira vírgula, meia-risca vira hífen, aspas curvas
e angulares viram retas, o caractere de reticências vira três pontos, marcador
vira hífen. A passada do travessão é a que mais importa: ela transforma ` — `
em `, ` e depois limpa a pontuação dupla que sobra.

Em português o travessão é pontuação legítima. Se o `voice.md` do usuário
disser que ele usa travessão, ou se ele pedir para mantê-lo, rode com
`--keep-dash`. Nesse caso o FINGERPRINT do `detect.py` vai cair um pouco, e
isso é esperado: avise o usuário em vez de remover o travessão por conta
própria.

**3. O léxico batido.** alavancar, robusto, inovador, crucial, sinergia,
holístico, "além disso", "vale ressaltar que", "no cenário atual", "em
constante evolução", "minha jornada", "fica a reflexão" e o resto, cada um
trocado por uma palavra simples, com maiúsculas preservadas e URLs intactas.
Quando uma abertura é apagada, a frase seguinte volta a começar com
maiúscula.

## O que NÃO é corrigido automaticamente

Estruturas denunciadoras são **apontadas, não reescritas**, porque mudar o
formato de uma frase exige julgamento:

- "Não é só X, é Y" e "não só X, mas também Y"
- "Não é sobre X. É sobre Y."
- Tríades (regra de três)
- Pergunta retórica de uma linha só: "O resultado?", "O segredo?"
- "Eis o que aprendi"
- Emoji de foguete, fogo, lâmpada, brilho e alvo
- Muro de hashtags
- Isca de engajamento automática: "Concorda?", "O que você acha?", "E você?",
  "Faz sentido?"
- Frases de tamanho uniforme e bullets de tamanho uniforme

Essa lista é trabalho seu. Reescreva cada linha apontada à mão, mantendo o
sentido, e rode o `detect.py` de novo. É essa parte que leva a nota de REVIEW
para PASS, e é a parte que um script não consegue fazer.

## As cinco checagens

O `detect.py` pontua cinco sinais de 0 a 100. Quanto maior, mais humano:

| checagem | o que mede | como fica quando é máquina |
| --- | --- | --- |
| BURSTINESS | variação no tamanho das frases | toda frase do mesmo tamanho |
| SPECIFICITY | números, nomes, siglas e valores (R$) a cada 100 palavras | substantivos abstratos, nenhum dado |
| SLOP DENSITY | ocorrências do léxico a cada 100 palavras | vocabulário batido |
| FINGERPRINT | invisíveis, travessões e aspas curvas a cada mil caracteres | tipografia perfeita demais |
| VOICE | marcas de oralidade (pra, tá, a gente), pronomes pessoais, estruturas denunciadoras | impessoal, revelações encenadas |

Os nomes das checagens e os vereditos (PASS, REVIEW, FLAGGED) ficam em inglês
na saída do script. Ao falar com o usuário, explique em português.

Na VOICE, a oralidade pesa pouco de propósito: post profissional em português
costuma ser mais formal, e um texto bem escrito sem gíria não deve ser punido.
Não encha um texto de "pra" e "né" só para subir a nota. O que mais move a
VOICE é escrever em primeira pessoa e eliminar as estruturas denunciadoras.

O veredito dá peso de 60% à média e 40% à **checagem mais fraca**, porque um
detector só precisa de um sinal para disparar. PASS exige nota geral 70+ e
nenhuma checagem abaixo de 55.

## Diga isto com honestidade

São cinco heurísticas locais, modeladas nos sinais que os detectores públicos
observam. Rodam inteiramente na máquina do usuário e nada é enviado. **Não**
são GPTZero, Originality, Copyleaks, Winston ou Turnitin, não chamam essas
APIs e não podem prometer o veredito deles. Corrigir o que elas medem tende a
mexer nas notas desses serviços, porque todos medem as mesmas coisas de fundo.
Essa é a afirmação. Não faça uma maior em nome do usuário e nunca diga que um
texto é indetectável.

Também nunca invente números, clientes ou resultados para subir a
SPECIFICITY. Se o texto precisa de um dado que o usuário não deu, deixe
`{{seu número}}` no lugar e avise.

## Ordem das operações

1. `humanize.py rascunho.txt -o limpo.txt --report`
2. Leia as estruturas apontadas. Reescreva essas linhas você mesmo.
3. `detect.py rascunho.txt limpo.txt` para mostrar o antes e o depois.
4. Se o veredito não for PASS, corrija a checagem mais fraca indicada na
   saída e rode de novo. Duas rodadas é normal. Cinco significa que o
   rascunho foi escrito por fórmula, e a solução é outro rascunho, não mais
   passadas.
5. Mostre ao usuário o texto limpo e a nota. Nunca só a nota.
