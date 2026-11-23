SUMMARY = (
    "O artigo analisa como ocorreu o processo de sensegiving nas narrativas produzidas pela Samarco após o "
    "rompimento da barragem de Fundão (novembro de 2015), entendido como prática estratégica dentro do "
    "strategizing de uma organização em crise, sob a perspectiva da estratégia como prática social (SAP) "
    "(p.1/L021-025; p.4/L138-140). Trata-se de pesquisa qualitativa baseada em dados secundários divulgados "
    "pela própria empresa entre 5/11/2015 e agosto de 2017: 307 arquivos do site da Samarco (893 páginas), "
    "297 arquivos do site da Fundação Renova (647 páginas) e 52 vídeos do canal do YouTube Samarco Mineração "
    "(191 minutos) (p.8/L335-342; p.8/L343-366). O trabalho mobiliza os construtos de sensemaking e sensegiving "
    "(Weick; Gioia & Chittipeddi; Maitlis & Lawrence) e a abordagem narrativa organizacional (Vaara, Sonenshein "
    "& Boje) para apreender como a empresa influenciou o sentido atribuído ao desastre (p.6/L234-277; "
    "p.7/L284-299). Metodologicamente, uma análise de conteúdo com Atlas.ti identificou os direcionamentos de "
    "conteúdo em oito períodos, dos quais se inferiram seis momentos narrativos analisados pela abordagem "
    "interacional de Shuman (p.8/L368-372; p.9/L380-399). Os resultados mostram que a Samarco construiu uma "
    "grande narrativa que a posiciona como heroína e vítima de uma 'injustiça' — a impossibilidade de operar — "
    "evoluindo de esclarecimentos e comprometimento, pelo discurso responsivo, o 'recomeço' da Fundação Renova, "
    "a justificação da inação e a ênfase nos impactos econômicos, até a conclamação pela volta das operações "
    "(p.10/L487-496; p.11/L497-501; p.19/L849-864). As contribuições teóricas apontam o sensegiving como prática "
    "proeminente no strategizing em crises, a abertura da estratégia sob pressão social proporcional à "
    "magnitude da crise, e a necessidade de incorporar a dimensão ético-moral da práxis à SAP "
    "(p.19/L879-895; p.20/L896-928)."
)

RESEARCH_QUESTION = (
    "O artigo não enuncia uma pergunta de pesquisa em forma interrogativa; declara como objetivo 'analisar "
    "como ocorreu o processo de sensegiving nas narrativas da Samarco, como uma prática estratégica dentro "
    "do strategizing de uma organização em crise' (p.1/L021-025; p.4/L138-140). Reconstruída como pergunta "
    "implícita: como a Samarco, por meio de suas narrativas, buscou influenciar o sentido atribuído ao "
    "desastre corporativo do rompimento da barragem de Fundão?"
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.5/L204-211", "p.5/L223-229", "p.11/L531-534", "p.20/L902-908"],
      "a perspectiva da estratégia como prática social evidencia o strategizing",
      "Lente principal: narrativas e sensegiving são apreendidos como práticas estratégicas na perspectiva da SAP."),
    V("T2", "uses", ["p.11/L531-537", "p.11/L538-542", "p.19/L879-885"],
      "o strategizing comporta todas as ações, interações e negociações de sentido a partir das quais as práticas organizacionais se estabelecem",
      "Construto que nomeia o processo analisado: o sensegiving narrativo é prática inerente ao strategizing pós-desastre."),
    V("T3", "uses", ["p.6/L244-254", "p.6/L262-270", "p.18/L820-823"],
      "processo de influência sobre a construção de significados (sensemaking) do outro em direção a uma redefinição preferível da realidade organizacional",
      "Objeto principal de análise; cada momento narrativo é lido como exercício de sensegiving."),
    V("T4", "discusses", ["p.6/L236-243", "p.6/L271-277", "p.19/L869-876"],
      "sensemaking envolve transformar as circunstâncias em uma situação que seja compreendida explicitamente em palavras e que servem como um suporte para ação",
      "Contraparte necessária do sensegiving, com seção própria no referencial; a análise usa o par, mas foca o sensegiving — no achado, a ausência de espaço para sensemaking alheio."),
    V("T5", "uses", ["p.5/L204-217", "p.7/L284-299", "p.7/L300-323", "p.8/L324-334"],
      "as narrativas sejam relevantes para compreender o fenômeno e se tornam um recurso importante para a sua apreensão na perspectiva da SAP",
      "Unidade de análise; as seis características das narrativas de Vaara, Sonenshein e Boje (2016) estruturam a justificativa do método."),
    V("T6", "uses", ["p.5/L221-223", "p.8/L331-334", "p.17/L776-778", "p.18/L816-820"],
      "dependente de um processo de legitimação social (Vaara & Monin, 2010; Whittington, 2017)",
      "A finalidade do sensegiving analisado é recuperar imagem e legitimidade rumo à retomada; cada narrativa é avaliada por seu papel legitimador."),
    V("T7", "discusses", ["p.11/L518-519", "p.19/L892-895", "p.20/L896-901"],
      "diante da pressão pela abertura dessa estratégia (Hautz, Seidl, & Whittington, 2017)",
      "Interpreta a estratégia tornado 'assunto aberto' pós-desastre e fundamenta a segunda contribuição teórica; não estrutura o referencial."),
    V("T8", "discusses", ["p.4/L152-182", "p.5/L183-185"],
      "a prática social é representada pelos padrões de comportamento permeados pelas conexões de diversos elementos",
      "Fundação teórica da SAP (Reckwitz, Bourdieu, Giddens, Schatzki, De Certeau) desenvolvida no referencial; a lente operacional é a SAP."),
    V("T9", "discusses", ["p.2/L049-050", "p.5/L186-187", "p.20/L902-924"],
      "se começarmos a discutir a dimensão ética da estratégia, conforme conclama Tsoukas (2018)",
      "Motiva a pesquisa e ancora a terceira contribuição (ética da práxis); não é usada como lente analítica dos dados."),
    V("T10", "discusses", ["p.3/L130-135", "p.19/L886-887"],
      "a metáfora do homo narrans para caracterizar a natureza humana (FISHER, 1984)",
      "Metáfora que justifica a centralidade das narrativas; suporte retórico à abordagem narrativa."),
    V("T11", "discusses", ["p.2/L085-086", "p.11/L535-537", "p.14/L644"],
      "a Samarco, consequentemente perde sua licença social para operar",
      "Conceito que nomeia o ativo perdido no desastre; usado para caracterizar o caso, sem desenvolvimento teórico próprio."),
    V("T12", "does_not_use", [], "", "Stakeholders aparecem apenas como termo solto ('stakeholders, interessados', p.12/L547); a teoria de Freeman não é mencionada nem mobilizada."),
    V("T13", "does_not_use", [], "", "Apesar do tema 'legitimidade', DiMaggio & Powell e o vocabulário de isomorfismo não são citados."),
    V("T14", "does_not_use", [], "", "A recuperação da imagem organizacional é tema do caso e Valdebenito (2013) é citado como trabalho relacionado (p.5/L222-223), mas a tipologia de Benoit não é nomeada nem aplicada."),
]

KEY_CONCEPTS = [
    dict(concept="Sensegiving",
         definition="Processo de influência sobre a construção de significados (sensemaking) do outro em direção a uma redefinição preferível da realidade organizacional.",
         quote="processo de influência sobre a construção de significados (sensemaking) do outro em direção a uma redefinição preferível da realidade organizacional",
         source_refs=["p.6/L244-246"]),
    dict(concept="Strategizing",
         definition="O fazer estratégico como processo contínuo de ações, interações e negociações de sentido a partir das quais as práticas organizacionais se estabelecem.",
         quote="o strategizing comporta todas as ações, interações e negociações de sentido a partir das quais as práticas organizacionais se estabelecem",
         source_refs=["p.11/L531-535"]),
    dict(concept="Narrativas organizacionais",
         definition="Construções discursivas temporais que fornecem meio para sensemaking e sensegiving individual, social e organizacional, com papel performativo na estabilidade e mudança organizacional.",
         quote="narrativas organizacionais são construções discursivas temporais que proporcionam um meio para o sensemaking e o sensegiving individual, social e organizacional",
         source_refs=["p.7/L300-303"]),
    dict(concept="Desastre corporativo",
         definition="Evento de grandes proporções causado por uma organização, com impactos socioambientais severos, que produz crise e motiva processos de sensegiving.",
         quote="um período de crise organizacional ou de enfrentamento a um desastre corporativo são episódios que podem gerar a motivação – isto é, ser um gatilho – para os processos de sensegiving",
         source_refs=["p.6/L266-270"]),
    dict(concept="Legitimidade / licença social",
         definition="Reconhecimento social do propósito e da conduta da organização; a Samarco perde a licença social para operar e orienta seu sensegiving para recuperá-la.",
         quote="a Samarco, consequentemente perde sua licença social para operar e, assim, seu strategizing perde seu lastro operacional",
         source_refs=["p.11/L535-537"]),
    dict(concept="Momentos narrativos",
         definition="Períodos inferidos da análise de conteúdo em que a empresa altera significativamente o enfoque do conteúdo publicado, compondo o enredo da grande narrativa pós-rompimento.",
         quote="a cada três ou quatro meses a Samarco alterou de maneira significativa os temas que eram publicados",
         source_refs=["p.10/L451-452", "p.10/L487-496", "p.11/L497-501"]),
]

METHODOLOGY = dict(
    study_type="empírico (qualitativo)",
    design="Estudo de caso único baseado em dados secundários, com nível de análise organizacional e unidade de análise nas narrativas organizacionais da Samarco.",
    sample_type="documentos e vídeos publicados pela Samarco e pela Fundação Renova (307 arquivos do site da Samarco, 893 páginas; 297 arquivos do site da Fundação Renova, 647 páginas; 52 vídeos do YouTube, 191 minutos)",
    sample_size=None,
    sector="mineração (Samarco) e desastre corporativo",
    period="5 de novembro de 2015 (rompimento) a agosto de 2017",
    methods=["análise de conteúdo (Saldaña) com Atlas.ti", "construção de linha do tempo e inferência de momentos narrativos", "análise de narrativa interacional (Shuman)"],
    analysis_note=("A análise procedeu em fases: (1) coleta de dados secundários nos sites da Samarco e da Fundação Renova e no canal do YouTube "
                   "(p.8/L338-366); (2) análise de conteúdo por leitura flutuante extraindo tipo de documento, tema geral e mensagem geral "
                   "(p.8/L368-372); (3) inferência de oito enfoques de conteúdo e seis momentos narrativos (p.10/L453-496; p.11/L497-501); e (4) análise de "
                   "narrativa das seis narrativas emblemáticas, na sequência de tellability, posicionamento, formato, intertextualidade, "
                   "categoria sociopolítica e mote, com análise cronológica (p.9/L386-399; p.9/L433-437)."),
    source_refs=["p.8/L335-372", "p.9/L380-437", "p.10/L449-496", "p.11/L497-501"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("A Samarco construiu, no período pós-rompimento, seis momentos narrativos: (1) esclarecimentos e comprometimento; (2) discurso responsivo de ação e proximidade; (3) narrativa de renascimento com a Fundação Renova; (4) narrativa defensiva que justifica a inação pela magnitude do desastre; (5) discurso sobre a não operação e seus impactos econômicos; e (6) narrativa da necessidade de voltar a operar.",
      "empirical",
      "infere-se a construção de uma narrativa baseada em seis momentos, os quais se direcionam ao slogan",
      ["p.10/L487-496", "p.11/L497-501"]),
    F("A sequência dos momentos compõe uma grande narrativa que posiciona a Samarco como heroína e vítima de uma 'injustiça' — a impossibilidade de operar — e estabelece a retomada das operações como única solução possível.",
      "empirical",
      "Toda a construção dessa narrativa posiciona a Samarco como herói e vítima de uma injustiça: a impossibilidade de voltar a operar",
      ["p.19/L849-860"]),
    F("A narrativa da empresa opera por negociação de vozes sucessivas (CEOs da Vale e BHP, Samarco, Fundação Renova, novo diretor-presidente) e sem espaço para sensemaking por outros atores: publicações respondem a questionamentos sem expô-los e só veiculam a versão da organização.",
      "empirical",
      "Ela não dá espaço aos questionados e só expõe seu lado, seu sentindo, sua versão. Ou ainda, quando abre algum tipo de espaço, são para versões que corroboram seu processo de sensegiving",
      ["p.19/L866-876"]),
    F("As escolhas discursivas dos momentos exercem função estratégica: minimizar o evento ('acidente'), omitir responsabilidade, transferir protagonismo à Fundação Renova, deslocar culpa para quem impede a retomada e coagir pela ameaça de impactos econômicos.",
      "empirical",
      "os locutores, ao escolherem a palavra “acidente”, amenizam o acontecimento",
      ["p.12/L576-580", "p.18/L833-836"]),
    F("O sensegiving se constitui como prática estratégica proeminente no strategizing de organizações em crise, em que a narrativa figura como recurso performativo de estabilidade e mudança.",
      "proposition",
      "o sensegiving se constitui como uma prática estratégica proeminente no strategizing de organizações em crise",
      ["p.19/L879-890"]),
    F("Em situações de crise, o grau de abertura da estratégia (transparência e inclusão) necessário para a legitimação parece proporcional ao tamanho da crise, do desastre ou da necessidade reputacional.",
      "proposition",
      "O grau de transparência e inclusão necessário nesse processo de abertura parece ser proporcional ao tamanho da crise, desastre ou necessidade reputacional",
      ["p.19/L892-895", "p.20/L896-901"]),
]

CONTRIBUTION = dict(
    theoretical=("Três contribuições teóricas: (1) identificar o sensegiving como prática estratégica proeminente no strategizing de organizações "
                 "em crise, com as narrativas como recurso performativo (p.19/L879-890); (2) sugerir que o grau de abertura da estratégia "
                 "(transparência e inclusão) é proporcional à magnitude da crise (p.19/L892-895; p.20/L896-901); e (3) dar corpo à conclamação de Tsoukas (2018) "
                 "pela dimensão ético-moral da práxis na SAP, ao evidenciar a tentativa de desresponsabilização que o caso torna visível "
                 "(p.20/L902-924)."),
    practical=("Não há seção de implicações gerenciais própria; o estudo indica como contribuição metodológica o caminho seguido (análise de "
               "conteúdo sobre grande volume de dados secundários + análise de narrativa interacional) para apreender sensegiving e estratégia "
               "sob a SAP (p.9/L430-432)."),
    limitations=("Não há seção de limitações declarada; o próprio estudo se reconhece como 'uma versão' narrativa sobre dados secundários "
                 "produzidos pela organização (p.19/L838-843)."),
    future_research=("Sugere que pesquisas futuras amplifiquem os três caminhos de contribuição teórica — sensegiving no strategizing em crise, "
                     "abertura da estratégia proporcional à crise e ética da práxis na SAP (p.20/L924-928)."),
    source_refs=["p.19/L879-895", "p.20/L896-928"],
)
