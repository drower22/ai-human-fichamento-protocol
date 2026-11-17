SUMMARY = (
    "O artigo revisa criticamente a pesquisa sobre Enterprise Risk Management (ERM) e argumenta que ela oferece um "
    "novo domínio de pesquisa para estudiosos de gestão (p.1/L008-014). O ERM propõe a gestão integrada de todos os "
    "riscos de uma organização, alinhada à governança e à estratégia, mas a pesquisa acadêmica ainda é incipiente e "
    "concentrada em contabilidade e finanças (p.1/L008-014; p.1/L025-032). Motivado por essas lacunas e pelas "
    "dificuldades de adotantes de destaque na crise de 2008, o texto responde a duas perguntas: o que é ERM e como a "
    "pesquisa em gestão pode informar sua teoria e prática (p.1/L041-043; p.2/L084-090). Mostra que autores e "
    "reguladores divergem sobre o que é ERM, descreve suas raízes conceituais e um consenso emergente sobre três "
    "elementos: a gestão de portfólio de riscos, a inclusão de riscos estratégicos e a visão do risco como fonte de "
    "vantagem (p.2/L092-102; p.2/L110-115; p.4/L210-224). Revisa achados empíricos, de resultados mistos e com "
    "problemas de endogeneidade, e a falta de atenção a conceitos como cultura e apetite de risco (p.4/L228-251; "
    "p.4/L252-256; p.5/L257-261). Em seguida indica onde a pesquisa em gestão pode contribuir: objetivos do ERM, "
    "concepções gerenciais de risco, medida de risco, dinâmica temporal, níveis de análise, implementação e "
    "estratégia (p.5/L278-281; p.5/L296-313; p.6/L336-368; p.7/L395-424; p.8/L450-498; p.9/L509-525). Defende uma postura "
    "mais prescritiva e a pesquisa engajada e mantém uma visão cautelosa dos benefícios do ERM enquanto faltar "
    "evidência (p.9/L534-548)."
)

RESEARCH_QUESTION = (
    "O artigo formula duas perguntas: o que é ERM e como a pesquisa em gestão pode informar a teoria e a prática do ERM "
    "(p.2/L084-090)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.1/L008-014", "p.1/L017-019"],
      "ERM proposes the integrated management of all the risks an organization faces, which inherently requires alignment of risk management with corporate governance and strategy",
      "Objeto central da revisão crítica."),
    V("T2", "uses", ["p.2/L087-090", "p.5/L265-268"],
      "Recent work in management on risk has focused largely on corporate level risk and performance. However, earlier work took a more micro approach, emphasizing both individual risk propensities",
      "A literatura micro e macro de gestão sobre risco é a base para as contribuições propostas ao ERM."),
    V("T3", "uses", ["p.5/L273-277", "p.5/L296-313"],
      "March and Shapira (1987) and Shapira (1995) found that managerial conceptions of risk emphasized the size of the potential loss and often did not consider it a probabilistic concept",
      "As concepções gerenciais de risco orientam a seção sobre como os gestores entendem e medem o risco."),
    V("T4", "does_not_use", [],
      "",
      "A teoria prospectiva não é mencionada."),
    V("T5", "discusses", ["p.7/L385-389", "p.8/L488-492"],
      "March and Simon (1958) argued that managers operate within implicit models of the world",
      "Ideias de March e Simon, como modelos implícitos e absorção de incerteza, sustentam argumentos, sem que a teoria comportamental seja apresentada como referencial."),
    V("T6", "discusses", ["p.3/L180-190"],
      "care about systematic risk (beta), so investing resources to reduce unsystematic risk was wasteful (Lintner, 1965; Sharpe, 1964)",
      "Apresenta o argumento clássico das finanças contra a gestão de risco corporativa e sua revisão posterior."),
    V("T7", "discusses", ["p.8/L466-473"],
      "their emphasis on agency theory has restricted their view to emphasize boards' control function and ignored their advice function",
      "A teoria da agência é criticada como limitação da literatura de finanças e contabilidade sobre conselhos."),
    V("T8", "uses", ["p.6/L336-352"],
      "individuals usually underestimate the amount of uncertainty they face",
      "Excesso de confiança e vieses de julgamento fundamentam a agenda sobre medida de risco."),
    V("T9", "does_not_use", [],
      "",
      "A teoria dos acidentes normais não é mencionada."),
    V("T10", "uses", ["p.7/L385-394", "p.5/L302-307"],
      "Weick (1969) argued that managers operate in “enacted environments”",
      "A cognição gerencial e os ambientes enacted sustentam a agenda sobre modelos gerenciais de risco."),
    V("T11", "uses", ["p.7/L405-418", "p.8/L445-448"],
      "Management scholars have studied how substantively different phenomena may exist as we move to different levels of analysis",
      "Os níveis de análise estruturam uma das áreas de contribuição propostas."),
    V("T12", "uses", ["p.7/L419-428", "p.8/L429-448"],
      "ERM usage assumes corporations can impose consistent risk cultures and risk appetites both across the organization and at differing levels of the hierarchy",
      "Cultura e apetite de risco são tratados como construtos problemáticos que a pesquisa em gestão deve examinar."),
    V("T13", "uses", ["p.8/L493-498", "p.9/L499-507"],
      "management scholars have a history of organizational change studies that could inform risk management",
      "A visão ingênua de mudança do ERM é criticada com base na literatura de mudança organizacional."),
    V("T14", "discusses", ["p.7/L395-404"],
      "This time-varying nature of risk ties to the management literature on managerial time horizons",
      "Relacionada à dinâmica temporal do risco, em um trecho curto."),
    V("T15", "uses", ["p.9/L509-525"],
      "Much of the extant ERM literature assumes that strategic decisions largely occur in the strategic planning process (c.f., Fraser and Simkins, 1987). In contrast, strategy scholars have turned away from formal strategic planning",
      "Contrasta a suposição do ERM sobre planejamento estratégico formal com a visão de estudiosos de estratégia."),
    V("T16", "discusses", ["p.4/L247-251"],
      "Mikes and Kaplan (2013) proposed a contingency framework, and called for research that would lead to the development of a contingency theory of ERM",
      "Citada como proposta e chamada para pesquisa, sem desenvolvimento próprio."),
    V("T17", "does_not_use", [],
      "",
      "'Stakeholders' aparece em definições de ERM (p.2/L054; p.8/L474) e em uma referência a Freeman et al. (p.5/L289-291), sem apresentar a teoria."),
    V("T18", "discusses", ["p.8/L450-464"],
      "The adoption of other business practices has been shown to depend on factors that include regulatory pressures, industry norms",
      "Pressões externas e normas são apresentadas como fatores que explicam a adoção do ERM, com sugestão de pesquisa."),
    V("T19", "discusses", ["p.7/L413-418"],
      "take more risk when their performance falls below their aspiration levels",
      "Aspirações aparecem como exemplo de confusão entre níveis de análise, em uma frase."),
    V("T20", "discusses", ["p.9/L534-542"],
      "Such a stance would align both with historical studies on planning systems and organizational change management and with recent efforts to increase engaged scholarship among management scholars",
      "Pesquisa engajada é invocada na conclusão como alinhada à postura prescritiva proposta."),
]

KEY_CONCEPTS = [
    dict(concept="Enterprise Risk Management (ERM)",
         definition="Abordagem que propõe gerir de forma integrada todos os riscos que uma organização enfrenta, alinhada à governança e à estratégia, em vez de gerir cada risco isoladamente (modelo de silos).",
         quote="ERM proposes the integrated management of all the risks an organization faces, which inherently requires alignment of risk management with corporate governance and strategy",
         source_refs=["p.1/L008-014", "p.1/L017-019"]),
    dict(concept="Consenso emergente sobre o núcleo do ERM",
         definition="Apesar das divergências, há consenso sobre três elementos: gerir o risco do portfólio é mais eficiente que gerir o de cada parte, o ERM inclui riscos estratégicos e o risco não é visto só como problema a mitigar.",
         quote="there has begun to emerge a consensus about the core elements of ERM",
         source_refs=["p.4/L210-224"]),
    dict(concept="Concepções gerenciais de risco",
         definition="Os gestores tendem a entender risco como o tamanho da perda potencial, muitas vezes sem noção probabilística, diferindo da concepção acadêmica de variação de retornos.",
         quote="March and Shapira (1987) and Shapira (1995) found that managerial conceptions of risk emphasized the size of the potential loss and often did not consider it a probabilistic concept",
         source_refs=["p.5/L273-277", "p.5/L296-313"]),
    dict(concept="Risco objetivo e risco subjetivo",
         definition="Medidas objetivas de risco servem para avaliar resultados de comportamentos, enquanto percepções gerenciais de risco são necessárias para explicar o comportamento dos gestores.",
         quote="While we might use objective measures of risk to assess the outcomes of risk-related behaviors, we need managerial perceptions of risk to explain managerial behavior",
         source_refs=["p.6/L320-335"]),
    dict(concept="Cultura de risco e apetite de risco",
         definition="Termos vagos de reguladores e práticos que supõem que corporações impõem culturas e apetites de risco consistentes em toda a organização, o que os autores tratam como questão empírica e conceitualmente problemática.",
         quote="ERM usage assumes corporations can impose consistent risk cultures and risk appetites both across the organization and at differing levels of the hierarchy",
         source_refs=["p.7/L419-428", "p.8/L429-448", "p.4/L252-256"]),
]

METHODOLOGY = dict(
    study_type="teórico (revisão crítica e agenda de pesquisa)",
    design="Revisão crítica da literatura acadêmica e prática sobre ERM e da pesquisa em gestão sobre risco, decisão, estratégia e organizações, para identificar limitações e propor contribuições da pesquisa em gestão.",
    sample_type="não se aplica (literatura de ERM e de gestão; sem coleta de dados)",
    sample_size=None,
    sector="",
    period="",
    methods=["revisão crítica da literatura"],
    analysis_note=("Os autores revisam pesquisas sobre ERM para identificar como pesquisadores e praticantes o definem e o operacionalizam "
                   "(p.2/L084-090), apresentando definições de periódicos acadêmicos e de órgãos normativos (Tabelas 1 e 2) e achados empíricos "
                   "(p.4/L228-251). O texto não descreve critérios de busca ou de seleção da literatura."),
    source_refs=["p.2/L084-090", "p.4/L228-251"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("Autores e reguladores divergem sobre o que constitui o ERM, por exemplo entre definir o risco independentemente dos objetivos ou em função deles e entre tratá-lo como problema ou como fonte de valor.",
      "proposition",
      "Authors and regulators disagree on exactly what constitutes ERM",
      ["p.2/L092-102", "p.2/L047-083", "p.3/L118-172"]),
    F("Há um consenso emergente sobre o núcleo do ERM: gestão do risco do portfólio, inclusão de riscos estratégicos e visão do risco como fonte de vantagem competitiva.",
      "proposition",
      "ERM incorporates not only traditional risks like product liability and accidents, but also strategic risks such as product obsolescence or competitor actions",
      ["p.4/L210-224"]),
    F("A pesquisa empírica sobre ERM é pequena, de resultados mistos e com problemas de endogeneidade, o que impede conclusão geral sobre sua eficácia.",
      "proposition",
      "Endogeneity and related methodological issues and the mixed results found in current research make it impossible to draw a general conclusion about ERM's effectiveness",
      ["p.4/L228-251"]),
    F("Conceitos centrais para os praticantes, como apetite de risco e cultura de risco, foram pouco examinados pela pesquisa empírica.",
      "proposition",
      "questions of exactly what risk appetite means",
      ["p.4/L252-256", "p.5/L257-261"]),
    F("Na medida de risco, não se deve supor que indivíduos ou organizações façam julgamentos ou tenham preferências de risco consistentes, o que abre uma agenda para estudiosos de gestão.",
      "proposition",
      "ERM scholars should not assume individuals or organizations make consistent risk judgments or have consistent risk preferences",
      ["p.6/L336-368"]),
    F("Em níveis de análise, não se devem projetar resultados individuais sobre organizações, e a consistência de cultura e apetite de risco é uma questão empírica.",
      "proposition",
      "scholars should not casually project results from individuals onto organizations",
      ["p.7/L405-424"]),
    F("A implementação do ERM é uma área importante para estudar a mudança organizacional, pois a literatura mostra que mudanças simples geram dinâmicas complexas e imprevistas.",
      "proposition",
      "Thus, implementation of ERM offers a new and important area in which to study organizational change management",
      ["p.8/L493-498", "p.9/L499-507"]),
    F("Se estudiosos de estratégia estiverem certos de que as decisões estratégicas ocorrem fora do planejamento formal, a ênfase do ERM na análise de risco nesse planejamento é equivocada, o que exige evidência empírica.",
      "proposition",
      "If strategy scholars are correct, then the ERM emphasis on risk analysis in formal strategic planning is misguided. Resolving these differences requires empirical evidence",
      ["p.9/L521-525"]),
    F("Enquanto a pesquisa não demonstrar os resultados atribuídos ao ERM, uma visão cética é justificada.",
      "proposition",
      "Until research conclusively demonstrates ERM actually has the outcomes its advocates claim",
      ["p.9/L542-548"]),
]

CONTRIBUTION = dict(
    theoretical=("Mostra que o ERM é um novo domínio de pesquisa para estudiosos de gestão e identifica limitações e lacunas que eles estão "
                 "mais bem equipados para tratar (p.1/L010-014). Aponta áreas de contribuição: objetivos do ERM, concepções gerenciais de "
                 "risco, medida de risco, dinâmica temporal, níveis de análise, implementação e estratégia (p.5/L278-281; p.9/L527-533) e "
                 "defende uma postura mais prescritiva, alinhada à pesquisa engajada (p.9/L534-539)."),
    practical=("Indica que praticantes precisam entender como indivíduos e grupos definem risco, possíveis vieses de avaliação e desafios de "
               "implementação, e que podem colaborar com pesquisadores em pesquisa engajada (p.9/L540-542). Recomenda cautela quanto aos "
               "benefícios do ERM, dado que estudos ainda não demonstraram benefícios consistentes (p.9/L542-548)."),
)
