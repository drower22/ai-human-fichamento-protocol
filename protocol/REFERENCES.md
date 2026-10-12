# Referências relacionadas — fundamentação do protocolo

Organizadas por tema, com nota sobre a relevância para este desenho.
(coletadas em 2026-10-12; verificar versões finais/publicadas ao citar)

## A. Comparação cega IA vs. humano — desenhos quase idênticos ao nosso

| trabalho | por que importa |
|---|---|
| **"Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth"** (arXiv:2607.28890, 2026) | O mais próximo do nosso desenho: especialista julga **pares às cegas** sem saber qual é IA/humano, com **ranking Bradley–Terry** colocando 2 LLMs acima de 2 dos 3 codificadores humanos. Demonstra que concordância com humanos ≠ qualidade — justifica nossa preferência A/B como métrica primária em vez de "distância do humano". |
| **"LLMs for thematic analysis in healthcare research: A blinded mixed-methods comparison with human analysts"** (PLOS Digital Health, 2026) | Comparação cega LLM vs. analistas humanos; quantifica **taxa de alucinação** (1,2%) e erros; testa **não-inferioridade** — modelo estatístico alternativo ao nosso Wilcoxon. |
| **"LLMs in Thematic Analysis: Prompt Engineering, Evaluation, and Guidelines"** (Software Eng. research) | 4 avaliadores cegos com rubricas; LLM preferido em 61% dos casos; documenta **refinamento iterativo de prompts** como parte do método — análogo à nossa calibração. |
| **"Meeting the machines half-way: Testing LLMs for qualitative coding"** (Ergonomics/T&F, 2026) | Humanos preferidos às cegas, mas baixa concordância entre humanos — evidência de que "humano = gold standard" é questionável; entrevistas pós-avaliação (inspira nossas qualitativas). |
| **"Can LLMs Reliably Code Qualitative Humanitarian Data?"** (arXiv:2606.26541, 2026) | 46 LLMs vs. gold standard humano; **Krippendorff α** + análise de discrepância correta/quase-correta/incorreta — referência para nossa taxonomia de erros. |

## B. Extração/fichamento de dados em revisões sistemáticas

| trabalho | por que importa |
|---|---|
| **"AI-Assisted Data Extraction with a Large Language Model: A Study Within Reviews"** (SWAR; Claude 2.1/3/3.5) | 9.341 elementos, 63 estudos, **adjudicadores cegados**; concordância 77,2% — desenho "study within a review" é template do nosso. |
| **"AI Tools as Second Reviewers for Data Extraction"** (PMC12257877; Elicit + ChatGPT) | Precisão/recall/F1 ~90%+; propõe exatamente o nosso endgame: **IA substitui o segundo extrator; humano reconcilia divergências**. |
| **"ChatGPT-4o as second rater for data extraction"** (PLOS ONE, 2025) | 92,4% de acurácia; avalia **reprodutibilidade entre sessões** (94,1%) — variável que nosso protocolo controla via temperatura/seed/prompt_version. |
| **"Elicit vs. human reviewers in RCT data extraction"** (Cochrane Evidence Synthesis & Methods, Wiley) | Classifica extrações em "mais/igual/parcial/divergente" — granularidade intermediária entre correta/errada, inspira nossa taxonomia. |
| **"Critical Assessment of LLMs' Performance in Data Extraction"** (JMIR AI, 2025) | **Refinamento iterativo de prompt melhorou acurácia 33%/23%** — evidência direta de que nossa etapa de calibração funciona; mostra que IA extrai melhor dados explícitos (93%) do que inferenciais (50%). |

## C. Frameworks, guidelines e revisões sobre IA em revisões

| trabalho | por que importa |
|---|---|
| **RAISE — Responsible use of AI in evidence SynthEsis** (Thomas et al., 2025; OSF) | Recomendações oficiais para uso responsável de IA em síntese de evidência; RAISE 2 = como **construir e avaliar** ferramentas de IA. Nosso protocolo deve citar conformidade com RAISE. |
| **Position Statement on AI Use in Evidence Synthesis — Cochrane, Campbell, JBI, CEE** (Campbell Systematic Reviews, 2025) | Posição conjunta das maiores organizações de revisão sistemática — legitima o desenho e exige rigor. |
| **GUEST: Preliminary Guidelines for Using and Evaluating GenAI Tools to Support SLRs** (arXiv:2607.24991) | Recomendações de processo para conduzir E avaliar GenAI em SLRs; útil na seção de ameaças à validade. |
| **ASReview** (van de Schoot et al., Nature Machine Intelligence, 2021) | Referência clássica de human-in-the-loop para screening via active learning (até 95% menos tempo); v.2 (Cell Patterns, 2025) tem múltiplos agentes + "crowd of oracles" — paralelo aos nossos 10 estudantes. |
| **"A hybrid framework for AI-augmented SLRs"** (Management Review Quarterly, 2025) | **Na nossa área (Administração)**: framework híbrido IA + rigor epistemológico, human-in-the-loop, prompt engineering iterativo — citação direta para a fundamentação. |
| **"LLMs as Tools for Integrative Reviews"** (editorial, Academy of Management Annals, 2025) | Editorial da AOM sobre LLMs em revisões — sinaliza aceitação da área e dá vocabulário para justificar o estudo. |
| **"Automating the SLR Process in Management Science Using AI"** (2025) | Mapeia onde IA contribui em cada etapa da SLR em management — posiciona nosso estudo na etapa de extração/síntese. |
| **"LLM automated systematic review"** (Scherbakov et al., arXiv:2409.04600) | Meta-revisão de projetos que usam LLMs em revisões, **protocolo pré-registrado no OSF** — precedente para nosso pré-registro. |

## D. Medição de aprendizagem / calibração metacognitiva

| trabalho | por que importa |
|---|---|
| **"Metacognitive Calibration: A Methodological Expansion and Empirical Application"** (ICLS, 2023) | Estatísticas para **acurácia de calibração** (gap auto-avaliação vs. desempenho real) e direção do erro (sobre/subconfiança) — fundamenta o módulo de auto-avaliação dos estudantes. |
| Literatura de *second-order judgments* (Miller & Geraci; Siedlecka et al.) | Confiança na própria estimativa como medida de consciência metacognitiva — padrão ouro para medir se estudantes "sabem o que não sabem". |
| Dunning–Kruger / calibration-em-exames (Hacker, Dunlosky et al.) | Piores desempenhos = pior calibração — prediz que estudantes mais fracos se auto-superavaliam; testável com nossos dados. |
