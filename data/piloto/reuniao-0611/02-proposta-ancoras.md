# Piloto R0: proposta de ajuste das âncoras (decisões)

**Reunião de calibração, 06/11/2026.** Material de decisão.
Cada item traz proposta e motivo: a sala bate **[MUDAR] / [MANTER]**.
Após esta reunião as âncoras **congelam para R1 e R2**. O que não
mudar hoje, não muda mais.

## Item 1: Regra geral (topo da rubrica)

> **Fidelidade limita a nota.** Completude não compensa fabricação nem
> cópia literal: uma seção com conteúdo inventado, extrapolado ou colado
> do texto **não passa de 4**, independente do volume de acertos.

*Motivo:* resolve a disputa central do piloto numa linha. Um juiz deu 6
a um fichamento que ele mesmo achou inventado; outro deu 2 pelo mesmo
comportamento. Sem a regra, cada juiz decide o trade-off do seu jeito.

## Item 2: Resumo executivo

- **4**: …ou excede/omite partes importantes, **ou é colagem de trechos
  literais em vez de síntese elaborada**.
- **7**: Síntese fiel e completa (~300 palavras) **escrita com
  elaboração própria, não copiada**: problema, método, achados e
  contribuição; quem lê entende o artigo sem abrir o PDF.

*Motivo:* divergência 4/6/2. "Reprodução literal sem elaboração" não
estava escrita em âncora nenhuma.

## Item 3: Questão de pesquisa

- **1**: Ausente ou errada. **Inclui inventar uma questão explícita que
  o artigo não enuncia.**
- **4**: Correta mas imprecisa: ampla demais, captura só parte, **ou
  cola o objetivo declarado quando a questão real é outra**.
- **7**: …no escopo correto. **Quando implícita, reconstruí-la a partir
  de objetivo/argumento/conclusão e sinalizar a implícitude conta como
  precisão.**

*Motivo:* o artigo-piloto não enuncia a questão; o corpus terá casos
assim. Decisão embutida: reconstruir questão implícita com fidelidade
merece nota alta.

## Item 4: Teorias presentes

- **4**: Vereditos corretos na maioria, mas confunde o **papel**: marca
  `uses`/`discusses` o que é só **menção na revisão**, ou omite tradição
  relevante.
- **7**: Vereditos fiéis ao papel no argumento: **`uses` = estrutura a
  análise · `discusses` = engajamento substantivo sem operacionalizar ·
  menção decorativa na revisão = `does_not_use`**; zero invenção.

*Motivo:* dois juízes levantaram o ponto independentemente:
`discusses` dado a citação de revisão. A âncora passa a nomear os três
papéis, no mesmo vocabulário das instruções aos estudantes.

## Item 5: Conceitos-chave

- **4**: 3 a 4 conceitos corretos e fiéis, mas a **seleção** é
  discutível: deixou de fora construto que carrega a análise, incluiu
  termo periférico como central, **ou definiu genericamente mesmo
  citando o texto literal**.
- **7**: 3 a 4 construtos **que de fato operam na análise** (não apenas
  mencionados), com definições fiéis ao uso no artigo.

*Motivo:* maior dispersão do piloto (6/2/5). A âncora passa a julgar
a **escolha** tanto quanto a definição.

## Item 6: Contribuição

- **4**: Identifica contribuição real mas superficial (repete o
  abstract) **ou a infla. Inflação mantém a nota em 4 mesmo quando a
  contribuição apontada é correta**.
- **7**: Articula avanço teórico **e** utilidade prática com a força que
  o artigo sustenta: **nem repete a retórica inflada do próprio
  artigo**, nem infla, nem reduz.

*Motivo:* um juiz chamou o fichamento de "superinflado" e deu 6.
Fronteira entre 4 e 7 estava solta.

## Item 7: O que não muda

`methodology` (range 1) e `main_findings` (range 2; âncora 1 usada
corretamente): régua funcionando. Escala de 1 a 7, âncoras em 1/4/7,
taxonomia de erros e preferência A/B ficam intactos.

## Item 8: Lado dos estudantes

- **8a.** Instruções: manter as definições de `usa`/`discute`/`não usa`;
  adicionar o alerta *"teoria só citada na revisão, sem retomada na
  análise, não é `discute`"*; exercitar os casos T1/T12/T13 na própria
  reunião.
- **8b.** **Sincronizar os forms**: a auto-avaliação do estudante mostra
  as mesmas âncoras dos juízes. A rubrica v1.1.0 precisa estar no form
  antes da R1.
- **8c.** Estratégias dos logs (ler o form antes, codebook durante a
  leitura, resumo por último, 2 sessões): **(a)** socializar agora,
  baseline instruído; **(b)** guardar para o checklist pós-R1, Δ limpo;
  **(c)** só usabilidade agora, qualidade depois *(recomendado)*.

## Item 9: Log reflexivo passa a 4 perguntas

O log é **diagnóstico do estudo** (mapear dificuldades/barreiras da
tarefa), não exercício de aprendizagem do estudante. No piloto, a
pergunta única misturou dois objetos: dificuldade **com o artigo/tema**
e dificuldade **com o formato da pesquisa**. Na R1 o log separa:
q1 barreiras de conteúdo, q2 barreiras de formato, q3 abordagem,
q4 uso de IA.

*Motivo:* barreira de conteúdo diz onde a leitura trava; barreira de
formato diz onde o instrumento trava. Implementação se aprovado:
`student-fichamento-template.json` (q1 a q4), `student-form.md`,
`student-column-map.json` e o form em produção.

## Registro das decisões

| # | item | decisão |
|---|---|---|
| 1 | regra geral: fidelidade limita nota | ☐ |
| 2 | resumo: síntese vs. colagem | ☐ |
| 3 | questão implícita reconstruída | ☐ |
| 4 | teorias: papel no argumento | ☐ |
| 5 | conceitos: seleção conta | ☐ |
| 6 | contribuição: inflação trava no 4 | ☐ |
| 7 | demais seções inalteradas | ☐ |
| 8a | alerta "citar ≠ discutir" + exercício | ☐ |
| 8b | sincronização dos forms antes da R1 | ☐ |
| 8c | estratégias: (a) agora / (b) pós-R1 / (c) usabilidade | ☐ |
| 9 | log reflexivo: 3 para 4 perguntas (conteúdo × formato) | ☐ |
