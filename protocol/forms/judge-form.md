# Especificação do Google Forms — avaliação dos juízes

**Uma submissão = um artigo avaliado por um juiz.** Cada juiz submete o
formulário 16 vezes por rodada. Os títulos das perguntas abaixo são os
nomes canônicos que o `fichamento ingest` espera no CSV exportado
(ver `column-map.json` — ao criar o form, copie os títulos exatamente).

## Identificação (por submissão)

| # | título da pergunta (canônico) | tipo |
|---|---|---|
| 1 | `judge_id` | Múltipla escolha: `J1`, `J2`, `J3`, `J4` |
| 2 | `article_id` | Múltipla escolha: `A01`…`A16` (round 1) |
| 3 | `confidence` | Linear 1–3: "quão bem você conhece este artigo?" |

## Bloco por fichamento — repetir para `A` e `B`

Prefixo canônico das colunas: `A.` / `B.` (posição no pacote do juiz).

| título da pergunta | tipo |
|---|---|
| `{X}.score.executive_summary` | Linear 1–7 |
| `{X}.score.research_question` | Linear 1–7 |
| `{X}.score.theories` | Linear 1–7 |
| `{X}.score.key_concepts` | Linear 1–7 |
| `{X}.score.methodology` | Linear 1–7 |
| `{X}.score.main_findings` | Linear 1–7 |
| `{X}.score.contribution` | Linear 1–7 |
| `{X}.errors` | Caixas de seleção: `hallucination`, `omission`, `misinterpretation`, `misattribution`, `terminology`, `extrapolation`, `invalid_source_ref`, `other`, `none` |
| `{X}.error_sections` | Caixas de seleção: seções onde os erros ocorreram (`executive_summary`…`contribution`) — opcional |
| `{X}.error_note` | Parágrafo curto (opcional) — detalhe dos erros |
| `{X}.would_question` | Parágrafo curto — "há algo que você questionaria?" |
| `{X}.missing` | Parágrafo curto — "o que faltou?" |

## Preferência (uma vez por submissão)

| título da pergunta | tipo |
|---|---|
| `preference` | Múltipla escolha: `A`, `B`, `tie` — "qual fichamento você usaria na sua revisão?" |
| `preference_reason` | Parágrafo — por quê? |

## Recomendações de configuração do Forms

- Não coletar e-mail automaticamente (pseudônimo `judge_id` basta).
- "Editar após envio": desligado (registro imutável da avaliação).
- Exportar CSV: *Respostas → ⋮ → Fazer o download das respostas (.csv)*.

## Ingestão

```bash
fichamento ingest --round 1 --csv respostas.csv --judge-map protocol/forms/column-map.json
```

Cada linha do CSV vira `data/evaluations/round1/E-R1-A{nn}-J{k}.json`
validado contra `schemas/evaluation.schema.json`.
