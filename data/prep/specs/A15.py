SUMMARY = (
    "O artigo examina a utilidade de medidas subjetivas de desempenho organizacional, obtidas de equipes de alta "
    "gestão, quando é difícil obter medidas objetivas confiáveis, como em firmas de capital fechado e unidades de "
    "negócio de conglomerados (p.2/L033-041; p.2/L062-066). Parte da premissa de que o desempenho organizacional é "
    "multidimensional e de que a pesquisa em estratégia precisa escolher um referencial conceitual e medidas "
    "acessíveis (p.2/L046-050; p.2/L059-061). Discute as dificuldades de medir o desempenho de unidades de firmas "
    "multi-indústria, como o efeito da rentabilidade do setor e a alocação de ativos e vendas, e de firmas privadas, "
    "como o acesso restrito a dados, os procedimentos contábeis variados e os créditos idiossincráticos do "
    "pesquisador (p.3/L073-097; p.3/L098-118; p.4/L121-133). O estudo testa três hipóteses sobre a correlação entre "
    "medidas subjetivas e objetivas de retorno sobre ativos e crescimento de vendas e medidas globais de desempenho "
    "(p.4/L135-147). A amostra reúne 22 fabricantes de tintas, privados e não diversificados, com entrevistas com "
    "CEOs, questionários às equipes de alta gestão (95 respostas válidas) e um questionário aos CEOs (p.4/L149-162; "
    "p.5/L165-178). Os resultados apoiam as hipóteses, com correlações de 0,611 para retorno sobre ativos e 0,694 para "
    "crescimento de vendas e seis de oito correlações significativas com medidas globais, além de alta "
    "confiabilidade entre avaliadores (0,84 a 0,87) e validade convergente com avaliadores externos "
    "(p.6/L237-246; p.7/L288-291; p.7/L299-302). Os autores afirmam que medidas subjetivas não substituem as objetivas "
    "e só devem ser usadas quando estas não estão disponíveis, e que a evidência sobre multidimensionalidade é "
    "tentativa e limitada a um setor (p.7/L304-310; p.8/L321-327; p.8/L344-353)."
)

RESEARCH_QUESTION = (
    "O artigo não enuncia uma pergunta de pesquisa; declara como objetivo avaliar a relação entre medidas subjetivas e "
    "objetivas de retorno sobre ativos e crescimento de vendas e entre essas medidas e medidas globais de desempenho "
    "(p.4/L135-139), formalizada em três hipóteses (p.4/L141-147). Reconstruída como pergunta implícita: medidas "
    "subjetivas de desempenho obtidas de equipes de alta gestão correspondem a medidas objetivas e globais, a ponto de "
    "serem úteis quando faltam dados objetivos (p.2/L038-041)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.2/L059-066", "p.8/L328-346"],
      "Regardless of the framework chosen to conceptualize OP, it is apparent that OP is a complex and multidimensional phenomenon",
      "A multidimensionalidade do desempenho justifica o uso de medidas globais e subjetivas ao lado das econômicas."),
    V("T2", "does_not_use", [],
      "",
      "A teoria da contingência não é mencionada; Lawrence e Lorsch (1967) aparecem só como fonte de um item do questionário (p.5/L210-212)."),
    V("T3", "discusses", ["p.2/L051-058", "p.8/L328-331"],
      "Ford and Schellenberg (1982) recently examined three major frameworks frequently used to conceptualize OP",
      "Descreve as abordagens de metas, de recursos sistêmicos e de constituintes, sem adotar uma delas."),
    V("T4", "discusses", ["p.3/L077-088"],
      "the profitability of the industry within which a firm competes is a significant predictor of firm profitability",
      "Explica por que comparar firmas sem controlar a rentabilidade do setor confunde efeitos; motiva a comparação com firmas semelhantes."),
    V("T5", "does_not_use", [],
      "",
      "A teoria da agência não é mencionada."),
    V("T6", "discusses", ["p.4/L128-133"],
      "Hollander's (1974) notion of 'idiosyncratic credits' is applicable to privately-held firm research",
      "Usada para explicar o custo de pedir dados sensíveis a donos de firmas privadas."),
    V("T7", "discusses", ["p.6/L228-234"],
      "a primary advantage of this measure lies in its implicit incorporation of aspiration levels. If aspirations are used to guide actions, Kirchhoff (1979) asserts that the actual results of these actions should be measured relative to the desired results",
      "Aspirações são citadas para justificar a vantagem da medida global do CEO."),
    V("T8", "discusses", ["p.3/L080-083"],
      "if comparisons are made across firms without controlling for industry profitability, the effects of intraindustry and interindustry variation (Beard and Dess, 1981), or alternatively, business-level and corporate-level strategy (Hofer and Schendel, 1978), on performance indicators are confounded",
      "Níveis de estratégia aparecem no argumento sobre efeitos confundidos no desempenho."),
    V("T9", "uses", ["p.4/L153-162"],
      "Members of the TMT were those individuals identified as being most influential in the strategic decisions made by the firm",
      "As equipes de alta gestão são a fonte dos dados subjetivos e sua composição é definida por influência nas decisões estratégicas."),
    V("T10", "does_not_use", [],
      "",
      "A teoria normativa aparece em uma frase de justificativa (p.2/L046-048), sem desenvolvimento."),
    V("T11", "does_not_use", [],
      "",
      "A relação organização-ambiente aparece apenas na justificativa da medida de crescimento de vendas (p.5/L184-187), sem desenvolvimento teórico."),
]

KEY_CONCEPTS = [
    dict(concept="Desempenho organizacional multidimensional",
         definition="Fenômeno complexo, que pode ser conceituado por abordagens de metas, de recursos sistêmicos e de constituintes, e cuja operacionalização é difícil, mesmo nas dimensões econômicas.",
         quote="Regardless of the framework chosen to conceptualize OP, it is apparent that OP is a complex and multidimensional phenomenon",
         source_refs=["p.2/L051-066"]),
    dict(concept="Medidas subjetivas de desempenho",
         definition="Percepções de membros da equipe de alta gestão sobre o desempenho da firma em relação a firmas semelhantes, usadas quando faltam medidas objetivas precisas.",
         quote="This paper examines the usefulness of subjective performance measures, obtained from top management teams, when problems are encountered in obtaining accurate performance data",
         source_refs=["p.2/L033-041", "p.5/L192-206"]),
    dict(concept="Medidas globais de desempenho",
         definition="Avaliações gerais do desempenho da firma, uma pela equipe de alta gestão (OVERPERF) e outra pelo CEO (SUBJCEOP), que incorporam dimensões não econômicas.",
         quote="The research used both subjective and 'self-reported' objective measures of return on assets and growth in sales as well as two measures of what may be considered overall or 'global' organizational performance",
         source_refs=["p.5/L188-191", "p.6/L222-234"]),
    dict(concept="Créditos idiossincráticos",
         definition="Capital de confiança que o pesquisador acumula com o dono da firma por conhecimento, interesse e conformidade às suas normas, e que 'gasta' ao pedir tempo e informações específicas.",
         quote="Hollander's (1974) notion of 'idiosyncratic credits' is applicable to privately-held firm research",
         source_refs=["p.4/L128-133"]),
    dict(concept="Confiabilidade entre avaliadores e validade convergente",
         definition="Os dados são considerados confiáveis quando há mais variabilidade entre firmas que entre avaliadores dentro de cada firma (correlação intraclasse); a validade convergente foi checada com avaliações externas.",
         quote="the data are considered reliable to the extent that there is more variability among raters across firms than variability among raters within firms",
         source_refs=["p.7/L281-291", "p.7/L292-302"]),
]

METHODOLOGY = dict(
    study_type="empírico (quantitativo)",
    design="Levantamento em três fases (entrevistas com CEOs, questionário às equipes de alta gestão e questionário aos CEOs) para testar a correlação entre medidas subjetivas, objetivas autorrelatadas e globais de desempenho.",
    sample_type="fabricantes de tintas privados e não diversificados; equipes de alta gestão e CEOs",
    sample_size=22,
    sector="tintas e produtos afins (SIC 2851)",
    period="dados objetivos de desempenho de 1975 a 1979",
    methods=["entrevistas com CEOs", "questionários", "correlação", "análise de variância e correlação intraclasse", "validação convergente com avaliadores externos"],
    analysis_note=("Foram contatadas 26 empresas, 24 aceitaram entrevistas com o CEO e 22 participaram da segunda fase; de 102 questionários às "
                   "equipes de alta gestão, 95 foram válidos (93,1%), e 18 CEOs responderam ao questionário final (p.4/L149-152; p.5/L174-178). "
                   "As medidas subjetivas usaram escalas de cinco pontos comparando a firma a pares (p.5/L192-206), e os dados objetivos "
                   "foram autorrelatados pelos CEOs (p.5/L207-210). A confiabilidade foi avaliada por ANOVA com correlação intraclasse e a "
                   "validade convergente por três membros de um comitê da associação do setor (p.7/L281-302)."),
    source_refs=["p.4/L149-162", "p.5/L165-178", "p.5/L192-210", "p.7/L281-302"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("Houve correlação positiva e significativa entre medidas objetivas e subjetivas de retorno sobre ativos (r = 0,611).",
      "empirical",
      "The first hypothesis, relating objective and subjective measures of return on assets (OBJATROA) with (SUBATROA), was strongly supported; the correlation coefficient (r= 0.611) was significant at a p<0.01 level",
      ["p.6/L237-241", "p.6/L248-261"]),
    F("Houve correlação ainda mais forte entre medidas objetivas e subjetivas de crescimento de vendas (r = 0,694).",
      "empirical",
      "The second hypothesis, relating objective and subjective measures of growth in sales (OBJSALES with SUBSALES), received even stronger empirical support (r= 0.694, n = 18, p<0.001)",
      ["p.6/L239-241"]),
    F("Seis das oito correlações entre as medidas globais e as quatro medidas econômicas foram significativas a pelo menos 5%.",
      "empirical",
      "Overall, six of the eight correlation coefficients between the two global measures and the four measures of economic performance attained a level of statistical significance of at least p < 0.05",
      ["p.6/L241-246"]),
    F("A confiabilidade entre avaliadores das medidas subjetivas foi alta, com correlações intraclasse de 0,84 a 0,87.",
      "empirical",
      "there were very high intraclass correlation coefficients (ranging from 0.84 to 0.87) for each of these measures",
      ["p.7/L288-291", "p.7/L265-280"]),
    F("A validade convergente das medidas subjetivas recebeu apoio adicional de avaliadores externos, apesar da amostra pequena (n = 8).",
      "empirical",
      "Despite the small sample (n = 8), these findings lend additional support to the convergent validity of these subjective measures",
      ["p.7/L292-302"]),
    F("Medidas subjetivas podem ser usadas para retorno sobre ativos e crescimento de vendas quando as objetivas não estão disponíveis e a alternativa seria excluir o desempenho do desenho, sem serem substitutas intercambiáveis.",
      "proposition",
      "this finding suggests that a researcher might consider using a subjective perceptual measure of at least two aspects of organizational performance (return on assets and growth in sales) under two specific conditions: (1) accurate objective measures are unavailable, and (2) the alternative is to remove the consideration of performance from the research design",
      ["p.8/L321-327", "p.7/L304-310"]),
    F("Medidas subjetivas globais podem ser úteis para operacionalizar dimensões não econômicas do desempenho, mas essa interpretação é tentativa.",
      "proposition",
      "subjective measures may be useful in attempting to operationalize broader, non-economic dimensions of OP",
      ["p.8/L333-346"]),
]

CONTRIBUTION = dict(
    theoretical=("Oferece evidência de que medidas subjetivas de desempenho de equipes de alta gestão se correlacionam com medidas objetivas e globais, "
                 "com boa confiabilidade e validade convergente, e sugere que podem ajudar a operacionalizar a multidimensionalidade do "
                 "desempenho (p.8/L314-346). Os autores ressalvam que o estudo se limita a uma indústria e recomendam replicação com firmas de "
                 "capital aberto (p.8/L347-353)."),
    practical=("O artigo não traz seção de implicações gerenciais; as implicações são metodológicas, para pesquisadores que não conseguem dados "
               "objetivos de firmas privadas e unidades de conglomerados (p.8/L321-327)."),
)
