# Protocolo de Validação IA–Humano para Fichamentos

**Versão 1.0.0** — status: *draft para pré-registro (OSF)*
Congelar antes da Rodada 1. Toda alteração posterior é registrada em
[`diary/`](../diary) e via `git tag` (`protocol-v1.1`, …).

## 1. Objetivo

Estabelecer um protocolo de validação iterativa IA–humano, replicável e de
ciência aberta, para produção de fichamentos estruturados de artigos
científicos em revisões de literatura na escala de centenas de documentos —
permitindo ao pesquisador concentrar tempo em reflexão e análise teórica, e
medir objetivamente onde IA e humano são melhores.

## 2. Desenho

Validação **às cegas** em **duas rodadas**:

- Para cada artigo, dois fichamentos **independentes** (IA via API + humano)
  são avaliados por juízes que **não sabem qual é qual**.
- A **Rodada 1** é o baseline: identifica lacunas e padrões de erro.
- Entre rodadas ocorre a **calibração**: refina-se o prompt da IA e cria-se
  checklist para os estudantes — o conteúdo do refinamento é, ele próprio,
  um achado do estudo.
- A **Rodada 2** mede o impacto da calibração.

**Alocação por rodada**: os 32 artigos são distribuídos entre R1 e R2 por
**sorteio com seed registrada** (equilibra dificuldade entre rodadas —
condição para ler "efeito da calibração" sem confundir com mix de artigos).

```
Juízes indicam artigos ──► Corpus (16/rodada)
                               │
              ┌────────────────┴────────────────┐
        IA (pipeline auditável)           Estudantes
        PDF→MD pág/linha → fichamento     fichamento manual + tempo
              └────────────────┬────────────────┘
                     Cegamento (posições A/B)
                               │
                    4 juízes avaliam às cegas
            BARS 1–7 por seção + taxonomia de erros
                    + preferência A/B (métrica primária)
                               │
        R1 baseline ──► calibração ──► R2 ──► análise final
```

## 3. Participantes

| papel | n | função |
|---|---|---|
| Juízes (indicação) | 4 | indicam 4 artigos cada/rodada → 16 artigos/rodada (8 por juiz no total) |
| Estudantes | ~4–5 por juiz | produzem fichamentos manuais (~2 artigos cada/rodada) |
| IA (API) | **1 modelo fixo** | produz fichamentos dos mesmos artigos; provider/modelo/versão/temperature registrados em `generator.*` |

**Modelo único**: o objeto do estudo é **calibração e limitação de cada
produtor** (estudante × máquina), não benchmark entre LLMs. A IA é um
instrumento do experimento — especificada como qualquer instrumento:
modelo fixo escolhido por representatividade prática, versão e
temperature registradas. O protocolo é modelo-agnóstico por desenho
(`--model` parametriza qualquer provider); replicação cruzada de modelos
fica como trabalho futuro sugerido.
| Juízes (avaliação) | 4 | avaliam **somente os artigos que indicaram**: 4 artigos × 2 = **8 fichamentos/rodada/juiz**, às cegas |
| Coordenador | 1 | não-juiz; executa sorteios, guarda mapas privados |

**Por que avaliação só pelo nominador**: cada juiz avalia exatamente os
artigos que domina — maximiza a verificação linha-a-linha e reduz a carga
(8 vs. 32 avaliações). Custo assumido: 1 rater por fichamento → sem
concordância inter-rater clássica, e severidade-do-juiz fica associada ao
seu conjunto de artigos. A comparação principal (IA vs. humano) é protegida
pelo **pareamento intra-juiz**: o mesmo juiz avalia A e B do mesmo artigo.

### 3.1 Atribuição artigo→estudante (grupos cruzados)

Estudantes se organizam em grupos por orientador (`G1–G4`, em
`data/private/groups.json`). Regra: **artigos indicados por J_i são
fichados por estudantes de OUTRO grupo** (`cross` map, escolhido pela
área mais próxima). O sorteio dentro do grupo destino é feito pelo
coordenador via `fichamento assign --seed N`, e a tabela fica em
`data/private/assignments-roundN.json` (privada até o descegamento).

Por quê: se o juiz soubesse qual estudante fichou seu artigo indicado, o
cego A/B vazaria (viés de lealdade + adivinhação por estilo). Com grupos
cruzados, nem o nominador nem o orientador conseguem ligar fichamento a
autor.

Regra complementar: orientadores **não coacheiam** os fichamentos durante
o estudo (treino geral de método, ok; feedback sobre fichamento
específico, não).

**Conflito de interesse (juiz = orientador/coautor do estudo).** Se um
juiz acumular papel de orientador ou coautor, duas proteções se aplicam:
(a) com grupos cruzados + avaliação-por-nominador, ele **nunca avalia
fichamentos dos próprios orientandos** (o `assign` recusa cross-map que
roteie para o grupo dele); (b) ele nunca tem acesso ao blinding map nem
às assignments (coordenador é o único guardião). No relato: declarar o
papel duplo e reportar a **análise de sensibilidade**
`fichamento analyze --all --exclude-judge J{n}` — resultados devem se
manter sem as avaliações dele.

Pseudonimização: juízes `J1–J4`, estudantes `S01–S…`. A tabela
identidade↔pseudônimo fica em `data/private/participants.csv` (nunca commitada).

## 4. Pipeline de ingestão (auditoria de leitura integral)

Antes de qualquer fichamento de IA, cada PDF passa por conversão rígida
para Markdown com **marcação de página e linha** (`fichamento pdf2md`):

```
<<p.3>>
L01| However, institutional pressures ...
L02| We argue that ...
```

- Cada página vira um bloco `<<p.N>>`; cada linha é `Lnn|`.
- Gera-se `data/articles/manifests/A{nn}.ingestion.json` com: sha256 do PDF e
  do MD, nº de páginas do PDF vs. extraídas, linhas/chars por página, método
  por página (`text`/`ocr`/`empty`/`manual`), estimativa de tokens, tool+versão.
- Páginas sem camada de texto → OCR (tesseract) + flag `needs_review`.
- **Gate**: `fichamento generate` só roda com `coverage_complete=true` e
  checksum do MD batendo. Override (`--force`) é possível mas fica
  **registrado** no manifest (`overrides[]`) e no fichamento gerado.
- Fichamentos citam a fonte de cada elemento como `p.N`/`Lnn`
  (`source_refs`), permitindo auditoria linha-a-linha pelos juízes.

### 4.1 Pool de teorias candidatas (seção fechada)

`fichamento candidates` roda **antes** do fichamento: a IA extrai os
candidatos a teoria (`usa`/`discute`/`does_not_use`) para
`data/candidates/roundN/A{nn}.candidates.json` + um checklist em Markdown
(`A{nn}.pool.md`) que os estudantes recebem junto ao PDF. O arquivo do
pool é **editável para curadoria** (itens adicionados com
`origin:"researcher"`; desativar com `active:false` em vez de deletar —
preserva o que a IA propôs).

## 5. Estrutura do fichamento

1. **Resumo executivo** — síntese em ~300 palavras
2. **Questão de pesquisa** — o que o artigo pergunta
3. **Teorias presentes** — *instrumento fechado*: pool de candidatos
   gerado previamente (IA → curadoria opcional); cada item recebe veredito
   `uses` / `discusses` / `does_not_use` com `source_refs` obrigatórios
   para vereditos positivos. Teorias fora do pool → lista livre (mede
   omissões do pool). IA responde o mesmo pool numa 2ª chamada →
   concordância IA×humano item a item.
4. **Conceitos-chave** — 3–4 construtos com definições + quote literal
5. **Metodologia** — tipo de estudo, delineamento, tipo/tamanho de
   amostra, setor, período, técnicas de análise
6. **Achados principais** — resultados e proposições + quote literal
7. **Contribuição** — avanços teóricos e utilidade prática
8. *Tempo de fichamento* — apenas estudante (metadado `generator`)

Template completo: [`fichamento-template.md`](fichamento-template.md).
Schema: [`../schemas/fichamento.schema.json`](../schemas/fichamento.schema.json).

## 6. Avaliação (instrumento dos juízes)

Definida em [`rubric.md`](rubric.md) — **congelar antes da R1**.

- **BARS 1–7** por seção, com âncoras verbais em 1, 4 e 7 (comportamentos
  observáveis por nota — reduz variância inter-rater).
- **Taxonomia de erros** marcável por seção: `hallucination`, `omission`,
  `misinterpretation`, `misattribution`, `terminology`, `extrapolation`,
  `invalid_source_ref`, `other`. Alimenta diretamente a calibração.
- **Preferência A/B** por artigo (métrica comparativa primária) + razão.
- Qualitativas por fichamento: "há algo que questionaria?" / "o que faltou?".

## 7. Cegamento

`fichamento blind --round N --seed S` embaralha (seed registrada) a posição
A/B dos fichamentos de cada artigo e emite:

- `data/private/blinding-map-roundN.json` — blind_id → fichamento → fonte
  (**publicar só após descegamento**);
- `data/private/judge-packets/` — pacotes para os juízes.

Metadados que revelariam a fonte (provider, tempo de fichamento) **nunca**
aparecem no material do juiz.

## 8. Calibração (entre R1 e R2)

1. Análise R1: seções mais fracas por fonte, taxonomia de erros mais
   frequente, padrões qualitativos.
2. Refina `prompts/` → nova versão semver + changelog (o *diff* do prompt é
   um achado do estudo).
3. Cria/atualiza `checklist-students.md` a partir das lacunas humanas.
4. Registrar tudo em `diary/` e tag `calibration-r1`.

## 9. Plano de análise

**Quantitativa**
- Média/mediana BARS por seção × fonte (IA vs. humano) × rodada.
- Teste pareado por seção (Wilcoxon signed-rank; mesmo juiz+artigo avalia
  ambos os fichamentos) + tamanho de efeito.
- Taxa de cada tipo de erro × fonte (qui-quadrado/Fisher).
- Preferência A/B: teste binomial; modelo Bradley–Terry com produtores
  (`S01–S10` + IA) como "jogadores" → ranking de produtores.
- Concordância inter-rater: N/A no desenho nominator-only (1 rater/item);
  confiabilidade vem do pareamento intra-juiz. Se 2º rater por artigo for
  adicionado depois, α ordinal por seção está implementado.
- **Pool de teorias**: concordância IA×humano item a item; taxa de
  rejeição de candidatos (alucinação do pool) e adições humanas
  (omissões do pool).
- Evolução R1→R2: Δ de médias, Δ de taxas de erro, Δ de preferência.

**Qualitativa**
- Codificação temática das respostas abertas → padrões de erro, lacunas
  sistemáticas, determinantes da preferência dos juízes.

## 10. Reprodutibilidade e ciência aberta

- Tudo versionado: protocolo, schemas, prompts (semver), código, dados.
- Cada fichamento de IA registra provider, modelo, `prompt_version`,
  temperatura, seed (se houver), timestamp e tokens.
- Seeds de cegamento registradas; pacotes regeneráveis deterministicamente.
- Recomendado: **pré-registro no OSF** do design + instrumento + plano de
  análise antes da R1; após descegamento, publicar blinding maps e dados.
- CI valida todos os JSONs contra os schemas a cada push.

## 11. Ética

- Consentimento informado de juízes e estudantes antes da R1.
- Pseudônimos em todos os artefatos; identidades nunca publicadas.
- Tempo de fichamento é metadado de pesquisa, não exposto aos juízes.
- PDFs não são redistribuídos (copyright); apenas metadados + MD derivados
  mediante verificação de direitos.
