# Data dictionary — `data/`

## `articles/registry.jsonl`

Uma linha JSON por artigo. Campos:

| campo            | tipo   | descrição                                        |
|------------------|--------|--------------------------------------------------|
| `article_id`     | str    | `A01`…`A32`                                       |
| `round`          | int    | `1` (artigos 1–16) ou `2` (artigos 17–32)         |
| `nominated_by`   | str    | juiz que indicou o artigo (`J1`…`J4`)             |
| `title`          | str    | título                                            |
| `authors`        | [str]  | autores                                           |
| `year`           | int    | ano de publicação                                 |
| `venue`          | str    | periódico/conferência                             |
| `doi`            | str    | DOI (string vazia se ausente)                     |
| `language`       | str    | `en`, `pt`, …                                     |
| `pdf_path`       | str    | caminho relativo, ex. `data/articles/pdfs/A01.pdf`|
| `notes`          | str    | livre                                             |

Exemplo:

```json
{"article_id":"A01","round":1,"nominated_by":"J1","title":"...","authors":["Silva, M."],"year":2021,"venue":"RAE","doi":"10.xxxx/...","language":"en","pdf_path":"data/articles/pdfs/A01.pdf","notes":""}
```

## `fichamentos/round{N}/{ai,human}/F-R{N}-A{nn}-{AI|HUM}.json`

Um arquivo por fichamento; validado contra `schemas/fichamento.schema.json`.
O campo `generator` é discriminado por `kind`:

- `"kind": "ai"` → provider, model, prompt_version, temperature, tokens…
- `"kind": "human"` → participant_id, elapsed_minutes, submitted_at

O bloco `human_review` registra a revisão humana posterior dos fichamentos
de IA (etapa pós-calibração, quando o protocolo evoluir para produção em
escala — IA ficha, humano revisa).

## `evaluations/round{N}/E-R{N}-A{nn}-J{k}.json`

Uma avaliação por (juiz × artigo): contém as notas Likert dos dois
fichamentos cegos (`ratings`, identificados por `blind_id`), perguntas
qualitativas e preferência. Validado contra `schemas/evaluation.schema.json`.

## `private/` — nunca commitado

- `blinding-map-round{N}.json` — mapa blind_id ↔ fichamento_id ↔ source.
  Publicar **somente após o descegamento**.
- `participants.csv` — identidade ↔ pseudônimo. Nunca publicar.
- `judge-packets/` — material enviado aos juízes (fichamentos já rotulados
  como "Fichamento A/B", sem proveniência).
