---
name: li-dm
description: >-
  Escreve convites de conexão e mensagens privadas que recebem resposta: o
  convite de 200 caracteres, a primeira mensagem e os dois acompanhamentos.
  Use quando o usuário disser "escreve um convite de conexão", "manda uma
  mensagem para essa pessoa", "mensagem de prospecção", "como faço o
  follow-up", "DM this person", ou estiver abordando alguém específico no
  LinkedIn.
---

# li-dm

O convite tem 200 caracteres. A primeira mensagem decide se haverá uma
segunda. Nenhum dos dois é uma oferta.

## Antes de escrever

1. Leia `~/.claude/linkedin/voice.md`: voz, temas, provas e regras de
   autorização.
2. Peça os detalhes, numa pergunta só:
   - **Quem**: nome, cargo, empresa.
   - **O gancho**: o motivo real para abordar agora. Um post que a pessoa
     escreveu, algo que a empresa dela lançou, uma conexão em comum, uma
     palestra. Não "ela se encaixa no meu perfil de cliente".
   - **O que o usuário quer**: uma conversa, uma indicação, uma parceria,
     uma venda. Seja honesto internamente, mesmo que a mensagem não comece
     por aí.
   - **Em nome de quem**: o usuário fala só como ele mesmo ou também como
     profissional de uma empresa dele? Isso define se a empresa pode aparecer
     na conversa.

Se não há um motivo específico para mandar mensagem para essa pessoa hoje,
diga isso. Mensagem sem motivo é o que todo mundo manda, e é por isso que a
taxa de resposta deles fica perto de 2%.

## Tom comercial nas mensagens

A mensagem privada é o lugar onde uma conversa comercial pode acontecer, mas
ela só acontece se a pessoa quiser. A escalada é gradual:

| etapa | carga comercial | o que pode ter |
| --- | --- | --- |
| Convite | 0% | uma referência específica à pessoa e uma linha sobre quem é o usuário. Nada de pedido, empresa ou serviço. |
| Primeira mensagem | baixa | primeiro entrega algo útil; o pedido é uma conversa curta, nunca uma apresentação de empresa. A empresa só aparece se for parte do gancho. |
| Acompanhamentos | baixa | algo novo e útil; o pedido continua sendo a conversa. |
| Depois que a pessoa responde com interesse | livre | aí sim a conversa pode falar de empresa, serviço e próximos passos. |

Se o `voice.md` tiver regras mais específicas, siga o `voice.md`. Citar
clientes, projetos ou certificações, mesmo no privado, recebe `[AUTORIZAR]`.

## O convite (200 caracteres)

```
{uma referência específica à pessoa} + {uma linha sobre quem é o usuário} + {nenhum pedido}
```

O convite não pede nada. Ele existe para tornar o aceite óbvio. Menos de 200
caracteres, contando espaços: conte e mostre a contagem.

```
Li seu post sobre expansão de lojas em cidades médias. Trabalho com
inteligência de localização há 26 anos e gostaria de acompanhar o que você
publica por aqui.
                                                                    [160/200]
```

## A primeira mensagem, depois do aceite

Espere um dia. Depois:

- **De duas a quatro frases.** Uma tela de texto vai para o lixo.
- **Retome o que foi citado no convite.** A continuidade é o motivo de o
  convite ter sido específico.
- **Entregue algo antes de pedir.** Uma observação técnica sobre o desafio
  da pessoa, uma fonte de dado aberto que resolve parte do problema, um
  número, uma resposta. Para quem trabalha com geografia, o mais valioso
  costuma ser mostrar algo que a pessoa não estava vendo no território dela.
- **Um pedido, e pequeno.** "Topa uma conversa de 15 minutos?" ganha de
  "deixa eu te apresentar nossas soluções".
- **Nada de link de agenda na primeira mensagem.** Parece funil, porque é.

## Acompanhamentos

Dois. Esse é o número.

- **Depois de 4 dias**: acrescente algo novo. Nunca "só passando para
  lembrar" ou "retomando minha última mensagem". Se não há nada novo, não há
  acompanhamento.
- **Depois de 10 dias**: a mensagem de encerramento. Diga que vai parar de
  insistir, e pare mesmo. Ela costuma trazer uma parte surpreendente das
  respostas, porque tira a pressão.

Depois disso, pare. Um terceiro acompanhamento não converte ninguém e
desgasta a relação.

## Idioma e tratamento

Escreva no idioma da pessoa. Em português, trate por "você", com o nível de
formalidade do `voice.md`. Em inglês, mesmo tom: direto, profissional e sem
gírias forçadas.

## Nunca

- Nunca envie sequências automáticas de convites ou mensagens. Ferramentas de
  automação violam os Termos de Uso do LinkedIn e levam à restrição da conta.
- Nunca invente uma conexão em comum, uma faculdade em comum ou a leitura de
  algo que o usuário não leu.
- Nunca abra com "Espero que esta mensagem o encontre bem", "Prezado(a)" ou
  "Venho por meio desta".
- Nunca mande mais de 20 convites por dia. Acima disso, o LinkedIn limita a
  conta, e conta limitada é conta morta.
- Nunca invente resultados ou números para parecer mais interessante. Se o
  dado não está no `voice.md` e o usuário não forneceu, ele não entra.

## Saída

O convite com a contagem de caracteres, a primeira mensagem e os dois
acompanhamentos, cada um com o dia em que deve ser enviado. Todos passados
pelo `/li-human` (em inglês, só o `humanize.py`). Se houver trechos com
`[AUTORIZAR]`, liste-os antes. O usuário envia cada um à mão.
