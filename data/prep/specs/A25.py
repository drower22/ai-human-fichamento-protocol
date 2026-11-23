SUMMARY = (
    "O artigo usa a sociologia da tradução (Callon) da Teoria Ator-Rede para estudar um 'caso extremo' de "
    "participação não-humana: o novo coronavírus. A pergunta é dupla — como líderes de Brasil, Itália e "
    "Estados Unidos tentaram, num processo de tradução, tomar a voz do vírus; e como o vírus resistiu à "
    "imposição de papéis por esses atores humanos (p.2/L073-074). Com dados de pronunciamentos oficiais, "
    "entrevistas e postagens em redes sociais (jan–mai/2020), analisados temática e indutivamente sob "
    "simetria analítica, o artigo teoriza o processo de desinteressement: o atuante não-humano resiste às "
    "ofensivas de interessement e o papel atribuído nunca se estabiliza (p.5/L203-220; p.11/L615-626). "
    "Quatro movimentos dos líderes organizam os resultados — subjugação (silenciar), domesticação "
    "(controlar), acomodação (restringir) e incorporação/embodiment (re-enquadrar via guerra e forças "
    "superiores) (p.7-10/L317-607). O desinteressement difere da dissidência, do contra-alistamento e do "
    "desemaranhamento porque nenhum alinhamento jamais se alcança: a recalcitrância do vírus desordena "
    "as reivindicações de controle (p.12/L684-721). A contribuição é dobrada: elementos teóricos novos "
    "para a escassa literatura de resistência na tradução, e a 'deflação humana' como questão moral e "
    "analítica — ignorar não-humanos é ignorar nosso papel de teóricos sociais (p.12-13/L727-762)."
)

RESEARCH_QUESTION = (
    "Dupla e explícita: 'we seek to understand how the leaders of three countries (Brazil, Italy and the "
    "United States) tried, in a translation process, to take the voice of the new coronavirus; and how the "
    "virus resisted the imposition of roles by these leaders' (p.2/L073-074). O objetivo mais amplo é "
    "investigar a participação de atuantes não-humanos nos arranjos organizacionais — em particular a "
    "tentativa de tradução para lhe conferir um papel e falar em seu nome (p.2/L057-061)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.2/L077-089", "p.3/L098-099"],
      "society is composed, made, built, stabilized, maintained, (re)assembled and challenged",
      "O enquadre ontológico geral: o social como efeito de associações, não causa."),
    V("T2", "uses", ["p.3/L110-119", "p.3/L131-140", "p.4/L141-174"],
      "to translate “is to establish oneself as a spokesman”",
      "A lente analítica adotada; os quatro momentos de Callon organizam o contraponto teórico."),
    V("T3", "uses", ["p.4/L180-186", "p.12/L684-721"],
      "The roles and identity attributed to the non-human actant are annulled by its recalcitrance in maintaining its flow of action",
      "O conceito-oposição: o desinteressement é definido contra o interessement e distinguido das outras traduções 'malsucedidas'."),
    V("T4", "uses", ["p.3/L100-104", "p.5/L206-208"],
      "the term actant indicates anything that acts in the relational system",
      "O compromisso metodológico: simetria analítica sem ausência nem 'absurda', operacionalizada em três regras do desenho."),
    V("T5", "discusses", ["p.11/L674-676", "p.13/L756-762"],
      "there cannot be any theory of sociomateriality without a theory of mediated action",
      "Barad fundamenta o movimento de embodiment; a agência distribuída e o pós-humanismo fecham a discussão e a agenda."),
    V("T6", "discusses", ["p.12/L735-738"],
      "adding new theoretical elements to the few studies that deal with resistance in the translation process",
      "A literatura de poder e resistência na tradução — e da crítica da TAR — que a contribuição endereça."),
    V("T7", "discusses", ["p.3/L124-130"],
      "(i) actor-network theory, (ii) knowledge-based theory, and (iii) Scandinavian institutionalism",
      "A tipologia de Wæraas & Nielsen situa a vertente adotada; as outras duas correntes são citadas mas não mobilizadas."),
    V("T8", "uses", ["p.5/L209-214"],
      "an extreme case of non-human participation and therefore a privileged space for theorization",
      "A justificativa do desenho: o vírus desestabiliza relações antes invisíveis, expondo-as à teorização."),
    V("T9", "does_not_use", [], "",
      "Explicitamente rejeitada nos métodos: 'we do not conduct data analysis guided by structuralist methods of language' (p.5/L238-239)."),
    V("T10", "does_not_use", [], "",
      "Ausente — a 'tradução' aqui é a de Callon/TAR, não o institucionalismo escandinavo."),
    V("T11", "does_not_use", [], "",
      "A interpretação dos líderes é analisada como interessement, não como sensemaking; Weick não é citado."),
    V("T12", "does_not_use", [], "",
      "Os enunciados são tratados como ofensivas de tradução, não como frames goffmanianos."),
    V("T13", "does_not_use", [], "",
      "O fenômeno é a pandemia, mas a lente é TAR, não a literatura de gestão de crises."),
    V("T14", "does_not_use", [], "",
      "Ausente; a conformidade buscada é a do alistamento na rede, não a isomórfica."),
    V("T15", "does_not_use", [], "",
      "A metáfora de guerra pertence aos enunciados dos líderes, não a uma lente estratégica do estudo."),
]

KEY_CONCEPTS = [
    dict(concept="Atuante (actant)",
         definition="Qualquer coisa que age no sistema relacional — humano ou não-humano — adotado em sentido semiótico, não sociológico; 'ator' é o que se torna fonte de uma ação.",
         quote="the term actant indicates anything that acts in the relational system",
         source_refs=["p.3/L100-104"]),
    dict(concept="Tradução",
         definition="O processo pelo qual algumas entidades passam a representar outras — estabelecer-se como porta-voz — através dos quatro momentos de problematização, interessement, alistamento e mobilização.",
         quote="to translate “is to establish oneself as a spokesman”",
         source_refs=["p.3/L110-119", "p.3/L131-133"]),
    dict(concept="Interessement",
         definition="O segundo momento da tradução: as ofensivas pelas quais um atuante tenta convencer outros de que os benefícios que definiu para eles estão alinhados aos seus próprios — estabilizando papéis e identidades.",
         quote="the aim is to stabilize the actors’ roles",
         source_refs=["p.4/L151-162"]),
    dict(concept="Desinteressement",
         definition="O processo teorizado pelo artigo — oposto ao interessement — em que atuantes resistem às ofensivas de outros atuantes que tentam impor-lhes papéis ou identidades; o papel atribuído é anulado pela recalcitrância e nenhum alinhamento se alcança.",
         quote="the participation of the new actant has not been stabilized",
         source_refs=["p.11/L624-626", "p.12/L709-721"]),
    dict(concept="Recalcitrância e participação ativa",
         definition="Os dois polos didáticos da participação do não-humano: ser ativo — alterar planos e ações humanos na rede — e ser recalcitrante — resistir, por desinteresse, aos papéis impostos.",
         quote="(i) is active in terms of participation in the network since it even alters human plans and actions in the system, and (ii) has recalcitrance since it has resisted (out of disinterest) the roles imposed on it",
         source_refs=["p.11/L668-676"]),
    dict(concept="Simetria analítica",
         definition="O compromisso de tratar humanos e não-humanos na mesma gramática — evitando tanto a 'ausência' (análise centrada no humano) quanto a 'simetria absurda' — para acompanhar a negociação de papéis entre atuantes.",
         quote="in analytical symmetry is recognized to understand how the relationships between them are translated",
         source_refs=["p.3/L098-109", "p.5/L206-208"]),
]

METHODOLOGY = dict(
    study_type="empírico qualitativo (análise longitudinal de casos extremos múltiplos)",
    design="Estudo qualitativo de três casos extremos — Brasil, Itália e Estados Unidos, escolhidos por volume de casos, dificuldade política e contraste de contextos; a China foi incluída inicialmente e excluída por restrição de acesso ao discurso oficial. Análise temática e indutiva sob simetria analítica da TAR, com teorização conjunta (não comparada par a par) e saturação teórica como critério de corte temporal.",
    sample_type="líderes de três países tratados como porta-vozes ('micro-actors sitting on many black boxes') e seus enunciados públicos sobre o novo coronavírus",
    sample_size=3,
    sector="governo federal / gestão pública da pandemia de COVID-19",
    period="21/jan/2020 a 20/mai/2020 — do primeiro diagnóstico nos EUA à saturação teórica",
    methods=["declarações oficiais à nação (Brasil 8, Itália 19, EUA 3)", "postagens em redes sociais (230 + 138 + 237)", "entrevistas e coletivas de imprensa (11 + 17 + 53)", "análise temática indutiva orientada pela tradução TAR (sem métodos estruturalistas de linguagem)"],
    analysis_note=("Critérios explícitos: inclusão apenas de enunciados 'directly and expressly related' a novo "
                   "coronavírus/pandemia/COVID-19; análise sensível a três pontos — como os líderes buscaram "
                   "falar em nome do vírus, as mudanças de postura diante dos papéis 'interessados' e a "
                   "dimensão de ação do vírus contra as ofensivas de silenciá-lo; teorização conjunta entre "
                   "os países, não comparação par a par (p.6/L270-282)."),
    source_refs=["p.5/L202-243", "p.6/L251-282"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("O vírus, como atuante não-humano em caso extremo, desestabilizou a rede relacional: os líderes foram forçados a mudar discursos e ações, expondo tentativas de assumir autoridade sobre o 'novo entrante' — o processo de tradução fracassou.",
      "empirical",
      "the leaders tried, in multiple attempts, to speak in the name of the virus, but were forced (by the relations triggered by the virus itself), to change their discourses and the course of their actions",
      ["p.11/L616-626"]),
    F("Movimento 1 — Subjugação: tentativa de silenciar o vírus — minimizar seus efeitos, impor-lhe duração breve e manter a estabilidade da rede — alinhada à chegada do vírus em cada país.",
      "empirical",
      "a direct (not necessarily intentional) attempt to silence the virus, speak on its behalf, and maintain the relative stability of the network in question",
      ["p.7/L321-367"]),
    F("Movimento 2 — Domesticação: os líderes passam a demonstrar controle e preparo — segmentando os efeitos do vírus, reivindicando ação planejada e significando a supremacia humana — em lugar de negá-lo.",
      "empirical",
      "the leaders sought to demonstrate control over the virus, instead of denying its effects",
      ["p.8/L429-444"]),
    F("Movimento 3 — Acomodação: com a transmissão comunitária, já não é possível negar nem controlar; os líderes gerenciam os efeitos indiscutíveis, reconhecem a força do vírus e exigem mudança nos padrões de comportamento.",
      "empirical",
      "the leaders no longer can deny, minimize or have plain control (intentional and unproblematic) over the new coronavirus",
      ["p.9/L506-519"]),
    F("Movimento 4 — Incorporação (embodiment): a ação do vírus é incorporada a fenômenos extremos — 'inimigo invisível', guerra, forças divinas e sobre-humanas — para re-enquadrar sua participação e justificar posições diante da impossibilidade de contê-lo.",
      "empirical",
      "human actors began to embody the action of the virus into extreme phenomena to justify their positions, their roles and their actions",
      ["p.10/L585-600"]),
    F("O desinteressement é teorizado como mecanismo de tradução 'malsucedida' — distinto de dissidência, contra-alistamento e desemaranhamento porque nenhum alinhamento ou acordo foi alcançado para ser desfeito: a recalcitrância anula os papéis atribuídos.",
      "model",
      "the participation of the new actant has not been stabilized",
      ["p.11/L624-626", "p.12/L688-721"]),
    F("Os efeitos da participação do não-humano — 'condições infelizes' — geram trajetórias indesejadas, desconstroem narrativas lineares, mudam comportamentos sociais e destituem quem quer falar em seu nome: poder, tamanho e força não bastam, como em Davi e Golias.",
      "proposition",
      "power, size, and strength are not enough to define the designees of action",
      ["p.10/L601-607", "p.12/L722-726"]),
]

CONTRIBUTION = dict(
    theoretical=("O desinteressement adiciona elementos teóricos novos à escassa literatura de resistência "
                 "na tradução: um quarto mecanismo de tradução 'malsucedida', distinto de dissidência, "
                 "contra-alistamento e desemaranhamento por não pressupor alinhamento prévio — e a "
                 "demonstração de que o não-humano é ativo e recalcitrante sem antropomorfismo "
                 "(p.12/L684-738). O caso mobiliza os estudos organizacionais para perspectivas "
                 "processuais e pós-humanistas e torna a 'deflação humana' uma questão moral "
                 "(p.13/L756-762)."),
    practical=("A análise das quatro ofensivas — subjugar, domesticar, acomodar e incorporar — oferece um "
               "mapa dos discursos de líderes diante de atuantes não-humanos recalcitrantes e dos limites "
               "de falar em nome do que não negocia (p.7-10/L317-607)."),
    limitations=("Desenho de enunciados públicos: três países e seus líderes como porta-vozes, sem "
                 "comparação par a par; a China foi excluída por restrição de acesso ao discurso oficial; "
                 "o recorte temporal termina na saturação teórica de 20/mai/2020, antes de eventuais "
                 "convergências futuras (p.5/L222-243; p.12/L732-734)."),
    future_research=("Estudar o interessement/desinteressement do vírus em contextos que tenham traduzido "
                     "sua participação de modo a minimizar seus efeitos; e estender a análise a outros "
                     "humanos (mídia, cientistas, oportunistas) e não-humanos (testes, vacinas, dispositivos) "
                     "nos sistemas sociais afetados (p.13/L749-755)."),
    source_refs=["p.12/L727-738", "p.13/L749-762"],
)
