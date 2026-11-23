SUMMARY = (
    "O artigo examina como a interdependência entre rotinas coordena as demandas concorrentes de "
    "padronização e flexibilidade em rotinas de serviços profissionais (p.5/L412-421). O enquadre combina "
    "a visão performativa das rotinas — aspecto ostensivo versus performances concretas (Feldman e "
    "Pentland) — com a literatura sobre padrões ostensivos coexistentes (D’Adderio; Turner e Rindova) e "
    "interdependência/ecologias de rotinas (Birnholtz et al.; Howard-Grenville), além da sociologia dos "
    "serviços profissionais (Maister; Abbott) e da tipologia de interdependência de Thompson "
    "(p.3-5/L158-391). A etnografia da deal appraisal routine (DAR) no resseguro de catástrofes de "
    "propriedades nos EUA cobre 280 dias de campo, 159 observações e 24 underwriters (p.5-7/L424-563). "
    "A análise de primeira ordem reconstrói a DAR em três fases — análise técnica, análise técnica "
    "ponderada e análise de mercado — mostrando performances de padronização e customização dentro de "
    "cada tarefa; a de segunda ordem identifica quatro insights: rotinas interseccionais amplificam "
    "pressão para um ou outro padrão ostensivo, interseções são mandatórias ou discricionárias, "
    "underwriters orientam-se pelo impulso e reorientam-se para o padrão oposto, e esse equilíbrio ocorre "
    "dentro de cada tarefa — a 'reciprocal task interdependence' (p.16-18/L1916-2125). O framework "
    "resultante mostra como a skillful accomplishment sustenta a complementaridade dos dois padrões, com "
    "o rating sheet como artefato central disciplinador e os artefatos suplementares transmitindo "
    "impulsos das rotinas interseccionais (p.18-21/L2126-2451)."
)

RESEARCH_QUESTION = (
    "Explícita: 'How is routine interdependence implicated in coordinating competing demands for "
    "standardization and ﬂexibility in the context of professional service routines?' (p.5/L412-416). O "
    "puzzle é como padrões ostensivos concorrentes — consistência e flexibilidade — são equilibrados na "
    "performance de rotinas profissionais altamente customizadas (p.2/L057-084)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.3/L204-216"],
      "abstract, generalized idea of the routine",
      "O enquadre central: ostensivo/performativo como realizações esforçadas que estruturam toda a análise."),
    V("T2", "uses", ["p.3/L158-172"],
      "Competing pressures for standardization and ﬂexibility are a core tension at the heart of routine theory",
      "O puzzle teórico que a pesquisa endereça."),
    V("T3", "uses", ["p.4/L233-252"],
      "ﬁrst selectively performed one goal and then the other",
      "A literatura estendida: padrões ostensivos coexistentes e performance seletiva (D’Adderio; Turner e Rindova)."),
    V("T4", "uses", ["p.4/L304-326", "p.5/L362-391"],
      "enmeshed in far-reaching, complex, tangled webs of interdependence",
      "O conceito desenvolvido: interseções entre rotina focal e rotinas interseccionais."),
    V("T5", "uses", ["p.4/L253-271", "p.7/L634-640"],
      "the rating sheet remains a stable template from deal to deal",
      "Artefatos como representações inscritas que guiam sem determinar — rating sheet central e artefatos suplementares."),
    V("T6", "uses", ["p.18/L2108-2119"],
      "we label this professional skill in acting on and reorienting each intersecting impulse reciprocal task interdependence",
      "A tipologia de Thompson nomeia a contribuição: interdependência recíproca dentro de cada tarefa."),
    V("T7", "uses", ["p.2/L070-084"],
      "Professional services involve a high degree of customization in their work. Little, even management information, can be reliably made routine",
      "O contexto teórico empírico: por que rotinas profissionais são o caso saliente."),
    V("T8", "uses", ["p.7/L604-613", "p.21/L2440-2447"],
      "mindful activities",
      "Fundamenta a 'skillful accomplishment'; a contribuição estende a ideia de trabalho mindful rotinizado."),
    V("T9", "discusses", ["p.3/L173-190", "p.17/L1946-1955"],
      "Sequential attention thus conceptualizes standardization and ﬂexibility as separate, prioritizing either one or the other",
      "O mecanismo rival contrastado: o equilíbrio ocorre dentro de cada tarefa, não sequencialmente."),
    V("T10", "discusses", ["p.5/L395-411"],
      "occupation-speciﬁc artifacts such as these make differences in knowledge accessible to other occupations",
      "Interlocução sobre como o conhecimento das rotinas interseccionais é inscrito e trazido à rotina focal."),
    V("T11", "does_not_use", [], "",
      "'Exploration/exploitation' aparece só no contexto da atenção sequencial de Cyert e March; a ambidestria não é mobilizada."),
    V("T12", "does_not_use", [], "",
      "O conflito estudado é entre padrões ostensivos de uma rotina, não entre lógicas de campo."),
    V("T13", "does_not_use", [], "",
      "O julgamento profissional é teorizado via rotinas performativas, não via sensemaking; Weick não é citado."),
    V("T14", "does_not_use", [], "",
      "A coordenação é explicada por interdependência de rotinas e habilidade, não por ajuste contingente estrutural."),
    V("T15", "does_not_use", [], "",
      "A materialidade é tratada via artefatos performativos (D’Adderio; Leonardi), não via TAR."),
]

KEY_CONCEPTS = [
    dict(concept="Rotina (ostensivo × performativo)",
         definition="Padrão de ação mutuamente constituído pelo aspecto ostensivo — a ideia abstrata e generalizada do padrão — e pelas performances específicas de pessoas, em lugares e tempos concretos, que o trazem à existência.",
         quote="abstract, generalized idea of the routine",
         source_refs=["p.3/L207-216"]),
    dict(concept="Interdependência de rotinas",
         definition="O enredamento de uma rotina focal em teias de conexão com rotinas adjacentes e sobrepostas, que lhe injetam conhecimento e pressões por meio de interseções mandatórias ou discricionárias.",
         quote="enmeshed in far-reaching, complex, tangled webs of interdependence",
         source_refs=["p.4/L310-313", "p.7/L650-661"]),
    dict(concept="Interseções mandatórias e discricionárias",
         definition="Os pontos em que rotinas interdependentes tocam a rotina focal: mandatórias, quando o underwriter deve responder a uma passagem de bastão; discricionárias, quando ele as promulga ad hoc segundo seu julgamento sobre a saliência para a tarefa.",
         quote="called these mandatory intersects",
         source_refs=["p.7/L650-661", "p.17/L2010-2044"]),
    dict(concept="Skillful accomplishment",
         definition="A habilidade profissional de reconhecer o impulso de uma rotina interseccional, orientar-se por ele e reorientar a performance para o padrão ostensivo oposto — ação mindful que equilibra os padrões na tarefa.",
         quote="The interplay of orienting and reorienting allows them to balance customizing and standardizing performances within each task",
         source_refs=["p.7/L676-682", "p.19/L2224-2230"]),
    dict(concept="Reciprocal task interdependence",
         definition="A forma mais complexa de interdependência (Thompson) promulgada no nível da tarefa: cada impulso de uma rotina interseccional é reconhecido e reorientado no momento, gerando complementaridade entre padronização e flexibilidade dentro de cada tarefa.",
         quote="we label this professional skill in acting on and reorienting each intersecting impulse reciprocal task interdependence",
         source_refs=["p.18/L2108-2125"]),
    dict(concept="Artefatos centrais e suplementares",
         definition="O artefato central (rating sheet) disciplina e padroniza a rotina, registrando cada decisão; os artefatos suplementares (brochura de submissão, outputs modelados, notas de reunião) inscrevem o conhecimento das rotinas interseccionais e transmitem seus impulsos.",
         quote="Supplementary artifacts enable ﬂexibility by transmitting impulses from interdependent routines, even as the core artifact enables standardization",
         source_refs=["p.7/L614-640", "p.20/L2368-2371"]),
]

METHODOLOGY = dict(
    study_type="empírico qualitativo (etnografia)",
    design="Etnografia em equipe da deal appraisal routine (DAR) no resseguro de catástrofes de propriedades dos EUA, com acesso aprofundado a 11 firmas em Londres e/ou Bermuda ao longo de um ciclo anual de renovações; observações não-participantes com notas digitadas em 24h e áudio com marcadores temporais; narrativa composta representativa do padrão típico entre underwriters, firmas e períodos.",
    sample_type="24 underwriters de resseguro de propriedades dos EUA (de um total observado de 86 pessoas), mais corretores, modeladores e executivos seniores entrevistados",
    sample_size=24,
    sector="serviços financeiros — resseguro de catástrofes de propriedades (EUA), operado de Londres/Bermuda",
    period="um ciclo anual de renovações; 280 dias coletivos de campo",
    methods=["observação não-participante (159 observações de 1–4h, com áudio)", "entrevistas semiestruturadas (~1h, gravadas e transcritas)", "dados documentais (pacotes de submissão, rating sheets, gráficos)", "triangulação de fontes (Guba e Lincoln)"],
    analysis_note=("Análise em fases: códigos in vivo e rótulos descritivos em campo; fluxograma da sequência "
                   "típica de ações (Table 1); três fases empíricas (análise técnica, técnica ponderada, de "
                   "mercado); codificação de performances padronizadoras vs. customizadoras e de reperformances; "
                   "identificação de interseções mandatórias vs. discricionárias e de artefatos "
                   "suplementares; e, por fim, orientação/reorientação codificada como núcleo da habilidade "
                   "profissional (p.6-7/L558-682)."),
    source_refs=["p.6/L512-563", "p.6/L564-566", "p.7/L567-682"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("A DAR equilibra os dois padrões dentro de cada tarefa: performances padronizadoras (repopular a planilha, capturar outputs modelados, calcular taxas) e customizadoras (instruções ao modelador, pesos e loadings por julgamento) coexistem, com reperformances quando o resultado não satisfaz.",
      "empirical",
      "some activities were consistent and helped convert each deal into a recognizable output such as creating a technical rate, which we termed standardizing performances",
      ["p.7/L592-613", "p.16/L1895-1915"]),
    F("Cada interseção amplifica pressão para um padrão ostensivo: a rotina de corretagem e a de reunião com cliente orientam para customizar; a de modelagem e a de planejamento de negócios orientam para padronizar — e a mesma rotina pode amplificar pressões diferentes em estágios distintos.",
      "empirical",
      "either ampliﬁed pressure to achieve consistency or ampliﬁed pressure to retain ﬂexibility",
      ["p.17/L1968-2009"]),
    F("As interseções são mandatórias ou discricionárias: obrigatórias quando o underwriter responde a uma passagem de bastão; discricionárias quando ele as promulga ad hoc — e ambas podem ser reperformadas; sua natureza não determina a pressão, mas a habilidade em promulgá-las, sim.",
      "empirical",
      "the mandatory or discretionary nature of the intersection does not determine whether it ampliﬁes pressures toward consistency or ﬂexibility",
      ["p.17/L2010-2044"]),
    F("O underwriter reconhece o impulso da interseção e depois reorienta a performance para o padrão oposto — por exemplo, aceita o impulso padronizador dos outputs modelados e os customiza por pesos e julgamento; o rating sheet registra cada reorientação em trilha de auditoria.",
      "empirical",
      "the underwriter then reorients the performance to counteract the initial impulse and rebalance coexisting ostensive patterns within the focal routine",
      ["p.18/L2054-2090"]),
    F("O equilíbrio não é sequencial mas recíproco na tarefa: como os impulsos não alternam ordenadamente, o underwriter reequilibra cada tarefa no momento — a 'reciprocal task interdependence' que sustenta julgamento e accountability.",
      "model",
      "we label this professional skill in acting on and reorienting each intersecting impulse reciprocal task interdependence",
      ["p.18/L2091-2125"]),
    F("Os artefatos distribuem o trabalho de coordenação: artefatos suplementares transmitem os impulsos das rotinas interseccionais e viabilizam a flexibilidade; o artefato central (rating sheet) disciplina, padroniza e se inscreve com o conhecimento do equilíbrio promulgado.",
      "model",
      "Supplementary artifacts enable ﬂexibility by transmitting impulses from interdependent routines, even as the core artifact enables standardization",
      ["p.20/L2350-2371", "p.21/L2372-2387"]),
    F("A interdependência de rotinas habilita e disciplina a habilidade profissional: a customização é possível e ao mesmo tempo é 'on record' para pares, gestores e auditores — com risco de desvio (favorecer clientes-chave) quando o julgamento pende a um extremo.",
      "proposition",
      "underwriters’ actions are always “on record,” holding them accountable to peers, management, and even external auditors",
      ["p.18/L2115-2125", "p.21/L2426-2451"]),
]

CONTRIBUTION = dict(
    theoretical=("Quatro contribuições declaradas: (1) os gatilhos pelos quais a ênfase entre padrões "
                 "ostensivos muda — interseções que orientam e a habilidade de reorientar; (2) os "
                 "micromecanismos da embeddedness e das ecologias de rotinas — sobreposições promulgadas em "
                 "interseções mandatórias/discricionárias e iterativas; (3) a 'reciprocal task "
                 "interdependence' como skillful accomplishment dentro de cada tarefa — estendendo "
                 "Thompson ao nível micro e à ideia de trabalho mindful rotinizado; (4) a divisão de "
                 "trabalho entre artefatos centrais (padronizam/disciplinam) e suplementares (transmitem "
                 "impulsos/flexibilizam) (p.19-21/L2251-2387)."),
    practical=("Mostra como trabalho profissional altamente customizado pode ser rotinizado mantendo "
               "autonomia e variação sem perder accountability — um mecanismo de controle: a "
               "padronização de habilidades que constitui o ator como profissional (p.21/L2416-2451)."),
    limitations=("Três condições de fronteira declaradas: rotina com alta autonomia no ponto de entrega "
                 "(menos aplicável a engenharia/software); trabalho de alto volume (~400 deals/ano, menos "
                 "aplicável a poucas relações de cliente como advocacia); e 24 underwriters experientes — "
                 "profissionais menos experientes podem não equilibrar orientação/reorientação "
                 "(p.21-22/L2452-2495)."),
    future_research=("Explorar o processo de patterning das rotinas interseccionais, feedback loops e "
                     "quebras que permitem mudança; variação por nível de habilidade profissional; e "
                     "outros contextos de serviços profissionais para testar o framework (p.21-22/L2388-2520)."),
    source_refs=["p.19/L2231-2250", "p.21-22/L2452-2495"],
)
