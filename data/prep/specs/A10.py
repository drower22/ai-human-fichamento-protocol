SUMMARY = (
    "O artigo investiga a constituição da identidade de professores de pós-graduação stricto sensu em uma universidade "
    "pública e uma privada, a partir das relações de poder e dos papéis nas organizações (p.1/L010-012; p.2/L078-082). "
    "O referencial combina identidade e identificação, com a Teoria da Identidade Social e a Autocategorização, papéis "
    "sociais e a metáfora dramatúrgica de Goffman, socialização em Berger e Luckmann e as dimensões de espaço, tempo e "
    "poder (p.2/L071-077; p.3/L108-125; p.4/L164-176; p.5/L219-227; p.6/L244-268). A pesquisa é qualitativa, um estudo "
    "de casos múltiplos com entrevistas semiestruturadas com 15 professores de dois cursos de engenharia, conduzidas de "
    "julho a setembro de 2014 e analisadas por análise de conteúdo categorial no ATLAS.ti (p.6/L272-277; p.7/L285-301; "
    "p.7/L326-334). Os resultados mostram que a identidade docente é permeada por significados da socialização ao "
    "longo da trajetória acadêmica: a escolha da carreira e os sentidos do ensino e da pesquisa foram construídos na "
    "interação com professores, orientadores e alunos, que atuam como figuras identificatórias (p.8/L355-368; "
    "p.12/L536-539). Os professores se identificam com a instituição, que chegam a ver como extensão de si "
    "(p.9/L395-400). Há proximidade com os alunos e separação entre o social e o profissional na relação com os pares "
    "(p.10/L455-458). Os múltiplos papéis, em especial o administrativo, tido como secundário, e as exigências de "
    "publicação geram angústia, e o tempo, heterogêneo, extrapola o espaço da universidade e invade outras esferas da "
    "vida (p.10/L459-468; p.11/L513-517; p.12/L544-550). O espaço de trabalho é visto como uma conquista "
    "(p.11/L483-499). Os aspectos foram convergentes nas duas instituições e não houve evidência de resistência "
    "(p.12/L565-568)."
)

RESEARCH_QUESTION = (
    "O artigo não enuncia uma pergunta de pesquisa formal; declara como objetivo compreender a constituição da "
    "identidade de professores de pós-graduação de duas instituições, uma pública e uma privada, com base nas relações "
    "de poder e nos papéis organizacionais (p.2/L078-082). Reconstruída como pergunta implícita: como esses professores "
    "constituem sua identidade, considerando socialização, papéis, espaço, tempo e poder (p.3/L098-103; p.9/L403-407)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.2/L071-077", "p.7/L303-311"],
      "identity is understood through processes of socialization",
      "Identidade e identificação são as categorias centrais de análise."),
    V("T2", "uses", ["p.4/L164-176", "p.12/L539-541"],
      "the Theory of Social Identity (TSI) stands out",
      "As dimensões cognitiva, afetiva e avaliativa da TSI e da autocategorização guiam a análise da identificação."),
    V("T3", "uses", ["p.3/L111-125"],
      "Based on the definition of roles proposed by Goffman (2011), it is possible to understand social life as a dramaturgical metaphor, which develops through face-to-face interactions",
      "Goffman fundamenta a noção de papéis e a análise das interações."),
    V("T4", "does_not_use", [],
      "",
      "O termo 'institucional' não aparece como teoria; 'instituições' refere-se às universidades."),
    V("T5", "uses", ["p.3/L108-110", "p.12/L536-539"],
      "The processes of socialization make it possible to understand the way in which individuals in the social field interact and share meanings, shaping themselves and the world through the relationship with the other",
      "A socialização (Berger e Luckmann) sustenta a explicação da identidade docente."),
    V("T6", "uses", ["p.6/L244-261", "p.11/L494-517"],
      "not only the spaces but also the organizational culture can be understood as an instrument of power",
      "Espaço, tempo e poder estruturam a análise das relações dos professores com a instituição."),
    V("T7", "does_not_use", [],
      "",
      "Bourdieu não é mencionado."),
    V("T8", "discusses", ["p.6/L244-250"],
      "not only the spaces but also the organizational culture can be understood as an instrument of power",
      "A cultura como instrumento de poder é apresentada em um parágrafo do referencial, sem ser retomada na análise."),
    V("T9", "uses", ["p.4/L150-154"],
      "refers to an understanding of the organization as a collective entity (macro)",
      "Distingue identidade organizacional (macro) de identidade em organizações, e adota a segunda."),
    V("T10", "uses", ["p.3/L126-129"],
      "identities organize meanings, while roles organize functions",
      "A relação entre identidade e papéis é a base da contribuição declarada (p.12/L530-531)."),
    V("T11", "does_not_use", [],
      "",
      "Weick (1995) é citado uma vez, para a construção de significados dos papéis (p.3/L115-117), sem desenvolver o sensemaking."),
    V("T12", "does_not_use", [],
      "",
      "Taylor, Fayol, Mayo e Barnard aparecem em uma citação de abertura, para indicar que a relação indivíduo-organização não é nova (p.2/L065-067)."),
]

KEY_CONCEPTS = [
    dict(concept="Identidade",
         definition="Construção social por processos de socialização, com sujeitos reflexivos que buscam autorreferência em suas experiências, baseada na identificação com a organização e seus grupos.",
         quote="Identity is based on processes of identification of the subject with the organization and the groups that are part of it",
         source_refs=["p.7/L303-307", "p.2/L072-077"]),
    dict(concept="Identificação",
         definition="Processo social construído na interação e nas experiências em um contexto, que se manifesta no sentido de pertencimento e no vínculo afetivo e comporta dimensões afetiva, cognitiva e avaliativa.",
         quote="Identification: the social process built over the interaction and experiences lived by individuals in a specific context",
         source_refs=["p.7/L309-311", "p.4/L167-176"]),
    dict(concept="Papéis sociais",
         definition="Funções sociais que os indivíduos exercem socialmente e nas organizações, observadas na forma como dão sentido a significados compartilhados e transmitem uma imagem na interação face a face.",
         quote="Roles: social functions individuals perform socially and within the organizations",
         source_refs=["p.7/L313-315"]),
    dict(concept="Poder multilateral, espaço e tempo",
         definition="Relações sociais expressas em ações e comportamentos no contexto organizacional, com caráter multilateral, analisadas pelas dimensões de tempo (homogêneo e heterogêneo) e espaço (material e simbólico).",
         quote="Power: social relations expressed in specific actions and behaviors in the organizational context. Power relations present a multilateral characteristic",
         source_refs=["p.7/L317-321"]),
    dict(concept="Figuras identificatórias",
         definition="Orientadores e outros professores com quem o docente estabelece vínculos sociais e afetivos ao longo da carreira e que oferecem conexões intelectuais e emocionais.",
         quote="the professor establishes social and emotional bonds with advisors and other professors, who can be understood as “identificatory figures” present in the lives of professors",
         source_refs=["p.5/L194-196", "p.8/L361-364"]),
    dict(concept="Tempo heterogêneo",
         definition="Tempo subjetivo, qualitativo e circular, vivido por professores que assumem vários papéis concorrentes e que extrapola o trabalho acadêmico para outras esferas da vida.",
         quote="the time for professors, both of the public and the private HEI are predominantly heterogeneous, because these professionals take on several roles that can compete with each other",
         source_refs=["p.11/L513-517", "p.6/L264-267"]),
]

METHODOLOGY = dict(
    study_type="empírico (qualitativo)",
    design="Estudo de casos múltiplos em duas instituições de ensino superior de uma mesma cidade, uma pública e uma privada, com dois cursos de pós-graduação em uma área da engenharia.",
    sample_type="professores de pós-graduação stricto sensu (9 de universidade pública e 6 de privada)",
    sample_size=15,
    sector="educação superior (pós-graduação stricto sensu em engenharia)",
    period="entrevistas de julho a setembro de 2014",
    methods=["estudo de casos múltiplos", "entrevistas semiestruturadas", "diário de campo", "análise de conteúdo categorial", "ATLAS.ti"],
    analysis_note=("Os cursos foram escolhidos pelo conceito Capes (nota 5), e o roteiro de entrevista foi submetido a pré-teste com 4 "
                   "professores (p.7/L285-295). Foram feitas 19 entrevistas, 4 piloto e 15 com os professores, de 20 a 45 minutos, "
                   "gravadas (p.7/L296-301). Os pesquisadores também usaram diário de campo (p.7/L322-325). As entrevistas e os documentos foram "
                   "tratados por análise de conteúdo, com a técnica categorial de Bardin e apoio do ATLAS.ti versão 7 (p.7/L326-334)."),
    source_refs=["p.2/L078-082", "p.6/L272-277", "p.7/L285-301", "p.7/L322-334"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("A escolha da carreira docente e os sentidos atribuídos a ensino e pesquisa foram construídos na interação com os próprios professores e depois com os alunos.",
      "empirical",
      "the choice for the teaching career and the meanings applied to teaching and research were built especially throughout the interaction experienced by the respondents with their own professors and then with their students in the HEI",
      ["p.12/L536-539", "p.8/L355-368"]),
    F("Os professores se identificam com a instituição nas dimensões cognitiva, afetiva e avaliativa, chegando a ver a universidade como extensão de si.",
      "empirical",
      "HEI can represent an extension of the subject",
      ["p.9/L395-400", "p.8/L377-380"]),
    F("Com os alunos há proximidade, e com os pares há separação entre as dimensões social e profissional.",
      "empirical",
      "there is a difference in the interaction of the professors with the students and the professors with their peers",
      ["p.10/L455-458", "p.10/L442-454"]),
    F("Os professores assumem múltiplos papéis, e o papel administrativo, visto como secundário, gera angústia.",
      "empirical",
      "At the same time that the professors want to develop their role as researchers, they end up assuming the administrative role, and there is a sense of anguish because interviewees consider administrative roles as secondary",
      ["p.12/L544-550", "p.10/L459-468"]),
    F("Os professores consideram o espaço de trabalho uma conquista, o que revela uma noção de territorialidade na identidade.",
      "empirical",
      "Professors consider the workspace in the HEI a “conquest”",
      ["p.11/L483-499"]),
    F("Os aspectos estudados foram convergentes nas duas instituições e não houve evidência de resistência, pois são tidos como legítimos e essenciais para a permanência na pós-graduação.",
      "empirical",
      "There was no evidence of possible resistance to such aspects, since they are issues legitimized and considered essential for the permanence of professors in advanced degree courses",
      ["p.12/L565-570"]),
]

CONTRIBUTION = dict(
    theoretical=("Contribui na interface entre identidade e papéis, ao mostrar como os atores se constituem e constituem a organização, "
                 "considerando espaço, tempo e poder (p.12/L530-533). Amplia a compreensão do trabalho de professores de pós-graduação, "
                 "em especial dos múltiplos papéis e das exigências de permanência e de publicação (p.12/L533-535)."),
    practical=("O artigo não traz seção de implicações gerenciais nem recomendações práticas explícitas."),
)
