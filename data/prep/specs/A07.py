SUMMARY = (
    "O editorial da edição especial da revista Organization faz um balanço de uma década de estudos críticos de "
    "diversidade e propõe direções para a área (p.1/L023-033; p.2/L058-063). Esses estudos surgiram em meados dos "
    "anos 1990 como reação à reapropriação da igualdade de oportunidades pelas empresas por meio da noção de "
    "diversidade, e compartilham uma compreensão não positivista e não essencialista da diversidade como socialmente "
    "(re)produzida (p.1/L023-033; p.2/L049-057). Os autores reconstroem a trajetória: os estudos sobre gênero e "
    "raça/etnia que mostraram a produção social da desigualdade, a virada para abordagens psicossociais, como "
    "identidade social e homofilia, e o paradigma da diversidade, que trata diferenças como ativos estratégicos, "
    "inclusive pela visão baseada em recursos (p.2/L069-074; p.3/L106-132; p.4/L145-147; p.4/L156-169). A literatura "
    "crítica se apoia em três críticas: a ontologia positivista da identidade, a pouca atenção ao contexto e a "
    "teorização inadequada do poder, e já avançou por análise de discurso, trabalho de identidade, branquitude, "
    "interseccionalidade e estudos sobre o contexto de cada país (p.5/L221-236; p.6/L246-274; p.7/L294-310; "
    "p.7/L335-340; p.8/L346-349; p.8/L371-374). A parte final propõe cinco direções: mais pesquisa empírica sobre "
    "como atores se apropriam dos discursos, estudo da experiência da força de trabalho diversa, análise de "
    "representações além do texto, ligação entre discursos e práticas sociais, inclusive pela virada de prática dos "
    "estudos de gênero, e uma pesquisa mais performativa, com pesquisa-ação (p.9/L404-415; p.9/L427-431; "
    "p.10/L457-459; p.10/L477-492; p.11/L528-541; p.12/L560-566). O texto situa os artigos da edição especial nessas "
    "direções (p.9/L415-426; p.9/L432-440; p.10/L469-476; p.11/L507-523). Por ser um editorial, não relata coleta "
    "própria de dados."
)

RESEARCH_QUESTION = (
    "O artigo é um editorial e não enuncia pergunta de pesquisa; declara o propósito de fazer um balanço dos novos "
    "insights teóricos dos estudos críticos de diversidade e iniciar uma conversa sobre os caminhos da área "
    "(p.2/L058-063). Reconstruída como pergunta implícita: o que as perspectivas críticas permitem repensar sobre a "
    "diferença para compreender a desigualdade, e para onde a pesquisa deve ir (p.2/L058-063; p.9/L399-403)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.1/L023-033", "p.2/L049-057"],
      "Critical diversity studies emerged in the mid-1990s as a reaction to the re-appropriation of equal opportunities by business through the notion of diversity",
      "Objeto e lente centrais do editorial."),
    V("T2", "uses", ["p.11/L528-541", "p.12/L551-559"],
      "it is time for the critical literature to become more performative, explicitly dealing with stimulating social change",
      "A performatividade crítica sustenta a quinta direção proposta pelos autores."),
    V("T3", "does_not_use", [],
      "",
      "A teoria queer aparece apenas no título de uma referência (p.14/L624-625), sem menção no texto."),
    V("T4", "discusses", ["p.3/L119-132", "p.6/L246-258"],
      "social identity theories explain discriminating behaviour as resulting from the need of human beings to classify themselves and others into groups to reduce the complexity of the social world",
      "Apresentadas e criticadas como base da literatura psicossocial, não adotadas como referencial."),
    V("T5", "discusses", ["p.4/L156-169", "p.5/L216-219"],
      "Richard (2000) elevated the study of the effects of diversity from the group level to the organization level",
      "A visão baseada em recursos é descrita como fundamento do paradigma da diversidade e depois criticada."),
    V("T6", "discusses", ["p.5/L204-216"],
      "on an information/decision making perspective to analyse the cognitive processes and outcomes of diverse groups’ work",
      "Descrita como abordagem da literatura de diversidade, sujeita à crítica geral às teorias psicossociais."),
    V("T7", "does_not_use", [],
      "",
      "Capital social não aparece no texto; só em título de referência (p.13/L759-760)."),
    V("T8", "uses", ["p.4/L149-169", "p.4/L177-180", "p.6/L266-274"],
      "The business rationale at the core of diversity has often been used to explain the popularity of this notion within the US business world",
      "O paradigma da diversidade e o business case são o alvo da crítica que estrutura o editorial."),
    V("T9", "discusses", ["p.7/L335-340", "p.8/L346-352", "p.9/L432-440"],
      "Yet another promising approach to diversity in organizations draws on intersectionality studies",
      "Apresentada como abordagem promissora e ilustrada com o estudo de Roggeband e Boogaard."),
    V("T10", "discusses", ["p.7/L294-310", "p.7/L320-328"],
      "Despite their subordinate positions, subjects continuously engage, as agents, in identity work",
      "Trabalho de identidade e estudos de branquitude são apresentados como linhas da literatura crítica."),
    V("T11", "discusses", ["p.8/L353-365"],
      "Acker (2006) proposed the notion of ‘inequality regimes’ to conceptualize interlocking practices and processes that result in continuing inequalities in all work organizations",
      "Racismo cotidiano (Essed) e regimes de desigualdade (Acker) são explicados em uma frase cada, em um parágrafo de síntese."),
    V("T12", "discusses", ["p.11/L507-523"],
      "Drawing from a post-colonial perspective, Kalonaityte examines the simultaneous construction of the majority’s identity as related and opposed to migrant identities",
      "Perspectiva pós-colonial apresentada a partir de um artigo da edição especial."),
    V("T13", "uses", ["p.10/L485-492", "p.11/L499-506"],
      "studies (Poggio 2006) could help re-conceptualize diversity as an ongoing dynamic social practice",
      "Quarta direção proposta pelos autores: tratar a diversidade como prática social."),
    V("T14", "discusses", ["p.2/L041-049", "p.6/L275-287"],
      "the critical diversity literature has recently expanded by drawing on a broad variety of critical theories including post-structuralism",
      "Análise de discurso é desenvolvida (p.6/L275-287); pós-estruturalismo, teoria institucional e labour process theory são apenas listados."),
]

KEY_CONCEPTS = [
    dict(concept="Estudos críticos de diversidade",
         definition="Abordagens que, apesar de perspectivas distintas, contestam a visão instrumental das diferenças do paradigma da diversidade e a tratam como socialmente (re)produzida em processos específicos de contexto.",
         quote="Despite their distinct perspectives, critical approaches to diversity all contest the instrumental view of differences inherent to the diversity paradigm",
         source_refs=["p.2/L049-057"]),
    dict(concept="Paradigma da diversidade (business case)",
         definition="Racional de negócio que trata as diferenças como ativos estratégicos que, bem geridos, geram vantagem competitiva e que orientou também grande parte da pesquisa acadêmica sobre diversidade.",
         quote="The business rationale at the core of diversity has often been used to explain the popularity of this notion within the US business world",
         source_refs=["p.4/L149-169", "p.4/L177-186"]),
    dict(concept="Três críticas à literatura de diversidade",
         definition="Ontologia positivista da identidade, que a naturaliza como categoria fixa; negligência do papel dos contextos organizacionais e sociais; e teorização inadequada do poder, com perspectiva gerencial sobre as diferenças.",
         quote="The critical diversity literature has developed on the ground of three fundamental points of critique towards the diversity literature",
         source_refs=["p.5/L221-236", "p.6/L246-274"]),
    dict(concept="Trabalho de identidade (identity work)",
         definition="Engajamento ativo de sujeitos, mesmo em posições subordinadas, na construção, manutenção ou ruptura de identidades favoráveis a eles, desafiando desigualdades.",
         quote="Despite their subordinate positions, subjects continuously engage, as agents, in identity work",
         source_refs=["p.7/L294-310"]),
    dict(concept="Interseccionalidade",
         definition="Conceito originado nos estudos feministas negros, aplicado às organizações para conectar múltiplas identidades de trabalho a fenômenos sociais amplos e às relações de poder subjacentes.",
         quote="Applied to organizations, intersectionality allows connecting multiple work identities to wider societal phenomena",
         source_refs=["p.7/L335-340", "p.8/L346-349"]),
    dict(concept="Diversidade como prática social",
         definition="Proposta de tratar a diversidade como prática social contínua, que abrange as práticas culturais disponíveis de 'fazer diversidade', tidas como dadas, e o ato de praticá-la na interação.",
         quote="diversity as a social practice could be developed to encompass both the currently available cultural practices to ‘do diversity’, which are now largely taken for granted",
         source_refs=["p.11/L499-503"]),
    dict(concept="Performatividade crítica",
         definition="Postura que pede à literatura crítica atuar na mudança social, indo além da crítica rumo a práticas e intervenções afirmativas e engajadas.",
         quote="it is time for the critical literature to become more performative, explicitly dealing with stimulating social change",
         source_refs=["p.11/L532-541"]),
]

METHODOLOGY = dict(
    study_type="teórico (editorial de edição especial)",
    design="Editorial que reconstrói a trajetória dos estudos de gênero, raça e diversidade, revisa a literatura crítica e propõe direções para pesquisa, situando os artigos da edição especial.",
    sample_type="não se aplica (sem coleta de dados)",
    sample_size=None,
    sector="",
    period="",
    methods=["editorial", "revisão narrativa da literatura"],
    analysis_note=("O texto não descreve critérios de busca ou seleção da literatura. A organização é argumentativa: raízes da pesquisa "
                   "(p.2/L064-066), paradigma da diversidade (p.4/L148-149), críticas (p.5/L221-223) e caminhos futuros (p.9/L399-403)."),
    source_refs=["p.2/L058-066", "p.9/L399-403"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("A predominância de abordagens psicossociais na literatura sobre gênero, raça e diversidade levou a uma compreensão estreita dos processos que geram desigualdade, que ignora elementos estruturais e específicos de contexto.",
      "proposition",
      "the predominance of social psychological approaches has also resulted in a narrow understanding of the processes leading to inequality",
      ["p.4/L145-147", "p.3/L106-132"]),
    F("O paradigma da diversidade, ancorado em um racional de negócio e na visão baseada em recursos, tratou as diferenças pela primeira vez como ativos estratégicos.",
      "proposition",
      "The business rationale at the core of diversity has often been used to explain the popularity of this notion within the US business world",
      ["p.4/L149-169", "p.4/L177-180"]),
    F("A literatura psicossocial naturaliza identidades como categorias fixas, em vez de reconhecer sua construção social.",
      "proposition",
      "Such unproblematic approach naturalizes identities into objective entities, rather than acknowledging their socially constructed nature",
      ["p.5/L223-236"]),
    F("Atores organizacionais não repetem discursos hegemônicos de diversidade, mas se apropriam deles seletivamente, o que abre espaço para formas cotidianas de resistência.",
      "proposition",
      "Organizational actors do not simply take over existing grand, hegemonic discourses of diversity but rather selectively appropriate them",
      ["p.9/L404-415"]),
    F("A maior parte da pesquisa crítica mostrou que práticas de gestão da diversidade não diminuem as desigualdades e até contribuem para sua reprodução.",
      "proposition",
      "most critical diversity research has focused on examining organizational inequalities and showing how existing (diversity) management practices not only do not diminish them",
      ["p.11/L528-532"]),
    F("A pesquisa deve buscar formas emancipatórias de organizar, tornar-se mais performativa e tratar a diversidade como prática social, com apoio em pesquisa-ação.",
      "proposition",
      "we plea for diversity studies that actively search for new, emancipating forms of organizing",
      ["p.11/L528-541", "p.10/L485-492", "p.12/L560-566", "p.12/L584-585"]),
]

CONTRIBUTION = dict(
    theoretical=("Faz um balanço de uma década de estudos críticos de diversidade, traça suas raízes nos estudos críticos de gênero e "
                 "raça e propõe cinco direções para a pesquisa (p.2/L058-066; p.9/L399-403). Defende uma pesquisa mais empírica, "
                 "centrada na experiência da força de trabalho, aberta a outras formas de representação, atenta à relação entre discurso e "
                 "prática e mais performativa, com 'reflexividade reconstrutiva' (p.9/L404-431; p.10/L457-492; p.11/L528-541)."),
    practical=("O editorial não traz seção de implicações gerenciais. Defende estudos performativos e pesquisa-ação que apoiem "
               "organizações na mudança de relações raciais e de gênero, aprendendo com desafios e conquistas (p.12/L560-566; p.12/L581-585)."),
)
