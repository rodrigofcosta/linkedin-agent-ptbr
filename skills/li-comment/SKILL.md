---
name: li-comment
description: >-
  Escreve comentários em posts de LinkedIn de outras pessoas e empresas que
  soam como alguém com opinião, não como um robô. Ajusta a carga comercial
  conforme o autor do post e responde no idioma do post. Use quando o usuário
  colar um post e quiser um comentário, ou disser "comenta isso", "o que eu
  respondo aqui", "me ajuda a comentar", "comment on this", ou quiser uma
  rodada de comentários de engajamento.
---

# li-comment

Comentar é a ação de maior alavancagem no LinkedIn e a mais fácil de fazer
mal. Um comentário num post com 400 reações é visto por mais gente do que a
maioria dos seus próprios posts. Um comentário genérico não é visto por
ninguém e ainda custa credibilidade com o autor.

## Antes de escrever

1. Leia `~/.claude/linkedin/voice.md`. Ele define a voz do usuário, os temas,
   as provas que podem servir de repertório e, principalmente, a tabela de
   **tom comercial por tipo de conteúdo**. Essa tabela manda nesta skill.
2. Identifique **quem publicou o post** e classifique (veja abaixo). Se o
   usuário não disse quem é o autor e isso não estiver claro no texto ou no
   print, pergunte. Na dúvida, use a classificação mais restritiva.
3. Identifique **o idioma do post**. O comentário sai no mesmo idioma.

## Entrada

O usuário cola o texto do post (e o nome e cargo do autor, se tiver). Se
mandar um print, leia o print. Se mandar um link que você não consegue abrir,
peça o texto: não adivinhe o que o post dizia e não use automação de
navegador para raspar o feed.

## Classificação do post e carga comercial

| quem publicou | carga comercial | como fica o comentário |
| --- | --- | --- |
| Página da Novaterra, ou colega da Novaterra falando de um trabalho da Novaterra | cerca de 10% | Comentário técnico que acrescenta algo ao post e, no fim, **uma frase** convidando quem tiver o mesmo desafio a conversar com a equipe da Novaterra. Sem lista de serviços, sem link, sem "entre em contato já". |
| Qualquer outra pessoa ou empresa | 0% | 100% técnico. Nunca mencionar Novaterra, Synthix, serviços, "me chama", "estamos à disposição" ou qualquer convite para contato. O objetivo é contribuir com conhecimento e ser lembrado por isso. |

Se o `voice.md` tiver regras mais específicas do que esta tabela, siga o
`voice.md`.

Exemplos da frase final nos posts da Novaterra (varie, não repita a mesma):

- "Se a sua equipe está com esse desafio em alguma linha de transmissão, vale uma conversa com o time da Novaterra."
- "Para quem está enfrentando isso na operação, o time da Novaterra pode ajudar a desenhar o caminho."

## Repertório e experiência

Use as provas do `voice.md` como repertório para dar concretude ao
comentário: "numa linha de transmissão de mais de 2.000 km, o mapeamento de
uso do solo muda o traçado", "um sistema que precisa rodar sem acesso à
internet". Regras:

- Nunca escreva "eu fiz", "eu implantei", "no meu projeto" sobre esses cases.
- Falar da experiência de forma geral é natural e permitido: "em 26 anos de
  geotecnologia, o erro que mais vejo é...".
- Em comentários com 0% de carga comercial, **não nomeie empresa nem
  cliente**, nem a Novaterra. O repertório entra sem assinatura.
- Nunca invente números. Se o comentário pedir um dado que o usuário não
  forneceu e que não está no `voice.md`, use outro tipo de comentário.
- Qualquer citação de cliente, parceiro ou certificação recebe `[AUTORIZAR]`,
  conforme a regra do `voice.md`.

## Os nove tipos de comentário

Escolha pelo que o post realmente é. Nunca vá direto no tipo 1.

| # | tipo | quando | formato |
| --- | --- | --- | --- |
| 1 | **Acrescentar um dado** | o post faz uma afirmação que você pode sustentar com um número | "O mesmo aparece em base de CRM: de 20% a 30% dos registros com..." |
| 2 | **O caso que faltou** | o post está certo, mas incompleto | "Isso vale até {condição}. A partir daí..." |
| 3 | **Discordância respeitosa** | você acha, de verdade, que está errado | primeiro o ponto de acordo, depois a bifurcação |
| 4 | **Estender uma frase** | uma frase do post é a melhor | cite a frase e construa a partir dela |
| 5 | **A pergunta de verdade** | o post pulou a parte difícil | uma pergunta, específica, sem "fiquei curioso para saber" |
| 6 | **A vivência** | você conhece por dentro o que o post descreve | o que acontece na prática, em duas frases, sem dizer "eu fiz" |
| 7 | **A correção** | há um erro factual | esteja certo, seja breve, seja gentil, tenha certeza |
| 8 | **O novo enquadramento** | os fatos estão certos, o enquadramento não | "Outra forma de ler isso:" |
| 9 | **A frase curta** | o post não precisa de nada, você quer presença | menos de 12 palavras, tem que ser espirituosa ou verdadeira |

Sempre que possível, puxe o comentário para o olhar geográfico: o território,
a localização, o dado espacial. É isso que diferencia o usuário dos outros
comentaristas.

## Regras

- **De 2 a 4 frases.** Mais longo parece sequestro do post. Mais curto parece
  enchimento.
- **Nunca abra com** "Excelente post", "Ótimo post", "Parabéns pelo post",
  "Muito bom", "Top", "Sensacional", "Concordo plenamente", "Faz todo
  sentido", "Que reflexão", ou o primeiro nome do autor seguido de ponto de
  exclamação. Em inglês, o mesmo vale para "Great post", "Love this", "So
  true", "Couldn't agree more" e "This resonates". Todos são invisíveis.
- **Nada de emoji na abertura.** Nada de 🔥 ou 👏 como primeiro caractere.
- **Nunca resuma o post.** O autor sabe o que escreveu, e quem está lendo
  também.
- **Uma ideia só.** Comentário com dois pontos parece tentativa de artigo.
- **Diga a coisa específica.** Se o comentário caberia em qualquer post sobre
  o mesmo tema, ele não é um comentário, é ruído.
- **Discordar é permitido e funciona**, mas o acordo vem primeiro e tem que
  ser real.

## Idioma

- **Post em português**: comentário em português, na voz do `voice.md`.
- **Post em inglês**: comentário em inglês, com o mesmo tom profissional e
  direto. Escreva como um especialista brasileiro escreveria em bom inglês, sem
  gírias americanas forçadas. A carga comercial segue a mesma tabela, e posts
  em inglês de fora do Brasil quase sempre são 0%.

## Humanizar

Passe as duas opções pelo `/li-human` antes de mostrar. Em comentário, um
travessão é ainda mais visível do que em post, porque o texto é curto e as
pessoas leem com atenção.

- **Comentário em português**: rode o `humanize.py` e o `detect.py`
  normalmente.
- **Comentário em inglês**: o léxico do `slop.json` é em português, então rode
  só o `humanize.py` (ele limpa caracteres invisíveis, travessões e aspas
  curvas em qualquer idioma) e não mostre a nota do `detect.py`, que é
  calibrada para português. Evite à mão os vícios clássicos de IA em inglês:
  delve, leverage, robust, seamless, crucial, game-changer, testament to,
  "it's not just X, it's Y".

## Saída

Duas opções de **tipos diferentes**, identificadas, mais uma linha dizendo qual
você publicaria e por quê.

```
COMENTÁRIOS  (post de @autor sobre IA aplicada a GIS)
autor: outra empresa · carga comercial: 0% · idioma: português

[2 · O caso que faltou]
O ganho com IA é real enquanto a base geográfica está limpa. Quando o
geocoding jogou metade dos clientes no centroide do CEP, o modelo só aprende
mais rápido a apontar para o lugar errado.

[5 · A pergunta de verdade]
Como vocês validam a saída do modelo em campo? Em análise de localização, a
diferença entre um ponto bom e um ruim às vezes só aparece no Street View.

Eu publicaria o primeiro: puxa para a qualidade do dado espacial, que é o
ponto que o post não tocou.
```

Se algum trecho tiver `[AUTORIZAR]`, liste os pontos antes do bloco de
opções.

## Modo em lote

Se o usuário quiser uma rodada de engajamento, peça de 5 a 10 posts como
texto colado numa mensagem só, com o autor de cada um, e devolva um
comentário por post num único bloco, já com a classificação de cada um.
Mantenha uma anotação de em quem o usuário já comentou na semana em
`~/.claude/linkedin/log.md`. Comentar nas mesmas três pessoas todo dia fica
visível e parece o que é.

## Nunca

Não publique automaticamente. Não use ferramenta de navegador para publicar
comentários em nome do usuário. Postagem automática e raspagem violam os
Termos de Uso do LinkedIn e colocam a conta em risco. Esta skill escreve o
comentário. Quem publica é o usuário.
