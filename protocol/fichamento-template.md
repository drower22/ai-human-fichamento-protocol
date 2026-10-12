# Template de fichamento

Formato canônico produzido por IA e estudantes. Conteúdo em **pt-BR**;
chaves do JSON em inglês (ver `schemas/fichamento.schema.json`).

Tudo que o fichamento afirma deve ser rastreável ao artigo: use
`source_refs` (`p.N`, `p.N-M`, `Lnn`, `Lnn-mm` ou `p.N/Lnn`) e, quando
possível, o `quote` literal do trecho.

## 1. Resumo executivo (`executive_summary`)
Síntese em ~300 palavras cobrindo problema, abordagem teórica, método,
achados e contribuição.

## 2. Questão de pesquisa (`research_question`)
A pergunta que o artigo busca responder, formulada precisamente.

## 3. Teorias presentes — **instrumento fechado**

Um **pool de candidatos** é gerado antes (`fichamento candidates`) e cada
item recebe um veredito em `theory_verdicts`:

| veredito | significado | evidência |
|---|---|---|
| `uses` | estrutura o argumento/modelo/hipóteses | `source_refs` **obrigatório** |
| `discusses` | debatida/citada substantivamente | `source_refs` **obrigatório** |
| `does_not_use` | ausente ou menção decorativa | — |

Campos por item: `item_id` (do pool), `name`, `verdict`, `source_refs`,
`quote` (opcional), `note` (opcional).

Teorias relevantes **fora do pool** vão em `theories` (lista livre:
`name`, `tradition`, `role`, `source_refs`) — para humanos, registrar
adições é o que permite medir as omissões do pool.

## 4. Conceitos-chave (`key_concepts[]`)
3–4 construtos centrais: `concept`, `definition` (como o artigo usa),
`quote` (trecho literal — recomendado), `source_refs`.

## 5. Metodologia (`methodology`)
`study_type` (teórico/empírico/simulação/revisão), `design`
(delineamento), `sample_type`, `sample_size` (null se não aplicável),
`sector`, `period`, `methods[]` (técnicas — tags para o knowledge graph),
`analysis_note` (descrição livre), `source_refs`.

## 6. Achados principais (`main_findings[]`)
Cada achado/proposição: `finding`, `type` (`empirical` | `proposition` |
`model`), `quote` (trecho literal — recomendado), `source_refs`.

## 7. Contribuição (`contribution`)
`theoretical` — avanço teórico reivindicado/entregue; `practical` —
utilidade prática.

## Metadados (fora do conteúdo)
- IA: provider, model, prompt_version, temperature, tokens, timestamp,
  `md_sha256`, `verdicts_prompt_version`.
- Humano: `participant_id`, `elapsed_minutes`, `submitted_at`.
