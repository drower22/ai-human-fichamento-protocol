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

**O quê**: pré-R1 e pós-R2, cada estudante revisa um fichamento com erros
*plantados* da taxonomia (`hallucination`, `omission`, `misinterpretation`,
`invalid_source_ref`…). Mede taxa de detecção + falsos positivos.

**Por que é forte**: é literalmente o teste de proficiência da tarefa final
do protocolo — revisar saída de IA. Se o checklist da calibração funciona,
a taxa de detecção deve subir do pré para o pós.

### Como se parece o instrumento

- Um artigo **fora do corpus** (ninguém ficha ele no estudo) — evita
  contaminação.
- Um fichamento construído pelos pesquisadores com ~10 erros conhecidos,
  um por código da taxonomia, com a resposta-chave registrada em arquivo
  privado (`data/learning/error-spotting-key.json`).
- Duas versões contrabalançadas (erros diferentes no mesmo artigo, ou dois
  artigos): metade dos estudantes recebe a versão X no pré e Y no pós —
  controla efeito de memorização do item específico.
- Tarefa do estudante: "marque os problemas que encontrar e classifique-os"
  — mesmo vocabulário da rubrica que os juízes usam.

### Medidas

| métrica | definição |
|---|---|
| taxa de detecção | erros encontrados / erros plantados |
| falsos positivos | flags que não correspondem a erro plantado |
| especificidade | detecção por código de erro (ele pega alucinação mas não omissão?) |

(Sem medida de tempo na tarefa B: auto-reportada em tarefa curta é
ruidosa e incentivaria pressa artificial.)

### Custo e agenda

- ~30–45 min por aplicação × 2 (pré-R1, pós-R2).
- Trabalho de preparação: construir o fichamento plantado + chave —
  ~1 dia de trabalho dos pesquisadores, fora do pipeline automático.
- **Não precisa estar pronto sexta**: o pré pode ser aplicado na primeira
  semana da R1, antes dos primeiros fichamentos.

- **Impacto no schema**: novo arquivo `data/learning/error-spotting-*.json`
  (não toca fichamento.schema).

## Módulo C — Trajetória por estudante (custo zero)

- **O quê**: curva individual de notas BARS × ordem de fichamento;
  `elapsed_minutes` × qualidade; evolução do perfil de erros por código.
- **`elapsed_minutes` = tempo total estimado** (leitura + fichamento),
  auto-reportado por artigo. Leitura principal: **métrica econômica** —
  custo-tempo humano por fichamento, comparável depois ao tempo/custo de
  geração+revisão com IA ("economia de tempo da IA"). Uso secundário:
  covariável descritiva na trajetória de aprendizagem.
- **Já está nos dados** — só exige código de análise (incluir no
  `fichamento analyze` se aprovado).

## Módulo D — Log de reflexão (qualitativo)

- 3 perguntas abertas por fichamento: o que foi difícil / o que aprendeu /
  o que faria diferente. Codificação temática → evidência qualitativa.
- **Momento**: imediatamente após submeter cada fichamento, no mesmo
  formulário de entrega — antes de qualquer retorno dos juízes (o log
  deve refletir a experiência de produção, não a nota recebida).
- Alternativa de menor carga: 1 log por rodada — perde a granularidade
  por artigo que conecta o relato ao perfil de erros.

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

**Pacote mínimo: A + C + D** — ~3 min/fichamento de custo total, alto
alinhamento com o objetivo final do projeto. **B é o stretch goal**: o
teste mais direto da competência-alvo, mas exige ~1 dia de preparação e
2× ~40 min dos estudantes; o pré pode ser aplicado na primeira semana da
R1, então não é blocker para a reunião de sexta — mas a decisão de
incluí-lo precisa sair nessa reunião, pois é o único módulo que exige
coleta extra *antes* dos fichamentos começarem.
