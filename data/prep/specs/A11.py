SUMMARY = (
    "O capítulo apresenta uma visão geral da teoria do resourcing, comparando-a com a dependência de recursos e a "
    "visão baseada em recursos, e a relaciona à pesquisa em Positive Organizational Scholarship (POS) "
    "(p.2/L021-027). As autoras criticam a visão típica de recursos como ativos com qualidades inatas e definem "
    "recurso como qualquer coisa que permita a um ator atualizar um esquema, distinguindo recursos potenciais e "
    "recursos em uso, que dependem de prática (p.3/L058-062; p.4/L070-082; p.7/L146-149). Ilustram a diferença com um "
    "experimento mental sobre donas de casa que fazem almôndegas sob racionamento de carne na Segunda Guerra e "
    "contrastam as previsões da dependência de recursos, das capacidades dinâmicas e do resourcing (p.4/L083-088; "
    "p.5/L089-108; p.9/L190-212; p.10/L216-241; p.11/L242-247). Em seguida descrevem três mecanismos de resourcing, "
    "extraídos de pesquisas empíricas anteriores: ajuste mútuo (equity sticks em salas de aula), justaposição "
    "(mudança cultural e liminaridade) e narração (o voo 93) (p.11/L258-265; p.12/L276-283; p.15/L342-352; "
    "p.17/L394-411). Introduzem o resourcing endógeno e os ciclos ampliativos, em que um framework criado vira "
    "recurso e os ciclos crescem em uma direção, e mostram que nem todo resourcing endógeno é ampliativo nem produz "
    "resultados positivos (p.18/L437-439; p.19/L443-450; p.20/L481-493; p.22/L523-527). Argumentam que a teoria "
    "interessa à POS porque a consciência dessas dinâmicas permite dirigi-las (p.21/L510-517). Encerram com cinco "
    "direções de pesquisa, como a sinergia com capacidades dinâmicas e o estudo de ciclos ampliativos "
    "(p.22/L529-543; p.23/L544-565; p.24/L571-582). O texto é teórico e não tem coleta de dados própria."
)

RESEARCH_QUESTION = (
    "O capítulo não enuncia uma pergunta de pesquisa formal; declara como propósito apresentar a teoria do resourcing, "
    "explicar três mecanismos e explorar como o resourcing endógeno e os ciclos ampliativos sustentam espirais "
    "positivas (p.2/L021-027). O texto se organiza em torno de questões centrais sobre o que constitui um recurso, "
    "como as ações criam recursos e como se dão os ciclos ampliativos (p.3/L051-056). Reconstruída como pergunta "
    "implícita: como o resourcing redefine recursos e que mecanismos e ciclos podem promover resultados positivos "
    "em organizações (p.3/L039-050)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.4/L070-076"],
      "Resourcing theory points to a definition of resources focusing on how organizational members take up and use assets as they pursue activities in line with what they wish to make happen in the world",
      "Teoria central do capítulo."),
    V("T2", "uses", ["p.19/L443-450", "p.3/L043-050"],
      "What makes endogenous resourcing ampliative is that the potential resources created in the recursive resourcing cycles are harnessed to move in a general direction",
      "Segunda parte da contribuição: o resourcing endógeno e os ciclos ampliativos."),
    V("T3", "uses", ["p.11/L258-265", "p.12/L271-283", "p.14/L338-341", "p.17/L394-399"],
      "we draw upon research related to three resourcing mechanisms in organizations",
      "Os três mecanismos (ajuste mútuo, justaposição e narração) organizam a seção central do capítulo."),
    V("T4", "does_not_use", [],
      "",
      "A teoria da agência não é mencionada; o texto usa 'agentic' para a ação dos atores."),
    V("T5", "uses", ["p.2/L024-027", "p.3/L039-043"],
      "mechanisms of resourcing in context that arise from recent empirical research and are likely to be of value to positive organizational scholars",
      "O capítulo é escrito para estudiosos de POS e ancora a relevância da teoria em espirais positivas."),
    V("T6", "discusses", ["p.5/L090-093", "p.9/L193-198"],
      "Theories of resource dependence (Pfeffer & Salancik, 1978) might predict that the homemaker would skip making meatballs and make something else for the family meal",
      "Comparada com o resourcing na Figura 2, como visão em que a ação depende da disponibilidade de recursos."),
    V("T7", "discusses", ["p.4/L064-069", "p.9/L200-214"],
      "The resource based view of the firm argues that the innate qualities of resources are highly valuable",
      "Comparada e criticada como visão de recursos com qualidades inatas; também aparece como possível sinergia (p.22/L541-543)."),
    V("T8", "discusses", ["p.5/L094-100", "p.22/L535-543", "p.23/L544-547"],
      "theories of dynamic capabilities (Eisenhardt & Martin, 2000; Teece, et al., 1997) make a slightly different prediction",
      "Comparada com o resourcing, e proposta como área de sinergia nas direções futuras."),
    V("T9", "does_not_use", [],
      "",
      "A teoria institucional não é mencionada; 'institucionalização' aparece só em títulos de referências (p.28/L678; p.28/L688)."),
    V("T10", "uses", ["p.4/L074-076", "p.18/L434-436"],
      "a new definition of a resource as anything that allows an actor to enact a schema",
      "A definição de recurso e a relação entre esquema e recurso derivam de Sewell (1992)."),
    V("T11", "uses", ["p.5/L101-105", "p.6/L127-129"],
      "Theories of resourcing offer a third prediction, in part because this body of theory posits the relationship between resources and action as it is lived in practice",
      "As práticas cotidianas, com de Certeau, são o que transforma recursos potenciais em recursos em uso."),
    V("T12", "does_not_use", [],
      "",
      "Weick é citado só para dizer que a linguagem é um recurso potencial disponível (p.18/L426-427); sensemaking não é desenvolvido."),
    V("T13", "does_not_use", [],
      "",
      "Objetos de fronteira e tecnologia em uso aparecem em duas menções breves de apoio à generalização dos mecanismos (p.14/L321-323; p.16/L387-390)."),
    V("T14", "does_not_use", [],
      "",
      "Teorias de emoção positiva (broaden-and-build) são citadas apenas como área de interesse nas direções futuras (p.23/L559-561)."),
]

KEY_CONCEPTS = [
    dict(concept="Recurso (definição do resourcing)",
         definition="Qualquer coisa que permita a um ator atualizar um esquema; define recursos pelo modo como são usados, e não apenas por qualidades inatas.",
         quote="a new definition of a resource as anything that allows an actor to enact a schema",
         source_refs=["p.4/L074-076"]),
    dict(concept="Recursos potenciais e recursos em uso",
         definition="Ativos com qualidades que lhes dão potencial só se tornam recursos em uso quando são tomados e usados na atualização de um framework, por meio de prática.",
         quote="potential resources become resources in use when they are taken up in enacting a framework",
         source_refs=["p.7/L146-149", "p.6/L121-129"]),
    dict(concept="Ajuste mútuo (mutual adjusting)",
         definition="Mecanismo em que recursos potenciais e frameworks se ajustam entre si no contexto da prática, em contraste com o ajuste estático (matching).",
         quote="Mutual adjusting as a resourcing mechanism helps illuminate the link between resources in use and frameworks for organizing by showing how potential resources and frameworks are adjusted to one another in the context of practice",
         source_refs=["p.12/L276-283"]),
    dict(concept="Justaposição (juxtaposing)",
         definition="Ação de colocar lado a lado símbolos ou práticas familiares e não familiares, com a qual atores criam recursos, como a liminaridade, e energizam frameworks para facilitar mudança.",
         quote="emphasizes the action of juxtaposing as an important means by which actors in organizations create resources and energize frameworks to facilitate change",
         source_refs=["p.15/L342-352"]),
    dict(concept="Narração (narrating)",
         definition="Ação que transforma recursos potenciais em recursos em uso ao alterar o framework ou o que está sendo reforçado, apoiando-se na linguagem.",
         quote="Narrating is action that transforms potential resources to resources in use by altering the framework or what is being resourced",
         source_refs=["p.17/L395-400", "p.18/L424-432"]),
    dict(concept="Resourcing endógeno e ciclos ampliativos",
         definition="O resourcing endógeno usa um framework já criado como novo recurso; é ampliativo quando os ciclos crescem em uma direção e dão energia a um metaframework.",
         quote="We use the term ampliative to refer to resourcing cycles that grow in a general direction, providing more energy for what one might refer to as a meta-framework or a larger framework",
         source_refs=["p.19/L443-450", "p.18/L437-439"]),
]

METHODOLOGY = dict(
    study_type="teórico (capítulo conceitual)",
    design="Capítulo que apresenta a teoria do resourcing, compara-a com a dependência de recursos e a visão baseada em recursos e a ilustra com um experimento mental e com estudos empíricos publicados.",
    sample_type="não se aplica (sem coleta de dados); exemplos de estudos anteriores",
    sample_size=None,
    sector="",
    period="",
    methods=["capítulo teórico", "experimento mental", "análise de estudos empíricos publicados"],
    analysis_note=("As autoras usam um experimento mental sobre donas de casa sob racionamento de carne na Segunda Guerra (p.4/L083-088; "
                   "p.5/L089-108) e reinterpretam estudos de outros autores, como Jaquith, Howard-Grenville et al., Quinn e Worline e "
                   "Feldman e Quick, como exemplos de mecanismos de resourcing (p.11/L258-265)."),
    source_refs=["p.2/L021-027", "p.4/L083-088", "p.5/L089-108", "p.11/L258-265"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("Recursos potenciais se tornam recursos em uso por meio de práticas, e a centralidade das práticas é um traço distintivo da teoria do resourcing.",
      "proposition",
      "it is these cooking practices that transformed bread from a potential resource to a resource in use. Emphasizing practices as central to resources is a unique and important aspect of theories of resourcing",
      ["p.6/L121-129"]),
    F("O resourcing é um processo dinâmico de ajuste mútuo entre recursos potenciais e frameworks emergentes, e não de combinação de objetos estáticos.",
      "proposition",
      "the process is not one of matching two static objects (ingredients and meatballs), but of mutual adjustment between potential resources and emerging frameworks",
      ["p.7/L150-160"]),
    F("A teoria do resourcing foca as ações dentro das organizações, e não as ações da organização em relação ao ambiente, o que a diferencia da dependência de recursos e da visão baseada em recursos.",
      "model",
      "The focus of resourcing theory, by contrast, is on actions in organizations (specific, identifiable actions taken by specific people (or sometimes machines such as computers) at specific times and places) rather than the actions of organizations in relation to their environments",
      ["p.10/L228-240"]),
    F("Há três mecanismos de resourcing: ajuste mútuo, justaposição e narração, ilustrados por equity sticks, mudança cultural e o voo 93.",
      "model",
      "we draw upon research related to three resourcing mechanisms in organizations",
      ["p.11/L258-265", "p.12/L276-283", "p.15/L342-352", "p.17/L394-411"]),
    F("O resourcing endógeno nem sempre é ampliativo; depende de o framework energizado ser usado como recurso para estender um metaframework.",
      "proposition",
      "endogenous resourcing is not always ampliative",
      ["p.20/L477-493", "p.21/L494-508"]),
    F("Recursos só podem ser julgados como bons ou ruins no contexto de seu uso, o que permite separar a avaliação do processo da avaliação do resultado.",
      "proposition",
      "it shows that resources can only be judged as good or bad in the context of their use",
      ["p.22/L520-527"]),
]

CONTRIBUTION = dict(
    theoretical=("Apresenta a teoria do resourcing como alternativa à dependência de recursos e à visão baseada em recursos, ao enfocar a "
                 "ação que transforma recursos potenciais em recursos em uso (p.4/L070-082; p.10/L216-241). Descreve três mecanismos de "
                 "resourcing e propõe o resourcing endógeno e os ciclos ampliativos como ponte para a POS (p.11/L258-265; p.19/L443-450). "
                 "Aponta cinco direções de pesquisa (p.22/L529-543; p.23/L544-565; p.24/L571-582)."),
    practical=("O capítulo não traz seção de implicações gerenciais. Afirma que entender o processo de resourcing é uma ferramenta para "
               "estudiosos e gestores que querem promover espirais positivas, ao permitir criar ciclos ampliativos e separar a avaliação "
               "do processo da do resultado (p.3/L040-050; p.21/L510-517)."),
)
