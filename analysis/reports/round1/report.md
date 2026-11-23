# Relatório R1 — Avaliações dos juízes (16/16)

Avaliações analisadas: 16 pares, 1 juiz por par.

## Preferência A/B (métrica primária)

- IA preferida: **13** | Humano preferido: **0** | Empate: 3
- Binomial (excl. empates, n=13): p = 0.0002 — proporção IA = 100%

## Notas médias por fonte e seção (BARS 1–7)

| seção | IA | humano |
|---|---|---|
| Resumo | 6.50 | 5.81 |
| Questão | 6.62 | 5.44 |
| Teorias | 5.81 | 5.38 |
| Conceitos | 5.94 | 5.06 |
| Metodologia | 6.44 | 4.38 |
| Achados | 6.31 | 4.94 |
| Contribuição | 6.50 | 5.12 |
| **Total** | **6.30** | **5.16** |

## Wilcoxon pareado (IA − humano; par = juiz×artigo)

| seção | n | mediana dif | média dif | p | rank-biserial |
|---|---|---|---|---|---|
| Resumo | 12 | 1.0 | 0.69 | 0.0383 | 0.654 |
| Questão | 10 | 0.5 | 1.19 | 0.1002 | 0.582 |
| Teorias | 9 | 0.0 | 0.44 | 0.1003 | 0.6 |
| Conceitos | 11 | 0.5 | 0.88 | 0.0546 | 0.636 |
| Metodologia | 13 | 2.0 | 2.06 | 0.0013 | 1.0 |
| Achados | 12 | 1.0 | 1.38 | 0.0019 | 1.0 |
| Contribuição | 13 | 1.5 | 1.38 | 0.0053 | 0.868 |
| TOTAL (todas as seções) | 80 | 1.0 | 1.14 | 0.0 | 0.796 |

## Erros por tipo e fonte

| fonte | extrapolation | hallucination | misattribution | misinterpretation | omission | other | terminology | total |
|---|---|---|---|---|---|---|---|---|
| ai | 2 | 3 | 1 | 5 | 5 | 5 | 1 | 22 |
| human | 2 | 13 | 0 | 8 | 18 | 6 | 2 | 49 |

## Meta-avaliação dos alunos (autoavaliação vs juiz)

| aluno | artigo | média auto | média juiz | gap médio | |gap| médio |
|---|---|---|---|---|---|
| S01 | A06 | 4.86 | 2.14 | 2.71 | 2.71 |
| S02 | A05 | 6.57 | 3.57 | 3.0 | 3.0 |
| S03 | A02 | 4.57 | 6.57 | -2.0 | 2.0 |
| S04 | A11 | 5.0 | 7.0 | -2.0 | 2.0 |
| S05 | A16 | 4.86 | 5.0 | -0.14 | 1.86 |
| S06 | A07 | 4.71 | 5.14 | -0.43 | 1.0 |
| S07 | A08 | 5.57 | 5.0 | 0.57 | 1.43 |
| S08 | A04 | 5.14 | 4.43 | 0.71 | 0.71 |
| S09 | A10 | 5.71 | 5.14 | 0.57 | 1.43 |
| S10 | A09 | 5.43 | 6.14 | -0.71 | 1.29 |
| S11 | A15 | 5.29 | 4.71 | 0.57 | 1.71 |
| S12 | A13 | 4.29 | 5.14 | -0.86 | 0.86 |
| S13 | A03 | 4.43 | 5.86 | -1.43 | 1.43 |
| S14 | A12 | 5.71 | 5.71 | 0.0 | 0.86 |
| S15 | A01 | 5.43 | 5.86 | -0.43 | 1.0 |
| S16 | A14 | 6.29 | 5.14 | 1.14 | 1.14 |

## Veredito

**A IA venceu a R1 de forma inequívoca.** 13 preferências contra 0, 3
empates (A02, A09, A11), binomial p=0,0002 — 12 das 13 vitórias com
confiança "alta". Nas 7 seções, a média da IA supera a humana em todas
(6,25 × 5,13 no total), com Wilcoxon significativo em metodologia
(p=0,001, efeito máximo rbc=1,0), achados (p=0,002, rbc=1,0),
contribuição (p=0,005) e resumo (p=0,038). A taxonomia de erros reforça:
22 erros atribuídos à IA vs 49 ao lado humano — e o perfil difere: a IA
erra por omissão cautelar e calibração de veredito teórico; os fichamentos
humanos por invenção (13 alucinações) e omissão (18).

**Leitura honesta:** isso valida a metade "produção" da pergunta de
pesquisa para este corpus e este pool — a IA em modo default produz
fichamento utilizável para triagem. Não diz nada ainda sobre aprendizado
dos alunos (é o Módulo A) nem sobre robustez da medida (1 juiz por par —
a R3 proposta cobre isso).

## Onde a IA errou (diagnóstico para a R2)

Concentração em 8 artigos; padrões claros:

1. **Calibração dos vereditos teóricos** — 5× `misinterpretation` +
   nota do juiz no A15 ("conceitos apenas falados marcados como
   discutidos"): o limiar de `discute` ficou liberal demais. Apertar:
   `discute` só quando o artigo mobiliza construtos da teoria, não
   nomeia.
2. **Completude de conceitos-chave** — 3× `omission` + nota no A16
   (faltou "risco puro"): falta varredura de conceitos antes de escrever.
3. **Completude de metodologia** — "faltou a terceira fase" (A15),
   "coleta em 2025" (A14): exigir enumeração explícita de fases/etapas.
4. **Alucinação residual** — 3 casos (A06, A15, ambos com OCR ruidoso):
   em texto corrompido, declarar incerteza em vez de reconstruir.
5. **Questão de pesquisa ausente** — no A16 o juiz observou que o artigo
   não formula PQ; o fichamento deve dizer "não há PQ explícita; o
   objetivo declarado é X" em vez de reconstruir uma.

## Prompt vs fine-tune para a R2

**Prompt + verificação, não fine-tune.** Os modos de falha são de
conteúdo e calibração (limiar de veredito, cobertura de conceitos), não
de estilo — e 16 exemplos não sustentam fine-tuning. Recomendações
concretas para a geração da R2:

- **Prompt:** elevar o limiar de `discute` (construtos mobilizados, não
  menção); exigir pré-listagem de conceitos candidatos do próprio texto
  antes de redigir; exigir enumeração das fases do estudo na metodologia;
  instruir "em OCR corrompido, declarar incerteza"; permitir "artigo não
  formula PQ explícita" quando for o caso.
- **Com a API key (novo recurso):** adicionar um **passo de crítica**
  — um segundo modelo lê fichamento × artigo e lista omissões/vereditos
  contestáveis antes de fechar o JSON. A verificação mecânica de
  referências (0 erros em 1.195 refs na R1) continua; a crítica cobre o
  que ela não vê (semântica, completude).
- **Manter:** formato `p.N/Lnn`, teto de não-extrapolação (é o que
  diferenciou a IA do lado humano: 3 alucinações vs 13).

## Meta-avaliação dos alunos (registro)

Arquivos: `meta_students_long.csv` (por seção), `meta_students.csv`
(resumo por aluno). Leitura:

- **Superestimadores** (gap ≥ +1): S02 (+3,00 — auto 6,57, juiz 3,57),
  S01 (+2,71), S16 (+1,14). Coerente com a literatura: pior desempenho,
  maior sobreconfiança (S02 teve a nota de juiz mais baixa do conjunto).
- **Subestimadores** (gap ≤ −1): S04 (−2,00 — auto 5,00, juiz 7,00!),
  S03 (−2,00), S13 (−1,43). Caso interessante: S04 recebeu 7,0 do juiz e
  ainda assim seu par empatou, não venceu.
- **Bem calibrados** (|gap| < 1): S14 (0,00), S05, S06, S08, S09, S11,
  S12, S15.
- Média do |gap| absoluto: ~1,4 pontos — espaço claro para a sessão de
  calibração em grupo do desenho de letramento.

CSV complementar: `errors_per_fichamento.csv`, `errors_long.csv`,
`paired_diff.csv`, `scores_long.csv`.
