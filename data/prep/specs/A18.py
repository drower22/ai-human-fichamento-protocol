SUMMARY = (
    "O artigo busca compreender como a estratégia torna-se uma prática social em contextos submetidos a "
    "lógicas diversas da lógica capitalista, estudando um empreendimento social do terceiro setor que atua "
    "para potencializar, pela gestão, os resultados de Escolas de Educação Especial (p.2/L017-021; "
    "p.3/L059-075). O delineamento é uma pesquisa narrativa em uma organização com acesso amplo e imersão "
    "de cinco meses (outubro/2014 a fevereiro/2015): sete entrevistas narrativas (~400 minutos), documentos "
    "e artefatos, e observação não participante (~960 minutos) de eventos do cotidiano organizacional "
    "(p.7/L253-282; p.8/L283-285; p.10/L352-401). A análise combina os cinco elementos estruturais da narrativa de Pentland "
    "com a tipologia de narrativas empreendedoras de O'Connor — histórias pessoais, genéricas e situacionais — "
    "adaptada ao contexto (p.8/L286-325). O argumento teórico articula estratégia como prática social, "
    "sensegiving e sensemaking, e os textos da estratégia como mediadores discursivos e materiais da "
    "negociação de significados (p.6/L214-228). Os resultados mostram que: (a) a narrativa dirigida aos "
    "investidores é carregada de histórias situacionais; (b) a dirigida ao público atendido é carregada de "
    "histórias genéricas; e (c) a negociação de significado assenta a legitimidade nas histórias pessoais e a "
    "plausibilidade nas genéricas e situacionais (p.15/L668-684). A conclusão é que a estratégia se torna "
    "prática social quando seus significados passam a ser compartilhados no novo contexto e orientam a práxis "
    "cotidiana — um exercício qualificado de escrita (sensegiving) e leitura (sensemaking), condicionado à "
    "negociação de regras compartilhadas do jogo de linguagem (p.17/L769-781)."
)

RESEARCH_QUESTION = (
    "O artigo enuncia perguntas específicas de pesquisa: 'a estratégia é uma prática social em qualquer "
    "contexto organizacional? As práticas a ela vinculadas são dadas em qualquer contexto organizacional? E "
    "qual é o processo de construção dessa prática como social? De que vale essa discussão compreensiva?' "
    "(p.3/L064-067), derivadas do objetivo de compreender como a estratégia torna-se uma prática social em "
    "contextos submetidos a lógicas diversas da lógica capitalista (p.3/L059-061)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.4/L120-146", "p.5/L147-178", "p.6/L214-228"],
      "as atividades (práxis), o que os sujeitos produzem, constroem e reconstroem (práticas), o strategizing, aparecem como dimensões importantes para a compreensão do fenômeno",
      "Lente principal; o modelo da Figura 1 (Fenton & Langley + Whittington/Jarzabkowski et al.) é adaptado e orienta toda a análise."),
    V("T2", "uses", ["p.5/L162-177", "p.9/L342-344", "p.17/L769-774"],
      "Esse processo de negociação – entre sensegiving e sensemaking – é que efetivamente faz surgirem os textos concretos da estratégia que são representativos do processo de strategizing",
      "O objeto explicado: como o strategizing emerge em contexto onde a estratégia não era prática social."),
    V("T3", "uses", ["p.6/L183-198", "p.11/L514-519", "p.17/L769-771"],
      "um processo, impulsionado pela violação de expectativas, que envolve o tratamento e o agrupamento das lacunas no ambiente, criando significado intersubjetivo",
      "Construto central; descreve a leitura/incorporação da estratégia pelos praticantes."),
    V("T4", "uses", ["p.6/L192-202", "p.12/L551-558", "p.15/L680-682"],
      "elemento de intencionalidade em que são empreendidos esforços por parte de alguns sujeitos para influenciar a construção de significados dos outros",
      "Construto central: a 'escrita' da estratégia pelos estrategistas; a condução estruturada do sensegiving por artefatos é argumento do próprio artigo."),
    V("T5", "uses", ["p.7/L232-252", "p.4/L140-145", "p.8/L286-293"],
      "forma narrativa é constitutiva da compreensão humana e é fundamental na construção de sentido, construção de identidade e ação propositada",
      "É ao mesmo tempo o delineamento metodológico e o fundamento teórico da mediação entre sensegiving e sensemaking."),
    V("T6", "uses", ["p.5/L162-172", "p.6/L203-213", "p.17/L778-781"],
      "Os textos da estratégia (em sua dimensão discursiva e material) aparecem como os principais mediadores",
      "Construto que costura a análise: a metodologia da organização (IDEE, ferramentas) são os textos que carregam o sensegiving."),
    V("T7", "uses", ["p.12/L559-569", "p.13/L615-623", "p.17/L776-778"],
      "a estratégia é um jogo de linguagem (Wittgenstein, 2000) jogado pelos praticantes na organização",
      "Explica a assimetria central: investidores compartilham as regras do jogo; escolas não — a prática só se instaura quando as regras são negociadas."),
    V("T8", "discusses", ["p.4/L127-129"],
      "a realidade é socialmente construída e que os sujeitos subjetivamente incorporam a dimensão objetiva, que é intersubjetivamente compartilhada",
      "Pressuposto ontológico do referencial; funda a leitura construtivista sem ser mobilizada na análise."),
    V("T9", "discusses", ["p.3/L084-091", "p.4/L129-134"],
      "Uma prática é assim o modo rotinizado como os corpos se movem, como os objetos são usados",
      "Reckwitz define o conceito-chave e Nicolini marca a não-unanimidade do campo; fundação teórica, não lente analítica."),
    V("T10", "discusses", ["p.11/L486-494"],
      "com base nas regras e recursos (Giddens, 2003) aprendidos em um contexto de formação profissional universitário",
      "Invocada para explicar a estratégia como produção dos fundadores a partir das regras e recursos da formação profissional."),
    V("T11", "discusses", ["p.4/L101-111", "p.17/L789-799"],
      "o institucionalismo organizacional trabalhe com a problemática da complexidade originada nas tensões causadas por lógicas institucionais dissonantes",
      "Literatura vizinha que define a lacuna (SAP em organizações híbridas); não é mobilizada na análise."),
    V("T12", "discusses", ["p.16/L735-740"],
      "os estrategistas assumem um papel fundamental como storytellers (corroborando com os achados de Boje, 1991; Samra-Fredericks, 2003)",
      "Corrobora o achado sobre o papel dos estrategistas; invocada na discussão, não no referencial."),
    V("T13", "does_not_use", [], "", "Investidores e atendidos são analisados como praticantes; a teoria de Freeman não é citada."),
    V("T14", "does_not_use", [], "", "O artigo fala de lógicas institucionais dissonantes (Battilana; Smets), mas não invoca DiMaggio & Powell nem isomorfismo."),
    V("T15", "does_not_use", [], "", "Tema vizinho tentador (incorporação de práticas por ensino-repetição), mas a literatura de aprendizagem organizacional não é citada."),
    V("T16", "does_not_use", [], "", "O artigo usa 'tradução' no sentido comum (traduzir a estratégia para o novo contexto, p.16/L727) e cita La Ville & Mounoud, mas nunca Latour/Callon ou a teoria ator-rede."),
]

KEY_CONCEPTS = [
    dict(concept="Estratégia como prática social",
         definition="A estratégia entendida como realização de pessoas — atividades cotidianas (práxis), produções compartilhadas (práticas) e sujeitos envolvidos (praticantes) — e não como ativo da organização.",
         quote="as atividades (práxis), o que os sujeitos produzem, constroem e reconstroem (práticas), o strategizing, aparecem como dimensões importantes para a compreensão do fenômeno",
         source_refs=["p.4/L134-137"]),
    dict(concept="Sensemaking",
         definition="Processo social, impulsionado pela violação de expectativas, de criação de significado intersubjetivo por meio de ciclos de interpretação e ação.",
         quote="um processo, impulsionado pela violação de expectativas, que envolve o tratamento e o agrupamento das lacunas no ambiente, criando significado intersubjetivo",
         source_refs=["p.6/L184-187"]),
    dict(concept="Sensegiving",
         definition="Esforço intencional de influenciar a construção de significados dos outros a partir de uma perspectiva preferencial sobre a realidade organizacional.",
         quote="elemento de intencionalidade em que são empreendidos esforços por parte de alguns sujeitos para influenciar a construção de significados dos outros",
         source_refs=["p.6/L192-195"]),
    dict(concept="Textos da estratégia",
         definition="Artefatos discursivos e materiais (planos, relatórios, ferramentas) que carregam regras e recursos das práticas e medeiam a negociação de sentido entre praticantes.",
         quote="Os textos da estratégia (em sua dimensão discursiva e material) aparecem como os principais mediadores",
         source_refs=["p.17/L778-781"]),
    dict(concept="Jogo de linguagem",
         definition="Metáfora wittgensteiniana para a estratégia como atividade regida por regras compartilhadas: praticantes só negociam sentido quando jogam o mesmo jogo de linguagem.",
         quote="a estratégia é um jogo de linguagem (Wittgenstein, 2000) jogado pelos praticantes na organização",
         source_refs=["p.12/L560-562"]),
    dict(concept="Histórias pessoais, genéricas e situacionais",
         definition="Tipologia de O'Connor para narrativas empreendedoras: histórias sobre a fundação e visão (pessoais), modelos exigidos por documentos convencionais (genéricas) e contexto fora de controle dos fundadores (situacionais).",
         quote="a narrativa desenvolvida na conversação com os investidores é carregada de histórias situacionais",
         source_refs=["p.8/L296-322", "p.15/L676-680"]),
]

METHODOLOGY = dict(
    study_type="empírico (qualitativo)",
    design="Pesquisa narrativa em estudo de caso único (organização de terceiro setor com nome fictício 'Empreendendo um Sonho'), com imersão profunda do pesquisador no campo.",
    sample_type="organização social fundada em 2008 em Curitiba/PR; fundadores, colaboradores, investidores e público atendido",
    sample_size=None,
    sector="terceiro setor / empreendimento social (apoio a Escolas de Educação Especial)",
    period="coleta entre outubro/2014 e fevereiro/2015 (5 meses)",
    methods=["entrevistas narrativas", "observação não participante (abordagem naturalística)", "análise documental e de artefatos", "análise narrativa por Pentland + tipologia de O'Connor", "mapas mentais"],
    analysis_note=("Foram realizadas 7 entrevistas narrativas (~400 minutos transcritos), coleta de documentos e artefatos e observação não "
                   "participante (~960 minutos) em eventos como Café de Boas Práticas, Voluntariado Corporativo, premiação IDEE e reuniões "
                   "estratégico-administrativas (p.7/L253-282; p.8/L283-285; p.10/L352-401). A análise usou os cinco elementos da estrutura narrativa de "
                   "Pentland (1999) — sequência temporal, atores focais, voz narrativa, padrões de referência, indicadores de conteúdo e contexto — "
                   "e a tipologia de O'Connor (2002) adaptada em histórias pessoais, genéricas e situacionais, com organização em mapas mentais "
                   "(p.8/L286-325; p.9/L338-344)."),
    source_refs=["p.7/L253-282", "p.8/L283-285", "p.8/L286-325", "p.10/L352-401"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("A narrativa desenvolvida na conversação com os investidores é carregada de histórias situacionais, articulando elementos das grandes narrativas da estratégia para convencimento do investimento.",
      "empirical",
      "a narrativa desenvolvida na conversação com os investidores é carregada de histórias situacionais e articulam elementos das grandes narrativas da estratégia, objetivando um convencimento para o investimento",
      ["p.15/L676-678", "p.15/L685-696"]),
    F("A narrativa desenvolvida na conversação com o público atendido (as escolas) é carregada de histórias genéricas, com textos e artefatos articulados no fazer cotidiano de práxis situadas.",
      "empirical",
      "a narrativa desenvolvida na conversação com o público atendido (Escolas de Educação Especial) é carregada de histórias genéricas – em que se articulam textos e artefatos – no fazer cotidiano de práxis situadas",
      ["p.15/L678-680", "p.16/L701-713"]),
    F("A negociação de significado entre os praticantes assenta a legitimidade nas histórias pessoais e a plausibilidade nas histórias genéricas (atendidos) e situacionais (investidores).",
      "empirical",
      "um processo narrativo de negociação de significado, cuja legitimidade está assentada nas histórias pessoais e cuja plausibilidade nas histórias genéricas (atendidos) e situacionais (investidores)",
      ["p.15/L680-684", "p.16/L714-726"]),
    F("A estratégia tornou-se prática social nas escolas quando seus significados passaram a ser compartilhados no novo espaço e a orientar as atividades cotidianas (práxis) — processo ativo de negociação, com resistência e aquiescência, não passivo.",
      "empirical",
      "a estratégia se torna uma prática social em um contexto a partir do momento em que as regras e os recursos a ela atrelados passam a orientar as atividades cotidianas nas organizações escolares",
      ["p.14/L660-663", "p.17/L769-774", "p.16/L744-750", "p.17/L751-758"]),
    F("Os estrategistas atuam como storytellers, articuladores de discursos legítimos e plausíveis na tradução da estratégia entre os dois mundos (investidores e atendidos).",
      "empirical",
      "os estrategistas assumem um papel fundamental como storytellers (corroborando com os achados de Boje, 1991; Samra-Fredericks, 2003), responsáveis por articular discursos legítimos e plausíveis na tradução da estratégia",
      ["p.16/L735-740"]),
    F("Para se tornar prática social num contexto onde não o é, a estratégia requer um exercício qualificado de escrita (sensegiving) e leitura (sensemaking), que só ocorre com sucesso quando regras compartilhadas do jogo de linguagem são negociadas.",
      "proposition",
      "para se tornar uma prática social em um contexto onde não o é, dá-se um exercício qualificado de escrita (sensegiving) e leitura (sensemaking), e que isso só ocorre com sucesso a partir do momento em que são negociadas regras compartilhadas, capazes de balizar o jogo de linguagem",
      ["p.17/L775-781"]),
]

CONTRIBUTION = dict(
    theoretical=("Explica o processo pelo qual a estratégia se torna uma prática social em contexto que lhe é estranho: um exercício de "
                 "sensegiving/sensemaking mediado por textos da estratégia, que depende da negociação de regras compartilhadas do jogo de "
                 "linguagem; e desagrega a negociação de significado em legitimidade (histórias pessoais) e plausibilidade (histórias genéricas e "
                 "situacionais) (p.17/L759-781). Responde ainda à lacuna de estudos de estratégia como prática em organizações submetidas a "
                 "lógicas não capitalistas, como os empreendimentos sociais (p.4/L101-111)."),
    practical=("Implicações gerenciais: os estrategistas assumem papel de storytellers, e a clareza discursiva somada ao domínio material-técnico "
               "empodera a tradução da estratégia e o engajamento dos praticantes (p.16/L735-743)."),
    limitations=("A opção pela pesquisa narrativa circunscrita à organização estudada deu pouca atenção ao contexto institucional do negócio; a "
                 "dimensão macro ficou limitada à tratada pela perspectiva da prática social, sem se estender ao campo do negócio "
                 "(p.17/L782-788)."),
    future_research=("Sugere pesquisas que combinem metodologias capazes de investigar conjuntamente as dimensões material e discursiva "
                     "(coconstitutivas), com discussão epistemológica consistente; e estudos sobre a institucionalização de práticas estratégicas "
                     "em novos contextos, como organizações híbridas (p.17/L789-803)."),
    source_refs=["p.16/L735-743", "p.17/L759-803"],
)
