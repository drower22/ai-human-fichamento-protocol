# Proposta de ajuste das âncoras — pós-piloto R0

> **Reunião de calibração, 06/11.** Material de decisão: cada item tem
> proposta + motivo; a reunião bate **[MUDAR] / [MANTER]** item a item.
> Depois desta reunião as âncoras **congelam para R1 e R2** (decisão de
> 15/10). O que não mudar hoje, não muda mais.

## 1. O que o piloto mediu

3 de 4 juízes avaliaram às cegas o mesmo par de fichamentos
(orientação A/B sorteada por juiz — as letras abaixo já estão
**realinhadas por fichamento**, não pela letra que cada um viu).

- **Fichamento 1** — cobertura alta (8 conceitos + 5 achados)
- **Fichamento 2** — cobertura baixa (1 conceito + 1 achado)
- Autoria mantida anônima ("Respondente 1/2") — ver §5.

### Fichamento 1 (alta cobertura) — notas 1–7

| seção | Juiz α | Juiz β | Juiz γ | range |
|---|---|---|---|---|
| resumo executivo | 4 | 6 | 2 | **4** |
| questão de pesquisa | 1 | 3 | 2 | 2 |
| teorias | 5 | 4 | 4 | 1 |
| conceitos-chave | 6 | 2 | 5 | **4** |
| metodologia | 4 | 5 | 4 | 1 |
| achados | 6 | 6 | 4 | 2 |
| contribuição | 6 | 6 | 4 | 2 |
| **total** | **32** | **32** | **25** | |

### Fichamento 2 (baixa cobertura)

| seção | Juiz α | Juiz β | Juiz γ | range |
|---|---|---|---|---|
| resumo executivo | 3 | 2 | 2 | 1 |
| questão de pesquisa | 1 | 1 | 1 | 0 |
| teorias | 4 | 4 | 2 | 2 |
| conceitos-chave | 3 | 4 | 1 | 3 |
| metodologia | 3 | 4 | 3 | 1 |
| achados | 1 | 3 | 2 | 2 |
| contribuição | 2 | 2 | 2 | 0 |
| **total** | **17** | **20** | **13** | |

<sub>Colunas na ordem dos arquivos `E-R0-PILOTO-{bq8w,gx6t,nz4f}` — cada
juiz reconhece a própria coluna.</sub>

### Leitura

1. **A régua funciona no piso**: no Fichamento 2, 10 de 14 células com
   range ≤ 2; `questão`=1 e `contribuição`=2 unânimes. Fichamento fraco
   é reconhecido por todos na mesma faixa.
2. **A disputa está na zona "completo porém impreciso"** (Fichamento 1):
   `resumo` e `conceitos` com range 4. Não é ruído — as qualitativas
   mostram desacordo de **critério**: um juiz pune reprodução literal e
   confusão citar/discutir; outro paga por completude mesmo vendo
   "invenções"; o terceiro fica no meio.
3. **As âncoras atuais não respondem a pergunta que dividiu a sala**:
   cobertura compra nota alta mesmo com problemas de fidelidade?
4. **É exatamente a zona da R1**: o fichamento de IA tende a ser
   completo, fluente e com erros sutis. Se a âncora não resolver esse
   trade-off, a comparação IA×humano mede a opinião do juiz sobre o
   trade-off — não a qualidade.

## 2. Regra geral proposta — **[APROVADO]**

> **Fidelidade limita a nota.** Completude não compensa fabricação nem
> cópia literal: uma seção com conteúdo inventado, extrapolado ou colado
> do texto **não passa de 4**, independente do volume de acertos.

Entra como parágrafo de princípio no topo de `rubric.md` — resolve a
disputa central numa linha, sem reescrever a escala.

## 3. Propostas por seção

### 3.1 Resumo executivo — **[APROVADO]**

| | texto |
|---|---|
| **4 atual** | Cobre problema, método e resultado centrais, mas perde nuances relevantes ou excede/omite partes importantes. |
| **4 novo** | …ou excede/omite partes importantes, **ou é colagem de trechos literais em vez de síntese elaborada**. |
| **7 atual** | Síntese fiel e completa (~300 palavras): problema, método, achados e contribuição; quem lê entende o artigo sem abrir o PDF. |
| **7 novo** | Síntese fiel e completa (~300 palavras) **escrita com elaboração própria — não copiada**: problema, método, achados e contribuição; quem lê entende o artigo sem abrir o PDF. |

*Motivo:* divergência 4/6/2; um juiz puniu "reprodução literal sem
elaboração" — comportamento hoje ausente das âncoras.

### 3.2 Questão de pesquisa — **[APROVADO]**

| | texto |
|---|---|
| **1 novo** | Ausente ou errada — **inclui inventar uma questão explícita que o artigo não enuncia**. |
| **4 novo** | Correta mas imprecisa: ampla demais, captura só parte, **ou cola o objetivo declarado quando a questão real é outra**. |
| **7 novo** | Formula precisamente a pergunta do artigo, no escopo correto — **quando implícita, reconstruí-la a partir de objetivo/argumento/conclusão e sinalizar a implícitude conta como precisão**. |

*Motivo:* o artigo-piloto **não enuncia** a questão — os 3 puniram os
fichamentos por razões diferentes. O corpus da R1 terá casos assim.
**Decisão de desenho embutida**: reconstruir questão implícita com
fidelidade merece nota alta (um juiz sugeriu isso ao punir quem não
sinalizou a ausência). Alternativa: punir reconstrução sempre —
rejeitada, pois premiaria só artigos "bem-comportados".

### 3.3 Teorias presentes — **[APROVADO]**

| | texto |
|---|---|
| **4 novo** | Vereditos corretos na maioria, mas confunde o **papel**: marca `uses`/`discusses` o que é só **menção na revisão**, ou omite tradição relevante. |
| **7 novo** | Vereditos fiéis ao papel no argumento: **`uses` = estrutura a análise; `discusses` = engajamento substantivo sem operacionalizar; menção decorativa na revisão = `does_not_use`**; zero invenção. |

*Motivo:* dois juízes levantaram o mesmo ponto independentemente —
esquema de estruturação marcado `uses` quando só citado; `discusses`
usado para menções de revisão. A âncora passa a definir os três
vereditos pelo **papel**, não pela presença da citação. O mesmo texto
alimenta o checklist dos estudantes — critério único para os dois lados.

### 3.4 Conceitos-chave — **[APROVADO]**

| | texto |
|---|---|
| **4 novo** | 3–4 conceitos corretos e fiéis, mas a **seleção** é discutível: deixou de fora construto que carrega a análise, incluiu termo periférico como central, **ou definiu genericamente mesmo citando o texto literal**. |
| **7 novo** | 3–4 construtos **que de fato operam na análise** (não apenas mencionados no texto), com definições fiéis ao uso no artigo. |

*Motivo:* maior dispersão do piloto (6/2/5). Um juiz puniu a **seleção**;
outro distinguiu "fiel porque cita literal" de "preciso porque é central".
A âncora passa a julgar a escolha tanto quanto a definição.

### 3.5 Contribuição — **[APROVADO]**

| | texto |
|---|---|
| **4 novo** | Identifica contribuição real mas superficial (repete o abstract) **ou a infla — inflação mantém a nota em 4 mesmo quando a contribuição apontada é correta**. |
| **7 novo** | Articula avanço teórico **e** utilidade prática com a força que o artigo sustenta: **nem repete a retórica inflada do próprio artigo**, nem infla, nem reduz. |

*Motivo:* um juiz chamou o fichamento de "superinflado" e ainda assim
deu 6 — a fronteira 4↔7 estava solta.

### 3.6 O que NÃO muda — **[APROVADO: manter]**

- **`methodology`** (range 1 nos dois fichamentos) e **`main_findings`**
  (range 2; a âncora 1 "inventados" foi usada corretamente) — régua
  funcionando, não mexer.
- **Escala 1–7, âncoras em 1/4/7, taxonomia de erros, preferência A/B** —
  estrutura intacta.
- Granularidade: manter 1/4/7 (decisão de 15/10 reconfirmada pelos
  dados — o problema não é falta de pontos intermediários, é critério).

## 4. O lado dos estudantes — instruções e checklist

O critério é um só, dos dois lados: toda mudança de âncora tem reflexo
nos materiais dos estudantes. Três frentes decididas na reunião
(4.1 e 4.2 aprovadas; 4.3 = opção (a); 4.4 aprovada):

### 4.1 Vereditos de teoria — a definição já existe e falhou

`student-instructions.md` já define os três vereditos quase com as
palavras da proposta 3.3: **USA** = "estrutura o
argumento/modelo/hipóteses", **DISCUTE** = "citada substantivamente, sem
estruturar", **NÃO USA** = "ausente ou menção meramente decorativa" —
mais a heurística *"remover esta teoria quebraria o argumento?"*.

O piloto mostra que **a definição existia e mesmo assim foi mal
aplicada**: vereditos inflados (`discusses` para citação de revisão,
`uses` para teoria só mencionada). A lição não é reescrever a definição
— é dar-lhe **contraexemplo concreto**. O artigo-piloto é o material
ideal para o exercício na própria reunião (todos leram): casos T1/T12/
T13 já identificados na análise dos logs.

- **Proposta**: manter as definições; adicionar às instruções uma linha
  de alerta — *"teoria que só aparece citada na revisão de literatura,
  sem ser retomada na análise, não é `discute`"* — e exercitar os 3
  casos na reunião.
- **E** alinhar `rubric.md` §3 à mesma semântica (proposta 3.3) — hoje a
  âncora fala "papel no argumento" genericamente; passa a nomear os
  três papéis.

### 4.2 Sincronização do form — ação obrigatória, não opcional

A auto-avaliação do estudante **mostra as mesmas âncoras dos juízes**
(instructions §"Depois de terminar"). Se a rubrica virar v1.1.0, o
formulário em produção precisa exibir o texto novo **antes da R1** —
senão juiz e estudante autorrespondem em réguas diferentes.

- Ação: atualizar âncoras no form de estudantes + form de juízes e
  redeployar antes da distribuição da R1.

### 4.3 `checklist-students.md` permanece fechado até a pós-R1

Por desenho (o próprio arquivo avisa): o checklist é o instrumento da
calibração entre rodadas — preenchê-lo agora com os padrões do piloto
vazaria para o baseline da R1 o que deveria ser efeito medido R1→R2.

**O que entra nas instruções agora** é só *definição alinhada ao
rubric* (4.1) e usabilidade — não coaching de qualidade.

**Decisão para a sala**: as estratégias de processo dos logs reflexivos
(ler o form antes do artigo, codebook durante a leitura, resumo por
último, dividir em 2 sessões) —

- (a) socializar verbalmente na reunião → vira prática da R1, baseline
  "instruído" (Δ R1→R2 passa a medir só o que o checklist *a mais*
  agrega);
- (b) guardar para o checklist pós-R1 → baseline "cru", Δ mais limpo;
- (c) meio-termo: instruções ganham só dicas de usabilidade do
  instrumento ("leia o formulário antes de começar"), estratégias de
  *qualidade* ficam para o checklist.

*Recomendação*: (c). Separa "aprender a usar o instrumento" de
"aprender a fazer bem" — e mantém o Δ interpretável.

### 4.4 Log reflexivo passa a 4 perguntas — **[APROVADO]**

O log é **diagnóstico do estudo** — mapear dificuldades/barreiras da
tarefa — e não exercício de aprendizagem do estudante. No piloto, a
pergunta única misturou dois objetos: dificuldade **com o
artigo/tema** e dificuldade **com o formato da pesquisa** (formulário,
PDF numerado, vereditos, referências). Na R1 o instrumento separa na
fonte: q1 barreiras de conteúdo, q2 barreiras de formato,
q3 abordagem, q4 uso de IA.

- Implementação se aprovado: `student-fichamento-template.json`
  (q1–q4), `student-form.md`, `student-column-map.json` e o form em
  produção. `reflection_log` é `dict[str,str]` no schema — não exige
  migração.

## 5. Registro das decisões da reunião

| # | item | decisão |
|---|---|---|
| 2 | regra geral (fidelidade limita nota) | **MUDAR** |
| 3.1 | resumo — síntese vs. colagem | **MUDAR** |
| 3.2 | questão implícita reconstruída | **MUDAR** |
| 3.3 | teorias — papel no argumento | **MUDAR** |
| 3.4 | conceitos — seleção conta | **MUDAR** |
| 3.5 | contribuição — inflação trava no 4 | **MUDAR** |
| 3.6 | demais seções inalteradas | **MANTER** |
| 4.1 | instruções: alerta "citar ≠ discutir" + exercício T1/T12/T13 | **MUDAR** |
| 4.2 | sincronizar âncoras nos forms (juiz + estudante) antes da R1 | **MUDAR** |
| 4.3 | estratégias dos logs: (a) agora / (b) pós-R1 / (c) só usabilidade | **(a) socializadas na reunião** |
| 4.4 | log reflexivo: 3 para 4 perguntas (conteúdo × formato) | **MUDAR** |

Tabela transcrita retroativamente em 09/11 a partir do registro verbal
da reunião — as 11 propostas foram aprovadas (4.3 na opção (a)).

Após a reunião: changelog `v1.1.0 — pós-piloto R0` em `rubric.md`,
registro em `diary/2026-11-06.md` e propagação do vocabulário para
`checklist-students.md` (mesmo critério dos dois lados).

## 6. Nota de desenho — estudantes na sala

**Não contamina**, desde que a autoria continue selada — e há um risco
real a gerenciar:

- **Por que não contamina**: transferir o critério da régua aos
  estudantes é a *função* do piloto — é o canal pelo qual o
  `checklist-students.md` opera (decisão de 15/10, item 8). O que os
  estudantes aprenderem hoje vira condição documentada da R1, simétrica
  ao refinamento do prompt da IA.
- **Risco real 1 — autocensura do juiz**: sabendo que os autores estão
  na sala, o juiz pode suavizar a crítica e a negociação da âncora fica
  enviesada para brandura. *Conduta*: apresentar números primeiro,
  criticar o instrumento (não o autor), exemplos sempre anonimizados.
- **Risco real 2 — desanonimização**: se alguém identificar os
  respondentes, o juiz aprende o estilo do estudante e pode reconhecê-lo
  na R1. *Conduta*: manter "Respondente 1/2", não confirmar autoria em
  voz alta, mapa de pares permanece em `data/private/`.
- **Risco 3 — custo social**: o Fichamento 2 será dissecado. Enquadrar
  como *sorteio de extremos para calibrar a régua*, não como ranking de
  desempenho.
- **O que permanece selado**: mapa par↔respondente, token↔juiz,
  `participants.csv`.
