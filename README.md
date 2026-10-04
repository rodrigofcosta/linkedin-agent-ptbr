# LinkedIn agent skill, em português do Brasil

Onze skills do Claude que cuidam de uma conta no LinkedIn, adaptadas para o
português do Brasil. Grátis, licença MIT, sem cadastro, sem chave de API, sem
nada para conectar.

Uma delas escreve seus posts a partir de 21 fórmulas de gancho. Uma comenta
nos posts dos outros. Uma cuida das respostas nos seus. Uma dá nota de 0 a 100
ao seu perfil e reescreve o que perdeu pontos. Uma planeja a semana: o que
postar, quando, e com quem interagir.

E uma é o humanizador, que é o que torna as outras utilizáveis. Ele tira
travessões, vocabulário batido de IA e caracteres invisíveis de um rascunho e
depois pontua o resultado num painel de cinco checagens, antes de você ver o
texto.

Nada é publicado sem o seu "sim". Estas skills escrevem. Quem publica é você.

Esta é uma adaptação do [linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill),
de Jake Schincariol. Não é uma tradução literal: o léxico do humanizador foi
refeito para o português, os scripts foram corrigidos para lidar com acentos,
e as skills ganharam regras de tom comercial, idioma e uso de repertório.

## Instalação

Cole isto no Claude:

```
https://github.com/SEU-USUARIO/linkedin-agent-ptbr

Instale esta skill e confirme que o /li-post funciona.
```

Ou faça você mesmo, no Claude Code:

```bash
git clone https://github.com/SEU-USUARIO/linkedin-agent-ptbr.git
cp -r linkedin-agent-ptbr/skills/li-* ~/.claude/skills/
```

Ou como plugin:

```
/plugin marketplace add SEU-USUARIO/linkedin-agent-ptbr
/plugin install linkedin-agent
```

Para usar só num projeto, e não em todos: copie as mesmas pastas para o
`.claude/skills/` do seu repositório. Sem Claude Code? Cole qualquer
`SKILL.md` no começo de uma conversa e ele funciona como um modo. Você perde
os dois scripts Python, que são a maior parte do valor do `/li-human`, mas o
resto funciona.

Depois, dedique dez minutos ao `templates/voice.md`. Copie para
`~/.claude/linkedin/voice.md` (no Windows,
`C:\Users\SEU-USUARIO\.claude\linkedin\voice.md`) e preencha, ou cole três
posts seus no Claude e diga "escreva meu voice.md a partir destes". Todas as
skills leem esse arquivo. Sem ele, tudo sai soando como todo mundo.

## O que o voice.md controla

Além da voz, o `voice.md` define regras que todas as skills respeitam:

- **Temas**: os pilares sobre os quais você escreve, e o filtro que impede
  posts fora deles.
- **Tom comercial por tipo de conteúdo**: quanto de venda cabe nos seus posts,
  nos comentários em posts da sua empresa e nos comentários em posts de
  outras pessoas.
- **Provas**: números e cases reais que você aceita assinar. As skills nunca
  inventam nenhum.
- **Autorização**: qualquer trecho que cite cliente, parceria, certificação
  ou assunto interno sai marcado com `[AUTORIZAR]` para você aprovar.
- **Idioma**: posts em português; comentários e respostas no idioma do post
  ou de quem escreveu.

## As onze

| comando | o que faz |
| --- | --- |
| `/li-post` | Transforma uma ideia num post. Três opções de gancho entre 21 fórmulas, um rascunho completo, humanizado antes de você ver. |
| `/li-comment` | Comentários nos posts dos outros. Nove tipos, escolhidos pelo que o post realmente é, com a carga comercial certa para cada autor. Nunca "Excelente post!". |
| `/li-reply` | As respostas nos comentários do seu post. Separa cada comentário em lead, substância, par, apoio e ruído, e escreve nessa ordem. |
| `/li-profile` | Dá nota ao seu perfil numa rubrica de 12 itens, de 0 a 100, e reescreve começando pelo que mais perde pontos. |
| `/li-plan` | A semana. O que postar, quando postar e as 10 pessoas com quem interagir. Grava em `~/.claude/linkedin/plan.md`. |
| `/li-human` | O humanizador. Dois scripts que rodam de verdade. Veja abaixo. |
| `/li-carousel` | Posts de documento. Texto slide a slide, a capa que faz deslizar e o PDF para subir, com regras para mapas e imagens de satélite. |
| `/li-repurpose` | Um vídeo, artigo, portfólio ou transcrição vira uma semana de posts que se sustentam sozinhos. |
| `/li-dm` | O convite de 200 caracteres, a primeira mensagem e os dois acompanhamentos. Dois. |
| `/li-inbox` | Faz a triagem da caixa de mensagens em lead, recrutador, par, pedido e spam, aponta sequências automáticas e alerta sobre golpes. |
| `/li-audit` | Análise do que você já publicou. Ordena por taxa de engajamento e múltiplo de alcance, não por impressões. |

## O humanizador

O `/li-human` traz dois scripts Python sem dependências. Eles rodam na sua
máquina, sobre o seu texto, e nada é enviado.

```bash
python3 humanize.py rascunho.txt --report      # limpa e mostra cada mudança
python3 detect.py rascunho.txt                 # pontua, cinco checagens
python3 detect.py antes.txt depois.txt         # comprova a diferença
python3 humanize.py rascunho.txt --keep-dash   # mantém o travessão
```

O que sai automaticamente:

- **Caracteres invisíveis.** Zero-width spaces e joiners, word joiners,
  hífens suaves, BOMs, caracteres Unicode de tag, espaços rígidos e
  estreitos. Seu teclado não produz nada disso. Eles sobrevivem ao copiar e
  colar e são invisíveis em qualquer editor.
- **Tipografia.** Travessão vira vírgula (a menos que você use `--keep-dash`,
  porque em português o travessão é pontuação legítima), meia-risca vira
  hífen, aspas curvas e angulares viram retas, o caractere de reticências vira
  três pontos.
- **O léxico.** Mais de 130 palavras e expressões batidas de IA em português,
  com substituições simples que respeitam gênero e número: alavancar,
  robusto, inovador, sinergia, holístico, "além disso", "vale ressaltar que",
  "no cenário atual", "em constante evolução", "fica a reflexão". Maiúsculas
  preservadas, URLs intactas, e a frase volta a começar com maiúscula quando
  a abertura é apagada. Está no `slop.json` e foi feito para ser editado.

Termos técnicos com uso legítimo ficaram de fora de propósito, como
"ecossistema", "divisor de águas" e "jornada de trabalho".

O que é apontado em vez de corrigido: "Não é só X, é Y", "Não é sobre X. É
sobre Y.", tríades, perguntas retóricas de uma linha, muro de hashtags, isca
de engajamento automática ("Concorda?", "O que você acha?") e frases de
tamanho uniforme. Mudar o formato de uma frase exige julgamento, então isso
volta para você reescrever, em vez de ser mutilado por uma regex.

As cinco checagens, de 0 a 100, quanto maior mais humano:

| checagem | o que mede |
| --- | --- |
| BURSTINESS | variação no tamanho das frases. Modelos escrevem por igual. |
| SPECIFICITY | números, nomes, siglas e valores em reais a cada 100 palavras |
| SLOP DENSITY | ocorrências do léxico a cada 100 palavras |
| FINGERPRINT | invisíveis, travessões e aspas curvas a cada mil caracteres |
| VOICE | marcas de oralidade, pronomes pessoais e estruturas denunciadoras |

O veredito dá peso de 60% à média e 40% à checagem mais fraca, porque um
detector só precisa de um sinal para disparar.

Na adaptação para o português, o `detect.py` passou a contar corretamente
palavras com acento e hífen, a reconhecer nomes com inicial acentuada, siglas
e valores em reais, e a usar marcas de oralidade e pronomes do português no
lugar das contrações do inglês, com pesos ajustados para não punir texto
profissional bem escrito.

Num teste com um parágrafo típico de IA sobre inteligência geográfica, o
texto original levou 17,2 (FLAGGED). Depois do `humanize.py`, com as
estruturas apontadas ainda sem reescrever, subiu para 29,6. Um post escrito
por um especialista, com números e linguagem direta, levou 91,3 (PASS). O
último trecho até o PASS é, de propósito, trabalho do autor.

## As letras miúdas, que são a parte honesta

Estas skills não publicam no LinkedIn, e não deveriam. Não existe API oficial
para publicar num perfil pessoal sem um aplicativo parceiro aprovado, e
automatizar o site com navegador ou ferramenta de terceiros viola os Termos
de Uso do LinkedIn e leva à restrição da conta. Por isso toda skill termina
do mesmo jeito: um bloco pronto para copiar, e você cola. Isso não é uma
limitação acrescentada depois, é o projeto. E é por isso que a trava de
aprovação é real, e não uma configuração.

As cinco checagens são heurísticas locais, não APIs de detectores. Elas são
modeladas nos sinais que os detectores públicos observam e rodam inteiramente
na sua máquina. Não são GPTZero, Originality, Copyleaks, Winston ou Turnitin,
não chamam esses serviços e não podem prometer o veredito deles. Corrigir o
que elas medem tende a mexer nessas notas, porque todos medem as mesmas
coisas de fundo. Essa é toda a afirmação. Ninguém pode vender "indetectável"
com honestidade, e quem vende está vendendo outra coisa.

A limpeza de caracteres invisíveis é real e é restrita. Ela remove os
caracteres de largura zero e de formatação que aparecem em texto gerado e
sobrevivem ao copiar e colar. É uma impressão digital real e verificável. Não
é uma afirmação sobre derrotar um esquema criptográfico de marca d'água, e
este repositório não faz essa afirmação.

Nada aqui inventa. Nenhuma métrica, cliente ou resultado inventado vai com o
seu nome. Se um rascunho precisa de um número que você não deu, ele volta com
`{{seu número}}` e um aviso, sempre.

## Arquivos

```
skills/li-post/hooks.json        21 fórmulas de gancho: modelo, exemplo, para que serve, como é estragada
skills/li-human/slop.json        o léxico em português: palavras, expressões, invisíveis e estruturas
skills/li-human/humanize.py      as três passadas de limpeza
skills/li-human/detect.py        o painel de cinco checagens
skills/li-profile/rubric.json    a nota de 100 pontos do perfil
templates/voice.md               o seu perfil de voz. Preencha primeiro.
```

## Créditos

Original de Jake Schincariol, [opusjake.ai](https://opusjake.ai). O texto
completo sobre o projeto original está em
[opusjake.ai/r/linkedin-agent](https://opusjake.ai/r/linkedin-agent).

Adaptação para o português do Brasil por Rodrigo Costa.

## Licença

MIT, a mesma do original. O arquivo `LICENSE` com o aviso de copyright do
autor original foi mantido, como a licença exige. Pegue, mude, distribua.
