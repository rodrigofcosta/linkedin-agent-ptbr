---
name: li-profile
description: >-
  Dá uma nota de 0 a 100 a um perfil de LinkedIn segundo uma rubrica de 12
  itens e reescreve as partes que perdem pontos: título, sobre, experiência,
  destaques e imagem de capa. Use quando o usuário disser "otimiza meu
  perfil", "avalia meu LinkedIn", "reescreve meu título", "arruma minha seção
  sobre", "optimize my profile", ou colar o perfil perguntando como ele está.
---

# li-profile

Perfil não é currículo. O currículo responde "o que você já fez". O perfil
responde "vale a pena mandar mensagem para essa pessoa?", e responde em uns
quatro segundos, a partir do título e das duas primeiras linhas do "Sobre".

## Antes de avaliar

Leia `~/.claude/linkedin/voice.md`. Dele vêm o posicionamento (seção "Meus
temas"), o público, a formação, as provas que podem ser usadas e a regra de
em nome de quem o usuário fala. Se o usuário tem mais de um cargo ou empresa,
o perfil precisa deixar claro qual é o eixo principal, sem parecer duas
pessoas diferentes.

## Entrada

Peça ao usuário para colar: título, seção "Sobre", cargo atual e as duas
últimas experiências, e dizer se tem imagem de capa e seção de destaques. Um
print do topo do perfil basta para a primeira passada. Não faça login no
LinkedIn em nome dele.

## Dar a nota

Leia o `rubric.json` desta pasta. São doze itens e 100 pontos, cada um com a
descrição do que vale nota máxima. Avalie todos, mostre a tabela e dê o
total. Seja honesto: a maioria dos perfis fica entre 30 e 40 na primeira
passada, e uma nota generosa não serve para nada.

```
NOTA DO PERFIL  41/100

  título                  3/12   só o cargo, sem resultado, sem público
  sobre, 2 primeiras      2/10   abre com "apaixonado por"
  sobre, corpo            4/10   conta a história, não a oferta
  destaques               0/8    vazio
  imagem de capa          0/6    o fundo azul padrão
  ...
```

## Depois, reescrever nesta ordem

Corrija na ordem de pontos perdidos, do maior para o menor. Não reescreva
tudo de uma vez: o usuário vai ter que colar cada parte no LinkedIn.

**1. Título (220 caracteres).** A fórmula que funciona:
`{o que você faz e para quem} | {prova} | {como começar}`. Não é o cargo.
Também não abra com "Ajudo X a Y" nem com "Apaixonado por", que metade dos
perfis brasileiros usa hoje. Dê três opções. As provas vêm do `voice.md`
(por exemplo, anos de mercado ou setores atendidos), nunca inventadas.

**2. "Sobre", as duas primeiras linhas.** Tudo depois da segunda linha fica
atrás do "ver mais" no celular, então essas duas linhas são a seção "Sobre"
inteira para a maioria dos leitores. Elas precisam dizer quem você ajuda e o
que muda para essa pessoa. Nada de "apaixonado", "focado em resultados",
"profissional dinâmico", biografia em terceira pessoa ou abertura com o
próprio nome.

**3. "Sobre", o corpo.** Escrito para um leitor só, tratando por "você".
Estrutura: o problema que ele tem, o que você faz a respeito, uma prova com
número e o próximo passo. Menos de 1.400 caracteres, mesmo com o limite sendo
2.600.

**4. Destaques.** Três itens: o melhor post, a prova mais forte e o jeito de
entrar em contato. A prova pode ser algo que já está no `voice.md`, como uma
reportagem, um case público ou um material de referência. Seção de destaques
vazia são oito pontos perdidos, e é o único lugar do perfil que o usuário
controla por completo.

**5. Experiência.** Cada cargo recebe uma linha de escopo e de dois a três
tópicos que são resultados com números, não atribuições. Experiências com
mais de dez anos viram uma linha só. Para quem tem uma carreira longa, isso
deixa o perfil mais forte, não mais fraco: o que vale é a trajetória somada,
e ela já aparece no título e no "Sobre".

**6. Imagem de capa.** Uma frase de posicionamento e um jeito de entrar em
contato. O fundo azul padrão é o sinal mais claro da página de que não há
ninguém cuidando do perfil. Para quem trabalha com geografia, um mapa ou uma
imagem de satélite com boa composição comunica a área antes de qualquer
palavra.

**7. Perfil em inglês (opcional).** O LinkedIn permite uma segunda versão do
perfil em outro idioma. Se o usuário comenta em posts internacionais, vale
oferecer título e "Sobre" em inglês, adaptados e não traduzidos ao pé da
letra.

## Regras

- **Nunca invente.** Números, clientes e resultados só se estiverem no
  `voice.md` ou se o usuário fornecer. Se faltar, use `{{seu número}}` e
  avise.
- **Clientes, parcerias e certificações** recebem `[AUTORIZAR]`, conforme a
  regra do `voice.md`.
- **Português de verdade:** nada de construções traduzidas do inglês e nada
  de aportuguesamentos que o `voice.md` proíbe.

## Saída

Tabela de notas e, em seguida, as reescritas como blocos prontos para copiar,
na ordem de correção, todas já passadas pelo `/li-human` (em inglês, só o
`humanize.py`). Se houver trechos com `[AUTORIZAR]`, liste-os antes dos
blocos.

Reavalie no final e mostre a diferença com honestidade: se a reescrita chega a
88 e não a 98, diga 88, e diga do que dependem os pontos restantes
(normalmente recomendações, uma imagem de capa de verdade e histórico de
posts, coisas que nenhuma reescrita consegue criar).

Esta skill não salva nada no LinkedIn. O usuário cola cada seção.
