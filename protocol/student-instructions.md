# Instruções aos estudantes (fichamento manual)

Você receberá, para cada artigo atribuído (IDs `A01…`; no piloto, o
`artigo-piloto`):

1. O **PDF numerado do artigo** (`*-numerado.pdf`) — o artigo original
   aparece ao centro da página e cada linha de texto tem um rótulo na
   margem esquerda no formato **`p.N Lnnn`** (página + número de linha
   global). Quando linhas ficam muito juntas (tabelas, figuras), o rótulo
   mostra um intervalo (`p.15 L846-857`).
2. O **link do formulário** —
   `https://ai-human-fichamento-protocol-form-s.vercel.app/` — onde você
   preencherá e enviará o fichamento. O pool de teorias candidatas já vem
   embutido nele.

> **Por que o PDF é numerado?** A IA que produzirá o fichamento rival
> lê o artigo com a mesma numeração `p.N Lnnn`. Citar dessa forma garante
> que você e a IA apontem para exatamente a mesma linha — é o que torna
> a comparação justa e auditável.

## Antes de começar

Ao abrir o formulário, a **primeira tela é o Termo de Consentimento
(TCLE)**. Leia por completo e marque *"Li e aceito participar"* — só
então o formulário aparece. Se preferir não participar, marque a outra
opção e avise a coordenação (não há qualquer prejuízo).

## Como fichar

Leia o artigo **integralmente** antes de fichar. Depois preencha o
formulário seção a seção.

### Referências à fonte — sempre no formato `p.N Lnnn`

As afirmações do fichamento devem apontar para o texto do artigo.
Escreva a referência **entre parênteses, dentro da própria frase** —
ex.: *"a empresa adotou mecanismos formais de controle do planejamento
(p.8 L356-361)"*.

| formato | exemplo | quando |
|---|---|---|
| `p.N Lnnn` | `(p.5 L165)` | uma linha específica — **preferido** |
| `p.N Lnnn-mmm` | `(p.5 L165-170)` | trecho contíguo |
| `p.N` | `(p.12)` | só se a referência cobrir a página toda |

Não basta dizer a página quando a afirmação vem de uma linha ou trecho —
o juiz vai conferir suas referências no mesmo PDF numerado. As
referências são importantes, mas a falta delas **não bloqueia** o envio.

### Seção de teorias (instrumento fechado)

O formulário lista as **teorias candidatas** (T1, T2…) com nome e
autores. Para **cada uma**, escolha um veredito:

| veredito | significado | evidência |
|---|---|---|
| **USA** | a teoria estrutura o argumento/modelo/hipóteses | escreva onde ela aparece — `p.N Lnnn` + trecho literal |
| **DISCUTE** | debatida/citada substantivamente, sem estruturar | idem |
| **NÃO USA** | ausente ou menção meramente decorativa | — |

- Em dúvida entre **USA** e **DISCUTE**, pergunte: *"remover esta teoria
  quebraria o argumento do artigo?"* Se sim → **USA**.
- **Faltou teoria no pool?** Pode acontecer — a lista foi montada antes
  da leitura e não cobre tudo. Se o artigo **usa ou discute** uma teoria
  não listada, registre-a no campo de "outras teorias", com nome e
  referência. Isso conta pontos a seu favor: mostra leitura além do
  checklist.

### Demais seções

Livres, conforme o formulário. Em conceitos e achados, **cite linha**
(`p.N Lnnn`) junto do texto e inclua o trecho literal quando possível —
os juízes podem conferir diretamente no PDF numerado.

No **resumo executivo**, o formulário mostra um **texto-modelo completo
do artigo-piloto** como referência do que a seção espera (problema,
método, achados e contribuição, com referências entre parênteses) —
leia-o antes de escrever o seu.

## Depois de terminar o fichamento — meta-avaliação e log

Dois blocos finais, **respondidos por você sobre o seu próprio
trabalho** (não são mostrados aos juízes):

1. **Auto-avaliação** — sua nota **1–7 em cada uma das 7 seções**, usando
   as mesmas âncoras que os juízes usarão (elas aparecem em cada seção).
   Seja honesto: o objetivo é medir o quanto cada pessoa consegue avaliar
   a própria produção — o gap entre a sua nota e a do juiz é o dado.
2. **Registro reflexivo** — quatro respostas curtas e sinceras sobre as
   dificuldades e barreiras da tarefa:
   - *Quais dificuldades ou barreiras você encontrou com o artigo e o
     tema, o conteúdo que leu?*
   - *Quais dificuldades ou barreiras você encontrou com o formato da
     pesquisa, o instrumento?*
   - *Se você fosse refazer, o que mudaria na sua abordagem?*
   - *Você usou alguma ferramenta de IA ou auxílio externo para ler ou
     fichar? Se sim, qual e como?* (a pergunta existe para auditoria —
     responda com franqueza; ver "Regras" abaixo)
3. **Tempo total** — última pergunta do formulário: sua estimativa do
   tempo total, em minutos (leitura do artigo + produção). Estimativa
   honesta, não precisa cronometrar. Esse dado é de pesquisa
   (custo-tempo do trabalho humano, para compararmos com o custo de usar
   IA) e **não** será mostrado aos juízes.

## Enviando

Clique em **"Enviar meu fichamento"** — o formulário transmite suas
respostas diretamente à coordenação, em formato já auditável. A tela
final confirma o envio.

Se o envio automático falhar, o formulário **baixa um arquivo `.json`**
com tudo preenchido — nesse caso, **anexe esse arquivo a um e-mail**
para a coordenação.

## A fase piloto

A primeira atividade é um **piloto**: todos os estudantes ficham o mesmo
artigo (o `artigo-piloto`, fora do corpus do estudo). Depois, **um
fichamento será sorteado** (com seed registrada) e os juízes o avaliarão
para **calibrar as âncoras da rubrica** — a régua final sai dessa
calibração e fica congelada para as rodadas oficiais. Ou seja: seu
fichamento do piloto conta para a pesquisa *e* define a qualidade da
régua.

## Regras

- Escreva em pt-BR. Nada que não esteja no artigo.
- **Não** consulte o fichamento da IA nem o de colegas — a independência
  é o que torna a comparação válida.
- Não use IA para ler ou fichar o artigo — o objeto de estudo é
  justamente o fichamento humano. Se algo escapar a essa regra, declare
  na última pergunta reflexiva.

## Após a Rodada 1

Você receberá o `checklist-students.md`, derivado dos padrões de erro da
R1 — é ele que operacionaliza a calibração humana.
