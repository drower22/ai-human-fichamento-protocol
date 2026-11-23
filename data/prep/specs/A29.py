SUMMARY = (
    "O artigo defende que a pesquisa qualitativa adote uma visão processual de validade: a validade não "
    "deve ser produto de um único teste ou etapa, mas uma busca contínua que atravessa todas as fases da "
    "pesquisa, do desenho à publicação (p.3/L056-071; p.7-8/L282-299). Os autores revisam a validade nos "
    "estudos quantitativos — confiabilidade como estabilidade e repetibilidade dos resultados — e as "
    "propostas qualitativas: os cinco tipos de Maxwell (descritiva, interpretativa, teórica, generalização, "
    "avaliativa), a trustworthiness de Lincoln e Guba (credibilidade, transferibilidade, dependabilidade, "
    "confirmabilidade) e os cinco critérios de Paiva, Leão e Mello (triangulação, corpus, descrição densa, "
    "surpresa, feedback dos informantes) (p.5-7/L151-273). A abordagem processual é então proposta em "
    "cinco etapas recursivas (A–E), com raízes na filosofia do processo e no argumento de Morse et al. de "
    "que a validade deve ser ativamente alcançada durante a investigação, não proclamada post hoc "
    "(p.8-9/L300-370). A aplicação é ilustrada pela tese de um dos coautores sobre a cadeia produtiva do "
    "vinho — 45 entrevistas semiestruturadas, observação não-participante, imersão prévia de três meses, "
    "teste piloto, triangulação de dados e de teorias, saturação, feedback de informantes e especialistas, "
    "participação em congresso internacional e revisão por três pesquisadores independentes "
    "(p.9-11/L381-493). A validade processual, concluem, é instrumento de aprendizagem do pesquisador e "
    "guia da pesquisa — não uma camisa de força mecânica (p.12/L496-536)."
)

RESEARCH_QUESTION = (
    "O artigo declara objetivo — 'This article aims to analyze the processual aspect of validity in "
    "qualitative research' (p.3/L085-089) — e formula uma pergunta retórica explícita: 'Why should a "
    "researcher adopt a processual rather than a traditional validity approach?' (p.3/L088-089, p.4/L090-093)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.6/L212-218", "p.8/L294-299"],
      "the trustworthiness of a research study is the central aspect of the issues that are conventionally called validity and reliability",
      "O alicerce com o qual a proposta processual se alinha explicitamente."),
    V("T2", "uses", ["p.5/L170-190", "p.6/L191-208"],
      "five different types of validity: descriptive, interpretive, theoretical, generalization and evaluative",
      "Taxonomia revisada em detalhe; descritiva, interpretativa e teórica apontadas como as mais importantes."),
    V("T3", "uses", ["p.7/L284-290", "p.8/L311-318"],
      "A processual approach aims to have a temporal interconnected search for holistic explanations",
      "O conceito central proposto pelo artigo."),
    V("T4", "uses", ["p.10/L396-404", "p.8/L300-303"],
      "reliability and validity are actively attained, rather than proclaimed by external reviewers on the completion of the project",
      "A base direta da proposta: a validade construída durante a investigação, não post hoc."),
    V("T5", "uses", ["p.6/L226-234", "p.11/L471-478"],
      "triangulation makes it possible to compare and to cross-check data",
      "Critério de validade operacionalizado no estudo ilustrativo (dados e teorias)."),
    V("T6", "uses", ["p.6/L238-242", "p.11/L474-478"],
      "The researcher has continued sampling and analyzing data until no new data appear",
      "Critério aplicado com as mais de 40 entrevistas do estudo ilustrativo."),
    V("T7", "uses", ["p.6/L219-225", "p.7/L245-273"],
      "five validity criteria in qualitative research: triangulation, the construction of a research corpus, a clear, rich and detailed description",
      "A proposição brasileira discutida em detalhe, incluindo o exemplo Hawthorne para 'surpresa'."),
    V("T8", "discusses", ["p.7/L245-250", "p.6/L227-229"],
      "a dense description of the phenomenon",
      "Critério de validade e confiabilidade, não a lente interpretativa do artigo."),
    V("T9", "discusses", ["p.7/L274-290"],
      "many efforts seem to be directed toward reduction of barriers",
      "Contexto contrastado: esses esforços não discutiram a natureza distinta da validade qualitativa — a questão central."),
    V("T10", "discusses", ["p.8/L305-310", "p.11/L452-453"],
      "The critical reflexivity developed by the researcher serves as a personal strategy to alternate and oscillate between the abstract world of theory and the practical reality",
      "Fundamenta a necessidade da validade processual; não é desenvolvida como construto próprio."),
    V("T11", "uses", ["p.11/L479-489"],
      "peer-review represents one of the fundamental pillars of science",
      "Operacionalizado na ilustração: congresso internacional + três revisores independentes."),
    V("T12", "discusses", ["p.5/L141-150"],
      "new ways of researching with big data and artificial intelligence (AI) seem to promote new discussions",
      "Mencionado como desenvolvimento que traz novas discussões de validade, sem aplicação."),
    V("T13", "does_not_use", [], "",
      "Ausente: codificação é mencionada genericamente, sem a metodologia Glaser/Strauss."),
    V("T14", "does_not_use", [], "",
      "Ausente — os autores de rigor citados são Morse, Lincoln & Guba, Maxwell, Whittemore."),
    V("T15", "does_not_use", [], "",
      "Ausente — artigo metodológico, sem teoria organizacional substancial."),
]

KEY_CONCEPTS = [
    dict(concept="Validade processual",
         definition="A validade como processo contínuo e recursivo que atravessa todas as etapas da pesquisa, não como produto de um teste único ou de uma etapa isolada — construída ex ante e ex post.",
         quote="validity cannot be seen as a product or something isolated",
         source_refs=["p.8/L293-299"]),
    dict(concept="Trustworthiness",
         definition="Os critérios de Lincoln e Guba que substituem validade interna, externa, confiabilidade e objetividade na pesquisa qualitativa: credibilidade, transferibilidade, dependabilidade e confirmabilidade.",
         quote="credibility, transferability, dependability and confirmability",
         source_refs=["p.6/L212-218"]),
    dict(concept="Triangulação",
         definition="A inter-relação de informações de diferentes fontes — de dados e teórica — para cruzar e aprofundar a compreensão do fenômeno, conferindo consistência e densidade descritiva.",
         quote="triangulation makes it possible to compare and to cross-check data",
         source_refs=["p.6/L226-234"]),
    dict(concept="Saturação de dados",
         definition="A continuação da amostragem e análise até que nenhum dado novo apareça e todos os conceitos estejam desenvolvidos — 'gold standard' para demonstrar a qualidade da pesquisa.",
         quote="The researcher has continued sampling and analyzing data until no new data appear",
         source_refs=["p.6/L238-242", "p.11/L474-478"]),
    dict(concept="Fluxo processual em cinco etapas (A–E)",
         definition="As etapas recursivas da construção da validade: atenção ao projeto e alinhamento tema-desenho-método (A); organização da coleta (B); codificação e estruturação de conceitos (C); análise com múltiplas fontes (D); discussão dos resultados e retorno à teoria (E).",
         quote="The goal of processual construction of validity",
         source_refs=["p.9/L338-358"]),
    dict(concept="Surpresa e feedback dos informantes",
         definition="Dois dos cinco critérios de Paiva, Leão e Mello: a salvaguarda do potencial inovador e da mudança de mentalidade cristalizada; e a 'validade comunicativa' — a auditoria regular do que o pesquisador obteve versus o que o informante quis dizer.",
         quote="Surprise is a criterion of validity in qualitative research",
         source_refs=["p.7/L251-269"]),
]

METHODOLOGY = dict(
    study_type="ensaio metodológico com ilustração empírica ('how to article')",
    design="Proposição teórico-metodológica construída sobre revisão das propostas de validade qualitativa, ilustrada pela aplicação da abordagem processual na tese de doutorado de um dos coautores sobre a cadeia produtiva do vinho",
    sample_type="a ilustração: 45 pessoas entrevistadas numa das maiores vinícolas brasileiras, com observação não-participante junto a representantes comerciais e lojista",
    sample_size=45,
    sector="ilustração: vitivinicultura (Rio Grande do Sul/Porto Alegre)",
    period="tese de 2011; imersão prévia de três meses como observador participante numa loja de vinhos",
    methods=["revisão das propostas de validade (Maxwell; Lincoln & Guba; Paiva et al.; Morse et al.)", "ilustração processual com tabela de medidas ex ante e ex post (imersão prévia, piloto, triangulação, descrição rica, feedback, exposição prolongada, saturação, evento científico, peer review)"],
    analysis_note=("Não é estudo empírico primário: o desenho é um ensaio metodológico que deriva a proposta "
                   "processual da literatura e a ilustra com as medidas de validade adotadas na tese de Hayashi "
                   "(2011) — imersão prévia de três meses, piloto em vinícola similar, triangulação de dados e de "
                   "teorias, mais de 40 entrevistas até saturação, feedback de informantes e especialistas, dois "
                   "artigos aprovados em congresso internacional e peer review por três pesquisadores "
                   "independentes (p.9-11/L381-493)."),
    source_refs=["p.3/L056-071", "p.9/L338-358", "p.9/L381-383", "p.10/L384-445", "p.11/L446-493"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("A validade difere de natureza entre quantitativo e qualitativo: nos estudos quantitativos ela é produto de testes; nos qualitativos envolve contexto, interpretação do pesquisador e construção/reflexão/reconstrução da informação — logo deve ser processual.",
      "proposition",
      "Validity is not in any simple sense a unitary concept",
      ["p.7/L282-290", "p.8/L291-299"]),
    F("A literatura oferece múltiplas propostas — 17 termos diferentes (Dellinger e Leech), cinco tipos de Maxwell, trustworthiness de Lincoln e Guba, cinco critérios de Paiva et al. — cuja variedade evidencia a importância e a necessidade de novas formas de organizar a questão.",
      "empirical",
      "found seventeen different terms related to the concept of validity",
      ["p.5/L168-172", "p.7/L270-273"]),
    F("A abordagem processual da validade organiza-se em cinco etapas recursivas (A–E) — projeto, coleta, codificação, análise, discussão/retorno à teoria — com movimento contínuo sobretudo entre B-C-D e D-E-A, e raízes na filosofia do processo, teorias sistêmicas e pós-estruturalistas.",
      "model",
      "an ongoing movement between the different steps is necessary. This process is recursive, particularly between steps B, C and D and between steps D, E and A",
      ["p.9/L338-370"]),
    F("No estudo ilustrativo, a validade foi assegurada ex ante e ex post: imersão prévia de três meses numa loja de vinhos, piloto em vinícola similar, triangulação de dados e teórica, descrição rica de campo, feedback de informantes e especialistas, exposição prolongada e saturação.",
      "empirical",
      "the researcher remained a participant observer in a wine shop for three months in order to compose a research proposal",
      ["p.10/L405-445", "p.11/L459-478"]),
    F("A fase ex post foi reforçada por participação em congresso internacional — dois artigos da tese aprovados — e por peer review de três pesquisadores independentes, cujas críticas foram discutidas até resolução.",
      "empirical",
      "peer-review represents one of the fundamental pillars of science, and reviewers can help build good practice that encourages more valid results",
      ["p.11/L479-489"]),
    F("A validade processual converte a validade em instrumento de aprendizagem do pesquisador — aproveita a tensão entre criatividade e rigor sem operar como regra mecânica — e afasta a acusação de encontrar apenas o que se quer encontrar.",
      "proposition",
      "Validity ceases to be a product that is verified only at the end using numerical tests and begins to serve as a learning instrument for the researcher himself",
      ["p.12/L503-520"]),
]

CONTRIBUTION = dict(
    theoretical=("Contribui um enquadramento da validade como processo contínuo e multicritério — não produto de teste "
                 "único — coerente com as ontologias processuais da literatura organizacional, e que desloca a "
                 "validade de verificação final para guia e instrumento de aprendizagem do pesquisador "
                 "(p.12/L496-520)."),
    practical=("Operacionaliza a proposta em cinco etapas recursivas (A–E) e uma tabela de medidas concretas por fase "
               "da pesquisa — imersão prévia, piloto, triangulações, descrição rica, feedback, exposição prolongada, "
               "saturação, evento científico e peer review — ilustradas num caso real de tese (p.9-11/L338-493)."),
    limitations=("A ilustração vem de um único estudo (a tese de um coautor), e a proposta reconhece que dificilmente "
                 "um conjunto fixo de critérios servirá a todas as abordagens qualitativas; o custo é o tempo e o "
                 "trabalho recursivo exigidos para resultados maduros (p.9/L363-365; p.12/L521-523)."),
    future_research=("Recomendam estudos mais funcionais centrados em validade — que superem sua condição de 'pequeno "
                     "complemento' ao produto final — e maior diálogo com estudos quantitativos e mistos, "
                     "enfatizando a relação entre validade e teorização no campo organizacional (p.12/L524-532)."),
)
