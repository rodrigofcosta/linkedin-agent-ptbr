---
name: li-plan
description: >-
  Monta a semana no LinkedIn: o que publicar, quando publicar e com quem
  interagir. Use quando o usuário disser "planeja minha semana", "o que eu
  posto?", "calendário de conteúdo", "não sei sobre o que postar", "plan my
  week", ou quiser uma agenda de posts e uma lista de engajamento.
---

# li-plan

A sala de controle. As outras skills do pacote executam; esta decide o que
será executado. Rode uma vez por semana, sempre no mesmo dia.

## Entrada

1. Leia `~/.claude/linkedin/voice.md`. Dele vêm os temas ("Meus temas"), o
   público, as posições, as provas que servem de repertório e a tabela de tom
   comercial.
2. Leia `~/.claude/linkedin/log.md`, se existir. O plano não deve repetir um
   tema ou um ângulo das últimas duas semanas.
3. **Pergunte sempre, numa pergunta só:** o que aconteceu de verdade nesta
   semana? Uma reunião com cliente, um número, um erro, algo que o usuário
   construiu, uma discussão, uma notícia do setor que o incomodou. É daí que
   os posts saem. Se o usuário já contou na mensagem, não pergunte de novo.

Se o `voice.md` não existir, pergunte também, de uma vez: o que o usuário
vende e para quem, os três ou quatro temas pelos quais quer ser conhecido, e
de 10 a 20 pessoas ou empresas para quem vale a pena estar visível. Anote
tudo.

## O que publicar

Quatro posts por semana valem mais que sete. Constância é piso, não meta, e o
quinto post da semana quase sempre é o fraco que derruba a média.

Varie ao longo da semana, nunca dois do mesmo tipo seguidos:

| tipo | frequência | função |
| --- | --- | --- |
| **Prova** | 1 por semana | algo concreto, com um número |
| **Opinião** | 1 por semana | uma posição que pode custar seguidores |
| **Ensino** | 1 por semana | uma coisa que o leitor pode fazer hoje |
| **História** | 1 a cada duas semanas | uma cena, com fala e com custo |
| **Oferta ou visão de mercado** | 1 a cada duas semanas | veja abaixo |

**Sobre o slot de oferta:** se o `voice.md` definir carga comercial baixa
para posts pessoais (até cerca de 5%), esse slot vira **Visão de mercado**:
uma tendência do setor lida pelo olhar do usuário, sem vender nada. A carga
comercial do `voice.md` sempre manda sobre esta tabela.

**Sobre os temas:** distribua os posts entre os pilares da seção "Meus temas"
do `voice.md`. Cada semana toca pelo menos dois pilares, e nenhum pilar
aparece em dois posts seguidos. Todo post precisa ter o olhar geográfico que
o `voice.md` exige.

**Sobre as provas:** o post de Prova pode usar o repertório do `voice.md`
("uma linha de transmissão de 2.420 km", "um sistema que precisava rodar sem
internet"), sempre com as regras de lá: nada de "eu fiz", nada de inventar
números, empresa e cliente só com `[AUTORIZAR]`.

Para cada slot, dê: o tipo, o pilar, o ângulo específico tirado do que
aconteceu na semana ou do repertório, e o número da fórmula de gancho do
`li-post/hooks.json` que combina com ele. Não um assunto, um ângulo. "IA" não
é plano. "Por que a IA aponta com confiança para o endereço errado quando o
geocoding caiu no centroide do CEP" é um post.

## Quando publicar

Publique quando o público estiver no trabalho. Todos os horários no **horário
de Brasília**. Para público B2B no Brasil, o padrão de trabalho é de terça a
quinta, entre 7h30 e 9h30, com segunda à tarde, sexta de manhã e o horário de
almoço (12h a 13h) como segunda opção. Fim de semana é para história pessoal
ou para nada.

Antes de fechar a semana, confira se há **feriado nacional ou emenda**. Em
semana com feriado, o público some no dia anterior e no posterior: mova ou
corte o post desses dias.

Mas diga isto com todas as letras: **o dia e a hora importam muito menos do
que uma primeira linha boa.** Se o usuário está ajustando horário antes de os
ganchos funcionarem, ele está polindo a coisa errada, e você deve dizer isso.

Se o público principal estiver em outro fuso, use o fuso do público, não o do
usuário.

## Com quem interagir

Monte uma lista de 10, dividida em três:

- **5 de alcance**: pessoas com o público que o usuário quer, em cujos posts
  ele consegue acrescentar algo de verdade. Comente antes de o post ter 20
  comentários, ou ninguém vê. Um ou dois podem ser referências internacionais
  da área, com comentário em inglês.
- **3 pares**: mesmo nível, mesma área. É o grupo que retribui.
- **2 compradores**: pessoas que poderiam de fato contratar. Comente nos posts
  delas por semanas antes de qualquer mensagem privada.

Os comentários seguem a `li-comment` e a tabela do `voice.md`: em posts de
outras pessoas e empresas, **zero carga comercial**, inclusive com os
compradores. Se o usuário tem uma empresa cujos posts ele comenta com carga
comercial maior (no caso do `voice.md`, a Novaterra), inclua uma linha à
parte lembrando de comentar os posts da empresa na semana.

Vinte minutos por dia, antes de publicar, não depois. Os comentários nos posts
dos outros são o que faz o post do usuário pegar.

## Saída

```
SEMANA DE 5 DE OUTUBRO

SEG  só engajamento  (20 min, lista abaixo)
TER  8h15  OPINIÃO        #1  Opinião Contrária   GIS nos setores
          drone não resolve dezenas de milhares de hectares; satélite é a base
QUA  só engajamento
QUI  8h00  ENSINO         #21 Entrega Direta      Inteligência de localização
          como separar a base pelo nível de precisão do geocoding antes de analisar
SEX  8h30  PROVA          #10 O Comprovante       GIS nos setores
          uma LT de 2.420 km e o que o mapeamento de uso do solo muda no traçado
SÁB  -
DOM  -

ENGAJAMENTO  (5 alcance / 3 pares / 2 compradores)
  ...
  + comentar os posts da Novaterra da semana (carga comercial de 10%)

Diga "escreve terça" e eu monto o rascunho.
```

Grave o plano em `~/.claude/linkedin/plan.md` para as outras skills lerem.
Nada é agendado ou publicado em lugar nenhum: isto é um plano, e quem o
executa é o usuário.
