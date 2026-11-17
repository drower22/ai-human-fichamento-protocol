SUMMARY = (
    "O artigo, do tipo prospectivo, trata de uma ambiguidade central na pesquisa de strategy as practice (SAP): o que "
    "caracteriza uma atividade como estratégica (p.2/L097-100; p.3/L126-129). Os autores observam que os principais "
    "frameworks de SAP, como os 3Ps, o Who/What/How e os 4Ps, não especificam que atividades qualificam como "
    "estratégicas (p.2/L100-117). Contra a proposta recente de ligar atividades estratégicas à consequencialidade, "
    "defendem apreciar a pluralidade de visões implícitas na literatura (p.3/L130-141). A partir de uma categorização "
    "sistemática das conceituações implícitas em estudos de SAP, identificam quatro visões: atividades com "
    "consequências importantes, atividades rotuladas como estratégicas, atividades realizadas por estrategistas e "
    "atividades que performam um padrão recorrente importante (p.3/L142-150; p.5/L319-330; p.6/L410-414; p.9/L548-550; "
    "p.11/L680-681). Cada visão suscita perguntas de pesquisa próprias, ilustradas com estudos existentes "
    "(p.5/L354-360; p.7/L428-432; p.9/L564-567; p.12/L738-741). Argumentam que as quatro visões formam um framework que "
    "complementa os existentes, ajuda a escolher a visão e a enquadrar estudos como SAP e amplia a agenda de pesquisa "
    "(p.14/L817-828; p.15/L879-912). Discutem implicações onto-epistemológicas quanto ao ponto de entrada, ao momento "
    "da identificação e à postura emic ou etic (p.16/L952-961; p.17/L983-1029). Mostram ainda conexões com outras "
    "correntes, como cognição e visão baseada em atenção, planejamento estratégico e performatividade, liderança "
    "estratégica e capacidades gerenciais dinâmicas, e estratégia emergente e capacidades dinâmicas (p.18/L1057-1078; "
    "p.19/L1079-1128; p.20/L1129-1136), e sustentam que o framework amplia a noção de estratégia além do desempenho "
    "da firma (p.20/L1137-1150). Por ser um artigo conceitual, não gera dados novos (p.20/L1155)."
)

RESEARCH_QUESTION = (
    "O artigo não enuncia uma pergunta de pesquisa explícita; identifica como problema a ambiguidade sobre o que "
    "caracteriza uma atividade como estratégica no domínio de SAP (p.2/L097-100) e propõe diferenciar várias definições "
    "paralelas em vez de adotar uma só (p.3/L136-141). Reconstruída como pergunta implícita: que visões existem sobre o "
    "que torna uma atividade estratégica e que perguntas e implicações cada uma traz para a pesquisa em SAP "
    "(p.3/L142-150)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.2/L084-096"],
      "SAP treats strategy as a particular practice, that is, as something that people do rather than something that firms have",
      "Abordagem sobre a qual o artigo constrói o framework."),
    V("T2", "uses", ["p.11/L691-704", "p.19/L1116-1126"],
      "typically refer to Mintzberg and Waters' (1985) classic conceptualization of strategy as a pattern in a stream of actions",
      "Fundamenta a visão do padrão e a conexão com estratégia emergente."),
    V("T3", "uses", ["p.5/L319-330", "p.3/L130-141"],
      "activity is considered strategic to the extent that it is consequential for the strategic outcomes, directions, survival and competitive advantage of the firm",
      "Primeira das quatro visões e ponto de partida da crítica de Jarzabkowski et al. (2021)."),
    V("T4", "does_not_use", [],
      "",
      "A teoria da dependência de recursos não é mencionada."),
    V("T5", "discusses", ["p.2/L097-117", "p.16/L924-931"],
      "the four-views framework constitutes an important complement to these earlier frameworks",
      "Os frameworks 3Ps, Who/What/How e 4Ps são discutidos como foco nos aspectos da prática, que o novo framework complementa."),
    V("T6", "uses", ["p.6/L410-414"],
      "Within the second view, which we refer to as nominalist view, activities treated as strategic are those that are labeled as such",
      "Segunda das quatro visões, desenvolvida com perguntas e exemplos."),
    V("T7", "discusses", ["p.13/L782-790", "p.16/L944-948"],
      "MacKay et al. (2021) traced the emergence of new patterns back to a recursive process in which situated coping actions result in a particular disposition",
      "Coping, disposições corporais e ontologia da prática aparecem na visão do padrão e como opção de lente para análise."),
    V("T8", "does_not_use", [],
      "",
      "A visão baseada em conhecimento não é mencionada."),
    V("T9", "discusses", ["p.18/L1057-1074"],
      "the consequentiality view can help connect SAP research, for example, with the broad literature on strategy cognition and attention",
      "Apresentada como conexão da visão da consequencialidade com cognição gerencial e visão baseada em atenção."),
    V("T10", "discusses", ["p.18/L1075-1078", "p.19/L1079-1094"],
      "the focus on activities formally labeled strategic can also serve as a basis for connecting SAP research with the performativity perspective on strategy",
      "Conexão da visão nominalista com planejamento estratégico e performatividade."),
    V("T11", "discusses", ["p.19/L1095-1107"],
      "strategic leadership research strives to establish the link between CEOs, TMTs, and boards of directors and strategy outcomes and organizational performance",
      "Conexão da visão baseada em papéis com liderança estratégica e upper echelons."),
    V("T12", "discusses", ["p.19/L1107-1115", "p.19/L1127-1128", "p.20/L1132-1136"],
      "the role-based view can help advance our understanding of what dynamic managerial capabilities are, how they are enacted, and how they can be acquired",
      "Capacidades dinâmicas e gerenciais dinâmicas são apresentadas como pontos de integração com as visões baseada em papéis e do padrão."),
    V("T13", "uses", ["p.17/L1006-1029", "p.17/L983-992"],
      "The third onto-epistemological implication concerns the extent to which researchers take an emic or etic stance (Morris et al., 1999) toward the identification of strategic activities",
      "A postura emic ou etic é uma das três implicações onto-epistemológicas do framework (Tabela 2)."),
    V("T14", "uses", ["p.20/L1137-1150", "p.4/L239-243"],
      "the four-views framework also contributes to the discussion about the boundaries of the field",
      "A discussão sobre fronteiras e identidade da gestão estratégica é uma das contribuições declaradas."),
    V("T15", "does_not_use", [],
      "",
      "Sensebreaking e sensemaking aparecem como exemplos de estudos citados (p.6/L381-385; p.8/L463-469), sem desenvolvimento teórico."),
    V("T16", "discusses", ["p.6/L392-406", "p.8/L531-536", "p.10/L620-631"],
      "in their study of open strategizing, Luedicke et al. (2017) revealed how “radically open” strategizing activities are complemented by “counterbalancing” strategizing activities to yield strategic outcomes",
      "Estudos de estratégia aberta são descritos repetidamente como exemplos de cada visão, não como lente do artigo."),
    V("T17", "does_not_use", [],
      "",
      "Dinâmica de rotinas aparece em uma analogia de Feldman (2024) entre ação estratégica e padrão (p.11/L701-709) e em exemplos de rotinas operacionais (p.15/L896-898), sem desenvolvimento."),
    V("T18", "discusses", ["p.11/L684-690"],
      "This is analogous to how gender, defined as a particular behavioral pattern (Butler, 1988), is performed through the way that people behave",
      "Usada como analogia para distinguir a visão do padrão (atividade que performa) da visão da consequencialidade."),
]

KEY_CONCEPTS = [
    dict(concept="Atividade estratégica (ambiguidade em SAP)",
         definition="Noção central de SAP cuja delimitação é ambígua: não está claro o que caracteriza uma atividade como estratégica e, portanto, como parte do domínio de pesquisa de SAP.",
         quote="there is still significant ambiguity around what characterizes an activity as strategic, thereby falling into the domain of SAP research",
         source_refs=["p.2/L097-100", "p.3/L126-129"]),
    dict(concept="Visão da consequencialidade",
         definition="Define atividades estratégicas como aquelas que geram consequências importantes, em qualquer nível; é a visão dos dois números especiais seminais de SAP.",
         quote="activity is considered strategic to the extent that it is consequential for the strategic outcomes, directions, survival and competitive advantage of the firm",
         source_refs=["p.5/L319-330"]),
    dict(concept="Visão nominalista",
         definition="Define atividades estratégicas como aquelas rotuladas como tal, porque os praticantes as chamam de estratégicas ou porque fazem parte do discurso institucionalizado de estratégia.",
         quote="Within the second view, which we refer to as nominalist view, activities treated as strategic are those that are labeled as such",
         source_refs=["p.6/L410-414"]),
    dict(concept="Visão baseada em papéis",
         definition="Define atividades estratégicas como aquelas realizadas por atores formalmente reconhecidos como estrategistas, que estão oficialmente encarregados do trabalho de estratégia.",
         quote="The third view, which we refer to as role-based view, defines strategic activities as those that are enacted by actors who are formally recognized as strategists because they are officially charged with strategy work",
         source_refs=["p.9/L548-555"]),
    dict(concept="Visão do padrão",
         definition="Define atividades estratégicas como aquelas que performam um padrão recorrente importante de atividades; a atividade performa o padrão, em vez de levar a um resultado separado.",
         quote="The fourth view, which we refer to as pattern view, defines strategic activities as those that perform an important recurrent pattern of activities",
         source_refs=["p.11/L680-690"]),
    dict(concept="Framework das quatro visões",
         definition="Quadro que reúne as quatro visões como complemento aos frameworks de SAP existentes, cobrindo o aspecto estratégico das atividades enquanto os outros cobrem o aspecto da prática.",
         quote="Together, the four views identified above can be understood as constituting a new research framework for SAP, complementing the existing SAP frameworks",
         source_refs=["p.14/L817-820", "p.16/L928-931"]),
]

METHODOLOGY = dict(
    study_type="teórico (artigo prospectivo)",
    design="Categorização sistemática das conceituações de atividade estratégica implícitas em estudos de SAP, que leva à diferenciação de quatro visões e a um framework de pesquisa, com discussão de implicações.",
    sample_type="não se aplica (literatura de SAP; sem coleta de dados)",
    sample_size=None,
    sector="",
    period="",
    methods=["categorização sistemática da literatura", "desenvolvimento de framework conceitual"],
    analysis_note=("Os autores afirmam partir de uma categorização sistemática das conceituações de atividades estratégicas "
                   "implícitas em estudos de SAP (p.3/L142-144), mas não descrevem critérios de busca ou de seleção da literatura. O "
                   "artigo declara que nenhum dado novo foi gerado (p.20/L1155)."),
    source_refs=["p.3/L142-150", "p.20/L1155"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("Além da consequencialidade, atividades podem ser tratadas como estratégicas por serem rotuladas como tal, realizadas por estrategistas ou parte de um padrão recorrente importante.",
      "model",
      "activities can be treated as strategic to the extent that they are labeled strategic (e.g., Whittington, 2003), to the extent that they are carried out by strategists (e.g., Samra-Fredericks, 2003), or to the extent that they perform an important recurrent pattern (e.g., Chia & MacKay, 2007)",
      ["p.3/L142-150"]),
    F("Cada visão foca um conjunto distinto de atividades e abre uma agenda de pesquisa com perguntas próprias.",
      "model",
      "each focuses on a different set of activities and each opens up a distinctive research agenda with different sets of research questions",
      ["p.3/L147-150", "p.4/L170-243"]),
    F("A visão do padrão difere da da consequencialidade: na primeira a atividade performa um padrão, na segunda leva a um resultado separado.",
      "proposition",
      "the first view is concerned with A (activity) leading to B (important outcome), while the fourth view is concerned with A (activity) performing B (important pattern)",
      ["p.11/L680-690"]),
    F("As visões diferem em ponto de entrada, momento de identificação e postura: a consequencialidade identifica atividades ex post e de modo etic, enquanto as demais as identificam ex ante.",
      "model",
      "For researchers adopting the consequentiality view, the starting point of the analysis is the outcome, as this is what defines the activities as strategic. This means that activities can be identified as strategic ex post only",
      ["p.16/L956-961", "p.17/L983-992", "p.17/L997-1005"]),
    F("O framework ajuda a escolher a visão e a enquadrar estudos como SAP e amplia a agenda, pois a pesquisa passada foi pouco sistemática no foco.",
      "proposition",
      "past SAP research has been somewhat random and sporadic in where it put its focus",
      ["p.15/L906-912", "p.16/L913-917"]),
    F("Cada visão conecta SAP a outras correntes de pesquisa em estratégia, o que abre oportunidades de integração.",
      "proposition",
      "our framework highlights the interests SAP shares with other streams of strategy research and thus reveals distinct opportunities for cross-fertilization and integration",
      ["p.3/L161-169", "p.18/L1050-1056"]),
    F("Ao ir além da consequencialidade, o framework amplia a noção de estratégia para além do desempenho da firma.",
      "proposition",
      "Our analysis helps to broaden the notion of strategy beyond its association with firm performance and outcomes",
      ["p.20/L1137-1150"]),
]

CONTRIBUTION = dict(
    theoretical=("Propõe um framework que complementa os frameworks de SAP centrados na prática, ao focar o aspecto estratégico das "
                 "atividades (p.3/L151-160), e estabelece uma agenda de pesquisa ampliada (p.15/L906-912). Revela conexões com outras "
                 "correntes de estratégia (p.18/L1050-1056) e contribui para o debate sobre as fronteiras do campo, ampliando a noção "
                 "de estratégia (p.20/L1137-1150)."),
    practical=("O artigo traz um Managerial Summary que apenas resume o framework de quatro visões (p.2/L059-077); não apresenta "
               "implicações gerenciais específicas."),
)
