---
name: li-comment
description: >-
  Escreve comentários em posts de LinkedIn de outras pessoas e empresas que
  soam como alguém com opinião e interesse genuíno pelo trabalho do autor, não
  como um robô. Ajusta o tom ao tipo de post, a carga comercial ao autor e o
  idioma ao post. Use quando o usuário colar um post e quiser um comentário, ou
  disser "comenta isso", "o que eu respondo aqui", "me ajuda a comentar",
  "comment on this", ou quiser uma rodada de comentários de engajamento.
---

# li-comment

Comentar é a ação de maior alavancagem no LinkedIn e a mais fácil de fazer
mal. Um comentário num post com 400 reações é visto por mais gente do que a
maioria dos seus próprios posts. Um comentário genérico não é visto por
ninguém. E um comentário que transforma o post do outro em vitrine para quem
comenta é pior do que nenhum: custa a simpatia do autor.

## O princípio: o autor é o protagonista

O comentário existe para começar uma conversa com o autor, não para mostrar
quem comenta. O objetivo é que o autor queira responder, e que quem ler a
troca pense "essa pessoa entende do assunto e é generosa".

- **Generosidade antes de autoridade.** Primeiro, o que o autor fez bem, de
  forma específica. Depois, a contribuição.
- **O repertório do usuário serve para fazer uma pergunta melhor**, não para
  listar o que ele já fez. Em post de outra pessoa, nada de "nas auditorias
  que eu faço", "em 26 anos de", "no meu trabalho eu vejo". No máximo uma
  referência leve à experiência, e só se ela tornar a pergunta mais precisa.
- **Nunca use o comentário para apontar, mesmo que indiretamente, que o
  trabalho do autor tem um problema que o usuário resolve.** Se houver uma
  limitação técnica, transforme em pergunta curiosa ("como vocês tratam
  X?"), não em diagnóstico.
- **Termine com um gancho de conversa**: uma pergunta técnica específica que
  o autor tenha prazer em responder, ou uma resposta à pergunta que o próprio
  autor fez no fim do post, seguida de uma pergunta de volta.

## Antes de escrever

1. Leia `~/.claude/linkedin/voice.md`. Ele define a voz do usuário, os temas e
   a tabela de **tom comercial por tipo de conteúdo**, que manda nesta skill.
2. Identifique **quem publicou** e classifique pela carga comercial (abaixo).
   Se o autor não estiver claro, pergunte. Na dúvida, a mais restritiva.
3. Identifique **o tipo de post** (abaixo). É ele que define o tom e o tipo de
   comentário.
4. Identifique **o idioma do post**. O comentário sai no mesmo idioma.

## Entrada

O usuário cola o texto do post (e o nome e cargo do autor, se tiver). Se
mandar um print, leia o print. Se mandar um link que você não consegue abrir,
peça o texto: não adivinhe o que o post dizia e não use automação de
navegador para raspar o feed.

## Tipo de post

| tipo de post | o que o autor espera | tipo de comentário padrão |
| --- | --- | --- |
| **Lançamento ou conquista** (projeto, produto, certificação, aprovação, novo cargo) | reconhecimento e interesse pelo que foi feito | 10 · Reconhecimento + pergunta |
| **Opinião ou tese** | concordância qualificada ou discordância respeitosa | 2, 3, 4 ou 8 |
| **Conteúdo técnico ou tutorial** | complemento, dúvida, caso de aplicação | 2, 5 ou 10 |
| **Notícia do setor** | leitura, interpretação, consequência | 4 ou 8 |
| **Pedido de ajuda ou pergunta aberta** | resposta útil | resposta direta + pergunta de volta |

Em post de **lançamento ou conquista**, o comentário **sempre** começa com
reconhecimento específico. Abrir com contribuição técnica ou com uma ressalva
nesse tipo de post soa como "deixa eu te corrigir no seu dia".

## Classificação do autor e carga comercial

| quem publicou | carga comercial | como fica o comentário |
| --- | --- | --- |
| Página da Novaterra, ou colega da Novaterra falando de um trabalho da Novaterra | cerca de 10% | Comentário técnico que acrescenta algo ao post e, no fim, **uma frase** convidando quem tiver o mesmo desafio a conversar com a equipe da Novaterra. Sem lista de serviços, sem link. |
| Qualquer outra pessoa ou empresa | 0% | 100% técnico e focado no autor. Nunca mencionar Novaterra, Synthix, serviços, "me chama" ou convite para contato. |

Se o `voice.md` tiver regras mais específicas, siga o `voice.md`.

## Os dez tipos de comentário

Escolha pelo tipo de post e pelo que o post realmente diz.

| # | tipo | quando | formato |
| --- | --- | --- | --- |
| 1 | **Acrescentar um dado** | o post faz uma afirmação que o usuário pode sustentar com um número | o dado a serviço do argumento do autor, não do usuário |
| 2 | **O caso que faltou** | o post está certo, mas incompleto | "Isso vale até {condição}. A partir daí..." |
| 3 | **Discordância respeitosa** | o usuário acha, de verdade, que está errado | primeiro o ponto de acordo, depois a bifurcação |
| 4 | **Estender uma frase** | uma frase do post é a melhor | cite a frase e construa a partir dela |
| 5 | **A pergunta de verdade** | o post pulou a parte difícil | uma pergunta específica, que mostre que o usuário leu com atenção |
| 6 | **A vivência** | o usuário conhece por dentro o que o post descreve | o que acontece na prática, em duas frases, sem "eu fiz" e sem currículo |
| 7 | **A correção** | há um erro factual | esteja certo, seja breve, seja gentil, tenha certeza. Nunca em post de lançamento |
| 8 | **O novo enquadramento** | os fatos estão certos, o enquadramento não | "Outra forma de ler isso:" |
| 9 | **A frase curta** | o post não precisa de nada, o usuário quer presença | menos de 12 palavras, espirituosa ou verdadeira |
| 10 | **Reconhecimento + pergunta** | lançamento, conquista ou trabalho que o autor está mostrando | 1) reconhecimento específico de uma escolha concreta do autor; 2) uma pergunta técnica que convide à troca |

**Como fazer o reconhecimento específico (tipo 10):** aponte uma decisão
concreta do autor e diga por que ela é boa. "Parabéns pelo projeto" sozinho é
ruído. "Parabéns pelo SmartRoute. Abrir uma demonstração com dados fictícios
para qualquer pessoa testar é um jeito muito honesto de mostrar o conceito" é
reconhecimento. Pode começar com "Parabéns, {nome}," ou "Parabéns pelo
{projeto}", desde que a frase seguinte seja específica.

**Como fazer a pergunta (tipos 5 e 10):** uma pergunta que o autor tenha
prazer em responder, porque mostra interesse pelo que ele construiu. Boas
perguntas tratam de uma decisão de projeto, de um limite que o autor
certamente já pensou ou de um próximo passo. Sempre que possível, com o olhar
geográfico do usuário: território, localização, malha viária, qualidade do
dado espacial.

## Regras

- **De 2 a 4 frases.** Mais longo parece sequestro do post. Mais curto parece
  enchimento.
- **Elogio genérico é proibido; reconhecimento específico é bem-vindo.** Nunca
  abra só com "Excelente post", "Ótimo post", "Muito bom", "Top",
  "Sensacional", "Concordo plenamente", "Faz todo sentido" ou "Que reflexão".
  Em inglês, o mesmo vale para "Great post", "Love this", "So true",
  "Couldn't agree more". Elogio só vale quando a frase diz o que,
  exatamente, foi bom.
- **Nada de emoji na abertura.**
- **Nunca resuma o post.** O autor sabe o que escreveu.
- **Uma ideia só.**
- **Diga a coisa específica.** Se o comentário caberia em qualquer post sobre
  o mesmo tema, ele é ruído.
- **Discordar é permitido**, mas o acordo vem primeiro e tem que ser real. Em
  post de lançamento ou conquista, prefira transformar a discordância numa
  pergunta.
- **Se o autor fez uma pergunta no fim do post, considere respondê-la.** É o
  convite mais direto para conversar. Responda em uma frase e devolva com uma
  pergunta.

## Repertório

As provas do `voice.md` podem dar precisão à pergunta ou à vivência, com as
regras de lá: nunca "eu fiz", nunca inventar números, empresa ou cliente só
com `[AUTORIZAR]`. Em comentário com 0% de carga comercial, não nomeie empresa
nem cliente. E lembre do princípio desta skill: o repertório entra para servir
à conversa com o autor, nunca para competir com ele.

## Idioma

- **Post em português**: comentário em português, na voz do `voice.md`.
- **Post em inglês**: comentário em inglês, com o mesmo tom profissional e
  direto, como um especialista brasileiro escreveria em bom inglês.

## Humanizar

Passe as duas opções pelo `/li-human` antes de mostrar.

- **Português**: rode `humanize.py` e `detect.py`.
- **Inglês**: rode só o `humanize.py` e evite à mão os vícios de IA em inglês
  (delve, leverage, robust, seamless, crucial, game-changer, "it's not just X,
  it's Y").

A nota do `detect.py` em comentário é **só informativa**. Comentários são
curtos e têm poucos números, então a nota tende a ficar abaixo do corte mesmo
quando o texto está bom. Nunca acrescente dados, números ou referências à
experiência do usuário só para subir a nota.

## Saída

Duas opções de **tipos diferentes**, identificadas, mais uma linha dizendo qual
você publicaria e por quê, pensando em qual tem mais chance de o autor
responder.

```
COMENTÁRIOS  (post de Talita Souza, lançamento do SmartRoute)
tipo de post: lançamento · autor: outra pessoa · carga comercial: 0% · idioma: português

[10 · Reconhecimento + pergunta]
Parabéns pelo SmartRoute, Talita. Abrir uma demonstração com dados fictícios
para qualquer pessoa testar é um jeito muito honesto de mostrar o conceito.
Uma dúvida técnica: na sugestão de rotas, a proximidade é calculada em linha
reta ou pelo tempo de deslocamento na malha viária?

[Resposta à pergunta do post + pergunta de volta]
Talita, gostei de você ter pensado o SmartRoute para além da manutenção,
porque instalação, inspeção e visita comercial têm o mesmo problema de fundo.
Respondendo à sua pergunta: para mim, o maior desafio aparece antes da rota,
na qualidade do endereço que chega na planilha. Como o SmartRoute trata
atendimentos que caem na mesma coordenada?

Eu publicaria o primeiro: reconhece uma escolha concreta dela e faz uma
pergunta técnica que ela certamente gosta de responder.
```

Se algum trecho tiver `[AUTORIZAR]`, liste os pontos antes do bloco de
opções.

## Modo em lote

Se o usuário quiser uma rodada de engajamento, peça de 5 a 10 posts como
texto colado numa mensagem só, com o autor de cada um, e devolva um
comentário por post num único bloco, já com a classificação de cada um. Anote
em quem o usuário já comentou na semana em `~/.claude/linkedin/log.md`.
Comentar nas mesmas três pessoas todo dia fica visível e parece o que é.

## Nunca

Não publique automaticamente. Não use ferramenta de navegador para publicar
comentários em nome do usuário. Postagem automática e raspagem violam os
Termos de Uso do LinkedIn e colocam a conta em risco. Esta skill escreve o
comentário. Quem publica é o usuário.
