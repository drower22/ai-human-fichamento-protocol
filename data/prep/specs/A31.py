SUMMARY = (
    "A revisão mapeia e avalia criticamente o campo em rápido crescimento de strategy-as-practice (s-as-p) "
    "— a pesquisa sobre o fazer da estratégia: quem a faz, o que faz, como, com o quê e com que "
    "implicações (p.4/L061-080). O campo surge da insatisfação com a pesquisa convencional de estratégia, "
    "dominada por fundamentos microeconômicos e análises multivariadas que marginalizam o ator humano, e "
    "culmina deslocamentos construtivistas na gestão estratégica (p.4-5/L061-097). A revisão seleciona "
    "trabalhos publicados que se identificam com a perspectiva via citação de cinco estudos fundacionais "
    "(p.6/L139-151) e organiza-se nos três conceitos do campo — practitioners, practices e praxis — e em "
    "duas questões iteradas: os vínculos micro-macro e a necessidade de outcomes (p.5/L121-124; p.6/L125-138). "
    "Primeiro, os autores desenvolvem uma tipologia de nove domínios cruzando três tipos de practitioner "
    "(indivíduo interno, agregado interno, agregado extra-organizacional) com três níveis de praxis (micro, "
    "meso, macro), mostrando que o campo se concentra nos domínios A, B, D e E e negligencia atores "
    "extra-organizacionais e macro-praxis (p.9-20/L246-609). Segundo, mapeiam os conceitos diversos e "
    "inconsistentes de practices — discursivas (dominantes), episódicas (reuniões/workshops), materiais e "
    "corporificadas (subempíricas) — propondo o estudo sistemático de practice bundles (p.21-25/L610-763). "
    "Terceiro, identificam cinco categorias de outcomes já substantivadas — pessoal, grupo, processo de "
    "strategizing, organizacional e institucional — e propõem dois tipos de explicação (mecanismos "
    "generativos e métodos comparativos) para desenvolvê-los (p.26-31/L765-932)."
)

RESEARCH_QUESTION = (
    "Sem pergunta formal: o objetivo é mapear e avaliar criticamente o corpo de pesquisa em strategy-as-"
    "practice, examinando como os estudos usam os conceitos de practitioners, practices e praxis e "
    "informando seu desenvolvimento futuro (p.3/L045-059; p.5/L102-109)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.5/L110-120"],
      "practitioners (those people who do the work of strategy); practices (the social, symbolic and material tools through which strategy work is done); and praxis",
      "O objeto e a estrutura da própria revisão."),
    V("T2", "uses", ["p.21/L622-640", "p.22/L654-662"],
      "an organization is a bundle of practices and arrangements",
      "O alicerce teórico dos conceitos de practices avaliados na revisão."),
    V("T3", "uses", ["p.9/L223-245"],
      "Praxis is where operation and action meet, a dialectic synthesis",
      "A definição que funda os três níveis de praxis (micro, meso, macro) da tipologia."),
    V("T4", "discusses", ["p.4/L088-093", "p.19/L572-579"],
      "differs from traditional process research in its view of agency",
      "O contraste identitário do campo; a concentração no Domínio E sinaliza a herança processual."),
    V("T5", "discusses", ["p.4/L067-069", "p.4/L085-087"],
      "unpacking the dynamism in dynamic capabilities theory",
      "A SAP é proposta para humanizar e dinamizar a RBV, não para substituí-la."),
    V("T6", "uses", ["p.23/L673-679"],
      "the most common approach to practices is grounded within the linguistic turn",
      "A corrente dominante do tratamento empírico de practices."),
    V("T7", "uses", ["p.23/L680-691"],
      "modes of doing strategy, such as meetings and workshops, as practices",
      "A abordagem emergente de practices episódicas (Luhmann; teoria do ritual)."),
    V("T8", "uses", ["p.18/L538-548", "p.20/L595-609"],
      "strategy may be seen as an institutional field",
      "Domínio I da tipologia e a agenda de macro-praxis; única via empírica de outcomes institucionais."),
    V("T9", "discusses", ["p.14/L387-403"],
      "experienced structural change through their own sensemaking behaviors and their changing schemata",
      "Lente de vários estudos mapeados (Balogun & Johnson; Rouleau), não da revisão em si."),
    V("T10", "discusses", ["p.10/L276-281", "p.25/L745-749"],
      "powerful use of ethnomethodology",
      "Método exemplar do Domínio A e recurso proposto para estudar práticas situadas."),
    V("T11", "uses", ["p.26/L777-786"],
      "detailed analysis of the generative mechanisms to explain how a particular outcome is constructed",
      "A proposta metodológica da seção de outcomes."),
    V("T12", "discusses", ["p.10/L272-281"],
      "the strategic appointment of a new CEO shaped the identity",
      "Lente de estudos do Domínio A; avenida proposta para práticas corporificadas."),
    V("T13", "discusses", ["p.13/L360-363"],
      "the reciprocity between agency and structure",
      "Recurso teórico oferecido para o Domínio C, não a lente do artigo."),
    V("T14", "does_not_use", [], "",
      "A materialidade é tratada pela sociomaterialidade de Orlikowski, não por TAR."),
    V("T15", "does_not_use", [], "",
      "Não nomeada no corpo; Jarzabkowski (2003) é mobilizada por suas práticas administrativas, não pelo enquadre da AT."),
]

KEY_CONCEPTS = [
    dict(concept="Practitioners",
         definition="Quem faz o trabalho da estratégia — definidos amplamente: gestores e consultores diretamente envolvidos, mas também policy-makers, mídia, gurus e escolas de negócio que moldam praxis e práticas legítimas; podem ser indivíduos ou atores agregados, internos ou externos.",
         quote="those people who do the work of strategy",
         source_refs=["p.5/L114-120", "p.7/L169-172"]),
    dict(concept="Praxis",
         definition="O fluxo de atividade em que a estratégia é realizada — síntese dialética entre o que as pessoas fazem e o que acontece na sociedade, operacionalizável em níveis micro, meso e macro.",
         quote="Praxis is where operation and action meet, a dialectic synthesis",
         source_refs=["p.9/L223-235"]),
    dict(concept="Practices",
         definition="As ferramentas sociais, simbólicas e materiais por meio das quais o trabalho de estratégia é feito — rotinas, discursos, conceitos e tecnologias, desde reviews e off-sites até ferramentas analíticas e artefatos materiais.",
         quote="Practices involve the various routines, discourses, concepts and technologies through which this strategy labour is made possible",
         source_refs=["p.22/L658-662"]),
    dict(concept="Tipologia de nove domínios",
         definition="O cruzamento de três tipos de practitioner (indivíduo interno, agregado interno, agregado externo) com três níveis de praxis (micro, meso, macro), gerando os domínios A–I que mapeiam a cobertura empírica e as lacunas do campo.",
         quote="typology of nine possible domains for strategy-as-practice research",
         source_refs=["p.3/L049-051", "p.9/L246-255"]),
    dict(concept="Practice bundles",
         definition="O feixe de práticas inter-relacionadas — ações corporais, mentais, coisas e seu uso, conhecimento de fundo, emoções e motivações — que se reúne em cada instância de praxis e cuja interação sistemática ainda carece de estudo.",
         quote="an organization is a bundle of practices and arrangements",
         source_refs=["p.21/L622-633", "p.25/L737-744"]),
    dict(concept="Cinco categorias de outcomes",
         definition="Os resultados já substantivados na literatura: pessoais, de grupo, de processo de strategizing, organizacionais e institucionais — ligados aos níveis de praxis e explicáveis por mecanismos generativos ou métodos comparativos.",
         quote="personal, group, strategizing process, organizational and institutional outcomes",
         source_refs=["p.26/L791-794"]),
]

METHODOLOGY = dict(
    study_type="revisão crítica de literatura (International Journal of Management Reviews)",
    design="Revisão estruturada nos três conceitos do próprio campo (practitioners, practices, praxis), com tipologia derivada de duas dimensões ontológicas — unidade do practitioner (individual × agregado; interno × externo) e nível de praxis (micro, meso, macro) — e mapeamento de outcomes por categoria",
    sample_type="trabalhos publicados ou in press — teóricos e empíricos — que se identificam explicitamente com a perspectiva s-as-p, inclusive pela citação de ao menos um dos cinco estudos fundacionais (Hendry 2000; Johnson et al. 2003; Jarzabkowski 2004; Whittington 1996; 2003)",
    sample_size=0,
    sector="campo de pesquisa em estratégia (strategy-as-practice)",
    period="literatura da primeira década do campo (até 2008)",
    methods=["critérios de inclusão explícitos por autoridentificação com a agenda s-as-p", "classificação dos estudos nas dimensões practitioner × praxis (nove domínios)", "mapeamento dos conceitos de practices e das cinco categorias de outcomes", "questões ilustrativas de pesquisa formuladas para cada domínio"],
    analysis_note=("Revisão conceitual-organizativa, não sistemática por contagem: os estudos foram lidos quanto à "
                   "forma de conceituar o practitioner e ao nível de praxis explicado, gerando a tipologia de nove "
                   "domínios; a seção de practices mapeia as definições teóricas subjacentes (Schatzki, Reckwitz, "
                   "Orlikowski) e seus usos empíricos; a seção de outcomes elicita cinco categorias a partir da "
                   "pergunta-guia 'o que este estudo explica?' (p.6/L139-151; p.26-27/L787-794; p.30/L918-927)."),
    source_refs=["p.6/L139-157", "p.7/L158-163", "p.9/L246-255", "p.26/L787-794", "p.30/L918-927"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("O campo se define por três conceitos inter-relacionados — practitioners, practices e praxis — e a estratégia como 'atividade situada e socialmente realizada'; a definição de practitioner é ampla, indo de gestores a gurus e escolas de negócio.",
      "empirical",
      "as a situated, socially accomplished activity",
      ["p.5/L110-120", "p.7/L169-172"]),
    F("A tipologia de nove domínios (três tipos de practitioner × três níveis de praxis) revela que o campo se concentra empiricamente nos Domínios A, B, D e E — atores internos em praxis micro e meso — herdando o foco da tradição processual.",
      "empirical",
      "the s-as-p field empirically has been dominated by studies in Domains A, B, D and E",
      ["p.19/L571-579", "p.20/L581-585"]),
    F("Há lacunas severas: atores extra-organizacionais quase não são foco empírico (Domínios G e H), e a macro-praxis tem pouca evidência empírica (Domínios C, G e I), apesar do interesse conceitual na institucionalização da estratégia como prática social e profissão.",
      "empirical",
      "the lack of attention to extra-organizational actors, particularly in Domains G and H is a matter of concern",
      ["p.20/L585-599", "p.24/L704-720"]),
    F("Não há visão dominante sobre practices: a abordagem discursiva domina; práticas episódicas (reuniões, workshops, rituais) emergem; e práticas materiais (PowerPoint, números, arranjos espaciais) e corporificadas (know-how, emoções, identidade) permanecem subempíricas — o estudo de practice bundles é proposto.",
      "empirical",
      "reveals no dominant view on the concept of practices",
      ["p.23/L671-672", "p.24/L721-734", "p.25/L735-744"]),
    F("O campo já substantiva cinco categorias de outcomes — pessoal, grupo, processo de strategizing, organizacional e institucional — frequentemente entrelaçadas entre níveis de praxis, embora poucos estudos os tenham como foco deliberado.",
      "empirical",
      "studies may have multiple outcomes spanning levels of praxis, which should not be seen in isolation but as inter-twined dynamic outcomes",
      ["p.26/L787-794", "p.27/L797-820", "p.30/L904-917"]),
    F("Para desenvolver outcomes, propõem-se dois tipos de explicação adequados à natureza idiográfica da SAP: análise detalhada de mecanismos generativos em casos únicos e métodos comparativos que examinam se variações nos mecanismos se associam a variações nos resultados.",
      "proposition",
      "detailed analysis of the generative mechanisms to explain how a particular outcome is constructed",
      ["p.26/L777-786", "p.30/L924-927", "p.31/L928-932"]),
]

CONTRIBUTION = dict(
    theoretical=("Três contribuições declaradas: (1) um mapa do campo baseado em sua própria terminologia — a tipologia "
                 "de nove domínios que organiza e ilumina o que se entende por practitioner e praxis; (2) a exposição "
                 "das lacunas empíricas — atores extra-organizacionais, macro-praxis, práticas materiais e "
                 "corporificadas, institutionalização e bundles; (3) recursos teóricos alternativos de outros campos "
                 "(antropologia, etnometodologia, sociologia, teoria crítica, teoria institucional) para endereçá-las "
                 "(p.31/L933-943)."),
    practical=("O guia operacional 'o que este estudo explica?' e os dois tipos de explicação de outcomes ajudam "
               "pesquisadores a desenhar estudos que substantivem resultados; as questões ilustrativas por domínio "
               "oferecem uma agenda concreta para as próximas pesquisas (p.26-31/L765-932)."),
    limitations=("A revisão cobre apenas trabalhos que se autoidentificam com a agenda s-as-p via os cinco estudos "
                 "fundacionais, negligenciando estudos complementares e trabalhos em andamento que endereçam as "
                 "próprias lacunas apontadas (p.6/L139-151)."),
    future_research=("A agenda proposta: estudos empíricos nos domínios pouco cobertos (C, F, G, H, I) — atores "
                     "extra-organizacionais também como indivíduos; práticas materiais, corporificadas e "
                     "institucionalizadas; practice bundles e sua reorganização; e desenvolvimento dos dois tipos de "
                     "outcomes — com recursos de campos complementares (p.19-20/L571-609; p.24-25/L721-763; "
                     "p.31/L960-1000)."),
)
