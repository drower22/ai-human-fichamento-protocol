SUMMARY = (
    "O artigo investiga como uma organização cultural desenvolve a prática do teatro a partir da "
    "enculturação das lógicas institucionais — um caminho que os estudos organizacionais têm deixado "
    "pouco explorado nas artes, e que a literatura de lógicas tem abordado 'de forma incompleta e com "
    "contradições' no que toca à recursividade entre atores e instituições (p.3/L154-171). O enquadre "
    "junta as lógicas institucionais, formuladas como troika sujeito-práticas-objeto movida por um bem e "
    "seus valores (p.2/L104-114; p.4/L210-219), com o modelo dual da cultura de Lizardo — a enculturação "
    "como internalização cognitiva de elementos culturais nos modos declarativo e não declarativo, "
    "pessoal e público — e a promulgação (enactment) como mecanismo de externalização (p.3/L136-148; "
    "p.6/L318-341; p.7/L381-396). Sob lógica abdutiva, o estudo etnográfico no grupo Art&Vida Teatro de "
    "Rosário do Sul (RS) durou 12 meses, com 2.061 documentos e 24 entrevistas, analisados por "
    "tipificação ideal e análise narrativa (p.10/L540-563; p.11/L568-619; p.12/L625-663; p.13/L742-755). Os achados "
    "mostram que o grupo encultura elementos das lógicas do teatro amador, profissional e moderno em "
    "níveis declarado e não declarado e que, ao promulgá-los combinados nas práticas — ensaios, "
    "espetáculos, festival e articulação de coletivos —, constitui uma lógica híbrida que os autores "
    "denominam 'teatro interiorano', movida pelo bem 'teatro como missão de vida que transforma a "
    "sociedade' (p.28/L1719-1751; p.29/L1761-1786; p.30-32/L1817-1960). A contribuição é mostrar a "
    "enculturação como processo de internalização que torna a recursividade empiricamente observável — "
    "significados negociados na comunidade, refeitos e disseminados para contextos mais amplos "
    "(p.33/L1983-2005; p.34/L2044-2055)."
)

RESEARCH_QUESTION = (
    "O artigo declara a pergunta duas vezes — na introdução como objetivo e, refinada, na seção "
    "metodológica como questão de pesquisa abdutiva: 'como uma organização cultural desenvolve a "
    "prática do teatro a partir da enculturação das lógicas institucionais?' (p.3/L154-156; "
    "p.11/L615-619). A pergunta nasceu de anomalias não explicadas observadas em campo — por que "
    "organizações do interior debatem assimetrias sociais, por que criaram um coletivo estadual, por que "
    "o Art&Vida mudou de categoria amadora para internacional — e foi refinada pelas idas e vindas "
    "entre campo e literatura (p.10/L539-563; p.11/L605-613)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.2/L104-114", "p.4/L210-219"],
      "uma lógica institucional é uma gramática de práticas de valoração, regularidades e regras",
      "Lente teórica principal: a troika sujeito-práticas-objeto e os quatro pressupostos estruturam toda a análise."),
    V("T2", "uses", ["p.3/L136-148", "p.6/L318-341"],
      "A enculturação é um processo cognitivo de internalização de elementos culturais que serão codificados, armazenados e, posteriormente, externalizados",
      "O arcabouço analítico adotado: os achados são classificados nos níveis declarado/não declarado, pessoal/público."),
    V("T3", "uses", ["p.13/L742-755"],
      "Os tipos ideais permitem identificar aquilo que é essencial em um determinado fenômeno a partir do ‘exagero’ de alguns dos seus aspectos",
      "Ferramenta analítica que gera o Quadro 02 — os cinco tipos ideais de lógica do teatro."),
    V("T4", "uses", ["p.7/L381-396", "p.30/L1820-1824"],
      "A promulgação, como é denominado esse processo, pode ser realizada em situações de complexidade institucional",
      "O mecanismo que liga a cultura pessoal à pública e explica como os elementos enculturados aparecem na prática."),
    V("T5", "discusses", ["p.3/L157-171", "p.32/L1963-1976", "p.33/L1977-1997"],
      "a compreensão deste processo tem sido abordada de forma incompleta e apresenta contradições",
      "O debate ao qual o estudo contribui: recursividade explicada pela enculturação, e não por intencionalidade ou eventos isolados."),
    V("T6", "discusses", ["p.3/L161-164", "p.4/L220-227"],
      "a relação entre agência e a estrutura são recursivas",
      "Citada via Giddens e Rossoni et al. para fundamentar a recursividade e a concepção de agência; não desenvolvida."),
    V("T7", "discusses", ["p.2/L076-079", "p.33/L2016-2018"],
      "Essas organizações podem ser consideradas entidades fluídas",
      "Caracteriza as organizações culturais e a ontologia relacional do estudo (Law 2007 nas referências); não é a lente analítica."),
    V("T8", "discusses", ["p.7/L395-396", "p.32/L1951-1954"],
      "Organizações em um mesmo setor, por exemplo, podem responder de maneiras diferentes a uma pressão institucional",
      "Enquadra a coexistência das lógicas amadora/profissional/moderna; o achado é um comportamento em complexidade institucional."),
    V("T9", "discusses", ["p.7/L383-388"],
      "ao externalizar, os indivíduos irão expressar seus comportamentos em sociedade",
      "Invocada pontualmente para explicar a externalização — elo entre enculturação e cultura pública."),
    V("T10", "uses", ["p.8/L444-455", "p.14/L794-803"],
      "três momentos que compõem a prática teatral, a saber: pré-produção, produção e pós-produção",
      "Base empírica da tipificação ideal (Quadro 02) e das fases que organizam os relatos da enculturação."),
    V("T11", "does_not_use", [], "",
      "Conteúdo do caso (o Diretor conheceu o método no CEAI e a lógica moderna o descreve), não lente teórica mobilizada."),
    V("T12", "does_not_use", [], "",
      "O artigo cita DiMaggio (1997, 'Culture and cognition') para a cultura, não o isomorfismo — o fenômeno é de heterogeneidade, não homogeneização."),
    V("T13", "does_not_use", [], "",
      "O vocabulário de 'prática' vem de lógicas institucionais e artes cênicas; a escola strategy-as-practice não é citada."),
    V("T14", "does_not_use", [], "",
      "Ausente; os públicos aparecem como comunidade, plateia e coletivos, não como stakeholders."),
    V("T15", "does_not_use", [], "",
      "Ausente; a explicação é cultural-cognitiva (enculturação), não ecológica."),
]

KEY_CONCEPTS = [
    dict(concept="Lógica institucional",
         definition="Padrões históricos socialmente construídos de símbolos culturais e práticas materiais — suposições, valores e crenças — pelos quais indivíduos e organizações dão sentido à atividade diária; estruturada como troika de sujeitos, práticas e objetos, movida por um bem institucional e seus valores.",
         quote="uma lógica institucional é uma gramática de práticas de valoração, regularidades e regras",
         source_refs=["p.2/L106-114", "p.4/L210-219"]),
    dict(concept="Enculturação",
         definition="Processo cognitivo de internalização de elementos culturais, codificados, armazenados e depois externalizados; ocorre nos modos declarativo (intencional, aquisição rápida) e não declarativo (não intencional, aprendizado lento), nos níveis pessoal e público.",
         quote="A enculturação é um processo cognitivo de internalização de elementos culturais que serão codificados, armazenados e, posteriormente, externalizados",
         source_refs=["p.3/L140-148", "p.6/L318-341"]),
    dict(concept="Promulgação (enactment)",
         definition="Ativação dos elementos institucionais internalizados para uso em situações do dia a dia; mecanismo da externalização que permite modificar práticas e as próprias instituições, sobretudo em complexidade institucional.",
         quote="é preciso compreender como os atores realizam o enactment, em português promulgação, dos elementos internalizados",
         source_refs=["p.7/L381-396", "p.30/L1820-1824"]),
    dict(concept="Tipificação ideal",
         definition="Ferramenta analítica baseada nos tipos ideais weberianos: identifica o essencial de um fenômeno pelo 'exagero' de aspectos — metáfora raiz, fontes de legitimidade e identidade — para medir a distância entre as observações e a forma pura.",
         quote="Os tipos ideais permitem identificar aquilo que é essencial em um determinado fenômeno a partir do ‘exagero’ de alguns dos seus aspectos",
         source_refs=["p.13/L742-755"]),
    dict(concept="Teatro interiorano",
         definition="A lógica institucional híbrida que emerge da enculturação no Art&Vida: combina elementos das lógicas amadora, profissional e moderna e é movida por um bem — o teatro como missão de vida que transforma a sociedade — específica de Rosário do Sul e difundida pela fronteira oeste gaúcha.",
         quote="um achado deste estudo que denomino de lógica interiorana",
         source_refs=["p.30/L1845-1851", "p.32/L1951-1960"]),
    dict(concept="Recursividade",
         definition="A relação constitutiva entre atores e instituições: os elementos institucionais são enculturados, têm seus significados modificados e são promulgados de volta à prática, refazendo as próprias lógicas do campo.",
         quote="Este processo é recursivo à medida que os elementos institucionais são enculturados e têm seus significados modificados",
         source_refs=["p.3/L157-171", "p.33/L1983-1988"]),
]

METHODOLOGY = dict(
    study_type="empírico qualitativo",
    design="Estudo de caso etnográfico sob lógica abdutiva (observação da anomalia, confirmação, palpites e avaliação, seguindo Saetre & Van de Ven): 12 meses de trabalho de campo no grupo Art&Vida Teatro, com etnografia online (período agudo da pandemia) e presencial (festival e espetáculos), diário de campo e participação em reuniões e grupos de trabalho.",
    sample_type="organização cultural teatral (Grupo Art&Vida Teatro, Rosário do Sul-RS), selecionada por anomalia não explicada na observação inicial do campo; corpus de 2.061 documentos (561 do acervo da organização) e 24 entrevistas (fevereiro/2020 a agosto/2022)",
    sample_size=24,
    sector="cultura / artes cênicas",
    period="etnografia junho/2021–junho/2022; dados documentais e entrevistas de fev/2020 a ago/2022",
    methods=["etnografia (observação participante online e presencial, diário de campo)", "fontes documentais e pesquisa histórica", "entrevistas", "tipificação ideal das lógicas institucionais", "análise narrativa"],
    analysis_note=("Dupla estratégia analítica declarada: (a) tipificação ideal — construção de cinco tipos "
                   "ideais das lógicas do teatro a partir da história do teatro brasileiro, medindo a "
                   "correspondência entre as características empíricas e as formas puras (Quadro 02); "
                   "(b) análise narrativa — construção do sentido na interação entre quem conta e o "
                   "pesquisador — para contar como ocorreu a enculturação, organizada nos níveis "
                   "declarado/público e não declarado/pessoal (p.12-13/L661-780). A saída de campo "
                   "ocorreu quando os convites para as reuniões cessaram (p.11/L600-604)."),
    source_refs=["p.11/L592-604", "p.12/L658-663", "p.13/L742-780"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("O Art&Vida encultura elementos de múltiplas lógicas do teatro — amadora, profissional e moderna — de formas distintas nos níveis declarado (intencional) e não declarado (aprendido pela convivência), e a sobreposição dessas lógicas é o que caracteriza a complexidade institucional vivida pelo grupo.",
      "empirical",
      "consequentemente, a complexidade institucional",
      ["p.24/L1497-1506", "p.28/L1719-1756", "p.29/L1757-1786"]),
    F("No nível declarado, o grupo compartilha o discurso do teatro como prática reflexiva preocupada com os problemas da sociedade — herança da lógica moderna vivenciada pelo Diretor no CEAI — mas enculturou também práticas da lógica profissional: elencos enxutos, especialistas contratados, temporadas planejadas e formação de plateia.",
      "empirical",
      "no nível declarado a prática teatral do Art&Vida é conceitualmente associada a um teatro como uma prática reflexiva e preocupada com os problemas vivenciados pela sociedade local",
      ["p.28/L1719-1751", "p.29/L1761-1767"]),
    F("No nível não declarado, manifestam-se elementos combinados das três lógicas: o teatro como prática social que se inter-relaciona com a vida pessoal dos atores, o voluntarismo e a articulação de recursos públicos e privados (amador), a formalização em CNPJ e diretoria eleita (profissional) e os coletivos como o Interior em Cena.",
      "empirical",
      "o Art&Vida busca representar um teatro reflexivo que se manifesta como prática social, um elemento da lógica modernista",
      ["p.29/L1768-1800", "p.31/L1899-1922", "p.32/L1923-1949"]),
    F("Ao promulgar os elementos enculturados em situações de complexidade institucional, o Art&Vida não priorizou uma única lógica: combinou práticas — espetáculos, festival, remuneração alternada, divulgação orgânica — e formou uma lógica híbrida, o 'teatro interiorano', movida por um bem: o teatro como missão de vida que transforma a sociedade.",
      "model",
      "o Art&Vida não considerou em sua interpretação priorizar apenas uma lógica, mas possibilitou que uma lógica híbrida fosse formada coletivamente",
      ["p.30/L1839-1851", "p.32/L1951-1962"]),
    F("O festival Rosário em Cena é a maior prática do grupo e condensa a hibridez: competição com prêmios e crítica especializada (profissional), jurados e trilha avaliados por 'contar uma história' (moderno), voluntarismo e formação de plateia (amador) — com conflitos recorrentes de cobrança, engajamento e rotatividade do elenco.",
      "empirical",
      "Apesar do festival representar a maior prática do grupo Art&Vida, ocorrem outras atividades",
      ["p.24/L1473-1485", "p.26/L1611-1636", "p.27/L1678-1696", "p.28/L1706-1710"]),
    F("A lógica do teatro interiorano é compartilhada e disseminada: desde 2008 difunde-se pela região da fronteira oeste do RS via festivais e coletivos como o Interior em Cena, que articula os grupos com o governo estadual — a comunidade negocia significados e torna uma lógica local atuante em contexto mais amplo.",
      "empirical",
      "a lógica híbrida do teatro interiorano no Art&Vida foi compartilhada com toda a região de Rosário do Sul a partir do ano de 2008",
      ["p.31/L1885-1897", "p.32/L1923-1929"]),
    F("A recursividade se realiza pela enculturação: os elementos institucionais internalizados são promulgados, seus significados são refeitos e adequados à prática local, e a lógica híbrida resultante retorna ao campo — mostrando como organizações de um mesmo campo desenvolvem práticas distintas porque os significados são negociados na comunidade.",
      "proposition",
      "a recursividade possibilitou que significados fossem refeitos e adequados à prática do teatro desempenhada em Rosário do Sul",
      ["p.32/L1963-1976", "p.33/L1977-1988", "p.34/L2036-2043"]),
]

CONTRIBUTION = dict(
    theoretical=("Três contribuições declaradas: (1) empiricamente, mostra como os elementos enculturados no "
                 "nível pessoal chegam ao público pela promulgação — a comunidade desenvolve entendimentos "
                 "locais que confrontam as instituições e, ao combinar elementos de lógicas distintas, forma "
                 "lógicas híbridas (p.30/L1816-1851); (2) à teoria de lógicas, oferece a enculturação como "
                 "processo de internalização que explica a recursividade — alternativa às explicações por "
                 "intencionalidade, eventos significativos ou construção de sentidos tomadas separadamente "
                 "(p.33/L1989-1997); (3) ao conceito de recursividade, acrescenta que ela é também "
                 "disseminação de entendimentos socialmente compartilhados entre comunidades, com a prática "
                 "como mecanismo de legitimação (p.34/L2044-2055)."),
    practical=("A compreensão do teatro como prática social acrescenta ao discurso do próprio Art&Vida a "
               "importância da arte para a sociedade; desvelar como a prática encultura elementos das "
               "lógicas situa a articulação do grupo com o contexto institucional; e a documentação "
               "histórica contribui para os registros dos grupos gaúchos, na linha de Ferreira (2014) "
               "(p.33/L2006-2013)."),
    limitations=("O próprio estudo enquadra seus limites pelo desenho: um único caso etnográfico, com "
                 "internalização e saída de campo marcadas pela disponibilidade do grupo — a participação "
                 "encerrou em junho/2022 'quando não houve mais abertura para participar das reuniões' — e "
                 "a combinação de técnicas buscou mitigar por triangulação (p.28/L1714-1716; "
                 "p.33/L1998-2005)."),
    future_research=("Sugere pesquisas sobre como a enculturação pode produzir mais de uma lógica "
                     "institucional híbrida e estudos das lógicas sob abordagem relacional processual, "
                     "combinando epistemologias distintas (p.33/L2014-2018)."),
    source_refs=["p.30/L1816-1851", "p.33/L1989-1997", "p.33/L2006-2018", "p.34/L2044-2055"],
)
