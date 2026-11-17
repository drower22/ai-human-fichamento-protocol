SUMMARY = (
    "O ensaio teórico propõe articular a rememoração, entendida como prática social, com a construção de sentido "
    "nas organizações (p.2/L052-057). Parte de dois autores pouco trabalhados na Administração: Ricœur, pela "
    "Fenomenologia Hermenêutica da Memória, que relaciona memória, história e esquecimento, e Certeau, pelas "
    "práticas sociais e microrresistências do cotidiano (p.2/L053-057; p.2/L087-094). Os autores situam o debate na "
    "crítica à visão funcional da memória organizacional, representada por Walsh e Ungson e por Wegner, e se unem aos "
    "que buscam superá-la pela vertente sociológica (p.2/L058-067; p.2/L085-086). Quanto à construção de sentido, "
    "recuperam a trajetória de Weick, apresentam o sensemaking por quatro fundamentos de Sandberg e Tsoukas e "
    "distinguem sensegiving e sensebreaking, com as quatro formas de sensegiving de Schildt et al. (supressivo, "
    "autoritário, inspirador e expansivo) ligadas ao poder (p.6/L296-300; p.7/L344-345; p.8/L368-380). O argumento "
    "central é que a construção de sentido nas organizações emerge de práticas cotidianas, relacionais e "
    "historicamente situadas, que articulam lembrar, narrar e esquecer (p.9/L430-432). A proposta é sintetizada no "
    "Quadro 1, que relaciona memória, história e esquecimento a modalidades de sensemaking (identitário, documental, "
    "latente), de sensegiving e de sensebreaking (revisionista, apagador) (p.11/L541-542; p.12/L655-657). Os autores "
    "afirmam que as organizações são orientadas por razão instrumental e intencionalidade consequencialista, de modo "
    "que memória, história e esquecimento ficam muitas vezes sob intenção de controle, o que aparece no sensegiving "
    "(p.12/L634-640). Não há coleta de dados: o trabalho se declara uma apresentação direcionada de conceitos, e não "
    "uma revisão de literatura (p.4/L170-171). Como agenda, sugerem estudar o papel da temporalidade, as práticas de "
    "esquecimento institucional e o lado sombrio das organizações, as disputas mnemônicas entre grupos e as "
    "microrresistências de indivíduos comuns (p.12/L662-665; p.13/L670-689)."
)

RESEARCH_QUESTION = (
    "O artigo não enuncia uma pergunta de pesquisa explícita; declara como objetivo propor uma articulação teórica "
    "entre a rememoração, entendida como prática social, e a construção de sentido nas organizações "
    "(p.2/L052-057). Reconstruída como pergunta implícita: como a rememoração, lida pela Fenomenologia "
    "Hermenêutica da Memória de Ricœur e pelas práticas sociais de Certeau, se relaciona com os processos de "
    "sensemaking, sensegiving e sensebreaking nas organizações (p.4/L172-179; p.12/L647-654)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.4/L181-187", "p.2/L087-089"],
      "Neste artigo, trabalharemos com o conceito de memória com base na obra de Ricœur (2020)",
      "Base conceitual declarada de memória, história e esquecimento."),
    V("T2", "uses", ["p.6/L276-285", "p.2/L090-094"],
      "o que entendemos é que o ato de rememorar é uma prática social",
      "Lente de Certeau (práticas sociais, táticas e microrresistências) usada para ler a rememoração."),
    V("T3", "does_not_use", [], "",
      "Não há menção à teoria da estruturação; 'estruturas' aparece só em sentido genérico (p.2/L064; p.5/L240; p.8/L380)."),
    V("T4", "uses", ["p.2/L052-053", "p.7/L324-331", "p.7/L344-345"],
      "propor uma articulação teórica entre a rememoração, entendida enquanto uma prática social, e a construção de sentido nas organizações",
      "Um dos dois eixos do ensaio; apresentado a partir de Weick e de Sandberg e Tsoukas."),
    V("T5", "uses", ["p.8/L377-380", "p.12/L655-657"],
      "quatro formas de sensegiving – supressivo, autoritário, inspirador e expansivo",
      "A tipologia de Schildt et al. estrutura o mapeamento de memória, história e esquecimento (Quadro 1)."),
    V("T6", "discusses", ["p.9/L458-461"],
      "a memória coletiva como representações construídas e reconstruídas coletivamente do passado a partir do presente",
      "Definição de Halbwachs usada para tratar a memória como sensegiving; apoio pontual, não fundamento."),
    V("T7", "discusses", ["p.2/L058-067", "p.5/L211-213"],
      "as caixas de armazenamento, de Walsh e Ungson (1991), e os sistemas de memória transacional (Wegner, 1987)",
      "Apresentadas como abordagens precursoras e funcionais que o ensaio busca superar."),
    V("T8", "does_not_use", [], "",
      "O termo aprendizagem não aparece no texto."),
    V("T9", "uses", ["p.2/L075-085", "p.4/L181-184"],
      "conduziram um estudo que buscou avaliar as principais perspectivas utilizadas pelos pesquisadores nos estudos de memória organizacional e encontraram quatro",
      "Posiciona o ensaio frente às quatro perspectivas de Foroughi et al. e ao organizational remembering."),
    V("T10", "discusses", ["p.11/L539-541", "p.13/L673-676"],
      "Tal prática pode ser associada aos estudos do dark side das organizações",
      "Associa o esquecimento institucional ao lado sombrio e o inclui na agenda de pesquisa."),
    V("T11", "discusses", ["p.12/L633-639"],
      "é orientado por uma razão instrumental e por inúmeras práticas sustentadas por uma intencionalidade consequencialista",
      "Caracteriza o contexto organizacional e explica o uso controlador de memória, história e esquecimento."),
    V("T12", "discusses", ["p.10/L496-501"],
      "a história organizacional é usada como um recurso estratégico da instituição e direcionada por interesses organizacionais",
      "Aparece na discussão da história como sensegiving autoritário e sensemaking documental."),
]

KEY_CONCEPTS = [
    dict(concept="Rememoração",
         definition="Ação pela qual a consciência de um momento passado é trazida à cena; distingue-se da memorização, ligada à memória funcional. Os autores a tratam como prática social, individual e coletiva, dinâmica.",
         quote="o rememorar é individual e coletivo, não é estático e nem dado",
         source_refs=["p.5/L208-213", "p.5/L225-228"]),
    dict(concept="Dialética entre memória, história e esquecimento",
         definition="Para Ricœur, a memória, que tem a ambição de fidelidade, está em relação dialética com a história, que tem a exigência de verdade, e com o esquecimento, que pode ser apagamento definitivo ou esquecimento de reserva.",
         quote="Ela está em uma relação dialética com a história e o esquecimento",
         source_refs=["p.5/L236-243", "p.6/L269-273"]),
    dict(concept="Prática social (Certeau)",
         definition="As diferentes maneiras de fazer dos indivíduos em seu cotidiano diante do que lhes é imposto, sempre situadas.",
         quote="Certeau compreende por prática social as diferentes maneiras de fazer dos indivíduos",
         source_refs=["p.6/L276-279", "p.2/L090-092"]),
    dict(concept="Microrresistências",
         definition="Micropráticas de resistência que ocorrem no cotidiano dos indivíduos, que utilizam as institucionalidades de formas diferentes e não são apenas fruto do contexto.",
         quote="micropráticas de resistência ou microrresistências que ocorrem no cotidiano dos indivíduos",
         source_refs=["p.6/L281-285", "p.6/L288-290"]),
    dict(concept="Sensemaking, sensegiving e sensebreaking",
         definition="Sentidos construídos, direcionados ou rompidos, respectivamente; o sensebreaking é o rompimento com sentidos já construídos e o sensegiving pode ser relacional ou o direcionamento de ideias de um ator sobre o processo de outro.",
         quote="os sentidos construídos, direcionados ou rompidos – sensemaking, sensegiving e sensebreaking, respectivamente",
         source_refs=["p.8/L368-372", "p.8/L392-395"]),
    dict(concept="Modalidades propostas: sensemaking identitário, documental e latente; sensebreaking revisionista e apagador",
         definition="Categorias com as quais os autores complementam as formas de sensegiving de Schildt et al. para relacionar memória, história e esquecimento aos processos de sentido.",
         quote="complementando com o sensemaking identitário, documental, latente, sensebreaking revisionista e sensebreaking apagador",
         source_refs=["p.12/L655-657", "p.11/L541-542"]),
]

METHODOLOGY = dict(
    study_type="teórico (ensaio teórico)",
    design="Ensaio teórico que articula a Fenomenologia Hermenêutica da Memória de Ricœur e as práticas sociais de Certeau com os conceitos de sensemaking, sensegiving e sensebreaking, a partir de uma proposta relacional.",
    sample_type="não se aplica (sem coleta de dados)",
    sample_size=None,
    sector="",
    period="",
    methods=["ensaio teórico", "articulação teórica relacional"],
    analysis_note=("Os autores afirmam que o trabalho não é uma revisão de literatura, mas uma apresentação direcionada de "
                   "conceitos de dois autores e de seus potenciais de pesquisa (p.4/L170-171). O texto não descreve procedimentos "
                   "de busca ou análise de dados; a articulação é construída conceitualmente e sintetizada no Quadro 1 (p.1/L017; p.11/L541-542)."),
    source_refs=["p.2/L052-057", "p.4/L170-179", "p.1/L017"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("O processo de construção de sentido nas organizações emerge de práticas cotidianas, relacionais e historicamente situadas, que articulam lembrar, narrar e esquecer.",
      "proposition",
      "o processo de construção de sentido nas organizações emerge de práticas cotidianas, relacionais e historicamente situadas, que articulam lembrar, narrar e esquecer",
      ["p.9/L430-432"]),
    F("Quadro 1 articula memória, história e esquecimento a modalidades de sensemaking, sensegiving e sensebreaking nas organizações.",
      "model",
      "apresentamos no Quadro 1 uma proposta de articulação entre conceitos apresentados e relações construídas",
      ["p.11/L541-542", "p.11/L548-612", "p.12/L626-633"]),
    F("A memória pode operar como sensemaking identitário, ligado ao pertencimento e à interpretação de si em uma história organizacional.",
      "proposition",
      "o entendemos como um sensemaking identitário, isto é, parte da rememoração que pode representar uma forma de pertencer e interpretar a si mesmo em uma história organizacional",
      ["p.9/L453-457", "p.9/L444-448"]),
    F("Memória, história e esquecimento são muitas vezes articulados à intencionalidade instrumental das organizações, sob intenção de controle, o que aparece no sensegiving.",
      "proposition",
      "os movimentos relativos a memória, história e esquecimento são, muitas vezes, articulados a essa intencionalidade instrumental",
      ["p.12/L633-640"]),
    F("O sensebreaking apagador pode ser interpretado como ferramenta de transformação organizacional.",
      "proposition",
      "um sensebreaking apagador pode ser interpretado como uma relevante ferramenta de transformação organizacional",
      ["p.11/L535-541"]),
    F("Algumas empresas que praticam crimes organizacionais usam narrativas para silenciar a memória dos indivíduos, o que justifica estudar suas microrresistências.",
      "proposition",
      "utilizam, muitas vezes, narrativas com o objetivo de silenciar a memória dos indivíduos",
      ["p.13/L673-681"]),
]

CONTRIBUTION = dict(
    theoretical=("Propõe articular Ricœur e Certeau, autores pouco trabalhados na Administração, com a tríade sensemaking, "
                 "sensegiving e sensebreaking (p.2/L052-057; p.4/L168-171), unindo-se aos esforços de superar a visão funcional "
                 "da memória organizacional (p.2/L085-086; p.3/L129-134). Acrescenta uma crítica à funcionalização do "
                 "conhecimento em management (p.9/L441-442), a articulação do Quadro 1 (p.11/L541-542) e uma agenda de "
                 "pesquisa sobre temporalidade, esquecimento institucional, disputas mnemônicas e uso estratégico da memória "
                 "(p.12/L662-665; p.13/L670-689)."),
    practical=("O artigo não traz seção de implicações gerenciais; o objetivo declarado é uma articulação teórica e uma "
               "agenda de pesquisa (p.1/L017-018). Indica apenas que a perspectiva pode instigar novos olhares e "
               "reivindicar vozes silenciadas nos espaços organizacionais (p.3/L132-134)."),
)
