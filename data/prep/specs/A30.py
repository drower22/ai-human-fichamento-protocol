SUMMARY = (
    "O artigo analisa como ocorre a gestão de riscos no processo de internacionalização de born globals "
    "brasileiras, por meio de estudo de caso múltiplo com sete cervejarias artesanais premiadas (mais um "
    "caso-piloto) e nove entrevistas semiestruturadas com fundadores e diretores, complementadas por "
    "pesquisa documental e observação não-participante em eventos do setor (p.1/L007-23; p.5-6/L252-358). "
    "O enquadre combina a literatura de born globals e novos empreendimentos internacionais, a "
    "classificação de riscos de Cavusgil, Knight e Riesenberger (comercial, monetário, país, intercultural), "
    "a percepção de risco de Sitkin e Weingart e o modelo de gestão de risco de Oviatt, Shrader e "
    "McDougall baseado em Miller (p.3-5/L107-251). Os achados mostram que o background internacional "
    "dos empreendedores e o uso de redes de negócios reduzem a percepção de risco; que os gestores "
    "reagrupam os quatro riscos em fatores internos controláveis (comercial, intercultural) e externos "
    "incontroláveis (monetário, país) — estes últimos salientes no contexto institucional brasileiro; e que, "
    "embora não haja programas formais, a gestão de risco existe como processo por meio de identificação, "
    "análise ambiental, pesquisa de mercado, planejamento, construção de cenários e uso de redes "
    "(p.8-12/L519-732). Como contribuição, propõe-se um modelo integrativo de gestão de risco para born "
    "globals que acrescenta redes de negócios, estratégias de internacionalização e velocidade do processo "
    "aos fatores do modelo de Oviatt et al. (p.12-14/L722-811)."
)

RESEARCH_QUESTION = (
    "O objetivo declarado é 'analisar como ocorre a gestão de riscos no processo de internacionalização de "
    "born globals brasileiras', desdobrado em dois objetivos específicos: (a) descrever os fatores de risco "
    "percebidos na internacionalização pelos empreendedores das empresas estudadas; e (b) verificar as "
    "ações e estratégias de gestão de risco no processo de internacionalização de empresas born globals "
    "(p.2/L083-088)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.3/L126-131", "p.12/L722-727"],
      "as empresas born globals são aquelas com visão global desde sua fundação",
      "O fenômeno central; os pilares de Madsen e Servais alimentam o modelo integrativo."),
    V("T2", "uses", ["p.3/L149-155", "p.10/L601-608"],
      "quatro tipos principais de risco: risco comercial, risco monetário, risco-país e risco intercultural",
      "A classificação adotada e depois reagrupada pelos achados em fatores internos × externos."),
    V("T3", "uses", ["p.4/L169-178"],
      "à avaliação do nível de risco inerente a uma situação",
      "O conceito de percepção de risco adotado pela maioria dos estudos e por esta pesquisa."),
    V("T4", "uses", ["p.5/L229-244", "p.12/L722-727"],
      "desenvolveram um modelo de gestão de riscos na internacionalização de novos empreendimentos",
      "Suporte direto do modelo integrativo proposto (Figura 2)."),
    V("T5", "discusses", ["p.3/L137-144"],
      "O modelo de internacionalização de Uppsala de Johanson e Vahlne ao tratar da incerteza",
      "Contrastado com o processo não-gradual; a incerteza é reconduzida ao conceito de risco de March e Shapira."),
    V("T6", "uses", ["p.4/L173-178", "p.9/L561-579"],
      "está relacionada à orientação internacional do indivíduo, seu nível de conhecimento, experiência internacional",
      "Achado-chave: o background internacional dos fundadores reduz a percepção de risco."),
    V("T7", "uses", ["p.2/L060-069", "p.3/L121-125", "p.12/L698-704"],
      "fortalecimento das redes de relacionamento pelo mundo",
      "Uso empírico direto: redes de negócios entram no modelo integrativo como variável de mitigação."),
    V("T8", "discusses", ["p.3/L116-125"],
      "as decisões de internacionalização estão fortemente relacionadas aos riscos e questões comerciais, monetárias e políticas",
      "Revisão contrastada: as teorias econômicas dão menos atenção ao risco intercultural do que Uppsala/redes."),
    V("T9", "uses", ["p.4/L179-184", "p.11/L671-675"],
      "um processo para identificar, avaliar e gerenciar riscos com o objetivo principal de proteger e criar valor",
      "Fornece a definição de gestão de risco mobilizada na discussão e nas conclusões."),
    V("T10", "discusses", ["p.3/L140-148"],
      "o risco a significância de resultados indesejáveis",
      "A definição conceitual de risco adotada, convergente com Sitkin e Weingart."),
    V("T11", "uses", ["p.5/L252-262", "p.7/L423-427"],
      "adotou-se uma estratégia de pesquisa em estudos de casos múltiplos",
      "O arcabouço metodológico: Eisenhardt, Miles & Huberman, Bardin e a matriz de Telles."),
    V("T12", "does_not_use", [], "",
      "Citado apenas como autor de born globals na enumeração da introdução; o construto não é mobilizado."),
    V("T13", "does_not_use", [], "",
      "Ausente como conceito — os custos da operação externa são tratados como riscos, não como liability of foreignness."),
    V("T14", "does_not_use", [], "",
      "O 'ambiente institucional' aparece como fator de risco-país, não via teoria institucional."),
    V("T15", "does_not_use", [], "",
      "Ausente — competências do empreendedor tratadas como orientação internacional, não como recursos VRIO."),
]

KEY_CONCEPTS = [
    dict(concept="Born global",
         definition="Empresa com visão global desde a fundação e produtos/serviços com potencial global, que acelera a internacionalização em vez de seguir o processo gradual.",
         quote="as empresas born globals são aquelas com visão global desde sua fundação",
         source_refs=["p.3/L126-131"]),
    dict(concept="Percepção de risco",
         definition="A avaliação do nível de risco inerente a uma situação, associada à sua incerteza e ao controle que os indivíduos percebem ter sobre os resultados possíveis.",
         quote="à avaliação do nível de risco inerente a uma situação, associado à sua incerteza e ao controle",
         source_refs=["p.4/L169-172"]),
    dict(concept="Quatro riscos da internacionalização",
         definition="A classificação de Cavusgil, Knight e Riesenberger — risco comercial, monetário, país e intercultural — riscos incontroláveis e inevitáveis cujos efeitos podem ser mitigados pela percepção e avaliação.",
         quote="quatro tipos principais de risco: risco comercial, risco monetário, risco-país e risco intercultural",
         source_refs=["p.3/L149-155"]),
    dict(concept="Fatores internos × externos",
         definition="O reagrupamento feito pelos entrevistados: riscos comercial e intercultural como fatores internos controláveis/gerenciáveis; risco monetário e risco-país como fatores externos, identificáveis e monitoráveis, mas não gerenciáveis.",
         quote="fatores de risco comerciais e culturais, podem ser controlados / gerenciados pela organização",
         source_refs=["p.9/L586-590"]),
    dict(concept="Gestão de risco como processo",
         definition="O processo contínuo de identificar, avaliar e gerenciar riscos para proteger e criar valor — nas born globals, ainda que sem programas formais, as etapas de identificação, análise e classificação já configuram gestão.",
         quote="um processo para identificar, avaliar e gerenciar riscos com o objetivo principal de proteger e criar valor",
         source_refs=["p.4/L179-184", "p.12/L705-712"]),
    dict(concept="Orientação internacional do empreendedor",
         definition="O conjunto de conhecimento, experiência internacional pessoal e profissional, escolaridade e habilidade com línguas que acentua a orientação internacional e reduz a percepção de risco.",
         quote="está relacionada à orientação internacional do indivíduo",
         source_refs=["p.4/L173-178"]),
]

METHODOLOGY = dict(
    study_type="empírico qualitativo exploratório",
    design="estudos de casos múltiplos (Eisenhardt, 1989) com sete cervejarias artesanais brasileiras born globals — selecionadas por ano de fundação (internacionalização até 7 anos), início de atividades internacionais e premiações — precedidas de caso-piloto integrado à base de dados",
    sample_type="fundadores, sócios-gerentes, mestres cervejeiros e diretores comerciais — os principais tomadores de decisão e responsáveis pela internacionalização — mais um gestor de projeto do Sebrae RS",
    sample_size=9,
    sector="indústria de bebidas — cervejarias artesanais (crescimento de 570% em dez anos; 679 registradas no Brasil até 2017)",
    period="coleta de dados de junho a novembro de 2016 (seis meses), precedida de aproximação ao campo em festivais e visita técnica",
    methods=["pesquisa documental (documentos internos e dados secundários)", "nove entrevistas semiestruturadas gravadas e transcritas (50–65 min; duas sem gravação no piloto)", "observação não-participante em eventos do setor e nas empresas", "análise de conteúdo (Bardin, 2006) no Atlas.ti com unidade hermenêutica", "matriz de amarração teórico-metodológica (Telles, 2001); protocolo de estudo de caso, diário de campo e informantes-chave para validade e confiabilidade (Miles & Huberman, 1994)"],
    analysis_note=("Codificação no Atlas.ti com famílias/códigos predefinidos (risco comercial, intercultural, "
                   "monetário, país; percepção do risco; empreendedor; organização; ambiente; born global), "
                   "relatórios do software e análise dos dados codificados; validade por protocolo, diário de "
                   "campo, revisão por informantes-chave e coerência problema-objetivos-literatura-métodos "
                   "(p.5-8/L252-518)."),
    source_refs=["p.5/L252-262", "p.6/L263-358", "p.7/L423-427", "p.8/L468-518"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("Ao contrário da PME típica, em que a avaliação de risco é intuitiva, as born globals estudadas realizam atividades internacionais com planejamento, e os riscos percebidos ao longo do processo são tratados.",
      "empirical",
      "as atividades internacionais são realizadas com planejamento e os riscos percebidos e identificados ao longo do processo são tratados",
      ["p.8/L520-526"]),
    F("A percepção de risco é reduzida pelo background internacional dos empreendedores — a maioria dos fundadores tem formação internacional e experiências pessoais ou profissionais no exterior —, gerando homogeneidade na identificação e percepção dos riscos.",
      "empirical",
      "a orientação internacional para o negócio é acentuada, e com isso a percepção de que a atividade global será arriscada, torna-se reduzida",
      ["p.9/L561-579"]),
    F("Os gestores reagrupam os quatro riscos: comercial e intercultural como 'fatores internos' controláveis; monetário e risco-país como 'fatores externos' que a empresa pode identificar, monitorar e reagir, mas não gerenciar — risco-país é saliente dada a instabilidade institucional brasileira e retraiu projetos de expansão.",
      "empirical",
      "fatores externos e incontroláveis pela organização",
      ["p.9/L580-591", "p.10/L592-600", "p.11/L655-664"]),
    F("As principais ações de mitigação são análise do ambiente, estudo do setor e pesquisa de mercado, complementadas por estruturação de portfólio internacional, fortalecimento de redes, escolha de parceiros e intermediários, participação em missões e festivais internacionais e terceirização de riscos via distribuidores.",
      "empirical",
      "a análise do ambiente, estudo do setor e pesquisa de mercado foram os mais utilizados pela maioria das empresas",
      ["p.11/L676-680", "p.12/L691-704"]),
    F("Embora não haja programas sistemáticos e formais de gestão de risco, as etapas de identificação, análise e classificação já configuram um processo de gestão que influencia decisões e desenho estratégico e acelera a internacionalização.",
      "empirical",
      "o mero fato de considerar as etapas de identificação, análise e classificação já indica um processo de gestão de riscos",
      ["p.11/L665-670", "p.12/L705-712"]),
    F("É proposto um modelo integrativo de gestão de risco em born globals — sobre os pilares de Oviatt et al., Madsen e Servais e Cavusgil et al. — que acrescenta três itens relevantes: uso de redes de negócios, escolha de estratégias de internacionalização e velocidade do processo.",
      "model",
      "um novo modelo integrativo de gestão de risco em born globals",
      ["p.12/L722-732", "p.13/L740-745", "p.14/L797-802"]),
]

CONTRIBUTION = dict(
    theoretical=("Contribui um modelo integrativo de gestão de risco para born globals que combina o modelo de Oviatt, "
                 "Shrader e McDougall, os pilares de Madsen e Servais e a classificação de Cavusgil, Knight e "
                 "Riesenberger, acrescentando redes de negócios, estratégias de internacionalização e velocidade; e "
                 "mostra que os fatores de risco de born globals de países emergentes diferem dos de países "
                 "desenvolvidos, com ênfase em risco monetário e risco-país (p.12-14/L722-802)."),
    practical=("Indica ações concretas de mitigação — análise ambiental, pesquisa de mercado, planejamento, construção "
               "de cenários, uso de redes, escolha de parceiros e terceirização de riscos — e que background "
               "internacional e planejamento reduzem a percepção de risco em novos empreendimentos "
               "(p.12/L691-720; p.13-14/L754-796)."),
    limitations=("Estudo exploratório de casos múltiplos em um único setor (cervejarias artesanais) e um único país; a "
                 "gestão de risco observada não é sistematizada nem formal; duas entrevistas do piloto sem gravação "
                 "(p.5-6/L252-358; p.12/L705-712)."),
    future_research=("Compreender a construção das relações em redes globais e sua influência no grau de "
                     "internacionalização e na percepção de risco; e estudar born globals de outros setores "
                     "(indústria e serviços além de tecnologia) para testar diferenças no gerenciamento de riscos "
                     "(p.14/L803-811)."),
)
