SUMMARY = (
    "O artigo apresenta elementos essenciais da observação participante, seus benefícios, dificuldades e desafios de "
    "adoção em estudos de Administração da Informação (AI) no Brasil, onde seu uso ainda é incipiente "
    "(p.1/L019-024; p.2/L114-118). Parte do crescimento das pesquisas qualitativas e do deslocamento da AI do "
    "tecnológico para o gerencial, o organizacional e o social, que pede abordagens interpretativas e críticas "
    "(p.2/L073-081; p.3/L193-205). Define a observação participante, ligada à etnografia, apresenta seus três tipos "
    "(periférica, ativa e completa) e discute críticas como a perda de objetividade e a não generalização "
    "(p.3/L239-261; p.4/L322-324; p.4/L299-312; p.4/L357-367). O método combina duas fontes: a revisão de 273 artigos de "
    "12 periódicos nacionais de Administração publicados de 2000 a 2010, dos quais apenas cinco (1,8%) usaram "
    "observação participante, e a análise de uma experiência de 12 meses de um dos autores, em um estudo de caso único "
    "e revelador sobre alinhamento estratégico entre negócio e TI em uma empresa de nome fictício, TESLA "
    "(p.2/L144-166; p.3/L170-191; p.6/L598-599; p.7/L735-749; p.7/L772-779). Os cinco artigos descrevem pouco o "
    "método, e nenhum detalha o papel do observador, mas mostram ganhos como captar engajamento e frustrações "
    "(p.6/L646-652; p.6/L702-706; p.7/L707-711). A experiência mostrou benefícios, como acessar conhecimentos tácitos e "
    "pontos de vista informais, e dificuldades, como a demora de seis meses até a reunião que viabilizou a pesquisa, a "
    "definição do papel, a aceitação, a objetividade e o tempo (p.8/L808-854; p.8/L877-882; p.8/L893-902; "
    "p.9/L903-941; p.9/L952-973; p.10/L1005-1009). O artigo propõe ações com base em seis elementos: liberdade de "
    "movimentação, acesso, relacionamento, confiabilidade, especificidade e objetividade (p.11/L1166-1173; "
    "p.11/L1174-1204; p.12/L1208-1251)."
)

RESEARCH_QUESTION = (
    "O artigo não enuncia uma pergunta de pesquisa; declara como objetivo identificar e discutir os principais "
    "benefícios, fragilidades e dificuldades da adoção da observação participante em estudos de AI (p.2/L114-118). "
    "A pergunta citada no texto, sobre a dimensão social no alinhamento estratégico, pertence ao estudo de caso usado "
    "como experiência (p.7/L737-740). Reconstruída como pergunta implícita: que benefícios, fragilidades e "
    "dificuldades a observação participante traz à pesquisa em AI no Brasil e como superá-las (p.2/L114-118; "
    "p.11/L1163-1166)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.2/L114-121", "p.3/L239-242"],
      "o objetivo deste estudo é identificar e discutir os principais benefícios, as fragilidades e as dificuldades verificados com a adoção da observação participante",
      "Método que é objeto do artigo; descrito como principal ferramenta operacional da etnografia."),
    V("T2", "uses", ["p.4/L322-324", "p.4/L272-290", "p.8/L893-902"],
      "Adler e Adler (1987) dividem a observação participante em três categorias – periférica, ativa e completa",
      "A tipologia de Adler e Adler (Quadro 1) é usada para classificar o papel do pesquisador na experiência (observação completa)."),
    V("T3", "does_not_use", [],
      "",
      "A teoria ator-rede não é mencionada; aparece apenas um título de referência com 'actor' (p.13/L1291)."),
    V("T4", "uses", ["p.11/L1166-1173"],
      "Esses elementos teóricos são: a liberdade de movimentação do pesquisador na organização; o acesso a informações relevantes para o estudo; a construção de relacionamento com os informantes; a confiabilidade da coleta e análise das informações; a atenção com a especificidade do conhecimento e a objetividade do pesquisador",
      "Os seis elementos, adaptados de Johnson et al. (2006), organizam a síntese de desafios e ações."),
    V("T5", "uses", ["p.11/L1111-1135"],
      "a confiabilidade na observação participante caracteriza-se pelo grau em que os achados independem de circunstâncias acidentais",
      "Confiabilidade e validade são discutidas com Angrosino e Kirk e Miller e ligadas aos procedimentos da experiência."),
    V("T6", "discusses", ["p.3/L193-205"],
      "requer abordagens epistemológicas, como a interpretativa e a crítica, em contraponto à positivista, e metodologias de pesquisa qualitativas em substituição às quantitativas",
      "Posiciona a observação participante entre abordagens interpretativa e crítica, em contraste com a positivista."),
    V("T7", "discusses", ["p.3/L206-217", "p.2/L087-091"],
      "As metodologias qualitativas, conforme Strauss e Corbin (2008), têm como principais contribuições: (i) a necessidade de sair a campo para descobrir o que está acontecendo",
      "Metodologias qualitativas, incluindo a grounded theory, são apresentadas como contexto da observação participante."),
    V("T8", "does_not_use", [],
      "",
      "A fenomenologia aparece apenas em uma lista de metodologias pouco usadas em AI (p.5/L494-495)."),
    V("T9", "uses", ["p.7/L781-787"],
      "O estudo de caso, caracterizado como caso único e revelador, é adequado às pesquisas em AI quando se busca o entendimento de interações complexas e ambíguas entre organizações, tecnologias e pessoas",
      "O desenho da experiência relatada é um estudo de caso único e revelador."),
    V("T10", "discusses", ["p.7/L735-749"],
      "A experiência vivenciada com a observação participante envolveu o estudo da dimensão social no processo de alinhamento estratégico entre negócio e TI",
      "É o tema da experiência usada para ilustrar a observação participante, não o foco teórico do artigo."),
    V("T11", "does_not_use", [],
      "",
      "O drifting aparece em um item da lista de benefícios, com definição de Ciborra (p.8/L838-843), sem desenvolvimento."),
    V("T12", "does_not_use", [],
      "",
      "'Práticas e práxis estratégicas' aparece em um item da lista de benefícios (p.8/L836-837) e no título da tese de Abib (p.13/L1279-1280), sem desenvolvimento."),
    V("T13", "does_not_use", [],
      "",
      "A dualidade da tecnologia aparece só como citação de Orlikowski (1992) (p.3/L195-196) e em referência (p.13/L1373)."),
]

KEY_CONCEPTS = [
    dict(concept="Observação participante",
         definition="Estratégia de pesquisa em que observador e observados interagem no ambiente de trabalho destes, com aprendizado pelo envolvimento nas atividades cotidianas; os observados são vistos como sujeitos que contribuem para o estudo.",
         quote="Angrosino (2009), por sua vez, caracteriza a observação participante como um processo de aprendizagem pelo envolvimento nas atividades cotidianas de quem participa da pesquisa",
         source_refs=["p.3/L252-261", "p.4/L263-268"]),
    dict(concept="Tipos de observação participante (periférica, ativa e completa)",
         definition="Três categorias de Adler e Adler: periférica, de posição marginal e pouco comprometida; ativa, de papel mais central e funcional; completa, por oportunidade ou por conversão.",
         quote="Adler e Adler (1987) dividem a observação participante em três categorias – periférica, ativa e completa",
         source_refs=["p.4/L322-324", "p.4/L272-290"]),
    dict(concept="Participação natural e artificial",
         definition="Na natural o observador já faz parte do grupo e deve cuidar da pluralidade de visões e da capacidade crítica; na artificial ele se junta ao grupo para pesquisar e precisa de aceitação e legitimação.",
         quote="A participação resulta de um processo natural ou artificial",
         source_refs=["p.4/L291-298"]),
    dict(concept="Confiabilidade e validade na observação participante",
         definition="Confiabilidade é o grau em que os achados independem de circunstâncias acidentais; validade é o grau em que as informações são interpretadas corretamente e críveis para observados e leitores.",
         quote="a confiabilidade na observação participante caracteriza-se pelo grau em que os achados independem de circunstâncias acidentais",
         source_refs=["p.11/L1111-1127"]),
    dict(concept="Objetividade do pesquisador",
         definition="Compromisso com a exposição sistemática das ideias e do conhecimento adquirido para que sejam criticados e complementados, e não neutralidade.",
         quote="A objetividade do pesquisador (em vez da neutralidade muitas vezes mencionada) resulta do seu comprometimento com as atividades de campo e da transparência das suas ações",
         source_refs=["p.12/L1236-1244"]),
]

METHODOLOGY = dict(
    study_type="empírico (qualitativo)",
    design="Revisão de artigos nacionais de AI que usaram observação participante, somada à análise de uma experiência de observação participante em estudo de caso único e revelador.",
    sample_type="273 artigos de 12 periódicos nacionais (cinco com observação participante) e uma experiência de 12 meses em uma empresa de energia renovável",
    sample_size=273,
    sector="administração da informação (artigos); energia renovável (experiência relatada)",
    period="artigos publicados de 2000 a 2010; 12 meses de campo na experiência relatada",
    methods=["revisão da literatura", "classificação de artigos", "estudo de caso único", "observação participante", "análise de conteúdo categórica"],
    analysis_note=("Os autores analisaram 273 artigos de 12 periódicos A1, A2, B1 e B2 no período 2000-2010 (p.2/L150-166), leram resumos e "
                   "seções de metodologia, criaram uma base de classificação e analisaram em profundidade os artigos com observação "
                   "participante, com segunda análise três meses depois (p.3/L170-184). A experiência foi um estudo de caso de 12 meses, "
                   "com 29 reuniões e 79 páginas de notas (p.7/L772-799), complementada por entrevistas e análise de documentos "
                   "(p.8/L858-865) e analisada por análise de conteúdo categórica (p.9/L993-998)."),
    source_refs=["p.2/L143-166", "p.3/L170-191", "p.7/L772-799", "p.9/L993-998"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("Apenas cinco dos 273 artigos de AI da última década (1,8%) adotaram a observação participante como estratégia de coleta de dados.",
      "empirical",
      "Na amostra pesquisada, apenas cinco artigos (1,8% dos artigos publicados em AI na última década) adotaram a",
      ["p.6/L598-599", "p.6/L658-661"]),
    F("Os artigos que usaram observação participante descrevem pouco o método e nenhum detalha o papel do observador.",
      "empirical",
      "Alguns artigos mencionaram que, além das entrevistas ou questionários, adotaram a observação para coletar dados, mas não apresentaram detalhes",
      ["p.6/L646-652", "p.6/L697-701"]),
    F("A observação participante permitiu captar aspectos individuais, como engajamento e frustrações, e uma compreensão mais detalhada do fenômeno.",
      "empirical",
      "O foco no nível micro traz como benefício uma compreensão mais detalhada do fenômeno, enriquecendo o entendimento do todo",
      ["p.6/L702-706", "p.7/L707-711"]),
    F("Na experiência vivenciada, a observação participante facilitou a compreensão de aspectos sociais ligados a conhecimentos tácitos e pontos de vista informais, que entrevistas e questionários não explicitam.",
      "empirical",
      "A observação participante facilitou a compreensão de aspectos sociais que resultaram de conhecimentos tácitos e pontos de vista informais raramente exteriorizados, não explicitados em entrevistas e tampouco em questionários",
      ["p.8/L808-854"]),
    F("Entrar no campo, definir o papel do pesquisador e ser aceito e legitimado pelo grupo foram dificuldades da experiência, com meses de espera para a primeira reunião formal.",
      "empirical",
      "O contato direto com a presidência resultou numa demora de quatro meses para se agendar uma reunião presencial",
      ["p.8/L871-887", "p.8/L893-902", "p.9/L914-920"]),
    F("Há uma síntese de ações para adotar a observação participante em AI: tratar a entrada no nível estratégico e formalizar o papel, entregar relatório executivo, preferir não gravar, usar protocolo e base de dados e planejar o tempo.",
      "proposition",
      "Sugere-se, por isso, que a entrada do pesquisador no campo seja tratada no nível estratégico da organização e que seu papel e as expectativas sejam formalizados por ambas as partes",
      ["p.11/L1174-1184", "p.11/L1192-1204", "p.12/L1216-1222", "p.10/L1005-1009"]),
    F("Apesar da limitação da influência da visão pessoal do pesquisador, os benefícios da observação participante justificam seu uso em pesquisas de AI.",
      "proposition",
      "Uma importante limitação dos estudos que adotam a observação participante decorre da influência da visão pessoal dos pesquisadores nos resultados, contudo os benefícios potenciais proporcionados pela metodologia para as pesquisas de AI",
      ["p.12/L1265-1277"]),
]

CONTRIBUTION = dict(
    theoretical=("Contribui para o conhecimento sobre métodos qualitativos e, em especial, sobre a observação participante em AI, ao "
                 "sistematizar elementos do método, benefícios, fragilidades e dificuldades (p.2/L128-133; p.1/L019-024). Organiza seis "
                 "elementos de rigor da observação participante a partir de Johnson et al. (2006) (p.11/L1166-1173) e espera estimular "
                 "pesquisas qualitativas longitudinais no Brasil (p.12/L1272-1277)."),
    practical=("Dirige-se a pesquisadores de AI e oferece sugestões práticas de entrada no campo, papel do pesquisador, registro de notas "
               "e protocolo (p.11/L1174-1205; p.12/L1206-1235). Não traz implicações gerenciais para organizações."),
)
