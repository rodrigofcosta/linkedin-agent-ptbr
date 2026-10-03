---
name: li-reply
description: >-
  Cuida das respostas nos comentários dos posts do próprio usuário no
  LinkedIn: organiza os comentários pelo que vale a pena responder e escreve
  uma resposta para cada um. Use quando o usuário colar os comentários de um
  post, ou disser "responde esses comentários", "me ajuda com os comentários",
  "fulano comentou X no meu post", "reply to these", ou estiver lidando com um
  crítico ou com um possível cliente nos comentários.
---

# li-reply

A conversa nos comentários do seu post é onde o alcance realmente se decide.
Cada resposta é um novo evento de engajamento no post, e as respostas da
primeira hora fazem a maior parte do trabalho. Mas os comentários não têm o
mesmo valor, então esta skill organiza antes de escrever.

## Antes de escrever

Leia `~/.claude/linkedin/voice.md`. Ele define a voz do usuário, o repertório
que pode ser usado e a carga comercial dos posts pessoais: **cerca de 2%**.
Isso vale também para as respostas nos comentários desses posts. Ninguém deve
sair da conversa com a sensação de ter lido um anúncio.

## Entrada

O usuário cola os comentários, de preferência com nome e cargo de quem
comentou. Prints servem. Não raspe a conversa com ferramenta de navegador.

## Primeiro, a triagem

Separe cada comentário em um de cinco grupos e diga quantos há em cada um:

| grupo | o que é | o que recebe |
| --- | --- | --- |
| **LEAD** | alguém descrevendo o problema que o usuário resolve | uma resposta de verdade + uma porta aberta discreta |
| **SUBSTÂNCIA** | acrescenta dado, discorda, amplia | a resposta mais longa da conversa |
| **PAR** | alguém da área ao lado de quem vale ser visto | uma resposta que entrega algo a essa pessoa |
| **APOIO** | "excelente post", 👏, uma marcação | uma curtida e, no máximo, uma resposta de 3 a 8 palavras |
| **RUÍDO** | oferta de serviço, spam, má-fé, política | nada, ou uma linha e encerra |

Depois escreva nessa ordem, e pare de escrever quando o valor acabar.

## Como responder

- **Responda à pergunta de verdade.** Se alguém perguntou como, explique como,
  na própria resposta. Não mande a pessoa para o privado para ouvir algo que
  ela poderia ter lido ali.
- **Use o nome da pessoa uma vez**, no começo, e nunca com ponto de
  exclamação.
- **Acompanhe o tamanho.** Um comentário de duas linhas não recebe uma
  resposta de seis.
- **Varie.** Nada de "Obrigado pelo comentário!" em série. Cada resposta tem
  que parecer escrita para aquela pessoa.
- **Para um crítico:** reconheça primeiro a parte verdadeira, com as palavras
  dele, e depois sustente o ponto em que você acredita. Nunca apague, nunca
  fique na defensiva, nunca responda duas vezes na mesma linha de conversa.
- **Para um lead:** responda por completo, em público. A porta aberta é uma
  frase só, no fim, oferecendo ajuda, nunca vendendo. Exemplo: "Se quiser, me
  chama no privado que te conto como costumo estruturar essa etapa." Não cite
  Novaterra, Synthix, serviços ou preços na resposta pública. Se o lead
  perguntar diretamente quem faz esse trabalho, a resposta pode citar a
  empresa, mas com `[AUTORIZAR]`. É o valor entregue em público que faz a
  próxima pessoa chamar no privado.
- **Para uma oferta de serviço nos seus comentários:** ignore. Responder dá
  alcance a ela.
- **Para um comentário que puxa para política:** não entre. Fica em RUÍDO,
  sem resposta.

## Repertório

As provas do `voice.md` podem dar concretude às respostas, com as mesmas
regras de sempre: nunca "eu fiz" ou "meu projeto" sobre os cases, nunca
nomear empresa ou cliente sem `[AUTORIZAR]`, nunca inventar números. Se a
resposta precisar de um dado que o usuário não deu, deixe `{{seu número}}` e
avise.

## Idioma

Responda no idioma do comentário. Comentário em inglês recebe resposta em
inglês, com o mesmo tom profissional e direto.

## Humanizar

Todas as respostas passam pelo `/li-human` antes de serem mostradas. Em
português, rode `humanize.py` e `detect.py`. Em inglês, rode só o
`humanize.py` e evite à mão os vícios de IA em inglês (delve, leverage,
robust, seamless, crucial, game-changer).

## Saída

Um bloco só, agrupado por triagem, com cada resposta pronta para copiar e já
humanizada. Se houver trechos com `[AUTORIZAR]`, liste-os antes do bloco.

```
RESPOSTAS  ·  9 comentários  ·  1 LEAD, 1 SUBSTÂNCIA, 2 PAR, 4 APOIO, 1 RUÍDO

LEAD
@Mariana Lopes - "temos esse problema na base de lojas e clientes, por onde começar?"
> Mariana, eu começaria separando os registros pelo nível de precisão do
> geocoding. Tudo que caiu no centroide do CEP ou do município vai para uma
> fila de correção antes de qualquer análise. Só essa separação já mostra o
> tamanho do problema. Se quiser, me chama no privado que te conto como
> costumo estruturar essa etapa.

SUBSTÂNCIA
@Paulo Reis - acha que 20% a 30% é alto
> Paulo, depende muito de onde a base nasce. Base que já entra com CEP
> validado no cadastro costuma vir bem mais limpa. O número que eu cito é de
> CRMs em auditorias para projetos de location intelligence, e ali ele se
> repete com frequência.

APOIO  (curtir todos, responder aos três primeiros)
@Carla Mendes "Muito bom!" -> Obrigado, Carla.
...

RUÍDO  (1)
Ignorado: oferta de serviço de uma agência. Responder dá alcance a ela.
```

Depois, a trava: **nada é publicado sem um "sim" do usuário.** Quem cola as
respostas no LinkedIn é ele.
