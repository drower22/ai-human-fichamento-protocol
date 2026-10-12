# Prompts — política de versionamento

Cada prompt de geração de fichamento é versionado com **semver**
(`v{MAJOR}.{MINOR}.{PATCH}-{tag}.txt`) e congelado por rodada:

| versão | rodada | descrição |
|---|---|---|
| `v1.0.0-baseline` | R1 | prompt baseline zero-shot |
| `v1.1.0-calibrated` | R2 | refinado na calibração (diff documentado abaixo) |

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
