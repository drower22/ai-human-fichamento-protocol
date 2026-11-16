# Aprendizagem dos estudantes entre fases

**Piloto → Rodada 1: o que os logs reflexivos e autoavaliações mostram até aqui** · 16/11/2026

## 1. Status da coleta R1

- **14 de 16 fichamentos recebidos** (faltam S03 e S12; o prazo era 15/11). Ligia Nauiack (S08, substituta) já enviou.
- **10 importados e validados**; 4 falharam o gate de auditoria do schema por marcarem vereditos `uses`/`discusses` sem `source_ref` verificável: S01/A06, S06/A07, S14/A12, S15/A01 (as referências vieram como prosa no campo de citação).
- **Tempo declarado**: 75 a 400 min, mediana ~280 (piloto: mediana ~90 a 124, com absurdos de 1 e 5 min).
- **Autoavaliação** (soma das 7 seções): 31 a 46 na R1, 27 a 47 no piloto; médias ~37 nas duas.

## 2. O que estava planejado medir

| módulo | o quê | status |
|---|---|---|
| A: calibração metacognitiva | gap \|auto-nota − média dos juízes\| por seção, trajetória R1→R2 | auto-notas coletadas; juízes avaliam 16 a 22/11 |
| C: tempo e qualidade agregada | `elapsed_minutes` + perfil de erros agregado (métrica econômica) | dados de tempo da R1 já disponíveis |
| D: log reflexivo | perguntas abertas por fichamento; R1 separou conteúdo × formato | 14 logs q1 a q4 analisados abaixo |

Decisões de desenho relevantes: sem trajetória individual (1 artigo/estudante/rodada; leitura agregada e exploratória); reframe pré → intervenção → pós, com a **calibração simétrica** (o protocolo calibra a máquina via prompt e o humano via checklist); estratégias do piloto socializadas na reunião 06/11 (**baseline instruído**); `checklist-students.md` selado até a pós-R1.

## 3. O que os dados mostram

### 3.1 O baseline instruído é real

As estratégias socializadas em 06/11 aparecem **adotadas** nos q3 ("o que faria diferente"):

- "resumo por último" (S02, S05; S10 também o aplicou),
- codebook institucionalizado: S10 codificou no **Atlas.ti**, exportou códigos para Excel e transpôs manualmente,
- anotações em arquivo separado antes de preencher (S13), bloco contínuo de tempo (S01).

Consequência para a medida: o Δ R1→R2 isolará o efeito do checklist além desse patamar, como previsto no desenho.

### 3.2 O split conteúdo × formato funcionou

No piloto a pergunta única misturava os dois objetos. Na R1, q1 concentra dificuldades de conteúdo (idioma, densidade, gênero do texto) e q2 concentra formato (quase exclusivamente o custo de referenciar `p.N Lnnn`). A decisão de instrumento se pagou: cada confundidor agora tem seu próprio sinal.

### 3.3 A fricção com `p.N Lnnn` é estrutural, não de aprendizagem

Segue a queixa nº 1 nas duas fases, mas o tom evoluiu: no piloto era frustração ("preciosismo", "burocrático"); na R1 virou custo reconhecido e em parte ressignificado: S16 chama de "excelente exercício de atenção"; S15 mantém crítica epistemológica elaborada (o referenciamento "segrega" um conhecimento que se extrai aglutinado). Aprendizagem aqui não é a tarefa ficar gostosa: é o incômodo virar argumento.

### 3.4 USA × DISCUTE: déficit operacional, não conceitual

Os estudantes citam a definição corretamente e erram na execução. S07 propõe renomear os vereditos (sugere NÃO CITA / CITA / FUNDAMENTA), ecoando a tensão que dividiu os juízes; e 4 dos 14 fichamentos marcaram vereditos sem referência verificável, reprovados no gate do schema. **Lição para o checklist pós-R1: precisa de exercício com contraexemplos, não só definição.**

### 3.5 Idioma: o confundidor não previsto

O piloto usava artigo em português; a R1 é majoritariamente em inglês. Resultado: tradutores viraram a zona cinzenta da regra "sem IA": 5 estudantes declaram Google Tradutor distinguindo-o de IA; S13 declarou uso real de IA (relembrar conceitos), mostrando que o canal de declaração honesta funciona. **Decisão pendente: tradutor conta como IA? Afeta o gate ético e a comparabilidade de tempo.**

### 3.6 Gênero textual virou variável

O instrumento foi calibrado sobre artigo empírico; a R1 trouxe capítulo de livro (S04) e teóricos sem contribuição prática explícita (S02, S11, S15). O mesmo problema da "questão implícita" do piloto reapareceu em outras seções. Opções para a sala: ajustar instruções da R2 ou tratá-lo como variável de análise.

### 3.7 O custo-tempo real da auditabilidade

Mediana ~280 min na R1 contra ~90 a 124 no piloto. Causas combinadas: artigos mais densos, inglês, e o vai e vem do `p.N Lnnn`. A correção do instrumento funcionou: `elapsed_minutes` no fim do form eliminou os valores absurdos do piloto. Para o Módulo C, há agora custo humano confiável por artigo (2 a 7h) para contrapor ao custo de geração+revisão com IA.

### 3.8 Autoavaliação estável e comparável

Totais ~37 nas duas fases, sem efeito teto. Quando os juízes avaliarem (16 a 22/11), o gap auto-nota × nota dada será a primeira medida empírica de calibração metacognitiva do estudo.

### 3.9 Convergência epistêmica: o caso narrativo

S07 pergunta no log se a tarefa é fichamento ou resenha crítica: os estudantes redescobriram sozinhos a tensão fidelidade × cobertura que dividiu os juízes na calibração. É aprendizagem no sentido forte: internalizaram *o problema* que a régua veio resolver. Material direto para a discussão do paper.

## 4. Pontos para deliberação

1. **Tradutor conta como IA?** Definir a regra antes da R2 e atualizar as instruções.
2. **Os 4 fichamentos sem referências** (S01, S06, S14, S15): devolver para correção ou aceitar com ressalva registrada? Decisão afeta o critério de auditoria.
3. **S03 e S12 fora do prazo**: contato e redefinição de data para completar a rodada.
4. **Conteúdo do checklist pós-R1**: exercício de veredito+referência (usa os casos reais anonimizados), nomenclatura USA/DISCUTE sob avaliação, tratamento de gêneros não empíricos.
5. **Confirmação do desenho**: os achados qualitativos reforçam a leitura agregada/descritiva prevista na proposta de medição de aprendizagem.
