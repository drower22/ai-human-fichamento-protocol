SUMMARY = (
    "O estudo analisa como as lógicas institucionais proporcionaram a mudança na configuração do campo da educação "
    "para institucionalizar a educação superior a distância (EaD) no Brasil (p.1/L007-010; p.3/L106-108). Situa-se "
    "no institucionalismo sociológico e na abordagem das lógicas institucionais, entendidas como padrões históricos "
    "de símbolos culturais e práticas materiais, e adota o hibridismo, em que lógicas se combinam e formam novas "
    "lógicas e práticas (p.2/L058-059; p.4/L140-147; p.5/L172-176). A partir de tipos ideais weberianos, trata de três "
    "lógicas: educação como valor social, como mercado e como direito de todos acompanhado pelo Estado "
    "(p.6/L207-210; p.22/L1137-1139). Metodologicamente, combina pesquisa histórica e análise documental de 23 "
    "normativos obtidos da ABED e do MEC, codificados em 281 trechos no Atlas.ti e submetidos a análise de conteúdo "
    "e análise axiológica nos planos vertical e horizontal (p.1/L009-010; p.7/L301-307; p.8/L351-355; p.8/L411-418; "
    "p.9/L419-420). Os achados indicam que a EaD entrou no Brasil sob a lógica da educação como valor social, mas a "
    "lógica de mercado esteve presente desde cedo e se fortaleceu com a política neoliberal e a LDB de 1996, com "
    "crescimento de organizações privadas e formação de um mercado concentrado por fusões e aquisições "
    "(p.9/L437-445; p.10/L465-466; p.12/L634-640; p.14/L854-859). A lógica do direito de todos acompanhado pelo Estado, "
    "expressa nos normativos, combinou-se às demais, mas os normativos permitiram a livre atuação privada e não "
    "estabeleceram padrões coerentes de qualidade (p.15/L888-892; p.18/L1022-1024; p.19/L1031-1032). Os autores "
    "concluem que a mudança institucional se explica pelo hibridismo entre as três lógicas, que configurou um mercado "
    "amparado pelo poder público e legítimo na sociedade (p.21/L1122-1131; p.22/L1137-1139). Como agenda, sugerem "
    "estudar a tradução dessas lógicas, comparar as esferas pública e privada e analisar rupturas em momentos de "
    "crise (p.23/L1167-1172)."
)

RESEARCH_QUESTION = (
    "Como as lógicas institucionais atuaram na configuração do campo da educação para institucionalizar a educação "
    "superior a distância no Brasil? A pergunta é enunciada explicitamente (p.3/L106-108) e retomada nas "
    "considerações finais (p.22/L1135-1137)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.4/L140-147", "p.2/L064-066"],
      "as lógicas são padrões históricos de símbolos culturais e práticas materiais socialmente constituídos, incluindo suposições, valores e crenças",
      "Lente central do estudo, aplicada à educação a distância."),
    V("T2", "uses", ["p.2/L058-059", "p.2/L074-082"],
      "Este estudo se insere no campo da educação sob a lente do institucionalismo sociológico",
      "Abordagem declarada como base teórica, em contraste com as abordagens histórica e econômica."),
    V("T3", "does_not_use", [],
      "",
      "A teoria da dependência de recursos não é mencionada; 'recursos materiais' aparece apenas para caracterizar a abordagem sociológica (p.4/L132-136)."),
    V("T4", "uses", ["p.5/L168-176", "p.5/L181-184"],
      "propõe-se o hibridismo no qual as lógicas podem combinar elementos e formar uma nova lógica",
      "O hibridismo explica a institucionalização da EaD e organiza a análise e as conclusões."),
    V("T5", "uses", ["p.6/L190-195", "p.6/L207-210"],
      "empregam o conceito de tipificação ideal de Weber (1922), na qual constituem um tipo ideal para identificar a lógica institucional predominante no campo",
      "Os tipos ideais das lógicas (Quadro 1) são o instrumento analítico do estudo."),
    V("T6", "does_not_use", [],
      "",
      "Não há teoria crítica da educação; Saviani é citado apenas como crítico dos fins utilitários dos normativos (p.17/L987-990)."),
    V("T7", "does_not_use", [],
      "",
      "Os mecanismos coercitivo, mimético e normativo são mencionados só na justificativa, como algo a ser explicado pelas lógicas (p.3/L111-113), sem desenvolvimento."),
    V("T8", "discusses", ["p.4/L125-132"],
      "A abordagem histórica critica o estruturalismo e o funcionalismo e considera as instituições como um conjunto de protocolos, normas e convenções que são determinadas pela vida política",
      "Descreve as abordagens histórica e de escolha racional para contrastá-las com a sociológica, sem usá-las na análise."),
    V("T9", "uses", ["p.10/L474-485", "p.12/L634-638", "p.20/L1089-1095"],
      "O neoliberalismo, uma vertente econômica que prioriza o livre mercado e a participação mínima do Estado, descentralizou o Estado e ampliou a necessidade do uso da EaD",
      "A política neoliberal é usada para explicar o fortalecimento da lógica de mercado e dos normativos."),
    V("T10", "uses", ["p.19/L1053-1058", "p.21/L1125-1127"],
      "a mudança institucional pode ser compreendida a partir do hibridismo de lógicas institucionais",
      "A mudança institucional é o fenômeno explicado pelo estudo."),
    V("T11", "does_not_use", [],
      "",
      "A sociedade em rede aparece em uma única frase, citando Arruda e Bozza (p.12/L644-646), sem desenvolvimento."),
    V("T12", "does_not_use", [],
      "",
      "A tradução de lógicas é só sugestão de pesquisa futura (p.23/L1167-1168)."),
]

KEY_CONCEPTS = [
    dict(concept="Lógicas institucionais",
         definition="Padrões históricos de símbolos culturais e práticas materiais, com suposições, valores e crenças, pelos quais indivíduos e organizações dão sentido à atividade diária e reproduzem suas vidas; coordenam práticas e comportamentos dos atores.",
         quote="as lógicas são padrões históricos de símbolos culturais e práticas materiais socialmente constituídos, incluindo suposições, valores e crenças",
         source_refs=["p.4/L140-147", "p.4/L148-153"]),
    dict(concept="Hibridismo de lógicas",
         definition="Combinação de elementos de diferentes lógicas institucionais que forma uma nova lógica e novas práticas disseminadas no campo.",
         quote="propõe-se o hibridismo no qual as lógicas podem combinar elementos e formar uma nova lógica",
         source_refs=["p.5/L168-176", "p.19/L1056-1058"]),
    dict(concept="Institucionalização (abordagem sociológica)",
         definition="Processo no qual as expectativas da sociedade influenciam a estruturação do campo e o comportamento dos atores.",
         quote="a institucionalização refere-se ao processo no qual as expectativas da sociedade influenciam a estruturação do campo e o comportamento dos atores",
         source_refs=["p.2/L074-082"]),
    dict(concept="Tipificação ideal das lógicas da EaD",
         definition="Uso do tipo ideal weberiano para caracterizar três lógicas (educação como valor social, como mercado e como direito de todos e dever do Estado) quanto a estrutura, governança, estudante, retorno e papel da EaD.",
         quote="foi utilizada a tipificação ideal Weberiana conceituada no estudo de Fávero e Guimarães (2019)",
         source_refs=["p.6/L207-210", "p.6/L211-262", "p.7/L263-345"]),
    dict(concept="Hibridismo entre valor social, mercado e direito de todos acompanhado pelo Estado",
         definition="Resposta dos autores à questão de pesquisa: as três lógicas se combinaram e configuraram o campo da educação a distância.",
         quote="A resposta para tal pergunta encontra-se no hibridismo entre as lógicas institucionais da educação como valor social, mercado e o direito de todos acompanhado pelo Estado",
         source_refs=["p.22/L1135-1139"]),
    dict(concept="Análise axiológica",
         definition="Técnica que permite identificar os fins sociais dos normativos a partir da interpretação do conteúdo e do contexto de sua criação, aplicada nos planos vertical (hierarquia) e horizontal (modificações da LDB).",
         quote="Esta técnica permite identificar os fins sociais dos normativos a partir da interpretação do conteúdo e o contexto em que foi criado",
         source_refs=["p.8/L411-418", "p.8/L415-418", "p.9/L419-420"]),
]

METHODOLOGY = dict(
    study_type="empírico (qualitativo)",
    design="Pesquisa histórica seguida de análise documental de normativos da EaD, com codificação, análise de conteúdo e análise axiológica nos planos vertical e horizontal.",
    sample_type="normativos e documentos históricos da EaD (ABED e MEC)",
    sample_size=23,
    sector="educação superior a distância no Brasil",
    period="registros históricos desde os anos 1900; normativos e dados até 2017 (dados da pesquisa de 2020)",
    methods=["pesquisa histórica", "análise documental", "codificação", "análise de conteúdo", "análise axiológica"],
    analysis_note=("Em três momentos: composição das tipificações ideais, análise histórica e análise documental (p.6/L201-206). "
                   "Foram analisados 23 normativos, agrupados em famílias (leis, decretos, portarias, pareceres e instruções normativas), "
                   "com três ciclos de codificação no Atlas.ti que resultaram em um corpus de 281 trechos (p.7/L301-307; p.7/L309-312; p.8/L351-355). "
                   "Os trechos passaram por análise axiológica nos planos vertical e horizontal (p.8/L415-418; p.9/L419-420). "
                   "Os autores citam critérios de validade e confiabilidade de Yin (p.9/L421-425)."),
    source_refs=["p.1/L009-010", "p.6/L201-206", "p.7/L301-307", "p.8/L351-355", "p.9/L421-425"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("A EaD foi inserida no Brasil sob a lógica da educação como valor social, impulsionada por atores da sociedade que buscavam ampliar o acesso à educação.",
      "empirical",
      "a modalidade foi inserida no Brasil sob a lógica da educação como valor social",
      ["p.1/L011-015", "p.9/L437-445", "p.10/L458-464"]),
    F("A lógica de mercado esteve presente desde cedo e se fortaleceu com a política neoliberal e a LDB de 1996, com forte crescimento das organizações privadas.",
      "empirical",
      "a partir da política neoliberal de 1990 e a LDB de 1996, ocorreu o crescimento das organizações privadas que ofertam a modalidade a distância",
      ["p.12/L634-640", "p.10/L465-466", "p.11/L517-518", "p.12/L628-629"]),
    F("O mercado da EaD passou a ser dominado por grupos educacionais, em movimento de fusões, aquisições e incorporações.",
      "empirical",
      "Foi formado um mercado dominado por grupos educacionais, como a Kroton, Estácio, Laureate Brasil, Ser Educacional, Cruzeiro do Sul, Anima e a Drevy Brasil",
      ["p.14/L854-859"]),
    F("A lógica da educação como direito de todos acompanhado pelo Estado, expressa nos normativos, se combinou às lógicas de mercado e de valor social.",
      "empirical",
      "a lógica da educação como direito de todos acompanhado pelo Estado foi combinada (híbrida) com as demais lógicas institucionais da EaD (mercado e valor social)",
      ["p.15/L888-892", "p.15/L893-897"]),
    F("Os normativos permitiram a livre atuação das organizações privadas e não estabeleceram padrões coerentes de qualidade, apoiados em estrutura física e recursos humanos.",
      "empirical",
      "normativo permitiu a livre atuação das organizações privadas no ensino superior, corroborando com a lógica da educação como mercado",
      ["p.18/L1022-1028", "p.19/L1031-1032", "p.17/L972-976"]),
    F("As lógicas institucionais configuraram o campo da educação em um mercado amparado pelo poder público e legítimo na sociedade brasileira.",
      "empirical",
      "a presença das lógicas institucionais configurou o campo da educação em um mercado amparado pelo poder público e legítimo na sociedade brasileira",
      ["p.21/L1122-1124", "p.21/L1125-1131"]),
]

CONTRIBUTION = dict(
    theoretical=("Esclarece como as lógicas institucionais atuaram na configuração do campo da educação, mostrando que podem se tornar "
                 "híbridas (p.21/L1127-1128; p.22/L1159-1162), e busca explicar a origem dos mecanismos coercitivo, mimético e normativo "
                 "a partir de aspectos cognitivos e culturais (p.3/L109-117). Identifica ainda a ineficiência dos normativos para regular a "
                 "modalidade (p.22/L1162-1164)."),
    practical=("O artigo não traz seção de implicações gerenciais. Indica como contribuição a reflexão sobre a competição do mercado, o aumento "
               "da oferta e as estratégias das organizações privadas (p.4/L120-122) e a utilidade da discussão para compreender as "
               "dificuldades do ensino na Covid-19 (p.4/L122-123)."),
)
