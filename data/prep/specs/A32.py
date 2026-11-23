SUMMARY = (
    "O artigo desenvolve o modelo resource-based de vantagem competitiva sustentada. Partindo da "
    "observação de que a pesquisa em estratégia se concentrou em oportunidades e ameaças ambientais "
    "(p.1-2/L019-062), Barney mostra que os modelos ambientais assumem implicitamente recursos "
    "homogêneos e perfeitamente móveis entre firmas — suposições que a visão baseada em recursos "
    "substitui por heterogeneidade e imobilidade (p.2-3/L063-097). Definidos os conceitos-chave — "
    "recursos da firma, vantagem competitiva e vantagem competitiva sustentada como definição de "
    "equilíbrio (p.3-5/L107-203) — o artigo demonstra que, sob homogeneidade e mobilidade, nem "
    "first-mover advantages nem barreiras de entrada/mobilidade geram vantagem sustentada: ambas "
    "pressupõem heterogeneidade de recursos (p.5-7/L204-304). O framework resultante propõe quatro "
    "indicadores empíricos do potencial de um recurso gerar vantagem sustentada — valor, raridade, "
    "imitabilidade imperfeita e não-substituibilidade — sendo a imitabilidade imperfeita derivada de "
    "condições históricas únicas, ambiguidade causal e complexidade social (p.7-14/L314-624). O modelo é "
    "aplicado a três recursos candidatos — planejamento estratégico formal, sistemas de processamento de "
    "informação e reputação positiva (p.14-17/L625-777) — e conclui examinando as implicações para "
    "bem-estar social (rents de eficiência vs. monopólio), para a integração entre teoria organizacional e "
    "economia, e para o papel das dotações de recursos e dos gestores (p.17-19/L778-862)."
)

RESEARCH_QUESTION = (
    "Sob quais condições um recurso da firma pode ser fonte de vantagem competitiva sustentada? O "
    "artigo examina o elo entre recursos da firma e vantagem competitiva sustentada, assumindo que "
    "recursos estratégicos são heterogeneamente distribuídos entre firmas e que essas diferenças são "
    "estáveis ao longo do tempo (p.1/L007-018; p.4/L142-144)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.3/L090-097"],
      "view of the firm substitutes two alternate assumptions in analyzing sources",
      "O objeto central do artigo."),
    V("T2", "discusses", ["p.2/L055-074"],
      "describes the attributes of an attractive industry",
      "O contraponto teórico do qual derivam as duas suposições alternativas."),
    V("T3", "discusses", ["p.1/L019-030"],
      "a single organizing framework has been used to structure much of this research",
      "Ponto de partida: a RBV teoriza o lado dos strengths subteorizado no SWOT."),
    V("T4", "uses", ["p.10/L460-465", "p.11/L471-482"],
      "it is difficult for firms that are attempting to duplicate a successful firm's strategies through imitation of its resources",
      "Uma das três fontes de imitabilidade imperfeita."),
    V("T5", "uses", ["p.9/L407-419", "p.10/L431-439"],
      "If a firm obtains valuable and rare resources because of its unique path through history",
      "Primeira fonte de imitabilidade imperfeita."),
    V("T6", "uses", ["p.12/L528-547"],
      "they may be very complex social phenomena, beyond the ability of firms to systematically manage and influence",
      "Terceira fonte de imitabilidade imperfeita; exclui tecnologia física pura."),
    V("T7", "discusses", ["p.6/L239-263"],
      "the first firm in an industry to implement a strategy can obtain a sustained competitive advantage",
      "Objeção dissolvida: ser primeiro mover pressupõe um recurso único."),
    V("T8", "discusses", ["p.6/L264-274", "p.7/L277-291"],
      "barriers to entry and mobility only exist when competing firms are heterogeneous in terms of the strategically relevant resources they control",
      "Barreiras e grupos estratégicos redefinidos como sintomas de heterogeneidade/imobilidade."),
    V("T9", "uses", ["p.2/L070-074", "p.19/L855-862"],
      "such advantages must be found in the rare, imperfectly imitable, and non-substitutable resources already controlled by a firm",
      "Fundamento da suposição de imobilidade e conclusão prescritiva."),
    V("T10", "discusses", ["p.5/L188-203"],
      "redefine which of a firm's attributes are resources and which are",
      "Qualifica a definição de equilíbrio: sustentada não significa eterna."),
    V("T11", "discusses", ["p.4/L153-160"],
      "not only all of its current competitors, but also potential competitors",
      "Alarga a definição de competição dos conceitos-chave."),
    V("T12", "discusses", ["p.7/L305-313"],
      "the concept of the value chain to assist",
      "Antecâmara da RBV, não rival."),
    V("T13", "discusses", ["p.19/L845-854"],
      "as some population ecologists would have it",
      "Reabilita a agência gerencial dentro do modelo de dotações."),
    V("T14", "discusses", ["p.12/L517-527"],
      "implicit, taken for granted by managers, rather than being subject to explicit analysis",
      "Suporta a plausibilidade de a própria firma não entender sua vantagem."),
    V("T15", "does_not_use", [], "",
      "Zucker (1977) é citado pela persistência cultural; isomorfismo institucional não é mobilizado."),
]

KEY_CONCEPTS = [
    dict(concept="Recursos da firma (firm resources)",
         definition="Todos os ativos, capacidades, processos organizacionais, atributos, informação e conhecimento controlados pela firma que lhe permitem conceber e implementar estratégias que melhoram sua eficiência e eficácia — classificados em capital físico, humano e organizacional.",
         quote="all assets, capabilities, organizational pro- cesses, firm attributes, informátion, knowledge",
         source_refs=["p.3/L111-130"]),
    dict(concept="Vantagem competitiva sustentada",
         definition="Uma firma a possui quando implementa uma estratégia criadora de valor não implementada simultaneamente por concorrentes atuais ou potenciais e quando estes são incapazes de duplicar seus benefícios — definição de equilíbrio, não de calendário.",
         quote="a competitive advantage is sustained only if it continues to exist after efforts to duplicate that advantage have ceased",
         source_refs=["p.4/L145-175"]),
    dict(concept="Heterogeneidade e imobilidade de recursos",
         definition="As duas suposições da RBV: firmas de uma indústria podem ser heterogêneas nos recursos estratégicos que controlam, e esses recursos podem não ser perfeitamente móveis — logo a heterogeneidade pode ser duradoura.",
         quote="firms within an industry (or group) may be heterogeneous with respect to the strategic resources they con- trol",
         source_refs=["p.3/L090-097"]),
    dict(concept="Imitabilidade imperfeita",
         definition="Recursos valiosos e raros só geram vantagem sustentada se firmas sem eles não puderem obtê-los — por condições históricas únicas, ambiguidade causal ou complexidade social.",
         quote="these firm resources are imperfectly imitable",
         source_refs=["p.9/L397-406"]),
    dict(concept="Ambiguidade causal",
         definition="O elo entre os recursos de uma firma e sua vantagem sustentada não é compreendido — ou só imperfeitamente — tanto por rivais quanto pela própria firma, inviabilizando a imitação direcionada.",
         quote="causal ambiguity exists when the link between the resources",
         source_refs=["p.10/L460-465", "p.11/L469-482"]),
    dict(concept="Substituibilidade estratégica",
         definition="Dois recursos são estrategicamente equivalentes quando cada um permite implementar as mesmas estratégias; se o substituto for comum ou imitável, nem mesmo um recurso valioso, raro e inimitável gera vantagem sustentada.",
         quote="Two valuable firm resources (or two bundles of firm resources) are strategically equivalent when they each can be ex- ploited separately to implement the same strategies",
         source_refs=["p.13/L568-585"]),
]

METHODOLOGY = dict(
    study_type="ensaio teórico / artigo conceitual",
    design="Derivação lógica de um framework a partir de duas suposições alternativas (heterogeneidade e imobilidade de recursos), com provas por contraposição (homogeneidade/mobilidade; first-mover; barreiras) e aplicação ilustrativa a três recursos candidatos",
    sample_type="não empírico — desenvolvimento teórico com exemplos de aplicação",
    sample_size=0,
    sector="gestão estratégica (teoria)",
    period="1991",
    methods=["análise conceitual e definição de termos-chave", "derivação de condições necessárias e suficientes para vantagem sustentada", "refutação lógica de objeções (first-mover; barreiras de entrada/mobilidade)", "aplicação ilustrativa do framework a planejamento formal, sistemas de informação e reputação"],
    analysis_note=("A estrutura argumentativa procede em três movimentos: (i) define recursos, vantagem competitiva e "
                   "vantagem sustentada como equilíbrio pós-duplicação; (ii) demonstra que sob homogeneidade e "
                   "mobilidade perfeitas nenhuma vantagem sustentada é possível, nem mesmo via first-mover ou "
                   "barreiras — que pressupõem heterogeneidade; (iii) deriva os quatro indicadores VRIN e os aplica a "
                   "três recursos plausíveis, mostrando as perguntas empíricas que o framework gera "
                   "(p.5-7/L204-304; p.7-14/L314-624; p.17/L778-788)."),
    source_refs=["p.3/L098-106", "p.5/L204-220", "p.14/L625-634", "p.17/L778-788"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("Sob recursos homogêneos e perfeitamente móveis, nenhuma firma pode obter vantagem competitiva sustentada — nem via first-mover advantage nem via barreiras de entrada/mobilidade, pois ambas já pressupõem heterogeneidade e imobilidade.",
      "proposition",
      "in this kind of industry, it is not possible for firms to enjoy a sustained competitive ad- vantage",
      ["p.6/L229-238", "p.6/L247-260", "p.7/L300-304"]),
    F("Para ter potencial de gerar vantagem competitiva sustentada, um recurso deve ter quatro atributos: ser valioso, ser raro, ser imperfeitamente imitável e não ter substitutos estrategicamente equivalentes (framework da Figura Dois).",
      "model",
      "a firm resource must have four attributes: (a) it must be valuable",
      ["p.7/L314-322", "p.8/L325-330"]),
    F("A imitabilidade imperfeita tem três fontes: condições históricas únicas (dependência de trajetória), ambiguidade causal (que deve valer para possuidores e imitadores) e complexidade social — esta última excluindo a tecnologia física pura.",
      "model",
      "Firm resources can be imperfectly imitable for one or a combination of three reasons",
      ["p.9/L397-406", "p.11/L483-500", "p.12/L528-560"]),
    F("Aplicado a recursos candidatos, o framework mostra que planejamento estratégico formal, por ser comum e documentado, dificilmente gera vantagem sustentada; processos informais de formação de estratégia, sistemas de informação profundamente embutidos e reputações podem gerá-la, dependendo de raridade, imitabilidade e substitutos — questões empíricas abertas.",
      "empirical",
      "formal strategic planning by itself is not likely to be a source of sustained com- petitive advantage",
      ["p.15/L656-667", "p.16/L704-712", "p.16/L725-749", "p.17/L750-753", "p.17/L759-777"]),
    F("O modelo reconcilia estratégia com bem-estar social (lucros como 'efficiency rents', não 'monopoly rents'), antecipa a integração entre teoria organizacional e economia, e implica que vantagens não se compram em mercados — encontram-se nas dotações raras, inimitáveis e insubstituíveis já controladas.",
      "proposition",
      "can be thought of as “efficiency rents”",
      ["p.18/L805-816", "p.18/L827-832", "p.19/L855-862"]),
]

CONTRIBUTION = dict(
    theoretical=("Formaliza a resource-based view como modelo de vantagem competitiva sustentada: as suposições de "
                 "heterogeneidade e imobilidade, a definição de equilíbrio de vantagem sustentada e o framework dos "
                 "quatro indicadores (valor, raridade, imitabilidade, substituibilidade) — reconciliando análise "
                 "interna e ambiental e redefinindo first-mover, barreiras e grupos estratégicos como manifestações "
                 "de heterogeneidade (p.2-3/L063-097; p.7/L314-322; p.8/L324-330)."),
    practical=("Oferece à análise interna a mesma rigorosidade que os modelos ambientais deram à externa: gestores e "
               "pesquisadores ganham quatro perguntas testáveis para avaliar qualquer recurso candidato a fonte de "
               "vantagem sustentada (p.17/L778-788)."),
    limitations=("O artigo não resolve a mensuração: quão raro um recurso precisa ser, e se processos formais e "
                 "informais são substitutos, são questões empíricas abertas; tampouco testa o modelo, que opera no "
                 "nível da derivação lógica (p.9/L377-387; p.16/L710-712)."),
    future_research=("Questões empíricas geradas pelo framework: a raridade necessária de recursos, a "
                     "substituibilidade entre processos formais e informais de formação de estratégia, os "
                     "substitutos de sistemas de informação embutidos e de reputações, e o estudo sistemático do "
                     "impacto da história no desempenho (p.16/L710-712; p.16-17/L732-742; p.17/L766-777; "
                     "p.10/L457-459)."),
)
