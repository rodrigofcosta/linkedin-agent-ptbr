---
name: li-audit
description: >-
  Faz a análise do que o usuário já publicou: quais posts funcionaram de
  verdade, por quê, e o que parar de fazer. Use quando o usuário colar as
  análises do LinkedIn ou posts antigos e perguntar "o que está funcionando?",
  "por que esse post flopou?", "analisa minhas métricas", "audita meu
  conteúdo", "audit my content", ou quiser saber em que apostar mais.
---

# li-audit

A única fonte honesta do que funciona para uma conta é a própria conta. Toda
regra de todo guia de LinkedIn, inclusive as deste pacote, é uma suposição
inicial. Os últimos 30 posts do usuário são a evidência.

## Entrada

Peça o que o usuário tiver:

- A exportação das análises de conteúdo do LinkedIn (planilha com
  impressões, reações, comentários e compartilhamentos por post). O caminho no
  menu muda de tempos em tempos; se o usuário não encontrar, aceite prints.
- Ou um print por post com impressões, reações, comentários e
  compartilhamentos.
- Ou só os posts com o número de reações, o que basta para uma primeira
  passada.

Sobre o `Shares.csv` da exportação de dados da conta ("Obter uma cópia dos
seus dados"): ele traz o texto e a data de todos os posts, mas **não traz
métricas**. Serve para reconstruir o histórico e classificar os posts, e
precisa ser combinado com as análises ou com os prints para ter números.

Leia também `~/.claude/linkedin/log.md`, se existir, porque ele registra a
fórmula de gancho de cada post publicado com o pacote. Para posts anteriores
ao pacote, classifique o gancho você mesmo pelo `li-post/hooks.json` e diga
que a classificação é sua.

Leia `~/.claude/linkedin/voice.md` para saber os temas e os tipos de voz do
usuário.

## O que medir de verdade

Impressões brutas são o número menos útil da página, porque dependem
principalmente de quantas pessoas já seguem o usuário. Calcule estes, e mostre
a conta:

| métrica | como | o que diz |
| --- | --- | --- |
| **Taxa de engajamento** | (reações + comentários + compartilhamentos) / impressões | se o post mereceu o alcance que teve |
| **Proporção de comentários** | comentários / reações | se o post começou uma conversa ou só recebeu um aceno |
| **Múltiplo de alcance** | impressões / número de seguidores | se o post foi além do público que já segue |
| **Salvamentos e envios** | se disponível | o melhor indicador isolado de alcance futuro |

Ordene por taxa de engajamento e múltiplo de alcance, não por impressões. Um
post com 900 impressões e 40 comentários ganhou do que teve 12.000 impressões
e 6 comentários.

Use o padrão brasileiro nos números: 8,1%, 12.000 impressões.

## Depois, ache o padrão

Com os 5 melhores e os 5 piores lado a lado, procure o que realmente os
separa, e esteja disposto a concluir algo que o usuário não vai gostar:

- **Fórmula de gancho.** Quais números do `hooks.json` estão entre os 5
  melhores?
- **Formato.** Texto, documento, imagem, vídeo.
- **Tamanho.**
- **Tema.** Qual dos pilares de "Meus temas" do `voice.md`.
- **Tipo de voz.** Opinião pessoal em primeira pessoa ou case institucional
  de empresa. Para quem alterna as duas, essa costuma ser a variável mais
  reveladora.
- **Número de hashtags.** Útil quando o usuário mudou de prática ao longo do
  tempo.
- **Comentários na primeira hora.** Posts em que o usuário respondeu dentro
  de uma hora contra os que não.
- **Dia e horário**: confira **por último**, e só se os outros itens não
  mostrarem nada. Quase nunca é a causa, e é onde as pessoas querem que a
  causa esteja.

Apresente cada conclusão como uma afirmação com a evidência junto, e diga o
grau de confiança. Com 30 posts dá para ver um padrão; com 6 não dá, e você
deve dizer isso em vez de inventar um.

## Saída

Exemplo ilustrativo (os números são fictícios):

```
AUDITORIA  ·  31 posts  ·  12 de junho a 5 de setembro

5 MELHORES POR TAXA DE ENGAJAMENTO
  8,1%  #3  Confissão de Erro    "O erro de geocoding que custou uma loja"      1.940 imp
  6,4%  #1  Opinião Contrária    "Sua meta não tem endereço"                    2.210 imp
  ...

5 PIORES
  0,4%  #5  Lista Prometida      "7 ferramentas de GIS que você precisa"       11.400 imp
  ...

O QUE OS DADOS DIZEM
1. Posts de opinião pessoal com um exemplo concreto do território: média de
   6,2% contra 1,1% do resto. n=6. É o sinal mais forte, com folga.
2. Cases institucionais têm alcance, mas quase nenhum comentário. Três dos
   cinco piores.
3. O dia da semana não mostra nada. A média de terça e a de sexta estão dentro
   do ruído. Pare de otimizar isso.

PARE: listas de ferramentas e case institucional sem opinião.
FAÇA MAIS: opinião em primeira pessoa com um exemplo concreto e um número.
```

Depois, passe as conclusões para o `/li-plan`, para que o plano da próxima
semana seja construído sobre a evidência do próprio usuário, e não sobre
padrões genéricos. Se a auditoria mostrar que outros posts representam melhor
a voz do usuário do que os listados no `voice.md`, sugira a troca, mas só
altere o `voice.md` com a confirmação dele.
