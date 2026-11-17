SUMMARY = (
    "O estudo explora o conceito de resourcing (recursos em uso), isto é, a transformação de recursos por atores "
    "organizacionais em suas práticas cotidianas, indo além de uma abordagem econômica da estratégia (p.1/L022-028). "
    "A pergunta de pesquisa é como os atores mobilizam recursos em suas atividades diárias para responder às "
    "restrições impostas por uma mudança estratégica inesperada (p.2/L086-088). O referencial contrasta as visões que "
    "tratam recursos como ativos estáticos, como dependência de recursos, visão baseada em recursos e capacidades "
    "dinâmicas, com a perspectiva do resourcing, de ontologia processual e praxeológica, para a qual o valor dos "
    "recursos emerge de seu uso (p.2/L056-066; p.2/L067-073; p.3/L112-117). O método é um estudo de caso único, de "
    "abordagem etnográfica, em uma unidade de educação a distância de uma universidade privada, com seis meses de "
    "observação, 42 entrevistas semiestruturadas e análise de documentos, tratados por codificação aberta e pelo "
    "método de Gioia (p.5/L190-212; p.5/L217-220; p.6/L228-238). Uma nova estratégia comercial gerou aumento "
    "inesperado de 200% nas matrículas e triplicou o número de alunos por docente, pressionando tempo, espaço e papéis "
    "profissionais (p.6/L250-259; p.7/L277-298). Os autores identificam três dinâmicas de resourcing: a responsiva, com "
    "soluções imediatas e internas, como a planilha de correção e vídeos; a configuracional, com FAQ, inteligência "
    "artificial e indicadores de trabalho remoto criados por outras áreas; e a ocupacional, em que docentes "
    "reinterpretam seus papéis (p.12/L525-529; p.13/L535-557; p.8/L329-341; p.10/L393-411). Concluem que as três se "
    "complementam e que tempo, espaço e papéis profissionais são recursos fundamentais (p.14/L611-626; "
    "p.14/L641-642). Criticam a expansão acelerada da EaD, que pode precarizar o trabalho docente (p.15/L679-695), e "
    "reconhecem como limitação o curto período de observação (p.16/L734-737)."
)

RESEARCH_QUESTION = (
    "Como os atores mobilizam recursos em suas atividades diárias para responder às restrições impostas por uma "
    "mudança estratégica inesperada? A pergunta é enunciada explicitamente (p.2/L086-088) e retomada como objetivo "
    "principal nas considerações finais (p.16/L711-713)."
)

V = lambda i, v, refs, quote, note: (i, v, refs, quote, note)
VERDICTS = [
    V("T1", "uses", ["p.4/L139-142", "p.2/L063-066"],
      "the creation in practice of assets such as people, time, money, knowledge, or skill; and qualities of relationships such as trust, authority, or complementarity such that they enable actors to enact schemas",
      "Conceito central: o resourcing, de Feldman, orienta a análise das dinâmicas."),
    V("T2", "uses", ["p.2/L067-073", "p.3/L118-125", "p.3/L126-132"],
      "Grounded in a processual and praxeological ontology, the resourcing perspective enables the analysis of the dynamics of daily activities and strategic action in organizational change processes",
      "Base ontológica declarada; usa Reckwitz e Schatzki para definir práticas."),
    V("T3", "does_not_use", [],
      "",
      "Não há teoria institucional; 'institutional' aparece em sentido descritivo (p.5/L185; p.6/L231)."),
    V("T4", "discusses", ["p.2/L056-066", "p.3/L105-111"],
      "The concept of resources has been central to various management perspectives, including resource dependence theory (Pfeffer & Salancik, 1978), the resource-based view (Helfat et al., 2023), and dynamic capabilities (Teece et al., 1997)",
      "Apresentadas como a visão tradicional, de recursos estáticos, que o resourcing busca superar."),
    V("T5", "uses", ["p.14/L627-637"],
      "Resourcing broadens the view of strategy as an emergent, situated, and collective process, emphasizing how the daily actions and interactions of organizational actors influence the construction and adaptation of strategy over time",
      "A relação entre estratégia e resourcing é a principal contribuição declarada."),
    V("T6", "does_not_use", [],
      "",
      "Aprendizagem organizacional não é mencionada; 'learning' refere-se a ensino a distância e ao aprendizado dos estudantes."),
    V("T7", "does_not_use", [],
      "",
      "A dinâmica de rotinas aparece apenas em citação de referência para justificar procedimentos (p.4/L163; p.17/L766-768) e em 'routine behaviors' (p.3/L127)."),
    V("T8", "discusses", ["p.15/L679-695", "p.16/L701-709"],
      "Short-term changes arising from improvised and creative practices often provide only temporary relief within the context of precarious academic labor",
      "Discutida na seção de discussão como implicação crítica; não estrutura o referencial."),
]

KEY_CONCEPTS = [
    dict(concept="Resourcing",
         definition="Criação em prática de ativos, como pessoas, tempo, dinheiro, conhecimento ou habilidade, e de qualidades de relacionamentos, como confiança e autoridade, que permitem aos atores atualizar esquemas.",
         quote="the creation in practice of assets such as people, time, money, knowledge, or skill; and qualities of relationships such as trust, authority, or complementarity such that they enable actors to enact schemas",
         source_refs=["p.4/L139-142"]),
    dict(concept="Recursos potenciais e recursos em uso",
         definition="Distinção entre elementos disponíveis (objetos, artefatos, pessoas, informação) e a mobilização efetiva desses recursos no tempo e no espaço das dinâmicas organizacionais.",
         quote="it is crucial to distinguish between potential resources – such as objects, artifacts, people, or information – and the resourcing process, which involves the actual mobilization of these resources",
         source_refs=["p.4/L143-149", "p.8/L331-333"]),
    dict(concept="Resourcing responsivo",
         definition="Transformação de recursos potenciais em recursos em uso por atores das práticas de ensino para resolver desafios de eficiência em curto prazo, com soluções internas e imediatas.",
         quote="Responsive resourcing: It occurs when actors within teaching practices transform potential resources into resources-in-use to address efficiency challenges arising from strategic change within a short timeframe",
         source_refs=["p.12/L525-529", "p.13/L535-536"]),
    dict(concept="Resourcing configuracional",
         definition="Colaboração entre áreas interdependentes para resolver problemas e aumentar a eficiência das práticas de ensino, com mudanças estruturais em prazo mais longo.",
         quote="Configurational resourcing: It entails collaboration between interdependent areas to solve problems and enhance the efficiency of teaching practices",
         source_refs=["p.13/L537-546"]),
    dict(concept="Resourcing ocupacional",
         definition="Processo dinâmico e emergente pelo qual os atores reconstroem seus esquemas interpretativos dos papéis profissionais ao transformar recursos.",
         quote="Occupational resourcing: It is a dynamic and emergent process through which organizational actors reconstruct their interpretative frameworks of professional roles by transforming resources",
         source_refs=["p.13/L547-557"]),
]

METHODOLOGY = dict(
    study_type="empírico (qualitativo)",
    design="Estudo de caso único com abordagem etnográfica em uma unidade de educação a distância de uma universidade privada brasileira (UAlpha), com abordagem abdutiva.",
    sample_type="gestores, professores online e funcionários de uma unidade de EaD",
    sample_size=42,
    sector="educação superior privada a distância",
    period="seis meses de observação; planejamento estratégico citado em entrevista para 2018",
    methods=["estudo de caso", "etnografia", "observação não participante", "entrevistas semiestruturadas", "análise documental", "codificação aberta e live coding", "método de Gioia"],
    analysis_note=("O primeiro autor fez 51 visitas de campo, cerca de 300 horas em seis meses, observando 29 reuniões e acessando cursos "
                   "como estudante (p.5/L194-201). Foram feitas 42 entrevistas semiestruturadas (p.5/L202-206) e analisados documentos "
                   "internos e fontes secundárias (p.5/L207-210). A análise combinou codificação aberta e live coding no Atlas.ti (p.5/L211-219) "
                   "e categorias de primeira e segunda ordem e dimensões agregadas, seguindo Gioia et al. (p.6/L228-238)."),
    source_refs=["p.4/L164-167", "p.5/L190-210", "p.5/L211-219", "p.6/L228-238"],
)

F = lambda f, t, q, refs: dict(finding=f, type=t, quote=q, source_refs=refs)
FINDINGS = [
    F("Uma nova estratégia comercial, desconhecida pela maioria dos setores, causou aumento inesperado de 200% nas matrículas e triplicou o número de alunos por docente online.",
      "empirical",
      "most other sectors were unaware of the strategy, leading to unexpected consequences, including a 200% increase in enrollments",
      ["p.6/L250-259", "p.7/L277-278"]),
    F("No resourcing responsivo, docentes padronizaram e customizaram atividades com recursos disponíveis, como a planilha de correção em Excel e vídeos explicativos, para reduzir a pressão de tempo.",
      "empirical",
      "the transformation of potential resources into resources-in-use addressed key challenges and redefined the work standards of online lecturers by promoting adaptive and improvised solutions",
      ["p.8/L329-341", "p.9/L349-358", "p.9/L372-386"]),
    F("No resourcing configuracional, outras áreas criaram um FAQ, propuseram um chat com IA e desenvolveram indicadores de trabalho remoto, transferindo perguntas administrativas para o suporte.",
      "empirical",
      "there was a consensus that answering administrative questions should not fall under the online lecturers’ responsibilities but should instead be assigned to support professionals or an artificial intelligence (AI) system",
      ["p.10/L393-411", "p.10/L412-421", "p.11/L437-441"]),
    F("No resourcing ocupacional, docentes reinterpretaram seus papéis e passaram a ver a situação como temporária, apoiados por gestores e supervisores.",
      "empirical",
      "Online lecturers began perceiving the current situation as temporary, believing that other areas would ultimately resolve existing challenges",
      ["p.13/L547-557", "p.11/L442-448", "p.11/L462-469"]),
    F("Os três tipos de resourcing se complementam, e o alcance das transformações depende de sua interdependência.",
      "proposition",
      "the scope of organizational transformations depends on the interdependence of these three resourcing types",
      ["p.14/L611-626"]),
    F("Tempo, espaço e papéis profissionais são recursos fundamentais para a ação organizacional e são afetados por decisões estratégicas.",
      "proposition",
      "The findings indicate that time, space, and professional roles are fundamental resources for organizational action",
      ["p.14/L638-647"]),
]

CONTRIBUTION = dict(
    theoretical=("Conecta o contexto estratégico à dinâmica microorganizacional da ação, representada pela interdependência entre atividades "
                 "operacionais (p.14/L631-637), amplia a compreensão da mudança estratégica ao destacar o papel ativo dos atores sob "
                 "incerteza e escassez (p.14/L638-641) e identifica três processos de resourcing, enfatizando tempo, espaço e papéis "
                 "profissionais (p.15/L656-665)."),
    practical=("Oferece implicações para organizações educacionais em contextos de mudança rápida (p.1/L027-028) e contribui para a "
               "crítica da expansão acelerada da EaD, com impacto na qualidade do ensino e nas condições de trabalho dos docentes "
               "online (p.15/L679-689; p.16/L703-709; p.16/L728-733)."),
)
