---
name: li-post
description: >-
  Escreve um post de LinkedIn em português a partir de uma ideia crua, usando
  21 fórmulas de gancho testadas, na voz do próprio usuário, humanizado para
  não parecer IA. Use sempre que o usuário quiser um post de LinkedIn, um
  gancho, um rascunho para o feed, "post sobre X", "transforma isso num post",
  "escreve um post", "me dá opções de gancho", "LinkedIn post" ou "write a
  post". Entrega três opções de gancho, um rascunho completo e um bloco pronto
  para copiar, que nunca é publicado sem um "sim" explícito.
---

# li-post

Transforma uma ideia crua num post de LinkedIn que soa como a pessoa que vai
publicá-lo.

## Antes de escrever

1. Leia `~/.claude/linkedin/voice.md`, se existir. Esse arquivo é o perfil de
   voz do usuário: como ele fala, o que ele nunca diz, com quem está falando,
   se usa travessão, o quanto é formal. Se não existir, peça **três posts
   antigos dele**, deduza a voz a partir deles e escreva o arquivo. Não pule
   esta etapa e não invente uma voz. Post na voz errada é pior do que post
   nenhum.
2. Leia `hooks.json` nesta pasta. São as 21 fórmulas, com modelos, exemplos
   preenchidos, para que cada uma serve e como cada uma costuma ser estragada.
   Os exemplos são ilustrativos: nunca use os números deles no post do
   usuário.
3. Se a ideia for rasa ("post sobre IA"), não encha linguiça. Faça uma
   pergunta só, juntando tudo: o que aconteceu, com quem, e quanto custou ou
   rendeu. Um post precisa de uma coisa específica e verdadeira. Consiga isso
   antes de escrever.

## O formato

O LinkedIn premia tempo de leitura, salvamentos e comentários, nessa ordem.
Então:

```
Linha 1      o gancho. Sozinho. Precisa sobreviver ao corte de ~140 caracteres no celular.
Linha 2      a recompensa da linha 1, não a preparação da linha 3.
Corpo        parágrafos curtos, de 1 a 3 linhas, com uma linha em branco entre cada um.
             Nada de paredão de texto. O espaço em branco é o formato.
A virada     uma linha que muda o sentido do que veio antes.
Fechamento   uma pergunta específica ou uma instrução. Nunca as duas.
```

Tamanho: entre 900 e 1.300 caracteres é a faixa de trabalho para post só de
texto. Abaixo de 400 parece um pensamento solto, não um post. Acima de 2.000,
cada linha tem que se justificar, e o toque no "ver mais" tem que ser pago
pela linha 2.

## Português de verdade

- Escreva como um profissional brasileiro escreve, não como tradução do
  inglês. "Aqui está o que eu aprendi" e "Deixe-me explicar" denunciam
  tradução. Prefira construções diretas: "Aprendi isto", "Explico".
- O nível de formalidade vem do `voice.md`. Na dúvida, português culto e
  direto, sem gíria forçada e sem "pra" e "né" só para parecer humano.
- Anglicismos de mercado (lead, pipeline, call, insight) só se o `voice.md`
  mostrar que o usuário usa. Se ele não usa, use o equivalente em português.
- Números no padrão brasileiro: R$ 1.500, 12,5%, 1.140 caracteres.
- Datas e horários no padrão brasileiro e no horário de Brasília.

## O ciclo

**1. Escolha três ganchos, não um.** Passe a ideia pelo `hooks.json` e escolha
as três fórmulas que de fato combinam com ela. Fórmulas diferentes, não três
variações da mesma. Mostre como três linhas numeradas e diga, numa frase, qual
você publicaria e por quê.

**2. Escreva o post completo** a partir do gancho mais forte.

**3. Humanize.** Passe o rascunho pelo `/li-human` antes de mostrá-lo. Todo
post desta skill sai humanizado. Isso não é um passo extra opcional, é o que
faz o rascunho valer a leitura. Se o `voice.md` disser que o usuário usa
travessão, rode o `humanize.py` com `--keep-dash`.

**4. Mostre o bloco.** Pronto para copiar, num bloco de código, exatamente como
deve ser colado. Logo abaixo:

```
POST PRONTO
gancho:       #17 Âncora de Tempo
tamanho:      1.140 caracteres
humanizador:  6 marcas removidas, nota humana 84 PASS
publicar em:  terça, 8h15 (horário de Brasília, do seu plano)

Responda "sim" para registrar, ou me diga o que mudar.
```

Se não houver plano da semana (`~/.claude/linkedin/plan.md`), omita a linha
"publicar em" em vez de inventar um horário.

**5. Nunca publique.** Esta skill produz texto. Quem publica é o usuário. Ao
receber "sim" (ou "yes", "pode", "fechado"), acrescente o post em
`~/.claude/linkedin/log.md` com a data, o gancho usado e a primeira linha,
para que o `/li-audit` tenha um histórico para trabalhar depois.

## Regras que fazem a diferença

- **Uma ideia por post.** Se o rascunho tem duas, são dois posts. Diga isso.
- **Número em vez de adjetivo.** "R$ 4.200" ganha de "muito". Se o usuário
  não deu um número, peça em vez de escrever contornando o buraco.
- **Nada de isca de engajamento.** "Concorda?", "O que vocês acham?" e "E
  você?" estão mortos. A pergunta final tem que ser uma que só este post
  poderia fazer.
- **No máximo três hashtags**, no final, e só se forem categorias reais que
  alguém segue. Em português, quando a categoria existir em português.
- **Nada de link no corpo do post.** O LinkedIn reduz o alcance de posts com
  link externo. Coloque o link no primeiro comentário e avise isso no resumo.
- **Nunca invente.** Nada de métricas, clientes, faturamento ou resultados
  inventados em nome do usuário, nem como provisório. Se um número for
  necessário e desconhecido, deixe `{{seu número}}` no rascunho e avise.

## Exemplo

```
/li-post criamos uma ferramenta interna que reduziu o tempo de montar proposta de 5 horas para 20 minutos
```

```
GANCHOS
1. #17 Âncora de Tempo   Montar uma proposta me tomava 5 horas. Hoje leva 20 minutos.
2. #12 A Comparação      5 horas por proposta contra uma ferramenta interna. A ferramenta ganhou.
3. #3  Confissão de Erro {{Por quanto tempo}} eu gastei 5 horas formatando cada proposta.

Eu publicaria o #17: a proporção é crível e o número é seu.
O #3 precisa de um dado que você não me deu: por quanto tempo isso durou.
```

Os três ganchos usam só os fatos que o usuário deu (5 horas, 20 minutos,
ferramenta interna). Onde falta um dado, o gancho mostra `{{...}}` e o resumo
pede o número, em vez de inventar um prazo que soe plausível.
