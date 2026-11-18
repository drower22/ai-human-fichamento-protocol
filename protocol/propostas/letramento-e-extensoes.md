# PROPOSTA — Letramento como intervenção e extensões do desenho

> **Status: EM DISCUSSÃO.** Memorando para a reunião de coautores
> (quinta, 19/11). Consolida as ideias discutidas em 17/11 sobre como o
> protocolo também funciona como intervenção formativa, e sobre três
> possíveis extensões do desenho (R3 de juízes, triagem por estudantes,
> Delphi de corpus). Nada aqui está implementado ou decidido.

## 1. Contexto: onde o desenho está hoje

- Piloto: calibração da régua BARS e dos juízes (material humano only).
- R1 em curso: 16 pares cegos (humano × IA), um juiz por par, 4 pares por
  juiz, janela até 22/11.
- R2 prevista: 16 novos artigos, alunos recebem dia 23, entregam até 29.
- Medidas já coletadas por fichamento: BARS 1–7 em 7 seções, taxonomia de
  erros, preferência A/B, tempo, autoavaliação do estudante na mesma
  régua, log de reflexão.

## 2. O ponto fraco atual: um juiz por par

Na R1 cada fichamento tem exatamente um avaliador. Consequências:

- Sem concordância inter-rater dentro da rodada (o Krippendorff α do
  `fichamento analyze` fica indefinido por desenho).
- Severidade do juiz e dificuldade do artigo ficam confundidas entre
  juízes. O pareamento A/B dentro de cada juiz segue limpo, mas a
  alegação "juízes diferentes avaliam parecido" só tem evidência no
  piloto.

Nova rodada com o mesmo desenho (mais pares, um juiz cada) só repete a
fraqueza com n maior.

## 3. Extensão 1: R3 somente de juízes (estudo de confiabilidade)

Eleger 4 a 8 artigos já fichamentados (R1 ou R2) e fazer **todos os 4
juízes avaliarem todos os pares**.

- Nenhum fichamento novo é produzido: os 32 pares já existirão.
- Cada artigo foi avaliado por exatamente um juiz na rodada original,
  então cada juiz vê 1 par conhecido (mede test-reteste intra-rater) e
  os demais novos.
- Re-sortear a orientação A/B para quem já viu o par.
- Resultado: α inter-rater em material real, não só no piloto;
  preferência com 4 votos por par; narrativa limpa de "estudo de
  confiabilidade do instrumento" no paper.
- Custo: 4 a 8 avaliações por juiz, equivalente a uma rodada. Recomendado
  6 a 8 artigos (4 é o mínimo viável para o α).

## 4. Extensão 2: rodada de triagem por estudantes

Os estudantes nunca usam fichamento para decidir. Uma rodada de
inclusão/exclusão testa o artefato no uso pretendido.

Três formatos possíveis:

- **A. Triagem cega com fichamento**: cada estudante vota inclui/exclui
  em N candidatos com seus fichamentos. Mede tempo, acordo com critério
  externo. Exige ground truth (decisão do PI ou consenso posterior).
- **B. Fichamento vs resumo (split-half)**: mesma decisão, ajudas
  diferentes. Separa o artefato do baseline real de triagem. Exige
  artigos distintos por braço.
- **C. Triagem como estágio zero do Delphi**: votos individuais alimentam
  o Delphi; só divergências vão a discussão. Mais barata e sinérgica.

Controle necessário: ninguém tria artigo que fichamentou (conhece demais,
o auxílio vira irrelevante).

Ponto fraco: para artigos além dos 32, faltam fichamentos do lado humano;
opções são restringir aos 32 existentes ou usar só IA nessa fase (a
pergunta passa a ser "o artefato funciona?", não "quem produz melhor?").

## 5. Extensão 3: Delphi de corpus

Delphi é método de convergência, não de confiabilidade. Usado no lugar da
R3 destruiria a independência das notas (concordância fabricada).

Encaixe correto: decisão de inclusão no corpus, a pergunta de pesquisa em
uso real. Pode ser do grupo todo:

- ~20 participantes é tamanho adequado; anonimato e feedback agregado
  neutralizam dominância professor/aluno.
- Permite medir convergência por subgrupo (alunos × juízes), um
  desdobramento da aprendizagem para o domínio do julgamento de corpus.
- Cuidados: participante não decide (ou vota com flag) sobre o próprio
  artigo; perguntas separadas "incluiria no corpus?" e "o fichamento foi
  suficiente para decidir?".

## 6. Como medir aprendizagem (o pacote defensável)

Aprendizagem é construto latente: nada a mede isoladamente. O pacote de
indicadores convergentes, por força:

| Indicador | O que mede | Status |
|---|---|---|
| Gap BARS aluno − IA por seção, R1→R2 | qualidade com dificuldade do artigo descontada pelo par | já coletado |
| Gap de calibração (autoavaliação − juiz) | metacognição | já coletado |
| Migração da taxonomia de erros | consolidação (de erro estrutural para superficial) | já coletado |
| Tempo × qualidade | fluência | já coletado |
| Reteste no artigo do piloto | pré/pós mesma pessoa × mesmo material | **a decidir** |

O reteste é o item que falta: cada aluno reficha o artigo do piloto no
fim da R2 (~30–60 min). Elimina os confounds de artigo mais fácil e de
material diferente. O fichamento do piloto já tem notas de juiz, com a
ressalva de que a régua foi recalibrada desde lá.

Cautela honesta: sem grupo controle, não se prova que o protocolo causou
o ganho. Redação recomendada: "indicadores convergentes de aprendizagem".

## 7. O protocolo como intervenção de letramento

O que o fichamento já treina por construção:

- Schema fixo: anatomia do artigo acadêmico.
- Referência `p.N/Lnn` obrigatória: leitura ancorada em evidência.
- Veredito de teoria ("citar não é discutir"): letramento teórico.
- Autoavaliação na régua dos juízes: letramento avaliativo.
- Log de reflexão: metacognição.

O que falta é fechar o circuito: hoje a avaliação do juiz entra na
análise e morre aí. As ações formativas propostas:

### 7.1 Devolutiva individual (após a R1 fechar, antes da produção da R2)

Página pessoal por estudante, acessada antes de ele começar a fichar o
artigo novo. Funciona como portão de entrada da R2.

Conteúdo: notas do juiz por seção, próprio × IA, lado a lado; preferência
do juiz e erros marcados por seção; a autoavaliação do próprio aluno ao
lado (tabela de calibração); os dois fichamentos completos do par.

### 7.2 O aluno como juiz do próprio par (duas sessões)

O aluno é quem mais conhece o artigo. Duas sessões, uma por rodada,
transformam o exercício em instrumento longitudinal.

**Sessão 1 — par da R1, embutida na devolutiva, antes de produzir a R2:**

1. Par cego como "versão X / Y"; ele marca por seção qual é melhor,
   antes de ver qualquer nota (se vir o placar do juiz antes, a própria
   avaliação fica contaminada).
2. Revelação junta: identidades, notas do juiz e a autoavaliação dele.
3. Reflexão guiada: onde discorda do juiz? onde a IA foi melhor? onde ele
   foi melhor? o que a IA se recusou a afirmar, e essa cautela era certa
   ou perda? o que faria diferente na R2?

**Sessão 2 — par da R2, após os juízes fecharem a rodada:**

Mesmo exercício, com a pergunta-guia trocada para "o que mudou do seu
primeiro para o segundo fichamento?". Cabe na janela da discussão de
calibração em grupo.

Comparando as duas sessões: se na segunda o aluno julga o próprio par
mais parecido com o juiz, isso é letramento avaliativo medido no ato, não
inferido. A cegueira na sessão 1 é fraca (ele reconhece o próprio texto),
mas a tarefa de justificar continua válida; na sessão 2 ele já conhece a
régua, o que é o ponto.

Dados novos gerados: preferência do aluno no próprio par (sinal de
honestidade avaliativa), discordância aluno × juiz por seção, reflexão
dirigida para o log da R2. É letramento crítico em IA: aprender onde a
máquina é forte (cobertura, fidelidade literal) e onde ela para
(extrapolação, nuance, as limitações autorregistradas).

### 7.3 Discussão de calibração em grupo

Uma reunião: cada aluno vê onde superestimou ou subestimou o próprio
fichamento. Núcleo do letramento avaliativo.

### 7.4 Triagem como exercício avaliativo

Julgar fichamentos alheios treina a habilidade dos juízes e fecha o ciclo
produtor → avaliador → usuário.

## 8. Implicação metodológica a decidir

Se a devolutiva entrar entre R1 e R2, o delta de aprendizagem mede
protocolo **com** feedback, não o protocolo isolado. Recomendação:
assumir de propósito e declarar no método "protocolo iterativo com
devolutiva estruturada". Condição: a devolutiva precisa existir de fato,
com registro (página + respostas do exercício).

## 9. Encaixe no cronograma

- 17–22/11: avaliações da R1 pelos juízes (em curso).
- 23/11: alunos recebem artigos da R2 + devolutiva da R1.
- 23–25/11: devolutiva + exercício do par da R1 (portão: antes de
  produzir o fichamento da R2).
- 29/11: entregas da R2.
- Início de dez: avaliações da R2 + discussão de calibração em grupo.
- Após R2: R3 de juízes (confiabilidade), se aprovada.
- Futuro: triagem + Delphi de corpus, se aprovados.

## 10. Decisões para a reunião

1. R3 de juízes: aprovada? 4, 6 ou 8 artigos?
2. Reteste no artigo do piloto: entra como tarefa no fim da R2?
3. Devolutiva individual: liberar por artigo conforme avaliações chegam
   ou tudo junto após 22/11?
4. Dentro do par, revelar ao aluno qual fichamento é o seu e qual é IA?
   (recomendado: sim, a análise perde sentido sem isso)
5. Aceitar que o delta R1→R2 mede protocolo com devolutiva?
6. Triagem de artigos por estudantes: qual formato (A, B ou C), se
   aprovada?
7. Delphi de corpus: fica no escopo deste estudo ou é trabalho futuro?
8. **DECIDIDO (17/11):** todo aluno mantém o mesmo juiz da R1 para a R2,
   para a devolutiva ter régua consistente e o delta de calibração não
   confundir aprendizagem com troca de avaliador. Executado: 3 trocas de
   artigo em `assignments-round2.json` (S03/S14, S07/S09, S06/S11); os 16
   alunos ficaram com o mesmo juiz nas duas rodadas.
