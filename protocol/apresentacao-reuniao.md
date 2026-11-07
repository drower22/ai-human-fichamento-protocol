# Protocolo de fichamentos auditáveis
### Reunião do grupo — 15/out/2026

---

## 1. Objetivo

**Criar um protocolo válido e fiel para produção de fichamentos — humanos e de IA — que faça o trabalho braçal das revisões de literatura e libere o pesquisador para refletir e analisar.**

Não é uma disputa IA × humano:

- **Diagnóstico**: identificar pontos fortes e fracos de cada produtor — onde a IA ajuda, onde erra, onde o humano é insubstituível
- **Aprendizagem**: medir como os estudantes evoluem ao longo do processo
- **Resultado**: um protocolo auditável — todo fichamento carrega evidência verificável (`p.N Lnnn`) — que o grupo pode confiar para usar em revisões reais

---

## 2. O modelo de fichamento (o que o protocolo produz)

| # | seção | o que mede |
|---|---|---|
| 1 | Resumo executivo (~300 palavras) | síntese fiel do artigo |
| 2 | Questão de pesquisa | precisão na identificação do problema |
| 3 | **Teorias — instrumento fechado** | veredito `uses`/`discusses`/`does_not_use` por item do pool + referência; campo aberto para teoria fora da lista |
| 4 | Conceitos-chave | definição + evidência textual |
| 5 | Metodologia | desenho, amostra, métodos, análise |
| 6 | Principais achados | classificação empirical/theoretical + evidência |
| 7 | Contribuição | teórica e prática |

- **Cada afirmação carrega referência `(p.N Lnnn)`** — qualquer um verifica a linha exata no PDF numerado
- O estudante também entrega **auto-avaliação** (1–7 por seção) e **log de reflexão** — é daí que sai a medida de aprendizagem

---

## 3. O método em 3 linhas

- **Corpus**: 32 artigos do grupo → 2 rodadas (16 artigos cada)
- **Por artigo**: 1 fichamento humano + 1 fichamento de IA → **par cego A/B**
- **4 juízes avaliam tudo** com a mesma BARS adaptada (1–7 por seção) + taxonomia de erros
- Mesmo texto, mesma numeração, mesma rubrica → comparação justa e auditável (IDs, hashes, seeds registrados)

---

## 4. A regra: estudantes **não** usam IA

- Para medir forças e fraquezas **de cada um**, o fichamento humano precisa ser feito **sem IA**
- Declaração explícita no formulário + campo honesto no log de reflexão
- Se usou, declara — o dado não é descartado, vira análise própria
- **Por quê?** Se o humano usa IA, os dois lados se confundem e o diagnóstico perde sentido

---

## 5. A etapa dos juízes

| o que recebem | o que entregam |
|---|---|
| PDF numerado do artigo | Nota 1–7 (BARS) por seção, para A e para B |
| Par cego de fichamentos (A/B) | Taxonomia de erros marcada + seção do erro |
| ~10 dias de prazo nas rodadas | "O que questionaria?", "o que falta?", "qual usaria?" |

- **Cego de verdade**: IDs aleatórios, ordem A/B embaralhada por juiz
- Juiz **verifica referências** no PDF numerado — citação errada = erro marcado
- É daqui que saem os **pontos fortes e fracos** de cada produtor
- Piloto antes: 1 fichamento só, 7 dias, para **calibrar as âncoras**

---

## 6. O que precisamos do grupo

1. **Lista de estudantes** — quem participa do piloto (mestrandos + doutorandos)
2. **Validar o material** — artigo-piloto, pool de teorias, formulário
3. **Confirmar presença dos juízes no dia 6/nov** — calibração não roda sem todos
4. **Bater o martelo no cronograma** — datas realistas para todos?

---

## 7. Cronograma — só 2 reuniões

| data | reunião | por que é insubstituível |
|---|---|---|
| **sex 6/nov** | **Calibração da BARS** | único momento em que os 4 juízes negociam juntos a interpretação da rubrica; depois disso a escala **congela** |
| **sex 11/dez** | **Entrega dos resultados** | fechamento + discussão dos achados |

| semana | datas | marcos |
|---|---|---|
| **0 — Piloto** | 15/out–6/nov | **23/out**: fecha estudantes → **2/nov**: prazo juízes (7d) → **6/nov**: **REUNIÃO** (calibra BARS + distribui R1) |
| **1 — Rodada 1** | 9–23/nov | **13/nov**: fecha estudantes → IA+pares aos juízes **no mesmo dia** → **23/nov**: prazo juízes (10d) → relatório async |
| **2 — Rodada 2** | 23/nov–7/dez | **27/nov**: fecha estudantes → juízes mesmo dia → **7/dez**: prazo juízes (10d) |
| **3 — Resultados** | 8–11/dez | **11/dez**: **REUNIÃO** de entrega |

**Cada estudante ficha 1 artigo.** Reunião extra só se divergência inter-juízes ≥2 pontos na R1. *Detalhe dia a dia: [`cronograma.md`](cronograma.md)*

---

## 8. Recados importantes

- **Anonimato**: estudantes usam `S{nn}`, nunca nome; dados pessoais ficam em arquivo privado — juízes nunca veem
- **Deadlines são duros**: sexta de fechamento = recebimento **e** envio aos juízes no mesmo dia
- **Não compartilhar fichamentos** entre estudantes nem consultar saídas de IA — trabalho independente
- **Prazo dos juízes**: 7d no piloto (1 fichamento), **10d nas rodadas** (vários pares)
- O pool de teorias tem **itens de controle** — vereditos errados são detectáveis, caprichem nas evidências

---

*Backup — números do corpus:* 32 artigos · 4 juízes · 2 rodadas · avaliação cega A/B · taxonomia de 9 tipos de erro · BARS congelada após o piloto
