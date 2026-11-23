SUMMARY = (
    "O artigo combina duas tradições do institucionalismo organizacional — a teoria da tradução, atenta "
    "à interpretação e ao embebimento local, e a literatura de lógicas institucionais, atenta aos "
    "sistemas de significado de nível de campo — para entender como uma lógica se torna embebida e "
    "promulgada dentro de uma organização (p.2/L059-069). O caso é a 'media logic' em uma agência "
    "governamental sueca altamente midiatizada: uma etnografia de três meses, 19 entrevistas e "
    "documentos, organizada e codificada pelos quatro elementos de Scott — artefatos, rotinas, sistemas "
    "simbólicos e sistemas relacionais (p.7/L291-312). Os resultados mostram que a lógica da mídia fez "
    "uma 'entrada decisiva' na agência — moldando o quê, como e quando comunicar —, mas que a "
    "tradução se desdobra de forma desigual: três sistemas de valores profissionais a interpretam "
    "diferentemente — gestão/profissionais de comunicação (ferramenta estratégica de competitividade e "
    "reputação), porta-vozes e cientistas (correção científica e integridade da evidência) e líderes de "
    "projeto/gerentes médios (utilidade cívica para o contribuinte) (p.15-18/L720-938). A lógica, portanto, "
    "é reconstituída em tradução contínua: os elementos são decompostos, ganham sentidos distintos e "
    "produzem variação local — e a energia para essa variação vem dos sistemas de valores "
    "profissionais, não necessariamente de lógicas rivais (p.19-20/L1006-1051)."
)

RESEARCH_QUESTION = (
    "Duas perguntas explícitas: '1) how is the media logic translated into an organizational setting?, "
    "and 2) how is this translation shaped by existing value systems belonging to different professional "
    "groups inside the organization?' (p.3/L096-099). O propósito maior é enriquecer a concepção de "
    "como as lógicas se embebem nas organizações, teorizando o papel dos sistemas de valores "
    "profissionais nos processos de tradução local (p.2-3/L086-094)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.2/L049-058", "p.4/L141-150"],
      "sets of material practices and symbolic constructions that constitute guiding principles for organizational behaviour",
      "Metade do enquadre combinado: lógicas como estruturas de significado de campo a serem embebidas localmente."),
    V("T2", "uses", ["p.3/L120-136"],
      "a never-finalized process through which institutions are noticed, selected and given meaning as they travel across different fields and organizational contexts",
      "A outra metade: a interpretação e o embebimento local dos elementos institucionais."),
    V("T3", "discusses", ["p.3/L123-127"],
      "with their roots in the sociology of science (Callon, 1986) and later also actor network approaches",
      "Citada como genealogia da teoria da tradução — não mobilizada como lente analítica."),
    V("T4", "uses", ["p.5/L218-230", "p.6/L255-257"],
      "a set of principles that guides news journalism in promoting certain ways of ‘seeing and interpreting social affairs’",
      "A lógica institucional cujo processo de tradução o caso observa."),
    V("T5", "uses", ["p.4/L171-182", "p.7/L302-312"],
      "four distinct elements: artefacts (including objects with specifications, conventions or standards for different types of products), routines (mainly instructions, procedures, duties and scripts associated with organizational processes), symbolical systems (rules, laws, values and categories) and relational systems (systems of governance, power and authority, identities)",
      "O aparato analítico que decompõe a lógica em rotas traduzíveis e organiza a codificação dos dados."),
    V("T6", "uses", ["p.5/L195-211"],
      "different elements of logics are likely to be adopted, resisted or modified in relation to values and preferences propagated and negotiated in the organizations by different professional groups",
      "O mecanismo explicativo: sistemas de valores profissionais como 'fluid negotiations' entre jurisdições."),
    V("T7", "discusses", ["p.5/L195-201", "p.20/L1041-1049"],
      "logics do not need to be challenged by other logics",
      "Interlocução ressignificada: a variação vem de valores profissionais, não da competição entre lógicas."),
    V("T8", "discusses", ["p.16/L734-743"],
      "the media were translated and understood as a tool for the agency to strengthen and increase its competitiveness, reputation and autonomy",
      "Descreve o primeiro sistema de valores (gestão/comunicação) — enquadre interpretativo, não teoria mobilizada."),
    V("T9", "discusses", ["p.3/L112-113"],
      "not as strategic elaborators of institutional logics, but as local interpreters and translators",
      "Contrastada explicitamente: atores como intérpretes, não elaboradores estratégicos de lógicas."),
    V("T10", "does_not_use", [], "",
      "DiMaggio & Powell aparecem apenas como editores do volume que abriga Friedland & Alford — o isomorfismo não é mobilizado."),
    V("T11", "does_not_use", [], "",
      "O estudo usa 'make sense of' coloquialmente e cobre interpretação via teoria da tradução — Weick não é citado."),
    V("T12", "does_not_use", [], "",
      "Públicos aparecem como 'customers/taxpayers' e grupos-alvo, não como stakeholders teóricos."),
    V("T13", "does_not_use", [], "",
      "O termo 'principals' aparece coloquialmente ('They are our principals' = contribuintes), sem ancoragem na teoria da agência."),
    V("T14", "does_not_use", [], "",
      "A mídia é tratada como lógica institucional a ser traduzida, não como recurso de dependência externa."),
]

KEY_CONCEPTS = [
    dict(concept="Lógica institucional",
         definition="Sistema de significado de nível de campo: práticas materiais e construções simbólicas que constituem princípios orientadores da ação organizacional — aqui entendida como 'bundle' de elementos decomponíveis e traduzíveis.",
         quote="sets of material practices and symbolic constructions that constitute guiding principles for organizational behaviour",
         source_refs=["p.4/L141-150", "p.4/L166-170"]),
    dict(concept="Tradução",
         definition="O processo nunca finalizado pelo qual instituições são notadas, selecionadas e recebem sentido ao viajar entre contextos — transformando tanto o que é traduzido quanto a organização que traduz.",
         quote="a never-finalized process through which institutions are noticed, selected and given meaning as they travel across different fields and organizational contexts",
         source_refs=["p.3/L120-136"]),
    dict(concept="Lógica da mídia",
         definition="Conjunto de ideias, normas, princípios, rotinas e atividades que orienta o trabalho jornalístico — interações com fontes, produção de notícias e avaliação de noticiabilidade — e que as organizações internalizam em suas práticas.",
         quote="a set of principles that guides news journalism in promoting certain ways of ‘seeing and interpreting social affairs’",
         source_refs=["p.2/L070-085", "p.5/L218-230"]),
    dict(concept="Elementos (carriers) das lógicas",
         definition="As quatro formas de Scott pelas quais uma lógica se materializa e é decodificada — artefatos, rotinas, sistemas simbólicos e sistemas relacionais — que servem de rotas para sua entrada nos contextos organizacionais.",
         quote="four distinct elements: artefacts (including objects with specifications, conventions or standards for different types of products), routines (mainly instructions, procedures, duties and scripts associated with organizational processes), symbolical systems (rules, laws, values and categories) and relational systems (systems of governance, power and authority, identities)",
         source_refs=["p.4/L171-182"]),
    dict(concept="Sistemas de valores profissionais",
         definition="Os valores e jurisdições dos grupos profissionais dentro da organização — gestão, ciência e serviço civil — que direcionam como cada elemento da lógica é interpretado e promulgado localmente.",
         quote="interpretations and meanings shaped by professional values and assumptions",
         source_refs=["p.3/L108-113", "p.16/L758-764"]),
    dict(concept="Embebimento local (embeddedness)",
         definition="O modo como elementos de uma lógica de campo são incorporados às práticas, rotinas e valores do trabalho organizacional por meio da tradução contínua.",
         quote="to provide an understanding of institutional logics as locally embedded and enacted",
         source_refs=["p.2/L059-069", "p.20/L1015-1029"]),
]

METHODOLOGY = dict(
    study_type="empírico qualitativo (estudo de caso etnográfico)",
    design="Etnografia organizacional de estudo de caso único: uma agência governamental sueca altamente midiatizada (31ª de 238 em visibilidade, 'caso normal' sem escândalos), observada por três meses (abril–junho/2012, três dias por semana) mais uma semana na Almedalen Week (julho/2013), com notas de campo sem gravações e checagem das transcrições com os participantes.",
    sample_type="departamento de comunicação da agência e grupos profissionais envolvidos em atividades midiáticas (porta-vozes, líderes de projeto, gestores)",
    sample_size=19,
    sector="setor público (agência governamental sueca, >500 empregados)",
    period="observações abril–junho/2012 + uma semana em julho/2013; documentos e releases de abril–julho/2012",
    methods=["observação participante (semi-estruturada pelos quatro elementos de Scott)", "19 entrevistas semiestruturadas", "análise documental (42 press releases, documentos estratégicos, 10 posts de Facebook, 48 tuítes, 10 posts de blog, 3 vídeos)", "codificação por elementos de Scott e, depois, por grupos profissionais; iteração e comparação para categorias mutuamente exclusivas", "member checking das transcrições"],
    analysis_note=("Três etapas analíticas declaradas: (1) corpus codificado nos quatro elementos de Scott; "
                   "(2) material categorizado por grupo profissional para identificar padrões de "
                   "interpretação de conteúdo, forma, enquadramento e timing; (3) iteração e comparação "
                   "para categorias mutuamente exclusivas de argumentos e motivos — os três sistemas de "
                   "valores (p.8/L359-373). Limitações declaradas: sem gravações, material anonimizado e "
                   "traduzido para o inglês, com ajustes de extensão para publicação (p.8/L374-380)."),
    source_refs=["p.7/L291-327", "p.7/L328-330", "p.8/L331-349", "p.8/L359-380"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("A lógica da mídia fez uma entrada decisiva na agência — artefatos, rotinas, sistemas simbólicos e relacionais evidenciam a 'mediatização do setor público', com a mídia moldando o quê, como e quando comunicar e recebendo a maior prioridade no trabalho de comunicação.",
      "empirical",
      "the media logic influenced the agency’s communication activities, variously shaping how, what and when to communicate",
      ["p.10/L449-458", "p.15/L720-722", "p.16/L723-726"]),
    F("A tradução se dá por rotas distintas e desiguais: os artefatos carregam 'media speak' e linguagem factual; as rotinas absorvem o ritmo da mídia (reunião matinal, kits de imprensa, coaching); os valores simbólicos e relacionais reorganizam o trabalho em torno da produção de notícias e das relações com ministério, indústria e outras agências.",
      "empirical",
      "the media logic has become embedded in the practices and routines of an organization",
      ["p.3/L116-123", "p.15/L686-698"]),
    F("Gestores e profissionais de comunicação traduzem a lógica da mídia estrategicamente: a mídia como ferramenta para competitividade, reputação e autonomia — 'speak with one voice', cobertura positiva, declarações dramatúrgicas e timing alinhado ao ciclo de produção dos veículos.",
      "empirical",
      "the media were translated and understood as a tool for the agency to strengthen and increase its competitiveness, reputation and autonomy",
      ["p.16/L734-757"]),
    F("Porta-vozes e cientistas traduzem pela 'correção científica': preferência por material despojado e factual, rotinas de checagem, resistência a one-liners e simplificações — e argumento de que resultados científicos devem sair quando prontos, não quando convém à mídia.",
      "empirical",
      "releasing news material based on scientific results the moment the results were available, without any consideration of when and how often the agency wished to seek publicity",
      ["p.16/L765-772", "p.18/L914-922"]),
    F("Líderes de projeto e gerentes médios traduzem pela 'utilidade cívica': a mídia como meio de projetar informação formal, confiável e útil ao contribuinte, guiada pelas regras do governo e pelo posicionamento da agência diante de outras agências e do ministério.",
      "empirical",
      "the importance of providing trustworthy, relevant, and useful information to ‘customers’ (mainly taxpayers), in a format that was accessible and available to those most affected",
      ["p.18/L923-938"]),
    F("A lógica é reconstituída na tradução: estável no nível organizacional (a agência é de fato midiatizada), seu significado é continuamente reformulado elemento a elemento conforme os sistemas de valores mobilizados por cada grupo — produzindo ao mesmo tempo conformidade e variação.",
      "model",
      "the meaning of the media logic has been (re-)constructed in and through ongoing translation to fit the specific context and value systems available and mobilized by professionals inside the agency studied",
      ["p.20/L1004-1013", "p.20/L1027-1040"]),
    F("A variação local não requer lógicas concorrentes: sistemas de valores profissionais, localmente embebidos e contextualmente dependentes, são uma fonte alternativa de energia para traduzir, decompor e renegociar a lógica — que não adquire sentido fixo nem necessariamente se hibridiza.",
      "proposition",
      "Local, professionally embedded and contextually dependent value systems provide alternative sources of energy and mobilizing force",
      ["p.20/L1041-1051"]),
]

CONTRIBUTION = dict(
    theoretical=("Duas contribuições declaradas: (1) às lógicas institucionais — mostra como elas são "
                 "embebidas localmente por tradução contínua, propondo entendê-las como 'loosely coupled "
                 "systems consisting of several elements' que podem ser traduzidos diferentemente, e não "
                 "como entidades monolíticas (p.20/L1015-1029); (2) à teoria da tradução — teoriza o papel "
                 "dos sistemas de valores profissionais como fonte de variação, e mostra que a tradução "
                 "não requer lógicas rivais nem produz sentido fixo ou híbrido necessariamente "
                 "(p.20/L1030-1051)."),
    practical=("Ao mapear as rotas pelas quais a lógica da mídia entra na organização e os três modos "
               "profissionais de interpretá-la, o estudo oferece a gestores e comunicadores do setor "
               "público um diagnóstico das tensões internas da comunicação — entre 'speak with one voice', "
               "rigor científico e utilidade cívica — e de como elas moldam o produto midiático "
               "(p.16-18/L734-938)."),
    limitations=("Limites do desenho: caso único em agência governamental sueca — um 'caso normal' "
                 "escolhido por ser altamente midiatizado — com observações concentradas no departamento "
                 "de comunicação; sem gravações de áudio/vídeo e com material anonimizado e traduzido "
                 "para o inglês (p.6-7/L258-290; p.8/L350-380)."),
    future_research=("A conclusão abre avenida para explorar como processos de tradução se desdobram "
                     "dentro das organizações e se ligam a estruturas de significado mais amplas moldadas "
                     "por sistemas profissionais (p.20-21/L1049-1055)."),
    source_refs=["p.20/L1015-1051", "p.8/L350-380"],
)
