# Passo a passo — criar o Google Form do piloto

Formulário de entrega do fichamento do artigo-piloto. Tempo de montagem:
~25 min. Regra de ouro: **copie os títulos das perguntas exatamente como
estão** — eles viram as colunas do CSV que o pipeline ingere.

No Forms: cada seção vira uma "seção" do formulário (ícone de dois
retângulos na barra lateral direita). Marque como **obrigatória** toda
pergunta que não tiver "(opcional)" no nome.

---

## 0. Título e descrição do formulário

**Título:**

```
Fichamento — Artigo-Piloto
```

**Descrição (cole na descrição do form):**

```
Entrega do fichamento do artigo-piloto. Leia o artigo numerado por
completo ANTES de preencher. Responda em português e inclua referências
entre parênteses no formato (p.N Lnnn) — ex.: (p.5 L165) ou
(p.5 L165-170). Não use IA e não consulte fichamentos de colegas.
Reserve ~30 minutos para preencher depois de terminar o fichamento.
```

**Configurações (engrenagem):** desligue "Coletar endereços de e-mail"
e "Editar após envio".

---

## 1. Seção "Identificação"

Descrição da seção:

```
Seus dados. Nome e demografia servem só para caracterizar a amostra da
pesquisa: NÃO aparecem no fichamento que os juízes avaliam.
```

Perguntas:

| título (copie exato) | tipo | opções / descrição |
|---|---|---|
| `full_name` | Resposta curta | `Nome completo.` |
| `age` | Resposta curta | `Idade (anos).` |
| `gender` | Múltipla escolha | `feminino` · `masculino` · `outro` · `prefiro não informar` |
| `program` | Múltipla escolha | `mestrado` · `doutorado` |
| `participant_id` | Múltipla escolha | Uma opção por estudante: `S01`, `S02`, … (crie quantas precisar). Descrição: `Seu identificador atribuído pela coordenação.` |
| `article_id` | Múltipla escolha | Opção única: `PILOTO`. Descrição: `Fixo nesta fase.` |
| `consent` | Caixas de seleção | Uma opção: `Declaro que li as instruções, produzi o fichamento sozinho(a) e não consultei fichamentos de IA ou de colegas.` |

---

## 3. Seção "Resumo executivo"

| título | tipo | descrição |
|---|---|---|
| `executive_summary` | Parágrafo | `Síntese em ~300 palavras: problema, abordagem teórica, método, achados e contribuição. Referências entre parênteses: (p.N Lnnn).` |

---

## 4. Seção "Questão de pesquisa"

| título | tipo | descrição |
|---|---|---|
| `research_question` | Parágrafo | `A pergunta que o artigo busca responder, formulada com precisão. Inclua a referência (p.N Lnnn).` |

---

## 5. Seção "Teorias"

Descrição da seção:

```
Para cada teoria da lista, escolha um veredito:
uses = estrutura o argumento (se remover, o argumento quebra)
discusses = debatida ou citada substantivamente, sem estruturar
does_not_use = ausente do artigo ou só menção decorativa
Para uses e discusses, preencha também a evidência: a linha (p.N Lnnn)
e, idealmente, o trecho literal.
```

**5a. Pergunta `theory_verdicts`** — tipo **Grade de múltipla escolha**
(obrigatória, "exigir uma resposta por linha"):

- **Linhas** (cole uma por linha — o código T{n} vem antes do nome):

```
T1 - Abordagem contingencial da estratégia
T2 - Capacidades dinâmicas
T3 - Estratégia como prática (strategy-as-practice)
T4 - Abordagem de conteúdo da estratégia
T5 - Aprendizagem organizacional
T6 - Teoria da estruturação
T7 - Teoria institucional
T8 - Abordagem processual da estratégia
T9 - Teoria dos custos de transação
T10 - Visão baseada em recursos (RBV)
T11 - Momentum burocrático
T12 - Esquema de estruturação de Barley & Tolbert
T13 - Escola de aprendizagem (learning school)
```

- **Colunas:**

```
uses
discusses
does_not_use
```

**5b. Evidências** — 13 perguntas de **Resposta curta**, todas
**opcionais**, descrição comum: `Se marcou uses ou discusses: referência
(p.N Lnnn) + trecho literal. Ex.: (p.5 L165-170) "a prática emerge..."`

Títulos (copie exato):

```
T1.evidence
T2.evidence
T3.evidence
T4.evidence
T5.evidence
T6.evidence
T7.evidence
T8.evidence
T9.evidence
T10.evidence
T11.evidence
T12.evidence
T13.evidence
```

> Dica: no Forms, crie a primeira e use "Duplicar" trocando só o número.

**5c. Pergunta `extra_theories`** — Parágrafo, opcional:

```
O artigo usa ou discute alguma teoria que NÃO está na lista? Uma por
linha: nome — tradição — uses ou discusses — (p.N Lnnn). A lista foi
montada antes da sua leitura e pode não cobrir tudo: encontrar o que
faltou conta pontos a seu favor.
```

---

## 6. Seção "Conceitos-chave"

Descrição da seção:

```
De 3 a 4 conceitos centrais do artigo: nome, como o artigo define/usa e
a evidência.
```

Para **i = 1, 2, 3** (obrigatórios) e **i = 4** (opcional), três
perguntas por slot:

| título | tipo | descrição |
|---|---|---|
| `key_concept.i.concept` | Resposta curta | `Nome do conceito.` |
| `key_concept.i.definition` | Parágrafo | `Como o artigo define ou usa.` |
| `key_concept.i.evidence` | Resposta curta | `(p.N Lnnn) + trecho literal.` |

(Ou seja: `key_concept.1.concept`, `key_concept.1.definition`,
`key_concept.1.evidence`, depois `key_concept.2.*`, `key_concept.3.*`,
`key_concept.4.*` — 12 perguntas no total.)

---

## 7. Seção "Metodologia"

| título | tipo | opções / descrição |
|---|---|---|
| `methodology.study_type` | Múltipla escolha | `teórico` · `empírico` · `simulação` · `revisão` · `outro` |
| `methodology.design` | Resposta curta | `Delineamento (ex.: estudo de caso único exploratório).` |
| `methodology.sample_type` | Resposta curta | `Ex.: profissionais da empresa. N/A se não houver.` |
| `methodology.sample_size` | Resposta curta | `Número ou N/A.` |
| `methodology.sector` | Resposta curta | `Setor/indústria dos dados.` |
| `methodology.period` | Resposta curta | `Período coberto pelos dados.` |
| `methodology.methods` | Resposta curta | `Técnicas separadas por vírgula (ex.: entrevistas semiestruturadas, análise documental, observação direta).` |
| `methodology.analysis_note` | Parágrafo, opcional | `Como os dados foram analisados.` |
| `methodology.source_refs` | Resposta curta | `(p.N Lnnn) da seção de método.` |

---

## 8. Seção "Achados principais"

Descrição da seção:

```
De 3 a 5 achados do artigo. Classifique cada um.
```

Para **i = 1, 2, 3** (obrigatórios) e **i = 4, 5** (opcionais), três
perguntas por slot:

| título | tipo | opções / descrição |
|---|---|---|
| `finding.i.finding` | Parágrafo | `O achado ou proposição, com suas palavras.` |
| `finding.i.type` | Múltipla escolha | `empirical` · `proposition` · `model` |
| `finding.i.evidence` | Resposta curta | `(p.N Lnnn) + trecho literal.` |

(15 perguntas no total: `finding.1.*` … `finding.5.*`.)

---

## 9. Seção "Contribuição"

| título | tipo | descrição |
|---|---|---|
| `contribution.theoretical` | Parágrafo | `O avanço teórico que o artigo entrega.` |
| `contribution.practical` | Parágrafo | `A utilidade prática.` |

---

## 10. Seção "Auto-avaliação"

Descrição da seção:

```
Agora avalie o SEU fichamento com a mesma régua dos juízes: nota de 1 a
7 por seção. Seja honesto: a pesquisa mede o gap entre a sua auto-nota e
a nota do juiz. Não será mostrado aos juízes.
```

**Pergunta `self_assessment`** — Grade de múltipla escolha
(obrigatória, uma resposta por linha):

- **Linhas:**

```
executive_summary
research_question
theories
key_concepts
methodology
main_findings
contribution
```

- **Colunas:** `1` `2` `3` `4` `5` `6` `7`

---

## 11. Seção "Reflexão"

Descrição da seção:

```
Quatro respostas curtas e sinceras sobre as dificuldades e barreiras da
tarefa. Não são avaliadas nem mostradas aos juízes.
```

| título | tipo | pergunta/descrição |
|---|---|---|
| `reflection.q1` | Parágrafo | `Quais dificuldades ou barreiras você encontrou com o artigo e o tema, o conteúdo que leu?` |
| `reflection.q2` | Parágrafo | `Quais dificuldades ou barreiras você encontrou com o formato da pesquisa, o instrumento (formulário, PDF numerado, vereditos, referências p.N Lnnn)?` |
| `reflection.q3` | Parágrafo | `Se você fosse refazer este fichamento, o que mudaria na sua abordagem?` |
| `reflection.q4` | Parágrafo | `Você usou alguma ferramenta de IA ou auxílio externo para ler ou fichar? Se sim, qual e como?` |

---

## 12. Seção "Tempo total"

Descrição da seção:

```
Última pergunta. Estime o tempo total, em minutos, que levou para ler o
artigo e produzir o fichamento. Estimativa honesta basta. Este dado é de
pesquisa (custo-tempo do trabalho humano) e não vai aos juízes.
```

| título | tipo | descrição |
|---|---|---|
| `elapsed_minutes` | Resposta curta | `Sua estimativa em minutos.` |

---

## 13. Depois de publicar

1. **Enviar** → copie o link → mande junto com o PDF numerado e as
   instruções.
2. Quando fechar (sex 23/out): **Respostas → ⋮ → Fazer o download das
   respostas (.csv)**.
3. Entrega pra coordenação rodar:

```bash
fichamento import-human-csv --round 0 --csv respostas.csv \
  --pool data/piloto/theory-pool.json
```

---

### Total: ~51 perguntas

| seção | perguntas |
|---|---|
| Identificação | 7 |
| Resumo / Questão | 2 |
| Teorias | 1 grade + 13 evidências + extra_theories |
| Conceitos | 12 (4 slots × 3) |
| Metodologia | 9 |
| Achados | 15 (5 slots × 3) |
| Contribuição | 2 |
| Auto-avaliação | 1 grade |
| Reflexão | 4 |
| Tempo total | 1 |
