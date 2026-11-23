SUMMARY = (
    "O ensaio apresenta a Hermenêutica de Profundidade (HP) de J. B. Thompson como referencial "
    "teórico-metodológico para investigar fenômenos sociais complexos, fundamentada na Teoria Social "
    "Crítica e na hermenêutica ricoeuriana (p.3/L074-079; p.7/L223-245). Após reconstruir a gênese da "
    "hermenêutica — da exegese dos textos sagrados à ciência da compreensão, à base metodológica das "
    "ciências humanas (Dilthey), à hermenêutica do Dasein (Heidegger, Gadamer) e ao sistema de "
    "interpretação de Ricoeur (p.4-6/L119-200) —, o artigo detalha o método: a interpretação da doxa como "
    "pré-etapa etnográfica e o enfoque tríplice de análise sócio-histórica, análise formal/discursiva e "
    "interpretação/re-interpretação (p.9-15/L286-563). A aplicabilidade é demonstrada no caso da EaD "
    "superior no Brasil: os atos normativos como formas simbólicas, analisados por Ciclos de Codificação, "
    "Análise de Conteúdo e Análise Axiológica, revelam uma legislação de baixo poder regulador cuja "
    "função foi legitimar uma modalidade já aceita e permitir a livre atuação das organizações privadas — "
    "o que favoreceu a formação de um oligopólio (p.15-21/L555-781). O estudo responde à questão de "
    "como a HP contribui para compreender as dinâmicas sociais em cenários institucionais, destacando "
    "a contextualização sócio-histórica e o tensionamento interpretativo — e as armadilhas do "
    "internalismo e do reducionismo (p.4/L110-118; p.22/L795-817)."
)

RESEARCH_QUESTION = (
    "O artigo formula a questão explicitamente: 'como a Hermenêutica de Profundidade pode contribuir "
    "para a compreensão das dinâmicas sociais em cenários institucionais?' (p.4/L112-114). Para ilustrar "
    "a aplicabilidade, os autores analisam a formação de um oligopólio na Educação a Distância no "
    "Brasil, investigando como as regulações influenciaram a consolidação de um pequeno grupo de "
    "organizações privadas no setor (p.4/L115-118)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.6/L197-200", "p.9/L286-293"],
      "1) Análise Sócio-histórica; 2) Análise Formal ou Discursiva; e 3) Interpretação/Re-interpretação",
      "Objeto do ensaio e método demonstrado no caso da EaD — enfoque tríplice sobre formas simbólicas."),
    V("T2", "uses", ["p.7/L223-230", "p.7/L238-245"],
      "contribuem para a reprodução das relações de poder e dominação",
      "Uma das duas proposições filosóficas da HP; sustenta a criticidade da fase de re-interpretação."),
    V("T3", "discusses", ["p.4/L119-146", "p.5/L179-185"],
      "um processo em que o significado se revelaria para além do conteúdo manifesto",
      "A genealogia da hermenêutica reconstruída como primeira base da HP — fundamento, não ferramenta."),
    V("T4", "discusses", ["p.11/L357-374", "p.23/L834-840"],
      "um momento etnográfico da pesquisa, realizado com base em entrevistas, observações participantes",
      "Pré-etapa da HP descrita como indispensável, mas o próprio estudo admite não tê-la aprofundado — limite declarado."),
    V("T5", "uses", ["p.14/L490-494", "p.17/L626-634"],
      "optaram pelos Ciclos de Codificação (Saldaña, 2015) e, posteriormente, pela Análise de Conteúdo (Bardin, 2011)",
      "As técnicas efetivamente empregadas na Análise Formal dos atos normativos, com auxílio do Atlas.ti."),
    V("T6", "uses", ["p.17/L635-640"],
      "A fase de interpretação dos achados foi realizada por meio da Análise Axiológica dos normativos",
      "O método de Nishiyama operacionaliza a re-interpretação dos normativos da EaD."),
    V("T7", "uses", ["p.16/L582-591", "p.21/L772-781"],
      "o sancionamento é um mecanismo formal emitido por meio de documentos normativos, os quais buscam desestimular o desvio ou atribuir-lhe legitimidade",
      "A tríade desvio–sancionamento–legitimidade de Dellaposta, Nee e Opper interpreta a institucionalização da EaD."),
    V("T8", "uses", ["p.7/L227-230", "p.16/L574-581"],
      "as estratégias de operação da ideologia",
      "O conceito de legitimidade de Thompson é o eixo da leitura crítica das formas simbólicas normativas."),
    V("T9", "discusses", ["p.10/L330-336", "p.12/L413-418"],
      "resultante de processos de diferenciação social, vinculados aos modos de ser e às formas de apreensão do mundo",
      "Bourdieu é citado para o aspecto estrutural das formas simbólicas e o 'campo de interação' da análise sócio-histórica."),
    V("T10", "does_not_use", [], "",
      "Listada no Quadro 2 entre as técnicas possíveis e sugerida como abordagem complementar para mitigar internalismo/reducionismo — não empregada no caso."),
    V("T11", "discusses", ["p.18/L647-653", "p.23/L838-840"],
      "a política neoliberal que influenciou a composição do normativo fez com que as atividades básicas da população fossem descentralizadas",
      "Contexto interpretativo do caso; mercantilização e financeirização reaparecem como conceitos a investigar na agenda futura."),
    V("T12", "does_not_use", [], "",
      "Armadilha plausível: o caso trata de legitimidade e mudança institucional, mas via Dellaposta/Nee/Opper (mudança endógena) e Thompson — DiMaggio & Powell não são citados."),
    V("T13", "does_not_use", [], "",
      "Ausente; a análise é hermenêutica e institucional, não de redes de atores."),
    V("T14", "does_not_use", [], "",
      "Os Ciclos de Codificação de Saldaña são técnica auxiliar da análise formal, não grounded theory; Glaser & Strauss não são citados."),
    V("T15", "does_not_use", [], "",
      "Ausente; a agência interpretativa vem da hermenêutica de Thompson, não de Giddens."),
]

KEY_CONCEPTS = [
    dict(concept="Hermenêutica de Profundidade (HP)",
         definition="Referencial teórico-metodológico de J. B. Thompson para interpretar formas simbólicas, articulando análise sócio-histórica, análise formal/discursiva e interpretação/re-interpretação — dimensões de um mesmo processo, não estágios sequenciais.",
         quote="1) Análise Sócio-histórica; 2) Análise Formal ou Discursiva; e 3) Interpretação/Re-interpretação",
         source_refs=["p.6/L197-200", "p.8/L274-280", "p.9/L286-293"]),
    dict(concept="Formas simbólicas",
         definition="Construções significativas — ações, falas, textos e imagens — que demandam interpretação e são delineadas por cinco aspectos: intencional, convencional, estrutural, referencial e contextual.",
         quote="construções significativas, que demandam uma interpretação",
         source_refs=["p.9/L294-300", "p.9/L304-319", "p.10/L320-354"]),
    dict(concept="Interpretação da doxa",
         definition="Pré-etapa da HP: a hermenêutica da vida cotidiana, que interpreta as opiniões, crenças e entendimentos compartilhados pelos sujeitos — 'momento etnográfico' que dá o ponto de partida à investigação.",
         quote="um momento etnográfico da pesquisa, realizado com base em entrevistas, observações participantes",
         source_refs=["p.11/L357-374"]),
    dict(concept="Análise sócio-histórica",
         definition="Primeira etapa do enfoque tríplice: reconstruir as condições sociais e históricas de produção, circulação e recepção das formas simbólicas — situações espaço-temporais, campos de interação, instituições, estrutura social e meios técnicos.",
         quote="reconstruir as condições sociais e históricas de produção, circulação e recepção das formas simbólicas",
         source_refs=["p.11/L383-389", "p.12/L394-436"]),
    dict(concept="Re-interpretação",
         definition="Última fase do enfoque tríplice: retomada crítica e criativa dos resultados, em que o hermeneuta 'realiza uma interpretação da interpretação', podendo divergir do sentido atribuído pelos próprios sujeitos.",
         quote="re-interpreta aquilo que já foi interpretado",
         source_refs=["p.14/L521-525", "p.15/L526-545"]),
    dict(concept="Desvio, sancionamento e legitimidade",
         definition="Mecanismos endógenos de mudança institucional: o desvio se afasta do padrão aceito, o sancionamento é o mecanismo formal que o desestimula ou legitima via documentos normativos, e a legitimidade ocorre quando o desvio é compartilhado e aceito.",
         quote="o sancionamento é um mecanismo formal emitido por meio de documentos normativos, os quais buscam desestimular o desvio ou atribuir-lhe legitimidade",
         source_refs=["p.16/L582-591"]),
]

METHODOLOGY = dict(
    study_type="ensaio teórico-metodológico com demonstração de caso",
    design="Ensaio que discute e demonstra as etapas da Hermenêutica de Profundidade e ilustra sua aplicabilidade reexaminando um caso já estudado: a formação de um oligopólio na EaD superior brasileira, com base nos atos normativos federais como formas simbólicas.",
    sample_type="atos normativos federais da EaD — leis, decretos, portarias, pareceres e instruções normativas (caso secundário de Slongo Garcia, 2019, e Slongo Garcia et al., 2024)",
    sample_size=None,
    sector="educação superior a distância",
    period="análise sócio-histórica dos anos 1900 a 2020, com ênfase na regulamentação de 1988–2017",
    methods=["Hermenêutica de Profundidade (análise sócio-histórica, análise formal/discursiva, re-interpretação)", "Ciclos de Codificação (Saldaña)", "Análise de Conteúdo (Bardin) com software Atlas.ti", "Análise Axiológica (Nishiyama)"],
    analysis_note=("É um ensaio de demonstração, não um estudo empírico primário: o caso EaD reutiliza os "
                   "achados de Slongo Garcia (2019) e Slongo Garcia et al. (2024), que aplicaram Ciclos de "
                   "Codificação e Análise de Conteúdo aos atos normativos com o Atlas.ti, e Análise "
                   "Axiológica na interpretação (p.15/L555-563; p.17/L626-640). A pré-etapa da doxa é "
                   "declarada não aprofundada — o que os autores registram como limite e agenda "
                   "(p.22-23/L807-843)."),
    source_refs=["p.15/L555-563", "p.17/L626-640", "p.23/L834-843"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("A HP se articula em duas proposições filosóficas — a hermenêutica fenomenológica (Husserl, Heidegger, Gadamer, Ricoeur) e a Teoria Social Crítica (Marx, Horkheimer, Adorno, Habermas) — e se estrutura na pré-etapa da doxa e no enfoque tríplice: análise sócio-histórica, análise formal/discursiva e re-interpretação.",
      "proposition",
      "1) Análise Sócio-histórica; 2) Análise Formal ou Discursiva; e 3) Interpretação/Re-interpretação",
      ["p.7/L231-245", "p.9/L286-293"]),
    F("A interpretação da doxa é a pré-etapa indispensável da HP — um 'momento etnográfico' que interpreta os entendimentos compartilhados dos sujeitos; negligenciá-la é ignorar como os sujeitos interpretam as formas simbólicas, mas considerá-la única fase é abstrair o que torna o método profundo.",
      "proposition",
      "não considerar essa pré-etapa é negligenciar a maneira com que os sujeitos que constituem este mundo social interpretam as formas simbólicas",
      ["p.11/L357-374"]),
    F("A análise sócio-histórica reconstrói as condições de produção, circulação e recepção das formas simbólicas — no caso da EaD, os atos normativos foram as formas simbólicas que substituíram correios, rádio e televisão quando a modalidade passou a incorporar o ensino superior e cumprir metas do poder público.",
      "empirical",
      "os atos normativos foram as formas simbólicas utilizadas",
      ["p.11/L383-389", "p.16/L599-602", "p.17/L620-625"]),
    F("A leitura hermenêutica dos normativos mostra uma legislação de baixo poder regulador cuja função foi legitimar uma modalidade já aceita socialmente, permitindo a livre atuação das organizações privadas — o Estado como facilitador e as organizações privadas como operacionalizadoras.",
      "empirical",
      "a legislação estudada demonstra baixo poder regulador e sua função foi legitimar a modalidade que já era aceita pela sociedade",
      ["p.21/L764-781"]),
    F("A ausência de políticas efetivas para a modalidade, somada às metas estatais de escolarização e à rentabilidade vislumbrada pelos grupos empresariais entre 2010 e 2020, favoreceu a formação de um oligopólio na EaD superior brasileira.",
      "empirical",
      "A ausência de políticas efetivas para a modalidade resultou na formação de um oligopólio no ensino superior EaD",
      ["p.17/L611-619", "p.21/L761-771"]),
    F("As normas avaliativas priorizaram estrutura física e recursos humanos — dispensa de avaliação in loco via IGC e Conceito Institucional — com reduzido poder de sancionar a ausência de qualidade pedagógica, o que consolida a crítica ao sucateamento da modalidade.",
      "empirical",
      "a qual apresentava reduzido poder de sancionar a continuidade institucional em casos de ausência de qualidade do modelo pedagógico",
      ["p.19/L692-716", "p.20/L717-744"]),
    F("Dois riscos metodológicos limitam a HP: o internalismo — tratar as formas simbólicas como analisáveis em si, ignorando suas condições sócio-históricas — e o reducionismo — o oposto, analisá-las apenas por suas condições sociais; sugere-se a Análise Crítica do Discurso como complemento.",
      "proposition",
      "O internalismo ocorre na medida em que ao analisar as formas simbólicas desconsideram-se os contextos de produção e reprodução",
      ["p.22/L795-806"]),
]

CONTRIBUTION = dict(
    theoretical=("Demonstra a relevância da HP para investigar transformações institucionais e normativas: "
                 "reconstrói a gênese hermenêutica, sistematiza o enfoque tríplice e suas técnicas, e mostra "
                 "como o tensionamento interpretativo — a re-interpretação que pode divergir do sentido "
                 "dos sujeitos — sustenta a análise crítica (p.9-15/L286-563; p.22/L818-830). Contribui "
                 "também ao delimitar internalismo e reducionismo como armadilhas do método (p.22/L795-806)."),
    practical=("Oferece um percurso aplicável — sem pretensão de manual — para pesquisadores das Ciências "
               "Sociais analisarem formas simbólicas e a ideologia nos fenômenos; o caso da EaD mostra "
               "como atos normativos podem ser lidos hermeneuticamente para desvelar legitimidade, "
               "sancionamento e formação de oligopólio (p.15/L555-563; p.22/L824-830)."),
    limitations=("Os próprios autores declaram que o estudo 'não se aprofundou na compreensão da doxa no "
                 "campo da EaD' — a pré-etapa etnográfica da HP ficou sem desenvolvimento empírico "
                 "(p.23/L834-836). Ademais, internalismo e reducionismo são riscos inerentes do método "
                 "(p.22/L795-806)."),
    future_research=("Sugerem vivências etnográficas, entrevistas e observações para compreender como "
                     "conceitos do campo — democratização, mercantilização, financeirização e qualidade — "
                     "foram significados na vida cotidiana da EaD; e aplicações da HP a outros fenômenos "
                     "sociais complexos e áreas do conhecimento (p.23/L834-849)."),
    source_refs=["p.22/L795-806", "p.22/L818-830", "p.23/L834-849"],
)
