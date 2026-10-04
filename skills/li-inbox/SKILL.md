---
name: li-inbox
description: >-
  Faz a triagem da caixa de mensagens do LinkedIn: separa convites e mensagens
  em leads, recrutadores, pares, pedidos e spam, e escreve as respostas que
  valem a pena. Use quando o usuário disser "minha caixa de mensagens está uma
  bagunça", "organiza minhas mensagens", "respondo isso?", "triage my DMs",
  colar um lote de mensagens do LinkedIn, ou estiver afogado em convites.
---

# li-inbox

A maioria das caixas de mensagens do LinkedIn é 80% ruído, e o custo desse
ruído é que os 20% importantes ficam uma semana sem resposta. Esta skill
separa um do outro e escreve só o que vale a pena escrever.

## Antes de começar

Leia `~/.claude/linkedin/voice.md`: voz, temas, assuntos fora dos limites,
regras de autorização e em nome de quem o usuário fala.

## Entrada

O usuário cola as mensagens. Prints servem. Não entre na conta dele nem leia
a caixa de mensagens com ferramenta de navegador.

## Separar em cinco

| grupo | sinal | ação |
| --- | --- | --- |
| **LEAD** | descreve um problema que o usuário resolve, ou pergunta sobre trabalhar junto | responder hoje, com resposta completa |
| **RECRUTADOR** | uma vaga, uma empresa, uma faixa salarial | responder se a vaga for real, uma linha se não for |
| **PAR** | alguém da mesma área com algo a dizer | responder nesta semana, com tom humano |
| **PEDIDO** | quer conselho, tempo, uma indicação, um favor | responder se for rápido e específico, recusar com elegância se não for |
| **SPAM** | oferta de agência, sequência de prospecção, cripto, "pergunta rápida" sem pergunta | arquivar, sem resposta |

Mostre as contagens primeiro. Ver "3 leads, 2 recrutadores, 41 spam" já é a
maior parte do valor.

## Reconhecendo uma sequência automática

Prospecção automática tem um formato: convite sem nada específico, mensagem
que chega minutos depois do aceite, "Olá, tudo bem? Vi seu perfil e...",
"posso te fazer uma pergunta rápida?", "notei que você atua em {setor}", link
de agenda na primeira mensagem e uma nova mensagem exatamente quatro dias
depois. No Brasil, são muito comuns as ofertas de agência de marketing,
geração de leads, tráfego pago, "parceria" vaga, renda extra e oportunidade
de investimento. Quando reconhecer o formato, marque como SPAM e diga qual
sinal entregou. O usuário não deve resposta a um roteiro.

## Golpes

Marque como **SPAM · GOLPE** e avise o usuário com destaque quando a mensagem:

- oferece vaga ou projeto que pede CPF, dados bancários, documentos ou
  qualquer pagamento antecipado;
- traz link encurtado ou arquivo pedindo login;
- se apresenta como suporte do LinkedIn ou de um banco.

Não responda, não abra o link e oriente o usuário a denunciar a mensagem no
próprio LinkedIn.

## Respostas

- **LEAD**: responda à pergunta da mensagem, por completo, de graça. Se a
  pessoa só descreveu um problema, a oferta é uma frase no fim. Se a pessoa
  perguntou diretamente sobre trabalhar junto, a conversa pode falar de
  empresa, serviço e próximos passos, porque o interesse partiu dela. Use a
  empresa que corresponde ao assunto, conforme o `voice.md`. Clientes,
  projetos e certificações citados recebem `[AUTORIZAR]`. Se não houver
  encaixe, diga e indique um caminho útil. Os dois desfechos são bons.
- **RECRUTADOR**: se a vaga for interessante de verdade, pergunte o que a
  mensagem deixou de fora: faixa de remuneração, nível do cargo, modelo de
  trabalho (presencial, híbrido ou remoto) e tipo de contratação (CLT ou PJ).
  Se não for, uma linha: não está procurando agora, pode indicar alguém, e
  indique mesmo.
- **PEDIDO**: se custa menos de dez minutos e é específico, faça. Se for
  "posso tomar 30 minutos do seu tempo?" ou "vamos tomar um café para eu
  entender sua área?", recuse numa frase calorosa e dê a resposta que você
  daria nessa conversa. É a versão educada e também a mais útil.
- **PAR**: responda como alguém da área responderia, com uma observação
  técnica de verdade, não com agradecimento genérico.
- **RECUSAS** são curtas, calorosas e definitivas. Nada de "vamos retomar no
  próximo semestre" se não existe próximo semestre.
- **Política**: mensagem que puxa para política não recebe resposta, conforme
  o `voice.md`.

Responda no idioma de quem escreveu. Em português, trate por "você".

## Saída

Agrupado por grupo, contagens primeiro, rascunhos só para os grupos que
recebem resposta, cada um passado pelo `/li-human` (em inglês, só o
`humanize.py`). Se houver `[AUTORIZAR]`, liste antes. Depois, a trava: quem
envia é o usuário.

```
CAIXA  ·  52 itens  ·  3 LEAD, 2 RECRUTADOR, 4 PAR, 2 PEDIDO, 41 SPAM

SPAM  (41): arquivar. 38 são a mesma sequência: convite sem nada específico,
"posso te fazer uma pergunta rápida?" quatro minutos depois do aceite e link
de agenda na primeira mensagem.

SPAM · GOLPE  (1): vaga de "analista GIS remoto" pedindo CPF e uma taxa de
cadastro. Não responda, não clique e denuncie a mensagem no LinkedIn.
```
