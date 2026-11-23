SUMMARY = (
    "O artigo investiga a subjetividade de mulheres empreendedoras de Paranaguá (PR), cidade litorânea de "
    "relevância econômica e cultural, buscando analisar como as experiências de vida influenciam a "
    "construção da subjetividade dessas mulheres no cenário empreendedor (p.4/L114-131). O referencial "
    "combina três esferas — o empreendedorismo feminino (GEM, Dornelas, Jonathan), a subjetividade como "
    "processo dinâmico de sentidos únicos (Rey; Ferreira e Nogueira) e o contexto familiar com o conflito "
    "trabalho-família (Greenhaus e Beutell; Hall; Shelton; Jonathan) (p.4-9/L145-318). O estudo de caso "
    "qualitativo reúne entrevistas narrativas com três empreendedoras — Vitória (clínica de estética), "
    "Geovana (loja e ateliê Floratta) e Luísa (Maya Modas) — analisadas em quatro dimensões predefinidas: "
    "motivação, rede de apoio, equilíbrio vida-trabalho e perspectiva de futuro (p.10-13/L324-457). As "
    "histórias mostram motivações por necessidade (Geovana, Luísa) e por oportunidade (Vitória), apoio "
    "familiar desigual, conflito trabalho-família intenso — maternidade, burnout, divórcio — e visões de "
    "legado: transmitir o negócio aos filhos e inspirar outras mulheres (p.13-25/L458-845). A conclusão é "
    "que a subjetividade é moldada por trajetórias, contextos culturais e experiências — sem pretensão de "
    "generalizar — e que o suporte externo fortalece a resiliência (p.26-27/L927-953)."
)

RESEARCH_QUESTION = (
    "O artigo não formula pergunta explícita; enuncia objetivo: 'este estudo busca analisar como as "
    "experiências de vida influenciam a construção da subjetividade dessas mulheres no cenário "
    "empreendedor do litoral paranaense' (p.4/L129-131), com foco nos papéis e na construção da "
    "subjetividade das empreendedoras de Paranaguá (p.4/L114-118)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.4/L151-154", "p.5/L155-171"],
      "destaca o empreendedor como um objeto central em seu sistema econômico, pelo fato de ser ele quem impulsiona o processo da inovação",
      "Enquadramento conceitual do empreendedorismo (GEM, Dornelas, Schumpeter)."),
    V("T2", "uses", ["p.7/L223-228", "p.8/L265-272"],
      "a subjetividade é um processo dinâmico, construído a partir de sentidos únicos que vão além de influências externas diretas",
      "O construto teórico central (Rey; Ferreira e Nogueira)."),
    V("T3", "uses", ["p.7/L229-235"],
      "a maneira como as mulheres percebem sua jornada no empreendedorismo é diretamente influenciada pelas expectativas sociais em relação ao papel feminino",
      "Identidade e estereótipos de gênero como moldantes da subjetividade empreendedora."),
    V("T4", "uses", ["p.8/L279-283", "p.9/L289-298"],
      "multiplicidade de papéis tende a ser considerada uma característica do universo feminino, levando ao reconhecimento de um talento nas mulheres para fazer e pensar várias coisas simultaneamente",
      "O conflito trabalho-família e as ações de enfrentamento de Hall e Shelton."),
    V("T5", "uses", ["p.6/L195-201", "p.20/L667-677"],
      "as empreendedoras brasileiras tendem a se envolver no empreendedorismo por questões de necessidade, como enfrentamento do desemprego, ao invés de apenas oportunidades de mercado",
      "Organiza a análise das motivações: necessidade (Geovana, Luísa) vs. oportunidade (Vitória)."),
    V("T6", "uses", ["p.9/L299-305"],
      "boa parte das mulheres entrevistadas identificam os maridos como principal apoiador para que elas permaneçam em atividade nos negócios",
      "A rede de apoio como dimensão analítica, contrastada com os relatos."),
    V("T7", "uses", ["p.11/L374-385", "p.11/L391-398", "p.12/L399-405"],
      "essa abordagem busca interpretar as experiências dos indivíduos, considerando o contexto social e cultural, e como eles atribuem significado aos eventos importantes de suas vidas",
      "Entrevista narrativa e análise narrativa como método (Boje; Riessman; Gibbs)."),
    V("T8", "uses", ["p.10/L325-329"],
      "sendo especificamente um estudo de caso, pois permite uma análise aprofundada do fenômeno investigado",
      "O desenho de pesquisa (Yin; Creswell)."),
    V("T9", "uses", ["p.5/L179-182", "p.13/L431-437"],
      "sendo as principais relacionadas à realização pessoal e o anseio por autonomia",
      "As motivações do empreendedorismo feminino mapeadas nas narrativas."),
    V("T10", "does_not_use", [], "",
      "A 'rede de apoio' é tratada como suporte familiar e emocional, não como capital social (Bourdieu/Putnam)."),
    V("T11", "does_not_use", [], "",
      "Gênero é tratado como eixo único; raça, classe e suas interseções não são mobilizadas."),
    V("T12", "does_not_use", [], "",
      "Os inícios improvisados ('vender do carro') são descritos empiricamente, sem a lente da effectuation."),
    V("T13", "does_not_use", [], "",
      "As narrativas são método de coleta e análise, não teoria do trabalho identitário."),
    V("T14", "does_not_use", [], "",
      "Ausente do referencial."),
    V("T15", "does_not_use", [], "",
      "A subjetividade é de Rey (processo dinâmico de sentidos únicos), não o assujeitamento foucaultiano."),
]

KEY_CONCEPTS = [
    dict(concept="Empreendedorismo feminino",
         definition="A atividade empreendedora liderada por mulheres — criação de valor por novos negócios, atividade autônoma ou expansão — motivada por independência financeira, autonomia e realização pessoal, e marcada por barreiras históricas e culturais.",
         quote="uma atividade empreendedora liderada por mulheres",
         source_refs=["p.3/L077-083", "p.4/L147-154"]),
    dict(concept="Subjetividade",
         definition="Processo dinâmico construído a partir de sentidos únicos que vão além de influências externas diretas — moldado por experiências pessoais que se acumulam e se transformam ao longo do tempo.",
         quote="a subjetividade é um processo dinâmico, construído a partir de sentidos únicos que vão além de influências externas diretas",
         source_refs=["p.7/L223-228"]),
    dict(concept="Conflito trabalho-família",
         definition="O atrito entre responsabilidades profissionais e familiares — intensificado pela 'multiplicidade de papéis' atribuída às mulheres — com ações de enfrentamento que eliminam, minimizam ou compartilham os fatores geradores.",
         quote="Equilibrar as responsabilidades pessoais e profissionais é uma constante nos conflitos relacionados entre o trabalho e a família",
         source_refs=["p.8/L273-283", "p.9/L306-310"]),
    dict(concept="Rede de apoio",
         definition="Os relacionamentos que oferecem suporte emocional, financeiro e prático às empreendedoras — com o marido recorrentemente identificado como principal apoiador.",
         quote="A rede de apoio inclui relacionamentos que oferecem suporte emocional, financeiro e prático às empreendedoras",
         source_refs=["p.9/L299-305", "p.13/L438-442"]),
    dict(concept="Entrevista e análise narrativa",
         definition="Técnica de coleta em que o entrevistado compartilha sua vivência espontaneamente, seguindo estrutura de início-meio-fim, e método de interpretação das histórias no contexto sociocultural em que significados são atribuídos.",
         quote="O intuito é permitir que ele compartilhe sua vivência de forma espontânea, com suas próprias palavras",
         source_refs=["p.11/L374-385", "p.11/L391-395"]),
    dict(concept="Motivação empreendedora (necessidade vs. oportunidade)",
         definition="O desejo de empreender e a coragem do primeiro passo — por necessidade (desemprego, conciliação familiar) ou por oportunidade de mercado — visíveis nas iniciativas e na determinação das empreendedoras.",
         quote="sendo as principais relacionadas à realização pessoal e o anseio por autonomia",
         source_refs=["p.6/L195-201", "p.13/L431-437"]),
]

METHODOLOGY = dict(
    study_type="empírico qualitativo (estudo de caso)",
    design="Estudo de caso qualitativo (Creswell; Yin) com entrevistas narrativas individuais, presenciais no local de trabalho de cada empreendedora, gravadas com consentimento; transcrição literal com limpeza de vícios de linguagem e reescrita de trechos para coesão; análise narrativa (Gibbs; Boje; Riessman) estruturada em quatro categorias predefinidas — motivação, rede de apoio, equilíbrio e perspectiva de futuro — com sigilo e nomes fictícios.",
    sample_type="três mulheres empreendedoras com no mínimo quatro anos de atividade em Paranaguá (PR), escolhidas por proximidade das pesquisadoras, uso prévio dos serviços e divulgação em redes sociais",
    sample_size=3,
    sector="comércio e serviços locais — clínica de estética, loja-ateliê de moda e loja de vestuário feminino",
    period="não informado explicitamente; dados tratados como coletados em 2024 (fonte dos quadros 'Os autores (2024)')",
    methods=["entrevista narrativa individual (roteiro de uma página)", "gravação e transcrição literal", "análise narrativa com categorias predefinidas"],
    analysis_note=("A análise combinou narrativa com quatro dimensões predefinidas (Quadro 1): Motivação "
                   "Empreendedora, Rede de Apoio, Equilíbrio entre Vida Pessoal e Profissional e Perspectiva "
                   "de Futuro — depois contrastadas com fragmentos das narrativas no Quadro 2; a maternidade "
                   "emergiu como experiência comum mas não recorrente em todas as entrevistas, ficando fora "
                   "do quadro (p.12-13/L407-425; p.25/L842-845)."),
    source_refs=["p.10/L324-365", "p.11/L369-390", "p.12/L401-425", "p.13/L426-457"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("As três trajetórias convergem em motivações por necessidade (Geovana e Luísa — pandemia, gravidez, insatisfação com a liderança masculina) e por oportunidade (Vitória — seguro-desemprego), corroborando Jonathan; e as motivações se modificaram ao longo do tempo, tornando o empreendedorismo realização e prazer pessoal.",
      "empirical",
      "Geovana e Luísa iniciaram seus empreendimentos por necessidade, motivadas pelas circunstâncias incertas que enfrentavam em suas vidas",
      ["p.19/L657-663", "p.20/L669-697"]),
    F("O início foi modesto e improvisado para todas — vender do carro, atender em casa, loja online — após experiências em empregos formais; as motivações foram além da renda: autonomia, satisfação pessoal e identificação de nichos.",
      "empirical",
      "todas iniciaram suas jornadas empreendedoras ainda jovens, após acumularem experiências anteriores em empregos formais",
      ["p.20/L698-706", "p.21/L707-718"]),
    F("A rede de apoio foi desigual: Vitória teve apoio braçal do pai e depois emocional dos pais e do namorado-sócio; Geovana enfrentou sozinha a ausência de familiares e amigos; Luísa contou apenas com marido e sogra — contrastes parciais com o estudo de Silva, Mainardes e Lasso.",
      "empirical",
      "a empreendedora também conta com o suporte do seu namorado, que hoje é um dos sócios da empresa",
      ["p.21/L719-737"]),
    F("O conflito trabalho-família é a dimensão mais intensa: maternidade levada para as lojas, burnout de Geovana (2022-2023), divórcio, doença da mãe e filho autista, momentos perdidos dos filhos de Luísa — sobrecarga que reflete a literatura sobre mulheres como principais cuidadoras.",
      "empirical",
      "Essa sobrecarga reflete o que Jonathan (2005) e Vilela (2018) descrevem sobre o papel social das mulheres como principais cuidadoras",
      ["p.22/L741-762"]),
    F("As estratégias de enfrentamento seguem Hall e Shelton: compartilhar responsabilidades (divisão de tarefas com o marido e sogra de Luísa), delegar (colaboradoras treinadas) e eliminar/minimizar geradores de conflito (Vitória planejando reduzir a carga horária).",
      "empirical",
      "focando em eliminar, minimizar ou compartilhar seus fatores geradores",
      ["p.23/L780-793"]),
    F("A perspectiva de futuro articula legado: Geovana e Luísa querem transmitir os negócios aos filhos; Vitória quer ser mentora e exemplo para outras mulheres — 'Eu trago mais como uma missão para mim, ensinar outras pessoas'.",
      "empirical",
      "Ela agora busca ser mentora e exemplo, demonstrando um compromisso com o futuro do empreendedorismo feminino",
      ["p.24/L819-827", "p.26/L905-920"]),
    F("A subjetividade das empreendedoras é moldada por trajetórias, contextos culturais e experiências de vida — sem pretensão de generalização; o suporte externo fortalece a resiliência e a disciplina em definir prioridades minimiza os conflitos.",
      "proposition",
      "A pesquisa não visa generalizar, mas apresentar como a identidade de cada empreendedora se forma por meio de suas experiências",
      ["p.24/L833-837", "p.25/L838-845", "p.27/L947-953"]),
]

CONTRIBUTION = dict(
    theoretical=("O estudo enriquece a literatura brasileira sobre empreendedorismo feminino — onde há "
                 "carência de estudos sobre subjetividade — ao mostrar, em narrativas de vida, como "
                 "experiências individuais e coletivas constroem a subjetividade das empreendedoras, "
                 "corroborando Ferreira e Nogueira e Rey (p.26-27/L927-953)."),
    practical=("Os resultados podem orientar políticas públicas, programas de apoio e práticas de "
               "instituições financeiras, além de fortalecer a inclusão de gênero no mercado — e revelam a "
               "importância do apoio emocional familiar e da gestão financeira para a resiliência dos "
               "negócios (p.26-27/L934-958)."),
    limitations=("Estudo de caso com três empreendedoras de uma única cidade litorânea, escolhidas por "
                 "proximidade das pesquisadoras — sem pretensão de generalização; a maternidade emergiu "
                 "mas não como padrão em todas as entrevistas (p.12/L418-422; p.27/L951-953)."),
    future_research=("Investigar a subjetividade de empreendedoras maternas; expandir para outras "
                     "regiões e realizar análises comparativas com diferentes contextos sociais, incluindo "
                     "o impacto das redes de apoio e da pandemia (p.27/L959-963)."),
    source_refs=["p.26/L927-944", "p.27/L945-963"],
)
