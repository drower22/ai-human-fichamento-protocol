SUMMARY = (
    "O artigo (Oliver, 1991) aplica os insights convergentes das teorias institucional e da dependência de recursos "
    "para prever como as organizações respondem às pressões institucionais, que podem variar da conformidade passiva "
    "à manipulação ativa (p.1/L007-014; p.2/L051-055). A autora parte da lacuna de que a literatura institucional deu "
    "pouca atenção aos comportamentos estratégicos das organizações diante dessas pressões e da crítica de que a "
    "teoria retrata organizações passivas (p.1/L029-031; p.1/L040-043; p.2/L047-051). Compara as duas perspectivas quanto a "
    "contexto e motivos (Tabela 1) e conclui que a teoria institucional pode explicar respostas ativas se não "
    "pressupuser organizações invariavelmente passivas (p.2/L067-081; p.7/L363-374). Propõe uma tipologia de cinco "
    "estratégias, em ordem crescente de resistência ativa: aquiescência, compromisso, evitação, desafio e "
    "manipulação, cada uma com três táticas (p.7/L380-383; p.8/L387-426). Em seguida, formula dez hipóteses, "
    "agrupadas em cinco antecedentes institucionais (causa, constituintes, conteúdo, controle e contexto), que "
    "preveem a probabilidade de resistência: menor legitimidade e ganho econômico esperados, maior multiplicidade de "
    "constituintes, menor dependência, menor consistência com os objetivos, maiores restrições de discricionariedade, "
    "menor coerção legal, menor difusão voluntária, menor incerteza e menor interconectividade (p.15/L781-789; "
    "p.16/L849-852; p.18/L976-983; p.20/L1097-1104; p.23/L1252-1253; p.24/L1254-1262; p.26/L1356-1362). O texto não tem coleta de "
    "dados; ilustra os argumentos com estudos anteriores e exemplos, e sugere como mensurar as variáveis em "
    "pesquisas futuras (p.28/L1449-1483). A conclusão é que a conformidade não é inevitável nem sempre instrumental "
    "para a sobrevivência, e que a resistência pode ser eficaz quando a multiplicidade é alta e dependência, "
    "coerção, difusão, incerteza e interconectividade são baixas (p.30/L1576-1578; p.31/L1590-1601)."
)

RESEARCH_QUESTION = (
    "O artigo não enuncia uma pergunta de pesquisa explícita; declara como objetivo identificar as respostas "
    "estratégicas que as organizações adotam diante das pressões institucionais por conformidade e desenvolver um "
    "referencial conceitual preliminar para prever sua ocorrência (p.1/L032-039). Reconstruída como pergunta "
    "implícita: que estratégias as organizações usam em resposta às pressões institucionais e que fatores preveem "
    "quando elas se conformam ou resistem (p.1/L032-039; p.15/L776-781)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.2/L051-055", "p.1/L032-035"],
      "This article applies the convergent insights of institutional and resource dependence theories to demonstrate how organizational behavior may vary from passive conformity to active resistance",
      "Primeiro dos dois referenciais centrais; é a teoria cujas premissas de passividade o artigo busca ampliar."),
    V("T2", "uses", ["p.2/L051-055", "p.3/L128-130"],
      "Resource dependence theory also emphasizes that most organizations confront numerous and frequently incompatible demands from a variety of external actors",
      "Segundo referencial central, que fornece o repertório de escolhas ativas e a noção de dependência."),
    V("T3", "uses", ["p.17/L918-923", "p.16/L849-852"],
      "the reasons for institutional pressures fall into two categories: social and economic fitness",
      "Legitimidade social e ganho econômico são o antecedente 'causa' e sustentam as hipóteses 1 e 2."),
    V("T4", "does_not_use", [],
      "",
      "O termo 'agency' aparece como agência ativa da organização (p.1/L041; p.2/L060) e em 'agências' governamentais; não há teoria da agência (principal-agente)."),
    V("T5", "uses", ["p.8/L441-445", "p.27/L1424-1431"],
      "Imitation, which is consistent with the concept of mimetic isomorphism, refers to either conscious or unconscious mimicry of institutional models",
      "Isomorfismo (mimético e coercitivo) fundamenta a tática de imitação e as hipóteses de difusão e interconectividade."),
    V("T6", "uses", ["p.11/L562-570", "p.10/L544-548"],
      "Institutional theorists have elaborated the virtues of decoupling internal work activities from formal structures and external assessment",
      "Desacoplamento, cerimônia e fachada estruturam as táticas de evitação (ocultar e amortecer)."),
    V("T7", "uses", ["p.13/L681-683", "p.13/L684-694"],
      "Manipulation can be defined as the purposeful and opportunistic attempt to co-opt, influence, or control institutional pressures and evaluations",
      "Cooptação é a primeira tática da estratégia de manipulação."),
    V("T8", "does_not_use", [],
      "",
      "A visão baseada em recursos não é mencionada em nenhum trecho."),
    V("T9", "uses", ["p.29/L1531-1536", "p.2/L056-058"],
      "recommendation that institutional and political models should be regarded as complementary tools",
      "A complementaridade das duas perspectivas é o ponto de partida e a conclusão do artigo."),
    V("T10", "uses", ["p.22/L1165-1177", "p.20/L1101-1104"],
      "It is suggested here that resistance will vary with the loss of autonomy associated with conforming pressures",
      "Restrições à discricionariedade são o antecedente da hipótese 6; o texto trata da discricionariedade organizacional, citando Hambrick e Finkelstein (p.22/L1171-1172)."),
    V("T11", "discusses", ["p.4/L219-225", "p.8/L431-434"],
      "their \"social fact\" quality renders them the only conceivable, \"obvious,\" or \"natural\" way",
      "Usa a noção de normas tomadas como dadas e 'fato social' para explicar comportamento de não escolha (hábito); Berger e Luckmann são citados, mas a teoria não é desenvolvida."),
    V("T12", "does_not_use", [],
      "",
      "Hirschman (1970) é citado só para indicar que a organização pode sair do domínio (p.11/L586-589), sem desenvolver exit, voice e loyalty."),
]

KEY_CONCEPTS = [
    dict(concept="Tipologia de respostas estratégicas",
         definition="Cinco estratégias que variam da passividade à resistência ativa: aquiescência, compromisso, evitação, desafio e manipulação, cada uma com três táticas.",
         quote="Five types of strategic responses are proposed here, which vary in active agency by the organization from passivity to increasing active resistance: acquiescence, compromise, avoidance, defiance, and manipulation",
         source_refs=["p.7/L377-383", "p.8/L387-426"]),
    dict(concept="Aquiescência",
         definition="Conformidade às pressões institucionais, que pode assumir as formas de hábito, imitação e cumprimento consciente (compliance).",
         quote="Although organizations commonly accede to institutional pressures, acquiescence may take alternative forms; these forms include habit, imitation, and compliance",
         source_refs=["p.8/L428-431", "p.8/L450-451"]),
    dict(concept="Evitação",
         definition="Tentativa organizacional de evitar a necessidade de conformidade, por ocultação da não conformidade, amortecimento (buffering) ou fuga.",
         quote="Avoidance is defined here as the organizational attempt to preclude the necessity of conformity",
         source_refs=["p.10/L539-543"]),
    dict(concept="Manipulação",
         definition="Resposta mais ativa: busca mudar ou exercer poder sobre o conteúdo das expectativas ou sobre as fontes que as expressam ou impõem, por cooptação, influência ou controle.",
         quote="Manipulation is the most active response to these pressures because it is intended to actively change or exert power over the content of the expectations themselves or the sources that seek to express or enforce them",
         source_refs=["p.13/L676-683"]),
    dict(concept="Antecedentes institucionais (cinco C's)",
         definition="Cinco categorias de fatores, correspondentes a perguntas sobre por que, quem, o quê, como e onde as pressões são exercidas: causa, constituintes, conteúdo, controle e contexto.",
         quote="The five institutional antecedents outlined in Table 3—cause, constituents, content, control, and context—correspond respectively to these five basic questions",
         source_refs=["p.15/L778-785", "p.16/L792-815"]),
    dict(concept="Multiplicidade de constituintes",
         definition="Grau de expectativas múltiplas e conflitantes de constituintes sobre uma organização.",
         quote="multiplicity, defined as the degree of multiple, conflicting, constituent expectations exerted on an organization",
         source_refs=["p.18/L1003-1008"]),
]

METHODOLOGY = dict(
    study_type="teórico (desenvolvimento conceitual)",
    design="Desenvolvimento teórico que compara as teorias institucional e da dependência de recursos (Tabela 1), propõe uma tipologia de cinco estratégias (Tabela 2) e formula dez hipóteses sobre antecedentes das respostas (Tabelas 3 e 4).",
    sample_type="não se aplica (sem coleta de dados)",
    sample_size=None,
    sector="",
    period="",
    methods=["desenvolvimento teórico", "tipologia", "proposição de hipóteses"],
    analysis_note=("O artigo se apresenta como um referencial conceitual preliminar (p.1/L032-035). Os argumentos são ilustrados com "
                   "estudos empíricos anteriores e exemplos hipotéticos, sem teste das hipóteses. Sugere medidas e abordagens, como "
                   "entrevistas e questionários com gestores, para pesquisas futuras (p.28/L1449-1471)."),
    source_refs=["p.1/L032-039", "p.2/L056-064", "p.28/L1449-1456"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("Cinco estratégias de resposta às pressões institucionais, em ordem crescente de resistência ativa: aquiescência, compromisso, evitação, desafio e manipulação.",
      "model",
      "Five types of strategic responses are proposed here, which vary in active agency by the organization from passivity to increasing active resistance: acquiescence, compromise, avoidance, defiance, and manipulation",
      ["p.7/L377-383", "p.8/L387-426"]),
    F("A teoria institucional pode acomodar uma variedade de respostas estratégicas se o grau de escolha e atividade das organizações não for tido como invariante.",
      "proposition",
      "the institutional framework can readily accommodate a variety of strategic responses to the institutional environment when the degree of choice and activeness that organizations exhibit in response to institutional constraints and expectations is not assumed to be invariant",
      ["p.29/L1518-1523"]),
    F("Dez dimensões preditivas, em cinco categorias, determinam a escolha da estratégia.",
      "model",
      "ten dimensions of these five categories are hypothesized to determine choice of strategy",
      ["p.15/L781-789", "p.16/L816-911"]),
    F("A aquiescência é mais provável quando a legitimidade atingível pela conformidade é alta; compromisso, evitação, desafio e manipulação são mais prováveis quando é baixa.",
      "proposition",
      "acquiescence is more likely to occur when the degree of legitimacy attainable from conformity is high",
      ["p.15/L785-789", "p.17/L933-939"]),
    F("Conformidade não é inevitável nem sempre instrumental para a longevidade, e a resistência não é necessariamente arriscada.",
      "proposition",
      "conformity is neither inevitable nor invariably instrumental in securing longevity",
      ["p.31/L1590-1601", "p.30/L1568-1578"]),
    F("Estratégias resistentes tendem a ser alternativas potencialmente eficazes quando a multiplicidade é alta e dependência, coerção, difusão, incerteza e interconectividade são baixas.",
      "proposition",
      "resistant strategies will be potentially effective alternatives when multiplicity, for example, is high and dependence, coercion, diffusion, uncertainty, and interconnectedness are low",
      ["p.30/L1576-1578"]),
]

CONTRIBUTION = dict(
    theoretical=("Preenche a lacuna de atenção da literatura institucional aos comportamentos estratégicos das organizações diante das "
                 "pressões (p.1/L029-031; p.1/L036-039), integra as teorias institucional e da dependência de recursos como "
                 "complementares (p.29/L1531-1536) e oferece uma tipologia de cinco estratégias e dez hipóteses sobre seus "
                 "antecedentes (p.7/L380-383; p.15/L781-789). Sugere ainda investigar fatores de gestores e organizações e "
                 "as condições em que as pressões falham em seus efeitos previstos (p.29/L1503-1513; p.31/L1602-1609)."),
    practical=("O artigo não traz seção de implicações gerenciais. A implicação declarada é que a conformidade pode ameaçar a "
               "sobrevivência de longo prazo ao impor rigidez estrutural e procedimental, e por isso convém investigar a gama de "
               "respostas disponíveis em vez de assumir conformidade ou não conformidade a priori (p.31/L1590-1601)."),
)
