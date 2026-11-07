# Especificação do Google Forms — fichamento do estudante

**Uma submissão = um fichamento humano.** No piloto, `article_id` é fixo
(`PILOTO`); nas rodadas, o estudante indica o artigo atribuído.

O formulário substitui o preenchimento manual do JSON — os campos abaixo
são os **nomes canônicos das colunas** no CSV exportado (copie os títulos
exatamente; ver `student-column-map.json`). O texto de ajuda sugerido vai
em "descrição" de cada pergunta.

## Seção 0 — Identificação

> `full_name`, `age`, `gender`, `program` caracterizam a amostra e ficam
> **fora do fichamento** — o conversor os grava apenas em
> `data/private/participants.csv` (gitignored). Juízes nunca os veem.

| título da pergunta (canônico) | tipo | descrição |
|---|---|---|
| `full_name` | Resposta curta | "Nome completo." |
| `age` | Resposta curta (número) | "Idade (anos)." |
| `gender` | Múltipla escolha | `feminino` / `masculino` / `outro` / `prefiro não informar` |
| `program` | Múltipla escolha | `mestrado` / `doutorado` |
| `participant_id` | Múltipla escolha `S01`…`S{nn}` | "Seu identificador atribuído pela coordenação." |
| `article_id` | Múltipla escolha | Piloto: opção única `PILOTO`. Rodadas: `A01`…`A16`. |
| `consent` | Caixa de seleção obrigatória | "Declaro que li as instruções, produzi o fichamento sozinho(a) e não consultei fichamentos de IA ou de colegas." |

## Seção 1 — Resumo executivo

> A seção exibe um **texto-modelo completo do artigo-piloto** (decisão da
> reunião 06/11) como referência do que a seção espera — problema,
> abordagem teórica, método, achados e contribuição, com refs reais
> `(p.N Lnnn)`. O modelo está em `student-fichamento-template.json` e no
> form piloto (seção 3, bloco "Ver texto-modelo").

| título | tipo | descrição |
|---|---|---|
| `executive_summary` | Parágrafo | "Síntese em ~300 palavras: problema, abordagem teórica, método, achados e contribuição. Referências entre parênteses: (p.N Lnnn)." |

## Seção 2 — Questão de pesquisa

| título | tipo | descrição |
|---|---|---|
| `research_question` | Parágrafo | "A pergunta que o artigo busca responder, formulada precisamente. Inclua (p.N Lnnn)." |

## Seção 3 — Teorias (instrumento fechado)

Descrição da seção: *"Para cada teoria do pool, escolha um veredito.
`uses` = estrutura o argumento (se remover, o argumento quebra);
`discusses` = debatida/citada substantivamente sem estruturar;
`does_not_use` = ausente ou menção decorativa. Para todo veredito
positivo, preencha também `T{n}.evidence` com a linha (p.N Lnnn) e,
idealmente, o trecho literal."*

| título | tipo | descrição |
|---|---|---|
| `theory_verdicts` | **Grade de múltipla escolha**: linhas `T1`…`T{nn}`, colunas `uses` / `discusses` / `does_not_use` | uma resposta por linha, obrigatório |
| `T{n}.evidence` | Resposta curta (uma por item do pool, opcional) | "Se marcou uses/discusses: refs `(p.N Lnnn)` + quote literal." |

> No Forms: a grade vira uma coluna por linha no CSV — o mapa de colunas
> resolve. `T{n}.evidence` junta `source_refs` + `quote` num campo só;
> o conversor separa refs (parênteses) do restante (quote).

| título | tipo | descrição |
|---|---|---|
| `extra_theories` | Parágrafo (opcional) | "O artigo usa ou discute alguma teoria que NÃO está no pool? Liste: nome — tradição — uses/discusses — (p.N Lnnn). Uma por linha. Encontrar o que faltou conta pontos a seu favor." |

## Seção 4 — Conceitos-chave

3 slots obrigatórios + 1 opcional. Por slot `key_concept.{i}` (i=1..4):

| título | tipo | descrição |
|---|---|---|
| `key_concept.{i}.concept` | Resposta curta | nome do construto |
| `key_concept.{i}.definition` | Parágrafo | como o artigo define/usa |
| `key_concept.{i}.evidence` | Resposta curta | `(p.N Lnnn)` + quote literal |

## Seção 5 — Metodologia

| título | tipo | descrição |
|---|---|---|
| `methodology.study_type` | Múltipla escolha: `teórico`, `empírico`, `simulação`, `revisão`, `outro` | |
| `methodology.design` | Resposta curta | "delineamento (ex.: estudo de caso único exploratório)" |
| `methodology.sample_type` | Resposta curta | "ex.: profissionais da empresa; N/A se não houver" |
| `methodology.sample_size` | Resposta curta | "número ou N/A" |
| `methodology.sector` | Resposta curta | "setor/indústria dos dados" |
| `methodology.period` | Resposta curta | "período coberto pelos dados" |
| `methodology.methods` | Resposta curta | "técnicas separadas por vírgula (ex.: entrevistas semiestruturadas, análise documental, observação direta)" |
| `methodology.analysis_note` | Parágrafo (opcional) | "como os dados foram analisados" |
| `methodology.source_refs` | Resposta curta | "(p.N Lnnn) da seção de método" |

## Seção 6 — Achados principais

3 slots obrigatórios + 2 opcionais. Por slot `finding.{i}` (i=1..5):

| título | tipo | descrição |
|---|---|---|
| `finding.{i}.finding` | Parágrafo | o achado/proposição |
| `finding.{i}.type` | Múltipla escolha: `empirical`, `proposition`, `model` | |
| `finding.{i}.evidence` | Resposta curta | `(p.N Lnnn)` + quote literal |

## Seção 7 — Contribuição

| título | tipo | descrição |
|---|---|---|
| `contribution.theoretical` | Parágrafo | "avanço teórico que o artigo entrega" |
| `contribution.practical` | Parágrafo | "utilidade prática" |

## Seção 8 — Meta-avaliação (Módulo A)

Descrição: *"Agora avalie o SEU fichamento com a mesma régua dos juízes
(rubric.md): nota 1–7 por seção. Seja honesto — a pesquisa mede o gap
entre sua auto-nota e a nota do juiz. Não será mostrado aos juízes."*

| título | tipo |
|---|---|
| `self_assessment` | **Grade de múltipla escolha**: linhas `executive_summary`…`contribution` (7), colunas `1`…`7` |

## Seção 9 — Log de reflexão (Módulo D)

Descrição: *"Quatro respostas curtas e sinceras sobre a experiência — não
são avaliadas nem mostradas aos juízes."*

| título | tipo |
|---|---|
| `reflection.q1` | Parágrafo — "Quais dificuldades ou barreiras você encontrou com o artigo e o tema, o conteúdo que leu?" |
| `reflection.q2` | Parágrafo — "Quais dificuldades ou barreiras você encontrou com o formato da pesquisa, o instrumento (formulário, PDF numerado, vereditos, referências p.N Lnnn)?" |
| `reflection.q3` | Parágrafo — "Se você fosse refazer este fichamento, o que mudaria na sua abordagem?" |
| `reflection.q4` | Parágrafo — "Você usou alguma ferramenta de IA ou auxílio externo para ler ou fichar? Se sim, qual e como?" |

## Seção 10 — Tempo total

| título | tipo | descrição |
|---|---|---|
| `elapsed_minutes` | Resposta curta (número) | "Última pergunta. Tempo total estimado, em minutos — leitura do artigo + produção do fichamento. Estimativa honesta basta. Dado de pesquisa (custo-tempo), não será mostrado aos juízes." |

## Configuração do Forms

- Não coletar e-mail automaticamente (`participant_id` basta).
- "Editar após envio": desligado.
- Coletar CSV: *Respostas → ⋮ → Fazer o download das respostas (.csv)*.

## Ingestão

```bash
fichamento import-human-csv --round 0 --csv fichamentos.csv \
  --map protocol/forms/student-column-map.json
```

Converte cada linha em `Fichamento` validado
(`schemas/fichamento.schema.json`): monta `content` das seções 1–7,
`generator.self_assessment` da seção 8, `generator.reflection_log` da
seção 9, `elapsed_minutes` da seção 10 e `participant_id` da seção 0.
