SUMMARY = (
    "O artigo propõe um quadro metodológico em quatro fases para análises ventríloquas em estudos organizacionais, a "
    "partir da perspectiva da constituição comunicativa das organizações (CCO) (p.1/L024-035; p.2/L080-084). Os autores "
    "partem do ventriloquismo, conceito da escola de Montreal segundo o qual as pessoas dão voz a outros seres, como "
    "políticas, fatos e valores, e ao mesmo tempo são levadas a falar por eles, o que decentra a agência e a trata de "
    "modo relacional (p.2/L051-065; p.3/L131-139). Argumentam que o conceito é atraente, mas carece de meios concretos "
    "para identificar atos ventríloquos (p.2/L066-072; p.5/L210-214). O quadro distingue figures, invocados explícita ou "
    "implicitamente, e vents, que animam quem fala, e organiza a análise em identificar, agrupar e atribuir atividades, "
    "relacionar por cadeias de autoria e mostrar com vinhetas (p.5/L190-209; p.6/L238-254). Para desenvolvê-lo e "
    "ilustrá-lo, estudaram conversas de funcionários sobre visões organizacionais em cinco grupos focais com 23 "
    "participantes de quatro organizações alemãs (banco, corpo de bombeiros, hospital e venda direta), com 117 páginas "
    "de transcrição analisadas no Atlas.ti (p.2/L084-089; p.5/L225-235; p.6/L262-265). A análise gerou 243 vents e "
    "figures, 59 clusters e 24 coleções, relacionados a vozes gerenciais e de equipe (p.7/L299-300; p.8/L409-411; "
    "p.9/L424-428; p.9/L430-438). As quatro vinhetas mostram funcionários traduzindo visões abstratas em práticas "
    "concretas e confirmando ou contestando a visão oficial por meio de figuras do cotidiano (p.11/L586-652; "
    "p.12/L653-663; p.13/L740-747; p.14/L807-813; p.15/L898-904). Concluem que as visões se materializam ao serem "
    "relacionadas à prática e que estrategistas devem apresentar visões dignas de serem ventriloquizadas "
    "(p.16/L909-930). Propõem refinar o quadro e aplicá-lo a valores, missões, identidades e fazer estratégia "
    "(p.17/L981-1005)."
)

RESEARCH_QUESTION = (
    "O artigo não enuncia uma pergunta de pesquisa formal; declara como contribuição principal um quadro metodológico "
    "para o ventriloquismo (p.2/L080-084). Reconstruída como pergunta implícita: como identificar, ordenar e apresentar "
    "sistematicamente efeitos ventríloquos, isto é, o que leva uma pessoa a dizer o que diz e que vozes se reconhecem "
    "no que diz, para mostrar como as visões são faladas à existência (p.2/L066-072; p.1/L029-035)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.2/L044-050", "p.3/L098-105"],
      "propagates a more fluid outlook where organizations emerge in communication, through interaction",
      "A perspectiva CCO é o referencial geral no qual o ventriloquismo se insere."),
    V("T2", "uses", ["p.2/L051-065"],
      "Ventriloquism illustrates how people give voice to other beings—policies, missions, facts, persons, etc.—that can then be deemed as participating in an interaction",
      "Conceito central cujo método o artigo desenvolve."),
    V("T3", "does_not_use", [],
      "",
      "A teoria da estruturação não é mencionada."),
    V("T4", "uses", ["p.3/L131-139", "p.3/L114-117"],
      "ventriloquism conceives of agency from a relational ontology, that is, as a joint mediation shared among various beings",
      "A agência relacional fundamenta a noção de vents e figures."),
    V("T5", "uses", ["p.5/L216-224", "p.16/L911-914"],
      "Visions express long-term goals and provide direction, they are ubiquitous in organizations and associated with effective leadership",
      "A visão organizacional é o gênero de fala usado como caso empírico para desenvolver o quadro."),
    V("T6", "discusses", ["p.4/L150-155", "p.2/L074-079"],
      "a ventriloquial approach negates the classical divide between what constitutes the interactional scene",
      "Contrasta a abordagem ventríloqua com outras abordagens do discurso organizacional."),
    V("T7", "does_not_use", [],
      "",
      "A teoria da complexidade organizacional não é mencionada; 'complexities' aparece só em sentido geral (p.17/L989)."),
    V("T8", "does_not_use", [],
      "",
      "Latour é citado apenas como apoio a um raciocínio sobre agência de objetos (p.3/L122) e em referências, sem desenvolver a teoria ator-rede."),
    V("T9", "does_not_use", [],
      "",
      "Pensamento processual aparece em uma citação de passagem (p.17/L970-971), sem desenvolvimento."),
    V("T10", "does_not_use", [],
      "",
      "'Polyphony' e 'dialogicity' aparecem só em títulos de referências (p.18/L1050-1051; p.19/L1088); o texto trata de 'múltiplas vozes' pelo ventriloquismo, sem teoria polifônica própria."),
    V("T11", "does_not_use", [],
      "",
      "Estratégia e fazer estratégia aparecem como aplicação futura sugerida (p.17/L998-1001) e como ligação com estrategistas (p.16/L925-930), sem abordagem de estratégia como prática."),
]

KEY_CONCEPTS = [
    dict(concept="Constituição comunicativa das organizações (CCO)",
         definition="Perspectiva segundo a qual as organizações emergem e se realizam em práticas comunicativas, interativas e dinâmicas, e não como entidades estáveis e fixas.",
         quote="propagates a more fluid outlook where organizations emerge in communication, through interaction",
         source_refs=["p.2/L044-050", "p.3/L098-105"]),
    dict(concept="Ventriloquismo",
         definition="Processo pelo qual as pessoas dão voz a outros seres (políticas, missões, fatos, pessoas) que passam a participar da interação, ao mesmo tempo em que são levadas a falar por eles; humanos são ventríloquos e bonecos.",
         quote="Ventriloquism illustrates how people give voice to other beings—policies, missions, facts, persons, etc.—that can then be deemed as participating in an interaction",
         source_refs=["p.2/L051-065"]),
    dict(concept="Figures e vents",
         definition="Figures são seres invocados e feitos falar por alguém; vents são o que leva as pessoas a dizer o que dizem e a agir como agem.",
         quote="Analyzing communication episodes from a ventriloquial perspective thus amounts to identifying, on the one hand, the figures that are implicitly or explicitly invoked and made to say things by people, and on the other hand, the vents that lead people to say what they say and act how they act",
         source_refs=["p.5/L190-197"]),
    dict(concept="Invocação explícita e implícita",
         definition="Na invocação explícita, o enunciado menciona diretamente a figura; na implícita, a figura está envolvida no enunciado e precisa ser desdobrada pelo analista.",
         quote="An explicit invocation means that the utterance directly mentions the figure",
         source_refs=["p.5/L202-209", "p.8/L371-373"]),
    dict(concept="Agência relacional",
         definition="Concepção de agência como mediação conjunta compartilhada entre vários seres, que inclui tudo o que faz diferença ou faz algo em uma situação.",
         quote="ventriloquism conceives of agency from a relational ontology, that is, as a joint mediation shared among various beings",
         source_refs=["p.3/L114-122", "p.3/L131-139"]),
    dict(concept="Quadro de quatro fases para análises ventríloquas",
         definition="Quadro proposto pelos autores: identificar vents e figures; agrupar em clusters e coleções e atribuir atividades; relacionar com vozes principais por cadeias de autoria; mostrar achados com vinhetas.",
         quote="Our ventriloquial framework comprises four phases, summarized in Table 1",
         source_refs=["p.6/L238-254", "p.6/L274-283"]),
]

METHODOLOGY = dict(
    study_type="empírico (qualitativo) com finalidade metodológica",
    design="Desenvolvimento de um quadro metodológico por iteração entre a revisão de análises ventríloquas anteriores e a análise de conversas de funcionários sobre visões, ilustrado com quatro vinhetas.",
    sample_type="funcionários (sem gerência, RH, marketing e comunicação) de quatro organizações alemãs: banco regional, corpo de bombeiros, hospital e empresa de venda direta",
    sample_size=23,
    sector="banco, corpo de bombeiros, hospital e venda direta",
    period="",
    methods=["grupos focais", "análise ventríloqua", "análise temática por clusters e coleções", "Atlas.ti"],
    analysis_note=("Foram realizados cinco grupos focais (dois na empresa de venda direta) com 23 participantes, conduzidos pela primeira autora "
                   "(p.5/L225-235), gravados, transcritos, traduzidos do alemão e codificados no Atlas.ti, com 117 páginas de "
                   "transcrição (p.6/L262-265). A análise seguiu as quatro fases do quadro e gerou 243 vents e figures, 59 clusters, "
                   "dez atividades e 24 coleções (p.7/L299-300; p.8/L409-411; p.9/L421-428)."),
    source_refs=["p.2/L084-089", "p.5/L225-235", "p.6/L262-265", "p.7/L299-300", "p.9/L421-428"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("O quadro metodológico tem quatro fases: identificar, agrupar e atribuir atividades, relacionar e mostrar efeitos ventríloquos.",
      "model",
      "Our ventriloquial framework comprises four phases, summarized in Table 1",
      ["p.6/L238-254", "p.6/L274-283"]),
    F("A análise das conversas sobre visões produziu 243 vents e figures, agrupados em 59 clusters e 24 coleções, ligados a vozes gerenciais e de equipe.",
      "empirical",
      "which resulted in a list of 243 vents and figures",
      ["p.7/L299-300", "p.8/L409-411", "p.9/L424-428", "p.9/L430-438"]),
    F("Funcionários traduzem visões abstratas em comportamentos e práticas concretas, e princípios como pôr o paciente em primeiro lugar animam essa tradução.",
      "empirical",
      "we see how a lot of work is done to concretize what at first sight looks like an abstract vision",
      ["p.13/L740-747", "p.16/L915-921"]),
    F("Quando a visão oficial condiz com a experiência cotidiana, os participantes mobilizam figuras que a confirmam.",
      "empirical",
      "ventriloquation consists of mobilizing multiple figures that are implicitly or explicitly presented as confirming the truthfulness of the organization’s vision",
      ["p.14/L807-813"]),
    F("Quando a visão oficial destoa da experiência, os participantes a contestam por figuras de seu trabalho, e o abstrato se separa do cotidiano.",
      "empirical",
      "participants check the official statement against multiple figures of their work experience and routine that they ventriloquize and that unanimously contradict it",
      ["p.15/L894-904"]),
    F("Estrategistas precisam apresentar visões dignas de serem ventriloquizadas pelos membros e que eles mesmos ventriloquizem em seu comportamento.",
      "proposition",
      "Strategists need to present a vision that is worthy to be ventriloquized by members and that they themselves ventriloquize in their behavior",
      ["p.16/L925-930"]),
]

CONTRIBUTION = dict(
    theoretical=("Oferece o primeiro esboço metodológico do ventriloquismo e uma ferramenta que guia a análise sistemática da constituição "
                 "comunicativa (p.2/L080-084; p.16/L932-939). Atende a pedidos de maior explicitação de métodos na CCO (p.16/L940-942), "
                 "inclui os vents, em geral ausentes de estudos anteriores (p.16/L945-949), e acrescenta verbos aos substantivos de vents e "
                 "figures para explicar como as vozes entram nas interações (p.17/L965-971)."),
    practical=("O artigo não traz seção de implicações gerenciais. Indica que estrategistas devem apresentar visões dignas de serem "
               "ventriloquizadas e que análises ventríloquas podem identificar fontes para suas afirmações, além de abstrações "
               "convencionais (p.16/L925-930)."),
)
