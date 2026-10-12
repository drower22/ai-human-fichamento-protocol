# Protocolo de Validação IA–Humano para Fichamentos

Protocolo replicável e de ciência aberta para calibração iterativa entre IA e
humanos na produção de **fichamentos estruturados** de artigos científicos,
em contexto de revisão estruturada de literatura

O objetivo é medir — às cegas — onde a IA e onde o humano são melhores,
calibrar prompts e instruções entre duas rodadas, e produzir um corpus de
fichamentos em **JSON validado por schema** que alimenta análises posteriores
(estatísticas, knowledge graphs, etc.).

> **EN**: This repository hosts a replicable, open-science protocol for
> iterative AI–human calibration of structured reading notes
> ("fichamentos") at literature-review scale. Two independent fichamentos
> (AI + human) per article are rated blind by judges across two rounds;
> everything — protocol, schemas, prompts, code and data — is versioned
> and auditable.

## Como funciona (visão de 1 minuto)

1. **4 juízes** indicam 4 artigos cada → 16 artigos por rodada.
2. Cada artigo recebe **2 fichamentos independentes**: um gerado por IA
   (API), um produzido por estudante.
3. **4 juízes avaliam às cegas** os 32 fichamentos da rodada (Likert 1–5 por
   seção + perguntas qualitativas + preferência A/B).
4. **Rodada 1 = baseline** → análise → **calibração** (refina prompt da IA e
   cria checklist para estudantes) → **Rodada 2 = pós-calibração**.
5. Análise final: médias por seção, IA vs. humano, evolução R1→R2, padrões
   qualitativos de erro.

O protocolo completo está em [`protocol/PROTOCOL.md`](protocol/PROTOCOL.md).

## Estrutura do repositório

```
├── protocol/          # Protocolo, templates, instruções, spec do Google Forms
├── prompts/           # Prompts versionados (semver) usados pela IA
├── schemas/           # JSON Schemas (gerados a partir dos modelos pydantic)
├── data/
│   ├── articles/      # registry.jsonl + pdfs/ (PDFs não versionados)
│   ├── fichamentos/   # round{1,2}/{ai,human}/*.json — um arquivo por fichamento
│   ├── evaluations/   # round{1,2}/*.json — avaliações dos juízes
│   └── private/       # NÃO versionado: mapa de cegamento, identidades
├── src/fichamento/    # Pacote Python (CLI `fichamento`)
├── analysis/          # Relatórios e notebooks
└── diary/             # Diário de bordo dia a dia (docs/diary/README.md)
```

## Quickstart

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# 1) Cadastre artigos em data/articles/registry.jsonl e coloque os PDFs em
#    data/articles/pdfs/<ARTICLE_ID>.pdf
# 2) Gere os fichamentos de IA (ex.: OpenAI; qualquer provider litellm)
export OPENAI_API_KEY=...
fichamento generate --round 1 --model gpt-4o --prompt-version 1.0.0

# 3) Crie o cegamento e o pacote para os juízes
fichamento blind --round 1 --seed 42

# 4) Após coleta via Google Forms: ingira o CSV exportado
fichamento ingest --round 1 --csv forms_export.csv

# 5) Valide todo o dataset e rode a análise
fichamento validate
fichamento analyze --round 1

# 6) Exporte nós/arestas p/ knowledge graph
fichamento export-kg --out analysis/reports/kg
```

## Convenções de dados

- **IDs**: artigos `A01…A32`; juízes `J1…J4`; estudantes `S01…S10`;
  fichamentos `F-R{round}-{article}-{AI|HUM}`; avaliações
  `E-R{round}-{article}-{judge}`; IDs cegos `B01…B32` por rodada.
- **Schemas/código em inglês**; conteúdo dos fichamentos em **pt-BR**.
- Um arquivo JSON por unidade → diffs git auditáveis e merges sem conflito.
- `data/private/` **nunca é commitado**: mapa de cegamento (`blinding-map-roundN.json`)
  e identidades de participantes ficam fora do git até o descegamento.
- Toda geração de IA registra `provider`, `model`, `prompt_version`,
  `temperature`, seed quando disponível, timestamp e uso de tokens —
  condições de reprodutibilidade.

## Ética e privacidade

- Participantes identificados apenas por pseudônimos (`S01`, `J1`); a tabela
  identidade↔pseudônimo vive em `data/private/participants.csv` (fora do git).
- Consentimento informado recomendado antes da Rodada 1 (ver PROTOCOL.md).
- PDFs dos artigos não são distribuídos (copyright); apenas metadados.
- Após o descegamento, publicar `blinding-map-*.json` para auditoria completa.

## Diário de bordo

Toda sessão de trabalho gera uma entrada em [`diary/`](diary/README.md) —
decisões, comandos executados, bloqueios e próximos passos. O diário é parte
da auditoria do protocolo.

## Licença

Código: **MIT**. Protocolo, prompts, schemas e dados: **CC BY 4.0**.
Ver [LICENSE](LICENSE).
