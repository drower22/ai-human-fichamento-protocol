# DECISÕES — escala de avaliação dos juízes

> **Atualizado pós-reunião de coautores (decisões em
> `diary/2026-10-15.md`).** Itens marcados **[DECIDIDO]** já foram
> propagados para `rubric.md` / `PROTOCOL.md` / schema. O instrumento
> precisa estar **congelado antes da Rodada 1** e, idealmente, entrar no
> pré-registro OSF.

Estado atual: escala tipo BARS 1–7 por seção (7 seções), âncoras verbais
em 1/4/7, taxonomia de 8 códigos de erro, preferência A/B por artigo.

---

## 1. Nome do instrumento — **[DECIDIDO: "BARS adaptada"]**

As âncoras foram escritas *a priori*. BARS canônico (Smith & Kendall 1963)
exige âncoras derivadas de *critical incidents* com retranslação entre
especialistas — não é o que temos.

- **Decisão**: reportar como **"BARS adaptada"** no paper.
  Propagado para `rubric.md`.

## 2. Congelar âncoras entre R1 e R2 ⚠️ (mais importante)

A regra de calibração atual permite **reescrever âncoras** entre rodadas.
Se a régua muda, a diferença de médias R1→R2 deixa de medir o efeito da
calibração — perde-se a comparabilidade que justifica as duas rodadas.

- **Opções**: (a) congelar âncoras nas duas rodadas e refinar só a
  taxonomia de erros; (b) aceitar régua móvel e abrir mão do Δ de notas.
- **Recomendação**: (a). A taxonomia é checklist — refinar não afeta a
  escala. A métrica primária (preferência A/B) é scale-free de qualquer
  forma.

## 3. Correção da justificativa (PROTOCOL §6)

O texto diz que BARS "reduz variância inter-rater" — mas no desenho
nominator-only há **1 rater por fichamento**, logo essa variância nem é
observável. Justificativa correta: notas auditáveis, consistência
intra-juiz no par A/B, vocabulário comum com a taxonomia de erros.

- **Decisão**: aprovar a reformulação do texto.

## 4. Piloto R0 — **[DECIDIDO: aprovado, desenho simplificado]**

- **Desenho aprovado**: 1 artigo **fora do corpus** fichado por **todos
  os alunos**; sorteia-se **1 fichamento de aluno** que os 4 juízes
  avaliam às cegas — divergências entre juízes indicam âncoras a
  reescrever. Depois do piloto, âncoras congeladas.
- A IA **não** participa do piloto: o pipeline de geração é testado à
  parte (dry-run técnico) quando modelo + API keys estiverem definidos.

## 5. Granularidade das âncoras

Hoje só 1/4/7 têm comportamentos ancorados; 2–3 e 5–6 interpolam.

- **Opções**: manter como está · ancorar um ponto intermediário.
- **Recomendação**: manter; se houver piloto, decidir com dados.

## 6. Hierarquia de métricas (confirmar)

O protocolo declara **preferência A/B** como métrica primária e BARS por
seção como secundária (Wilcoxon pareado + tamanho de efeito). Confirmar —
define o que o paper reporta como resultado principal.

## 7. Uso do campo `confidence` (1–3)

O juiz marca o quanto conhece o artigo, mas o plano de análise não define
o uso.

- **Opções**: só descritivo · análise de sensibilidade excluindo
  avaliações com confidence = 1.
- **Recomendação**: os dois (descritivo + sensibilidade).

## 8. Acoplamento com módulos de aprendizagem — **[DECIDIDO]**

Módulos **A + C + D aprovados** (auto-avaliação, trajetória, log de
reflexão); **B descartado**. Como todos os alunos ficham o artigo-piloto,
todos ganham contato com a escala antes da R1 — o piloto serve também de
calibração dos estudantes para o Módulo A. Implementado: campo
`self_assessment` em `generator` (human) + item no template do aluno.

---

### Resumo — status pós-reunião

| # | decisão | status |
|---|---|---|
| 1 | nome | ✅ **BARS adaptada** |
| 2 | âncoras R1→R2 | ✅ congeladas pós-piloto (propagado a `rubric.md`); confirmação explícita da regra entre rodadas recomendada |
| 3 | justificativa §6 | ✅ reformulação aplicada a `PROTOCOL.md` §6 |
| 4 | piloto R0 | ✅ aprovado — alunos ficham, sorteia 1 p/ juízes |
| 5 | granularidade | ⏸ manter 1/4/7 (revisitar após piloto, se divergência) |
| 6 | métrica primária | ⏸ pendente de confirmação (preferência A/B) |
| 7 | confidence | ⏸ pendente (proposta: descritivo + sensibilidade) |
| 8 | módulos aprendizagem | ✅ **A + C + D**; B descartado |
