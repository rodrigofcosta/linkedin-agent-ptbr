---
name: li-repurpose
description: >-
  Transforma um material longo (vídeo, podcast, newsletter, artigo de blog,
  transcrição, palestra, portfólio, apresentação ou reunião com cliente) numa
  semana de posts de LinkedIn. Use quando o usuário disser "reaproveita isso",
  "transforma isso em posts", "tenho um vídeo/artigo/transcrição",
  "repurpose this", ou colar um conteúdo longo e quiser levá-lo para o
  LinkedIn.
---

# li-repurpose

Um bom material longo tem de quatro a seis posts dentro dele. A maioria das
pessoas tira um e joga o resto fora.

## Antes de começar

Leia `~/.claude/linkedin/voice.md`: voz, temas, regras de uso das provas e
tom comercial. Elas valem para cada post que sair daqui.

## Entrada

Uma transcrição, um artigo, uma newsletter, um roteiro, um resumo de
reunião, um PDF de apresentação ou portfólio. Se o usuário mandar um link do
YouTube e houver uma ferramenta de transcrição disponível na sessão, use;
caso contrário, peça para colar o texto. Leia o material inteiro antes de
extrair qualquer coisa.

## De onde veio o material

Antes de extrair, identifique a origem, porque ela muda as regras:

| origem | cuidado |
| --- | --- |
| **Do próprio usuário** (palestra, vídeo, artigo dele) | Pode usar livremente, na voz dele. |
| **De uma empresa do usuário** (blog, portfólio, apresentação institucional) | O post pessoal não pode soar como material da empresa. Tire o "nós", a linguagem de vendas e qualquer chamada para contratar. Os cases viram repertório, seguindo as regras do `voice.md`: nada de "eu fiz", e empresa ou cliente só com `[AUTORIZAR]`. |
| **Material marcado como confidencial ou privado** | Não use sem autorização explícita do usuário. Pergunte antes de extrair. |
| **De terceiros** (artigo, estudo, vídeo de outra pessoa) | O post é a leitura do usuário sobre o material, nunca uma cópia. Não reproduza trechos, reescreva com as próprias palavras, cite a fonte e nunca apresente dados de terceiros como se fossem experiência do usuário. |

## Extraia, não resuma

O resumo de um vídeo não é um post. Ninguém quer o resumo. Percorra o
material e tire as coisas que se sustentam sozinhas:

| o que tirar | o que é |
| --- | --- |
| **Afirmações** | toda frase que começaria uma discussão |
| **Números** | todo valor, custo, duração, percentual, área, extensão |
| **Histórias** | todo momento com uma pessoa, uma cena e um custo |
| **Mecanismos** | toda explicação do tipo "funciona assim..." |
| **Erros** | toda admissão de algo que deu errado |
| **Frases** | toda frase que já pode ser citada do jeito que está |

Fique só com o que tem olhar geográfico, como o `voice.md` exige. O que não
passa pelo território, pela localização ou pelo dado espacial fica de fora,
mesmo que seja bom.

Liste o que encontrou, com as contagens, antes de escrever qualquer coisa. Se
o material render menos de quatro itens, ele é fraco, e quatro posts
espremidos dele também serão fracos. Diga isso.

## Depois, monte a semana

Cada item extraído vira um post, e cada post precisa se sustentar sozinho: o
leitor não viu o vídeo e nunca vai ver. Nunca escreva "como falei no meu
último vídeo" ou "como está no nosso portfólio". O post é a coisa.

Atribua uma fórmula de gancho do `li-post/hooks.json` a cada um e varie:
cinco posts de uma mesma fonte com o mesmo formato de gancho parecem fábrica
de conteúdo.

Ordene ao longo da semana: a afirmação mais forte primeiro, a história no meio
da semana e o post de mecanismo por último, quando quem gostou dos anteriores
já está esperando por ele. Use os horários e o dia do plano da semana
(`~/.claude/linkedin/plan.md`), se existir.

## Saída

```
FONTE: Portfólio da Novaterra (29 páginas, PDF)
ORIGEM: empresa do usuário  ·  cases viram repertório, sem tom comercial

ENCONTRADO  3 afirmações, 9 números, 2 histórias, 4 mecanismos, 0 erros, 2 frases

SEMANA
TER  #1  Opinião Contrária   Licenciamento não trava por falta de dado. Trava por dado espalhado.
QUA  #10 O Comprovante       Uma linha de transmissão de 2.420 km começa num mapa de uso do solo.
QUI  #9  Começo de Cena      Em 2008, o IBAMA pediu algo que nunca tinha pedido numa grande hidrelétrica.
SEX  #2  Número Revelado     Mais de 1.000 tarefas num projeto ambiental. Nenhum e-mail.

Diga "escreve terça" e eu monto o rascunho.
```

Depois, escreva sob pedido, um de cada vez, cada um passando pelo `/li-post`
e pelo `/li-human`. Não entregue quatro posts prontos de uma vez: eles vão
soar todos iguais, e o usuário não vai editar nenhum.
