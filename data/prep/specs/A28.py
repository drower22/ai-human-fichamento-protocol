SUMMARY = (
    "O artigo examina o papel do talk reflexivo — a fala como forma de reflexão coletiva — na mudança de "
    "rotinas organizacionais (p.2/L038-049). A lacuna: estudos indicam que o talk reflexivo facilita ou "
    "até previne a quebra de rotinas, mas não especificam os processos pelos quais o talk está envolvido "
    "na mudança (p.2/L051-073). Com a perspectiva prática de rotinas — a interação recursiva entre "
    "aspecto performativo e ostensivo (Feldman e Pentland) — e um estudo etnográfico de um ano na CellCo, "
    "startup farmacêutica de 18 empregados (30 entrevistas, ~1.000 páginas de notas, 150h de áudio, "
    "~8.000 documentos, mais de 100 performances de shipping observadas; p.4-5/L304-410), os autores "
    "identificam três aspectos pelos quais o talk promulga reflexão coletiva — nomear e situar, "
    "vislumbrar e explorar, avaliar e questionar — e duas formas complementares: reflexão sobre ações "
    "situadas (performativo) contra o padrão, e reflexão sobre variações do padrão (ostensivo) contra "
    "performances concretas (p.3/L122-145). Adaptações flexíveis envolvem sobretudo a primeira forma; "
    "mudanças de padrão combinam ambas, com deslocamentos frequentes entre elas; e o desdobramento "
    "progressivo do talk abre oportunidades distintas de mudança — embora discussões excessivamente "
    "abstratas possam bloqueá-la (p.12-14/L1156-433). O talk é assim fonte de variação e mecanismo "
    "adicional de retenção seletiva, e a reflexão coletiva equilibra as pressões por consistência e "
    "mudança, preservando o 'pattern-in-variety' (p.15-17/L1462-688)."
)

RESEARCH_QUESTION = (
    "O artigo não enuncia uma pergunta de pesquisa formal; o objetivo declarado é examinar 'how "
    "reﬂective talk contributes to routine change' (p.2/L105-108) — isto é, como o talk promulga a "
    "reflexão coletiva e está envolvido nos diferentes tipos de mudança de rotinas, lacuna deixada "
    "aberta pela literatura (p.4/L299-303)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.2/L081-086", "p.3/L197-217"],
      "abstract, generalized idea of the routine",
      "O enquadre central: a distinção ostensivo/performativo estrutura toda a análise e os dois tipos de mudança."),
    V("T2", "uses", ["p.2/L050-056", "p.5/L441-446"],
      "Talk is at the heart of all organizations",
      "O fenômeno estudado: o talk como ação que expressa reflexividade e promulga reflexão coletiva (perspectiva prática heideggeriana)."),
    V("T3", "uses", ["p.3/L218-228", "p.4/L229-232", "p.15/L1548-555", "p.16/L1556-587"],
      "variations that are selectively retained in the abstract, general pattern of the routine",
      "A segunda contribuição: o talk reflexivo como fonte de variação e mecanismo adicional de seleção estende o modelo evolucionário."),
    V("T4", "uses", ["p.3/L203-217", "p.16/L1640-648"],
      "pattern-in-variety",
      "A terceira contribuição: a reflexão coletiva como modo de equilibrar o 'paradoxo do mundo (n)unca mutável'."),
    V("T5", "discusses", ["p.4/L247-260", "p.4/L286-296"],
      "group-level reﬂection",
      "A literatura que indica a importância da reflexão grupal sem analisar como o talk a viabiliza — a lacuna do estudo."),
    V("T6", "discusses", ["p.2/L054-056"],
      "collective sensemaking, collective learning and, more generally, collective reﬂection",
      "Citado entre as funções do talk; a lente adotada é a de reflexão coletiva, não de sensemaking."),
    V("T7", "uses", ["p.3/L190-197", "p.9/L817-830"],
      "effortful accomplishment",
      "As adaptações idiossincráticas promulgadas via talk são descritas como effortful accomplishment."),
    V("T8", "discusses", ["p.15/L1530-538"],
      "institutionalized spaces for reﬂecting on routines, such as debrieﬁng meetings",
      "Estendido: o estudo mostra como o talk dentro desses espaços promulga a reflexão coletiva."),
    V("T9", "discusses", ["p.3/L165-185"],
      "highly automatic or mindless behaviors",
      "A visão tradicional de rotinas como comportamento automático que a perspectiva prática superou."),
    V("T10", "discusses", ["p.17/L1729-740"],
      "talk may be less prevalent or replaced by other genres of communication",
      "Invocado na limitação: em organizações maiores outros gêneros podem suplantar o talk."),
    V("T11", "does_not_use", [], "",
      "Poder/política tratado explicitamente como limitação (poucos conflitos na CellCo), não como lente mobilizada."),
    V("T12", "does_not_use", [], "",
      "Aspectos linguísticos do talk (retórica, persuasão) são explicitamente delegados a pesquisa futura — o foco é a função do talk, não a análise do discurso."),
    V("T13", "does_not_use", [], "",
      "Ausente; a mudança estudada é endógena e micro-processual, sem pressões institucionais."),
    V("T14", "does_not_use", [], "",
      "Ação analisada pela perspectiva prática de rotinas, não por redes de atuantes."),
    V("T15", "does_not_use", [], "",
      "Ausente — o talk reflexivo não é tratado como recurso estratégico."),
]

KEY_CONCEPTS = [
    dict(concept="Talk reflexivo (reflective talk)",
         definition="A fala empregada como forma de reflexão coletiva — quando atores conversam sobre a rotina e seu padrão para nomear problemas, imaginar alternativas e avaliá-las em conjunto.",
         quote="reﬂective talk—that is, when actors engage in talk as a form of collective reﬂection",
         source_refs=["p.5/L441-446"]),
    dict(concept="Aspecto ostensivo × performativo",
         definition="O ostensivo é a ideia abstrata e generalizada da rotina; o performativo são as ações específicas de pessoas em tempos e lugares. Os dois aspectos interagem recursivamente e definem os dois tipos de mudança.",
         quote="abstract, generalized idea of the routine",
         source_refs=["p.2/L081-086", "p.3/L197-217"]),
    dict(concept="Adaptação flexível × mudança de padrão",
         definition="Dois tipos de mudança de rotina: desvios temporários do padrão em performances específicas versus alterações duradouras no padrão ostensivo — ligados pelo processo de variação e retenção seletiva.",
         quote="the ﬂexible adaptation of individual performances",
         source_refs=["p.3/L218-228"]),
    dict(concept="Nomear/situar, vislumbrar/explorar, avaliar/questionar",
         definition="Os três aspectos pelos quais o talk promulga a reflexão coletiva: situar o objeto de discussão em contexto, gerar e explorar alternativas de promulgação, e avaliá-las criticamente de ângulos diferentes.",
         quote="naming and situating problems or opportunities",
         source_refs=["p.3/L122-130", "p.7/L558-595"]),
    dict(concept="Variação e retenção seletiva",
         definition="O processo evolucionário endógeno pelo qual variações nas performances são retidas seletivamente no padrão ostensivo — o talk reflexivo atua como fonte de variação e estágio adicional de seleção.",
         quote="variations that are selectively retained in the abstract, general pattern of the routine",
         source_refs=["p.4/L229-232", "p.16/L1562-587"]),
    dict(concept="Desdobramento progressivo do talk",
         definition="À medida que a conversa avança, o talk revela aspectos relevantes adicionais e abre oportunidades distintas de levantar tópicos e conectar elementos da rotina, promovendo reflexão e mudança.",
         quote="reﬂective talk also provided distinct opportunities for routine change by highlighting the relevance of other elements",
         source_refs=["p.12/L1161-168"]),
]

METHODOLOGY = dict(
    study_type="empírico qualitativo (etnografia)",
    design="Etnografia de um ano na CellCo — startup farmacêutica spin-off universitária de 18 empregados — focada na rotina de expedição (shipping), ilustrada por vinhetas detalhadas de talk gravado em áudio; acesso por imersão de 2–3 dias/semana e participação em reuniões e eventos sociais",
    sample_type="os membros da CellCo envolvidos na rotina de shipping (CEO, funcionários de laboratório, gerente de qualidade, export manager); seis rotinas acompanhadas, com shipping como caso saliente",
    sample_size=18,
    sector="indústria farmacêutica — produção de placas e tecidos celulares",
    period="12 meses de campo contínuo; mais de 100 performances de shipping observadas",
    methods=["observação etnográfica não-participante com notas de campo expandidas em 24h", "gravação de áudio de reuniões e talk durante performances (~150h)", "30 entrevistas semiestruturadas (30min–2,5h) complementadas por discussões informais", "documentos e dados arquivísticos (~8.000 documentos internos)"],
    analysis_note=("Análise iterativa em cinco estágios: (1) timeline de eventos das seis rotinas, com foco em "
                   "shipping; (2) códigos descritivos dos usos do talk, com ampliação da literatura para "
                   "estudos práticos — a perspectiva heideggeriana (Dreyfus; Tsoukas) revelou o talk reflexivo "
                   "como foco; (3) identificação de todas as instâncias de talk sobre mudar a rotina e "
                   "codificação das três categorias (nomear/situar, vislumbrar/explorar, avaliar/questionar); "
                   "(4) comparação das instâncias e distinção das duas formas de talk reflexivo; (5) análise "
                   "de como as formas e os deslocamentos entre elas promulgavam mudança flexível ou de padrão "
                   "(p.5/L411-456, p.7/L558-627)."),
    source_refs=["p.4/L304-342", "p.5/L343-410", "p.5/L411-456", "p.7/L558-627"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("O talk promulga reflexão coletiva por três aspectos: nomear e situar problemas ou oportunidades em relação aos aspectos performativo e ostensivo; vislumbrar e explorar conjuntamente formas alternativas de promulgação; e avaliar e questionar as sugestões de ângulos diferentes — em prática, entrelaçados.",
      "empirical",
      "We clustered the ways in which talk supports the enactment of collective reﬂection into three distinct categories",
      ["p.5/L447-456", "p.7/L558-595"]),
    F("Duas formas complementares de talk reflexivo emergem: uma reflete sobre ações situadas (performativo) contra o pano de fundo do padrão ostensivo; a outra reflete sobre padrões alternativos (ostensivo) contra performances concretas ou imaginadas — distintas no que vislumbram e avaliam.",
      "empirical",
      "we decided to distinguish between the two forms of reﬂective talk that we described earlier",
      ["p.7/L596-617", "p.12/L1103-134"]),
    F("A adaptação flexível de performances tende a envolver a primeira forma de talk; mudanças no padrão da rotina tendem a combinar as duas formas, com deslocamentos frequentes — refletir sobre ações situadas recontextualiza o discutido em abstrato e facilita a promulgação das mudanças.",
      "empirical",
      "the ﬂexible adaptation of speciﬁc routine performances tends to involve the former form of reﬂective talk, whereas changes in the routine’s pattern tend to involve a combination of both forms",
      ["p.3/L139-145", "p.13/L1281-326", "p.14/L1327-362"]),
    F("O talk reflexivo permite adaptar uma performance e ao mesmo tempo manter a consistência: as variações são reconhecidas como idiossincráticas e o padrão é implicitamente reconfirmado; mas o talk também pode bloquear variações — como na recusa da sugestão de eliminar a membrana respirável.",
      "empirical",
      "reﬂective talk allows the participants to adapt a speciﬁc performance and at the same time maintain consistency in future performances",
      ["p.9/L826-830", "p.9/L832-849", "p.11/L1069-093", "p.12/L1094-102"]),
    F("O desdobramento progressivo do talk cria oportunidades distintas de mudança — atores aproveitam a conversa para endereçar problemas já reconhecidos (centralização do shipping, documento ligando pedido e expedição) — e conversas que começam sem intenção reflexiva podem revelar problemas; já discussões excessivamente abstratas sobre contingências podem impedir a promulgação.",
      "empirical",
      "reﬂective talk also provided distinct opportunities for routine change by highlighting the relevance of other elements",
      ["p.12/L1161-182", "p.14/L1407-433"]),
    F("O talk reflexivo é fonte de variação — ao vislumbrar alternativas — e mecanismo adicional de seleção — ao eliminar alternativas por avaliação —, inclusive gerando variações deliberadas no aspecto ostensivo; e a reflexão coletiva equilibra as pressões por consistência e mudança, comunicando o 'pattern-in-variety'.",
      "model",
      "reﬂective talk acts as a mechanism of selection when actors eliminate certain alternatives by evaluating and questioning them",
      ["p.16/L1562-587", "p.16/L1640-648", "p.17/L1683-688"]),
]

CONTRIBUTION = dict(
    theoretical=("Três contribuições declaradas: (1) avança a compreensão da reflexão em rotinas ao mostrar como o talk "
                 "produz formas distintas e complementares de reflexão coletiva; (2) estende o modelo evolucionário de "
                 "mudança endógena (Feldman e Pentland 2003), identificando no talk reflexivo fonte de variação das "
                 "performances e estágio adicional de retenção seletiva — inclusive de variações no próprio aspecto "
                 "ostensivo, que precisam ser recontextualizadas em performances concretas; (3) mostra a reflexão "
                 "coletiva como modo adicional de equilibrar as pressões concorrentes por consistência e mudança "
                 "(p.3/L146-162; p.15/L1462-500)."),
    practical=("Para praticantes: examinar a presença das diferentes formas de talk reflexivo e prover espaços para ele "
               "aumenta a variabilidade das rotinas sem impactos negativos diretos — permite experimentar ideias em "
               "comunicação antes de promulgá-las — e ajuda a reconstruir senso de continuidade diante de mudanças "
               "radicais (p.18/L1814-874)."),
    limitations=("O estudo foca o talk numa organização pequena e empreendedora, de comunicação oral frequente — em "
                 "organizações maiores, gêneros escritos/assíncronos podem suplantá-lo; a escassez de conflitos "
                 "políticos limitou a observação de como poder e autoridade condicionam quem participa e quem é "
                 "ouvido; e os aspectos linguísticos do talk ficaram fora do escopo (p.17/L1724-785)."),
    future_research=("Comparar como diferentes formas de comunicação (síncrona × assíncrona, oral × escrita) promulgam "
                     "reflexão coletiva; estudar a relação entre poder e rotinas via talk reflexivo; e investigar como "
                     "aspectos linguísticos (estilos retóricos, persuasão, 'taglines') moldam a reflexão coletiva e as "
                     "dinâmicas de rotinas (p.17/L1736-785)."),
)
