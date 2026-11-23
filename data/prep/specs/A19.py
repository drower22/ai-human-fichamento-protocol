SUMMARY = (
    "O artigo revisita a 'gaiola de ferro' de Weber e argumenta que o motor da racionalização organizacional "
    "mudou: depois de alcançada a burocratização da empresa e do estado, a mudança estrutural passa a ser "
    "dirigida menos pela competição ou eficiência e mais por processos que tornam as organizações similares sem "
    "necessariamente torná-las mais eficientes — o estado e as profissões tornaram-se os grandes racionalizadores "
    "da segunda metade do século XX (p.2/L092-117). A pergunta invertida é por que há tamanha homogeneidade de "
    "formas e práticas, e não por que há variação (p.3/L133-140). O artigo é teórico: propõe o campo "
    "organizacional estruturado como unidade de análise e descreve a estruturação em quatro partes — interação "
    "crescente, estruturas de dominação e coalizão, carga informacional e consciência de empreendimento comum "
    "(p.3/L165-200). Distingue isomorfismo competitivo (seleção, Hannan & Freeman) e institucional, e "
    "desmembra este último em três mecanismos: coercivo (dependência e mandatos legais), mimético (resposta a "
    "incerteza e ambiguidade de metas) e normativo (profissionalização, filtragem e socialização) "
    "(p.4/L312-337; p.5/L396-416; p.5/L417-493; p.6/L494-523; p.6/L547-618; p.7/L619-744; p.8/L745-790). Deriva doze hipóteses — seis em nível "
    "organizacional (dependência, centralização de recursos, incerteza meio-fim, ambiguidade de metas, "
    "credenciais acadêmicas, associações) e seis em nível de campo (fonte única de suporte, transações com o "
    "estado, poucos modelos visíveis, tecnologias incertas/metas ambíguas, profissionalização, estruturação) — "
    "todas governadas por cláusulas ceteris paribus (p.9/L910-992; p.10/L993-1118; p.11/L1119-1180). Como implicações, resolve o paradoxo "
    "'sociedades espertas, organizações bobas' sem recorrer só a seleção natural ou controle por elites, e propõe "
    "uma visão bifocal do poder (definir premissas; ponto de intervenção crítica) e orientações para políticas "
    "que preservem a diversidade organizacional (p.11/L1195-1242; p.12/L1243-1368; p.13/L1369-1403)."
)

RESEARCH_QUESTION = (
    "O artigo não formula uma seção de 'pergunta de pesquisa', mas enuncia explicitamente a questão central e a "
    "contrastando com a da tradição: em vez de 'why are there so many kinds of organizations?', os autores "
    "perguntam 'why there is such startling homogeneity of organizational forms and practices' e afirmam buscar "
    "explicar a homogeneidade, não a variação (p.3/L126-140). O objetivo que enquadra a pergunta é mostrar que, "
    "depois de Weber, a burocratização e outras formas de homogeneização emergem da estruturação de campos "
    "organizacionais, efetivada pelo estado e pelas profissões (p.2/L092-117)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.4/L312-337", "p.5/L371-416", "p.8/L856-870", "p.9/L871-873"],
      "we maintain that there are two types of isomorphism: competitive and institutional",
      "A teoria proposta pelo artigo: isomorfismo como o conceito que captura a homogeneização; os três mecanismos estruturam todo o desenvolvimento."),
    V("T2", "uses", ["p.3/L165-200", "p.2/L101-117", "p.3/L201-226"],
      "The process of institutional definition, or \"structuration,\" consists of four parts",
      "Unidade de análise e mecanismo de fundo: campos só existem na medida em que se institucionalizam; a homogeneização segue a estruturação."),
    V("T3", "uses", ["p.2/L032-117"],
      "the rationalist order had become an iron cage in which humanity was, save for the possibility of prophetic revival, imprisoned",
      "O enquadre revisitado: o artigo reabre a gaiola de ferro mostrando que a racionalização migrou do mercado competitivo para o estado e as profissões."),
    V("T4", "uses", ["p.3/L213-225", "p.5/L480-493", "p.6/L494-497", "p.9/L992", "p.10/L993-1008", "p.10/L1058-1059"],
      "As an innovation spreads, a threshold is reached beyond which adoption provides legitimacy rather than improves performance",
      "Bloco construtivo central: adoção como legitimidade (não desempenho), rituais de conformidade e redes relacionais; os autores divergem só no acoplamento frouxo (A-3)."),
    V("T5", "uses", ["p.5/L417-422", "p.5/L466-479", "p.9/L939-979"],
      "pressures exerted on organizations by other organizations upon which they are dependent",
      "Microfundação do isomorfismo coercivo e das hipóteses A-1/A-2 (dependência e centralização de recursos)."),
    V("T6", "uses", ["p.7/L672-731", "p.7/L732-744", "p.11/L1145-1155"],
      "the collective struggle of members of an occupation to define the conditions and methods of their work",
      "Fundamento do isomorfismo normativo (Larson/Collins): formação educacional comum, filtragem de pessoal e socialização como fontes de homogeneidade; gera A-5, A-6 e B-5."),
    V("T7", "discusses", ["p.3/L121-134", "p.4/L318-334", "p.5/L371-395", "p.12/L1246-1267"],
      "Hannan and Freeman's focus is almost solely on the first process: selection",
      "O contraponto teórico principal: a isomorfia competitiva/seleção é reconhecida como relevante para campos competitivos, mas insuficiente no mundo moderno."),
    V("T8", "discusses", ["p.3/L213-217"],
      "infused with value beyond the technical requirements of the task at hand",
      "Uma citação substantiva (Selznick): explica como práticas inovadoras deixam de ser técnicas e passam a ser buscadas por legitimidade."),
    V("T9", "discusses", ["p.6/L559-564", "p.11/L1207-1214", "p.12/L1351-1355"],
      "problemistic search may yield a viable solution with little expense",
      "Fornece a micro-lógica da modelagem (busca problemística) e da visão de poder como definição de premissas."),
    V("T10", "discusses", ["p.6/L574-586", "p.12/L1262-1267"],
      "unconsciously innovate by unwittingly acquiring some unexpected or unsought unique attributes",
      "Alchian sustenta que a inovação pode emergir de imitação imperfeita; Nelson & Winter limitam o alcance da seleção econômica."),
    V("T11", "discusses", ["p.11/L1196-1236", "p.12/L1268-1329"],
      "Societies (or elites), so it seems, are smart, while organizations are dumb",
      "O paradoxo enquadrado e resolvido: nem seleção natural nem controle por elites bastam para explicar a homogeneização."),
    V("T12", "discusses", ["p.12/L1346-1365"],
      "the power to set premises, to define the norms and standards which shape and channel behavior",
      "Implicação desenvolvida na seção final: o isomorfismo ilumina a luta por poder e sobrevivência ausente da ecologia populacional."),
    V("T13", "discusses", ["p.4/L247-252", "p.10/L1112-1118", "p.11/L1119-1125"],
      "a threshold level, or a tipping point, beyond which adoption of the dominant form will proceed with increasing speed",
      "Apoia a hipótese B-3 sobre a velocidade da homogeneização; a metáfora de Schelling descreve o ambiente de respostas recursivas."),
    V("T14", "does_not_use", [], "",
      "Citada só como exemplar da tradição que busca explicar variação entre organizações (p.3/L121-125) — exatamente o programa do qual o artigo se afasta."),
    V("T15", "does_not_use", [], "",
      "Armadilha de sobrenome: o 'Freeman' do texto é John H. Freeman, ecólogo organizacional (1982, 1977), não R. Edward Freeman dos stakeholders."),
    V("T16", "does_not_use", [], "",
      "Difusão de modelos é tema do artigo, mas a teoria ator-rede e seus termos (Latour, Callon, tradução) não aparecem."),
    V("T17", "does_not_use", [], "",
      "O artigo trabalha poder e dependência em chave sociológica; a estrutura principal-agente e custos de agência não são citados."),
]

KEY_CONCEPTS = [
    dict(concept="Campo organizacional",
         definition="Conjunto de organizações que, no agregado, constituem uma área reconhecida da vida institucional: fornecedores-chave, consumidores de recursos e produtos, agências reguladoras e organizações que produzem serviços ou produtos similares.",
         quote="those organizations that, in the aggregate, constitute a recognized area of institutional life",
         source_refs=["p.3/L165-170"]),
    dict(concept="Estruturação do campo",
         definition="Processo de definição institucional do campo em quatro partes: mais interação, estruturas de dominação e coalizão, maior carga informacional e consciência mútua de empreendimento comum.",
         quote="an increase in the extent of interaction among organizations in the field; the emergence of sharply defined interorganizational structures of domination and patterns of coalition",
         source_refs=["p.3/L189-200"]),
    dict(concept="Isomorfismo",
         definition="Processo constritivo que força uma unidade de uma população a se assemelhar às outras que enfrentam o mesmo conjunto de condições ambientais (Hawley); distinguindo-se a forma competitiva (seleção) da institucional.",
         quote="isomorphism is a constraining process that forces one unit in a population to resemble other units that face the same set of environmental conditions",
         source_refs=["p.4/L312-337"]),
    dict(concept="Isomorfismo coercivo",
         definition="Pressões formais e informais sobre organizações exercidas por outras de que dependem e pelas expectativas culturais da sociedade — sentidas como força, persuasão ou convite à conluio (mandatos estatais, ciclo orçamentário, padrões de relato).",
         quote="results from both formal and informal pressures exerted on organizations by other organizations upon which they are dependent",
         source_refs=["p.5/L417-452", "p.5/L454-493", "p.6/L494-523"]),
    dict(concept="Isomorfismo mimético",
         definition="Modelagem de outras organizações como resposta a tecnologias mal compreendidas, metas ambíguas ou incerteza ambiental simbólica; tende a copiar organizações percebidas como mais legítimas ou bem-sucedidas.",
         quote="organizations may model themselves on other organizations",
         source_refs=["p.6/L547-572", "p.7/L656-671"]),
    dict(concept="Isomorfismo normativo",
         definition="Fonte de mudança isomórfica que emana da profissionalização: base cognitiva e legitimação por educação formal de especialistas universitários e redes profissionais que difundem modelos por filtragem e socialização.",
         quote="One is the resting of formal education and of legitimation in a cognitive base produced by university specialists; the second is the growth and elaboration of professional networks",
         source_refs=["p.7/L672-744"]),
]

METHODOLOGY = dict(
    study_type="teórico (artigo conceitual/ensaio teórico)",
    design="Construção teórica dedutiva: o artigo parte de Weber e da literatura organizacional para formular um modelo de mudança homogeneizante e derivar proposições; não coleta nem analisa dados empíricos próprios.",
    sample_type="sem amostra própria; ilustrações retiradas de estudos de terceiros (reforma do serviço civil, hospitais, editoras, teatros, agências públicas)",
    sample_size=None,
    sector="não aplicável (artigo teórico sobre organizações em geral)",
    period="não aplicável",
    methods=["argumentação teórica dedutiva", "integração de literatura organizacional e sociológica", "derivação de hipóteses testáveis", "ilustrações por estudos empíricos alheios"],
    analysis_note=(
        "Trata-se de ensaio teórico, não de pesquisa empírica: a 'arquitetura' do artigo é (1) definir o objeto "
        "(campo organizacional e sua estruturação, p.3/L165-200); (2) distinguir isomorfismo competitivo e "
        "institucional (p.4-5/L312-395); (3) desenvolver os três mecanismos institucionais — coercivo "
        "(p.5/L417-493; p.6/L494-546), mimético (p.6/L547-618; p.7/L619-671) e normativo (p.7/L672-744; p.8/L745-855); e (4) derivar doze hipóteses "
        "organizacionais (A-1 a A-6) e de campo (B-1 a B-6), explicitadas como ponto de partida de um programa "
        "empírico e não como teste realizado (p.9/L910-992; p.10/L993-1118; p.11/L1119-1180). A própria seção reconhece que 'an empirical "
        "test of such predictions is beyond the scope of this paper' (p.9/L915-918)."),
    source_refs=["p.9/L910-928", "p.11/L1170-1180"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("As causas da burocratização e racionalização mudaram desde Weber: a mudança estrutural é cada vez menos dirigida pela competição ou pela necessidade de eficiência e passa a resultar de processos que tornam as organizações mais similares — o estado e as profissões são os grandes racionalizadores contemporâneos.",
      "proposition",
      "bureaucratization and other forms of organizational change occur as the result of processes that make organizations more similar without necessarily making them more efficient",
      ["p.2/L092-117"]),
    F("Uma vez estruturado um campo organizacional, os atores racionais constroem ao seu redor um ambiente que depois os constrange: decisões racionais individualmente produzem, no agregado, menos diversidade; a adoção passa a prover legitimidade, não desempenho.",
      "proposition",
      "organizational actors making rational decisions construct around themselves an environment that constrains their ability to change further in later years",
      ["p.3/L201-226", "p.4/L243-252"]),
    F("O isomorfismo institucional se dá por três mecanismos com antecedentes próprios: coercivo (influência política e problema da legitimidade), mimético (respostas padronizadas à incerteza) e normativo (profissionalização).",
      "proposition",
      "We identify three mechanisms through which institutional isomorphic change occurs, each with its own antecedents",
      ["p.5/L396-416"]),
    F("Os processos isomórficos podem avançar sem evidência de que aumentem a eficiência interna: as organizações são recompensadas por se parecerem com outras do campo — o que facilita transações, contratação e enquadramento em categorias de elegibilidade — sem que isso as torne mais eficientes.",
      "proposition",
      "each of the institutional isomorphic processes can be expected to proceed in the absence of evidence that they increase internal organizational efficiency",
      ["p.8/L856-870", "p.9/L871-873", "p.9/L874-909"]),
    F("Seis hipóteses em nível organizacional (A-1 a A-6): quanto maior a dependência de outra organização, a centralização do suprimento de recursos, a incerteza meio-fim, a ambiguidade de metas, a dependência de credenciais acadêmicas e a participação em associações, maior a isomorfia.",
      "proposition",
      "The greater the dependence of an organization on another organization, the more similar it will become to that organization in structure, climate, and behavioral focus",
      ["p.9/L928-979", "p.9/L980-992", "p.10/L993-1059"]),
    F("Seis hipóteses em nível de campo (B-1 a B-6): dependência de fonte única de suporte, transações com agências do estado, escassez de modelos alternativos visíveis, tecnologias incertas ou metas ambíguas, extensão da profissionalização e grau de estruturação elevam o nível de isomorfismo do campo.",
      "proposition",
      "The greater the extent to which an organizational field is dependent upon a single (or several similar) source of support for vital resources, the higher the level of isomorphism",
      ["p.10/L1060-1118", "p.11/L1119-1180"]),
    F("A teoria do isomorfismo institucional resolve o paradoxo de teorias macrossociais (funcionalistas e marxistas) que veem a sociedade como edifício proporcionado e as organizações como 'confusas': nem seleção natural nem controle por elites bastam para explicar a homogeneização.",
      "proposition",
      "neither of these processes is sufficient to explain the extent to which organizations have become structurally more similar",
      ["p.11/L1196-1236", "p.12/L1246-1329"]),
    F("Implicações para a teoria social e a política: foco na luta por poder e sobrevivência ausente da ecologia populacional; visão bifocal do poder (definir premissas; ponto de intervenção crítica); políticas que valorizem o pluralismo devem considerar o impacto sobre a estrutura dos campos, não só das organizações.",
      "proposition",
      "Policy makers concerned with pluralism should consider the impact of their programs on the structure of organizational fields as a whole",
      ["p.12/L1330-1365", "p.12/L1368", "p.13/L1369-1386"]),
]

CONTRIBUTION = dict(
    theoretical=("Propõe a teoria do isomorfismo institucional como resposta à pergunta que a tradição organizacional "
                 "invertia — por que tanta homogeneidade, e não variação (p.3/L133-140): desloca o motor da racionalização "
                 "da competição para o estado e as profissões (p.2/L092-117), fornece o campo organizacional estruturado "
                 "como unidade de análise e os três mecanismos coercivo-mimético-normativo (p.5/L396-416), e deriva doze "
                 "hipóteses testáveis em dois níveis como agenda empírica (p.9/L910-992; p.10/L993-1118; p.11/L1119-1180). Resolve ainda, sem seleção "
                 "nem controle por elites, o paradoxo 'sociedades espertas, organizações bobas' e adiciona à lente "
                 "institucional a dimensão de poder (gênese e interesses dos modelos legitimados) que faltava a Meyer "
                 "(p.12/L1310-1341)."),
    practical=("Para gestores e formuladores: as pressões isomórficas podem avançar sem aumento de eficiência — a "
               "conformidade é recompensada por legitimidade, elegibilidade e facilidade de transação (p.8/L856-870; p.9/L871-873); e "
               "políticas públicas que pretendem pluralismo precisam avaliar o impacto sobre a estrutura dos campos, e "
               "não apenas sobre organizações individuais (p.12/L1368; p.13/L1369-1386)."),
    limitations=("O próprio artigo delimita o alcance: as hipóteses são esquemáticas, governadas por cláusulas ceteris "
                 "paribus (tamanho, tecnologia, centralização de recursos) e não exaurem os preditores; não trata de "
                 "não-linearidades, efeitos teto nem dos indicadores de homogeneidade (p.9/L915-927; p.11/L1170-1190). "
                 "O teste empírico das predições fica explicitamente fora do escopo (p.9/L915-918)."),
    future_research=("Aponta como programa de pesquisa testar as hipóteses com dados de características de "
                     "organizações em um campo, transversalmente ou de preferência ao longo do tempo, usando como "
                     "indicador de mudança isomórfica a diminuição da variação/diversidade (menores desvios-padrão de "
                     "indicadores estruturais) (p.9/L915-927; p.10/L1060-1076); e sugere medir estruturação por "
                     "razões de concentração, estudos reputacionais e dados de redes (p.11/L1164-1169)."),
    source_refs=["p.9/L915-927", "p.10/L1060-1076", "p.11/L1170-1194", "p.12/L1368", "p.13/L1369-1386"],
)
