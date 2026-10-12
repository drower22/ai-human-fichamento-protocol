# Template de fichamento

Formato canônico produzido por IA e estudantes. Conteúdo em **pt-BR**;
chaves do JSON em inglês (ver `schemas/fichamento.schema.json`).

Cada teoria, conceito, achado e bloco de metodologia deve citar sua origem
no documento marcado via `source_refs` no formato `p.N` ou `p.N/Lnn`
(ex.: `p.3/L12`). Isso vale também para estudantes (usar nº de página do PDF).

## 1. Resumo executivo (`executive_summary`)
Síntese em ~300 palavras cobrindo problema, abordagem teórica, método,
achados e contribuição.

## 2. Questão de pesquisa (`research_question`)
A pergunta que o artigo busca responder, formulada precisamente.

## 3. Teorias presentes (`theories[]`)
Para cada teoria/framework: `name`, `tradition` (tradição/campo), `role`
(lente principal, framework de análise, citação periférica…), `source_refs`.

## 4. Conceitos-chave (`key_concepts[]`)
3–4 construtos centrais: `concept`, `definition` (como o artigo define/usa),
`source_refs`.

## 5. Metodologia (`methodology`)
`design` (survey, case study, experimento, teórico…), `sample_size`,
`sector`, `period`, `methods[]` (técnicas de análise), `source_refs`.

## 6. Achados principais (`main_findings[]`)
Cada achado/proposição: `finding`, `type` (`empirical` | `proposition` |
`model`), `source_refs`.

## 7. Contribuição (`contribution`)
`theoretical` — avanço teórico reivindicado/entregue; `practical` —
utilidade prática.

## Metadados (fora do conteúdo)
- IA: provider, model, prompt_version, temperature, tokens, timestamp.
- Humano: `participant_id`, `elapsed_minutes`, `submitted_at`.
