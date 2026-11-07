# Rubrica de avaliação — v1.1.0 (BARS adaptada)

Escala tipo **BARS adaptada** 1–7 por seção, com âncoras em **1 / 4 / 7**;
notas 2–3 e 5–6 interpolam. Juiz avalia cada fichamento (A e B) em todas
as 7 seções.

> **Regra geral — fidelidade limita a nota.** Completude não compensa
> fabricação nem cópia literal: uma seção com conteúdo inventado,
> extrapolado ou copiado literalmente do artigo **não passa de 4**,
> independente do volume de acertos.

> "Adaptada": as âncoras foram escritas a priori pelos pesquisadores, sem
> o procedimento canônico de Smith & Kendall (1963) — que deriva âncoras
> de incidentes críticos com retranslação entre especialistas. No relato,
> usar "BARS adaptada" ou "rubrica ancorada em comportamentos
> observáveis".

## Âncoras por seção

### 1. Resumo executivo
- **1** — Ausente, genérico a ponto de valer para qualquer artigo, ou
  contradiz o artigo.
- **4** — Cobre problema, método e resultado centrais, mas perde nuances
  ou omite partes importantes, **ou é colagem de trechos literais em vez
  de síntese elaborada**.
- **7** — Síntese fiel e completa (~300 palavras), com elaboração
  própria: problema, método, achados e contribuição; quem lê entende o
  artigo sem abrir o PDF.

### 2. Questão de pesquisa
- **1** — Ausente ou errada (não é a pergunta do artigo) — inclui
  inventar uma questão explícita que o artigo não enuncia.
- **4** — Correta mas imprecisa: ampla demais, captura só parte, ou copia
  o objetivo declarado quando a questão real é outra.
- **7** — Formula precisamente a pergunta do artigo, no escopo correto;
  se implícita, reconstruí-la a partir do objetivo/argumento/conclusão e
  sinalizar que é implícita conta como precisão.

### 3. Teorias presentes
- **1** — Teorias centrais ausentes ou inventadas.
- **4** — Vereditos corretos na maioria, mas confunde o papel: marca
  usa/discute o que é só citação de revisão, ou omite tradição relevante.
- **7** — Vereditos fiéis ao papel no argumento: **usa** = estrutura a
  análise; **discute** = tratada com substância sem estruturar; citação
  decorativa na revisão = **não usa**; zero invenção.

### 4. Conceitos-chave
- **1** — Conceitos errados, inventados ou definições incorretas.
- **4** — 3–4 conceitos corretos e fiéis, mas a seleção é discutível:
  deixou de fora construto que carrega a análise, ou incluiu termo
  periférico como central.
- **7** — 3–4 construtos que de fato operam na análise (não apenas
  mencionados), com definições fiéis ao uso no artigo.

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
- **4** — Identifica contribuição real mas superficial (repete o
  abstract) ou a infla — **inflar mantém a nota em 4**.
- **7** — Articula avanço teórico **e** utilidade prática com a força que
  o artigo sustenta: nem repete a retórica inflada do próprio artigo, nem
  infla, nem reduz.

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

- **Âncoras**: ajustáveis somente no **piloto R0** (pré-R1); depois
  **congeladas para as duas rodadas** — reescrever âncora entre R1 e R2
  quebra a comparabilidade das notas e o Δ da calibração. **v1.1.0 é a
  versão congelada de R1 e R2.**
- **Taxonomia de erros**: refinável entre R1 e R2 (novo código, definição
  mais precisa) — é checklist e não altera o valor das notas. Todo
  refinamento é registrado no changelog + `diary/` e reportado como
  achado metodológico.

### Changelog
- **v1.0.0** — versão inicial (taxonomia e âncoras propostas a priori).
- **2026-10-15** — decisão de reunião: nomenclatura "BARS adaptada";
  âncoras congelam pós-piloto para ambas as rodadas.
- **v1.1.0 (2026-11-07)** — revisão pós-piloto a partir da dispersão dos
  juízes (reunião 06/11, `data/piloto/reuniao-0611/`): regra geral de
  fidelidade; resumo (síntese elaborada vs. colagem literal); questão
  (implícita reconstruída e sinalizada conta como precisão; inventar
  explícita vira âncora 1); teorias (papel no argumento: usa/discute/não
  usa — citação só na revisão = não usa); conceitos (seleção: construtos
  que operam na análise); contribuição (inflação mantém nota em 4).
  **Congelada para R1 e R2.**
