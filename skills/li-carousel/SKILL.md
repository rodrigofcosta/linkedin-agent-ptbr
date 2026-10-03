---
name: li-carousel
description: >-
  Monta um post de documento no LinkedIn (carrossel): o texto de cada slide, a
  capa que faz a pessoa deslizar e o PDF para subir. Use quando o usuário
  disser "carrossel", "post de documento", "slides para o LinkedIn",
  "transforma isso num carrossel", "carousel", ou tiver uma ideia em formato de
  lista ou de etapas que morreria como post de texto.
---

# li-carousel

Post de documento é o formato com maior tempo de leitura no LinkedIn, porque
cada deslizada conta e a rolagem não. O formato premia uma ideia dividida em
etapas. E pune um post de texto picotado em pedaços.

## Antes de começar

Leia `~/.claude/linkedin/voice.md`: voz, temas, provas que servem de
repertório, tom comercial e hashtags. Todo carrossel precisa ter o olhar
geográfico que o `voice.md` exige.

## Quando usar no lugar de um post de texto

Use carrossel quando a ideia tem **sequência**: etapas, uma contagem
regressiva, uma progressão de antes e depois, um método com partes. Use post
de texto quando a ideia é uma afirmação só. Espalhar uma afirmação por oito
slides é o jeito mais comum de um carrossel fracassar. Se é isso que o
usuário tem, diga e mande para o `/li-post`.

## Estrutura

De 8 a 12 slides. Menos de 8 é post de texto. Mais de 12, a taxa de leitura
até o fim despenca.

```
1        CAPA        o gancho, em até 6 palavras, mais uma linha de promessa
2        O QUE ESTÁ  por que isso importa, numa frase
         EM JOGO
3-N      UMA IDEIA POR SLIDE. Um título de 3 a 7 palavras e no máximo 25
                     palavras abaixo dele. Se o slide precisa de um parágrafo,
                     são dois slides.
N+1      RESUMO      tudo em forma de lista, para o print ser útil sozinho
ÚLTIMO   CHAMADA     uma ação só: seguir, comentar ou salvar. Uma.
```

## Regras do texto dos slides

- **O slide 1 é 80% do resultado.** Seis palavras. Grande. O resto do
  carrossel não salva uma capa que ninguém desliza.
- **Numere todos os slides** (3/10). A leitura até o fim aumenta quando a
  pessoa vê onde termina.
- **Nenhum slide é parágrafo.** Se não cabe em 25 palavras, divida. Em
  português as palavras são mais longas que em inglês, então na dúvida corte.
- **O slide de resumo é o que as pessoas printam.** Ele tem que funcionar
  sozinho.
- **O nome do usuário em todos os slides**, pequeno, no canto inferior. O
  print viaja sem você. Use o nome e o endereço do perfil que estiverem no
  `voice.md`; se não estiverem, pergunte.
- **A chamada final segue o tom comercial do `voice.md`.** Em carrossel
  pessoal com carga comercial baixa, a chamada é seguir, comentar ou salvar,
  nunca "contrate" ou "fale com a nossa equipe".

## Mapas e imagens de satélite

Para quem trabalha com geografia, um bom mapa ou uma imagem de satélite num
slide comunica mais do que três slides de texto. Regras:

- **Um mapa, uma mensagem.** O título do slide diz o que a pessoa deve ver no
  mapa. Legenda mínima, só o necessário para entender essa mensagem.
- **Legível no celular.** O mapa vai ser visto do tamanho de uma miniatura:
  poucas classes, cores bem contrastadas, nada de rótulos pequenos.
- **Sempre com fonte**, em letra pequena no rodapé do slide (por exemplo,
  "Fonte: IBGE", "Imagem: Sentinel-2/ESA", "MapBiomas").
- **Cuidado com a licença.** Imagens comerciais (Planet, Kompsat e outras) e
  mapas de projetos de clientes têm restrição de uso e de divulgação. Prefira
  dados abertos (IBGE, MapBiomas, Sentinel-2, Landsat, OpenStreetMap). Qualquer
  imagem ou mapa de projeto de cliente recebe `[AUTORIZAR]`.
- **Peça o arquivo ao usuário.** Não invente mapa nem desenhe um "mapa
  ilustrativo" que pareça dado real. Se o usuário não tiver a imagem, deixe um
  espaço marcado `{{mapa: o que ele deve mostrar}}` no slide.

## Gerando o PDF

O LinkedIn pede PDF, em 1080x1350 (proporção 4:5, que ocupa mais espaço no
feed), com menos de 100 MB e menos de 300 páginas. Monte como HTML e imprima
em PDF:

```bash
# uma página por slide, 1080x1350, sem margem
# depois: Chrome em modo headless com --print-to-pdf, ou qualquer conversor
# de HTML para PDF que o usuário já use
```

Escreva o HTML com um `<section>` por slide, `width:1080px; height:1350px;
page-break-after:always`, uma única cor de destaque e fonte nunca menor que
28px, porque as pessoas leem isso no celular, em tamanho de miniatura.
Declare `<meta charset="utf-8">` no `<head>` para os acentos saírem certos, e
confira no PDF final se "ç", "ã" e "é" aparecem corretamente.

Se o usuário tiver uma skill de marca ou um guia visual neste projeto, use e
não invente paleta. Em carrossel pessoal, não use logotipo de empresa, a não
ser que o usuário peça.

## Saída

Primeiro, o texto slide a slide, como lista numerada que o usuário lê em dez
segundos. Depois, o **texto do post** que acompanha o carrossel: ele ainda
precisa de duas ou três linhas acima do documento, e essas linhas são o
verdadeiro gancho no feed. Hashtags no limite do `voice.md`. Passe os dois
pelo `/li-human`. Se houver trechos com `[AUTORIZAR]`, liste-os antes.

Exemplo do começo de uma lista de slides:

```
1/9   CAPA     Sua base de clientes mente
               5 checagens geográficas antes de qualquer análise
2/9   EM JOGO  Análise de mercado em cima de coordenada errada aponta,
               com confiança, para o lugar errado.
3/9   CHECAGEM 1 · Pontos empilhados
               Muitos clientes no mesmo ponto quase sempre são geocoding
               no centroide do CEP.
...
```

Só gere o PDF depois que o usuário aprovar o texto.

Nada é enviado ao LinkedIn. O usuário publica o PDF.
