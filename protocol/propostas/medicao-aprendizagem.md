# PROPOSTA — Medição de aprendizagem dos estudantes

> **Status: sugestão para discussão com os coautores. NÃO implementada no
> protocolo/schema.** Adicionar qualquer módulo exige decisão antes da
> Rodada 1 (instrumento congelado) — idealmente entra no pré-registro OSF.

## Racional

O desenho final do pipeline é "IA ficha → humano revisa". Logo, a habilidade
crítica do estudante não é só *produzir* fichamentos, mas **julgar a
qualidade de um fichamento** (detectar alucinação, omissão, etc.). Medir
aprendizagem = medir evolução dessa competência avaliativa, além da
produtiva.

## Módulo A — Calibração metacognitiva (auto-avaliação)

- **O quê**: estudante auto-atribui nota BARS 1–7 por seção ao próprio
  fichamento antes de submeter.
- **Medida**: `|auto-nota − média dos juízes|` por seção → gap de
  calibração; trajetória R1→R2 mostra se o estudante aprende a *julgar*
  melhor o próprio trabalho.
- **Custo**: ~2 min/fichamento.
- **Impacto no schema**: campo opcional `self_assessment` em
  `generator` (human) — 7 inteiros 1–7.
- **Literatura**: metacognitive calibration (ICLS 2023 — ver
  REFERENCES.md §D); literatura prevê piores performers = mais
  sobre-confiantes → hipótese testável.

## Módulo B — Teste de detecção de erros (transfer test)

- **O quê**: pré-R1 e pós-R2, cada estudante revisa um fichamento com
  erros *plantados* da taxonomia (`hallucination`, `omission`,
  `invalid_source_ref`…). Mede taxa de detecção + falsos positivos.
- **Por que é forte**: é literalmente o teste de proficiência da tarefa
  final do protocolo (revisar saída de IA).
- **Custo**: ~30–45 min × 2 aplicações; requer artigo fora do corpus +
  2 versões contrabalançadas do fichamento plantado.
- **Impacto no schema**: novo arquivo `data/learning/error-spotting-*.json`.

## Módulo C — Trajetória por estudante (custo zero)

- **O quê**: curva individual de notas BARS × ordem de fichamento;
  `elapsed_minutes` × qualidade; evolução do perfil de erros por código.
- **Já está nos dados** — só exige código de análise (incluir no
  `fichamento analyze` se aprovado).

## Módulo D — Log de reflexão (qualitativo)

- 3 perguntas abertas por fichamento: o que foi difícil / o que aprendeu /
  o que faria diferente. Codificação temática → evidência qualitativa.

## Ressalva metodológica

Com ~3 fichamentos/estudante/rodada, trajetórias individuais são
**exploratórias/descritivas** — não sustentam inferência estatística.
Reportar como tal; o valor está nos padrões, não em p-valores.

## O desenho JÁ é pré/pós (insight do pesquisador, 2026-10-12)

As duas rodadas já são estruturalmente um **pré-teste → intervenção →
pós-teste**: a calibração (checklist de estudantes + refinamento do
prompt) é a intervenção. Isso sugere reframing elegante para o paper:
**calibração simétrica** — o protocolo calibra a máquina (prompt) e o
humano (checklist); medir aprendizagem = medir o efeito da calibração
humana. Pergunta extra "de graça": *o protocolo calibra melhor a máquina
ou o humano?*

### Confounds e mitigações

| risco | mitigação |
|---|---|
| checklist vs. maturação (prática sozinha já melhora) | (a) reportar efeito bundado "prática+checklist" como descritivo; (b) análise por código de erro — se o checklist mira omissões e só omissões caem, é evidência de efeito específico; (c) split-half (5 recebem, 5 não) se quiserem claim causal — custa n e simetria |
| dificuldade dos artigos difere entre rodadas | sortear alocação artigo→rodada com seed registrada (ver PROTOCOL §2) — necessário independentemente deste módulo |
| n pequeno por estudante | reportar trajetórias individuais como descritivas; testes só no agregado |

## Recomendação (proponente)

A + C: baixíssimo custo, alto alinhamento com o objetivo final do projeto.
B se houver disponibilidade de tempo dos estudantes.
