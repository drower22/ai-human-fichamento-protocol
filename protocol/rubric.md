# Rubrica de avaliação — v1.0.0 (congelar antes da Rodada 1)

Escala **BARS 1–7** (Behaviorally Anchored Rating Scale) por seção, com
âncoras em **1 / 4 / 7**; notas 2–3 e 5–6 interpolam. Juiz avalia cada
fichamento (A e B) em todas as 7 seções.

## Âncoras por seção

### 1. Resumo executivo
- **1** — Ausente, genérico a ponto de valer para qualquer artigo, ou
  contradiz o artigo.
- **4** — Cobre problema, método e resultado centrais, mas perde nuances
  relevantes ou excede/omite partes importantes.
- **7** — Síntese fiel e completa (~300 palavras): problema, método,
  achados e contribuição; quem lê entende o artigo sem abrir o PDF.

### 2. Questão de pesquisa
- **1** — Ausente ou errada (não é a pergunta do artigo).
- **4** — Correta mas imprecisa: ampla demais, ou captura só parte.
- **7** — Formula precisamente a pergunta do artigo, no escopo correto.

### 3. Teorias presentes
- **1** — Teorias centrais ausentes ou inventadas.
- **4** — Lista as principais mas confunde papel (lente vs. citação
  periférica) ou omite tradição relevante.
- **7** — Identifica todas as teorias centrais, sua tradição e o papel de
  cada uma no argumento; zero invenção.

### 4. Conceitos-chave
- **1** — Conceitos errados, inventados ou definições incorretas.
- **4** — 3–4 conceitos corretos, mas definições genéricas ou escolha
  discutível (deixou construto central de fora).
- **7** — 3–4 construtos centrais com definições fiéis ao uso no artigo.

### 5. Metodologia
- **1** — Design/método errados ou inventados.
- **4** — Design correto mas omite informação essencial (N, setor,
  período, técnicas de análise).
- **7** — Design, N, setor, período e técnicas corretos e completos.

### 6. Achados principais
- **1** — Achados inventados, invertidos ou que o artigo não sustenta.
- **4** — Achados corretos mas incompletos (perde resultado/proposição
  central) ou sem distinguir evidência de especulação.
- **7** — Captura todos os achados/proposições centrais, distinguindo
  resultado empírico de proposição/modelo teórico.

### 7. Contribuição
- **1** — Ausente ou não corresponde ao que o artigo reivindica/entrega.
- **4** — Identifica contribuição real mas superficial (repete abstract)
  ou infla o que o artigo sustenta.
- **7** — Articula avanço teórico **e** utilidade prática de forma fiel e
  calibrada (nem infla nem reduz).

## Taxonomia de erros (checklist por seção — marcar todos que aplicam)

| código | definição | exemplo |
|---|---|---|
| `hallucination` | conteúdo fabricado, inexistente no artigo | cita achado que o paper não reporta |
| `omission` | elemento central do artigo ausente | não lista a teoria principal |
| `misinterpretation` | elemento real interpretado incorretamente | lê correlação como causalidade |
| `misattribution` | atribui a teoria/autor/variável errada | troca a lente teórica |
| `terminology` | termo técnico usado/traduzido incorretamente | "validade" por "confiabilidade" |
| `extrapolation` | afirma além do que o artigo sustenta | generaliza achado de 1 setor p/ todos |
| `invalid_source_ref` | `p.N/Lnn` citado não existe ou não sustenta | ref aponta para página errada |
| `other` | qualquer outro (descrever em nota) | — |

## Preferência (métrica comparativa primária)

Por artigo: *"Qual fichamento você usaria na sua revisão?"* →
**A / B / Empate** + razão aberta.

## Qualitativas (por fichamento)

1. Há algo que você questionaria?
2. O que faltou?

## Regra de calibração

Âncoras e taxonomia são **fixas na R1**. Entre R1 e R2 podem ser refinadas
(novo código de erro, âncora reescrita) — todo refinamento é registrado no
changelog deste arquivo + `diary/` e reportado como achado metodológico.

### Changelog
- **v1.0.0** — versão inicial (taxonomia e âncoras propostas a priori).
