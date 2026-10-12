# `data/private/` — conteúdo sensível, NÃO versionado

Esta pasta está no `.gitignore`. Nada aqui sobe para o GitHub.

| arquivo                        | conteúdo                                        | destino                          |
|--------------------------------|-------------------------------------------------|----------------------------------|
| `blinding-map-roundN.json`     | blind_id → fichamento_id → source (`ai`/`human`)| publicar após descegamento       |
| `participants.csv`             | nome real ↔ pseudônimo (S01…, J1…)              | nunca publicar                   |
| `judge-packets/`               | fichamentos rotulados A/B para envio aos juízes | regenerável via `fichamento blind`|

Somente este README é rastreado pelo git.
