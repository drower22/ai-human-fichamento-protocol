# Prompts — política de versionamento

Cada prompt é versionado com **semver + tag de papel** e o **id é o nome
do arquivo**: `v{id}.txt`. Três papéis atuais:

| arquivo / id | papel | rodada |
|---|---|---|
| `v1.0.0-baseline.txt` | prompt principal de fichamento (zero-shot) | R1 |
| `v1.0.0-theory-pool.txt` | extrai pool de teorias candidatas | R1 |
| `v1.0.0-theory-verdicts.txt` | 2ª chamada: IA classifica o pool | R1 |
| `v1.1.0-calibrated.txt` | refinado na calibração (diff documentado) | R2 |

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
