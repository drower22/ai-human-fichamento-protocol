# Prompts — política de versionamento

Cada prompt é versionado com **semver + tag de papel** e o **id é o nome
do arquivo**: `v{id}.txt`. Três papéis atuais:

| arquivo / id | papel | rodada |
|---|---|---|
| `v1.0.0-baseline.txt` | prompt principal de fichamento (zero-shot) | R1 |
| `v1.0.0-theory-pool.txt` | extrai pool de teorias candidatas | R1 |
| `v1.0.0-theory-verdicts.txt` | 2ª chamada: IA classifica o pool | R1 |
| `v1.1.0-calibrated.txt` | fichamento refinado na calibração da R1 | R2 |
| `v1.1.0-theory-verdicts.txt` | vereditos com limiar de `discusses` apertado | R2 |
| `v1.0.0-critic.txt` | passo opcional de crítica (omissões/vereditos) | R2 |

Regras:

1. O prompt usado em cada fichamento é registrado em
   `generator.prompt_version` — nunca editar um prompt já usado; criar nova versão.
2. O **diff entre versões é um achado do estudo**: documentar no changelog
   abaixo *o que* mudou e *por que* (ligado aos padrões de erro da R1).
3. Mudanças de texto que não afetam saída (typo) = PATCH; novas instruções/
   restrições = MINOR; redesign = MAJOR.
4. Template usa `{schema_hint}` e `{document}` como placeholders — o
   `fichamento generate` injeta o contrato JSON resumido e o markdown
   paginado do artigo.

## Changelog

- **v1.0.0-baseline** — instruções estruturais + contrato JSON + exigência
  de `source_refs` (`p.N/Lnn`) por elemento + proibição de conteúdo fora do
  documento.
- **v1.1.0-calibrated** (R2, diff do baseline; motivação = erros marcados
  pelos juízes na R1, `analysis/reports/round1/`):
  - regra 8: se o artigo não formula PQ explícita, dizer isso e informar o
    objetivo declarado (R1: juiz flagou PQ reconstruída no A16);
  - regra 9: `key_concepts` de "3 ou 4" para **3–6** + instrução de
    varredura prévia dos termos centrais (R1: omission de conceitos
    centrais, ex.: "risco puro" no A16, EaD/oligopólio no A05);
  - regra 10: enumerar TODAS as fases/etapas na metodologia (R1: "faltou
    a terceira fase" no A15; período de coleta omitido no A14);
  - regra 11: em texto corrompido por OCR, declarar incerteza em vez de
    reconstruir (R1: 3 hallucination concentradas em A06/A15, artigos com
    OCR ruidoso);
  - regra 12: cautela ≠ omissão — o teto de fidelidade proíbe extrapolar,
    não proíbe completude.
- **v1.1.0-theory-verdicts** (R2): regra 5 nova — limiar de `discusses`
  exige mobilização de construtos/lógica da teoria; menção ao nome, citação
  honorífica ou conceito "falado de passagem" = `does_not_use`. Na dúvida,
  `does_not_use`. (R1: juízes marcaram `misinterpretation` em vereditos
  liberais demais — ex.: nota no A15.)
- **v1.0.0-critic** (novo papel, R2): segundo passo — modelo distinto
  audita o fichamento contra o artigo e devolve JSON de `issues`
  (omissões, alucinações, vereditos contestáveis). Cobre a revisão
  semântica que a verificação mecânica de referências não vê.
