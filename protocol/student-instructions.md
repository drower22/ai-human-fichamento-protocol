# Instruções aos estudantes (fichamento manual)

Você receberá, para cada artigo atribuído (IDs `A01…`):

1. O **PDF do artigo**;
2. Um **pool de teorias candidatas** (`A{nn}.pool.md`) gerado
   automaticamente — uma lista de teorias que *podem* estar no artigo.

## Antes de começar

**Cronometre** o tempo de fichamento (leitura → entrega) e registre em
minutos. Esse dado é de pesquisa e **não** será mostrado aos juízes.

## Como fichar

Leia o artigo **integralmente** antes de fichar. Produza o fichamento
seguindo [`fichamento-template.md`](fichamento-template.md) — entregue o
JSON preenchido ([`student-fichamento-template.json`](forms/student-fichamento-template.json)).

### Seção de teorias (instrumento fechado)

Para **cada** candidato do pool, escolha um veredito:

| veredito | significado | evidência exigida |
|---|---|---|
| `uses` | a teoria estrutura o argumento/modelo/hipóteses | `source_refs` **obrigatório** (`p.N`; ideal `p.N/Lnn`) |
| `discusses` | debatida/citada substantivamente, sem estruturar | `source_refs` **obrigatório** |
| `does_not_use` | ausente ou menção meramente decorativa | — |

- Em dúvida entre `uses` e `discusses`, pergunte: *"remover esta teoria
  quebraria o argumento do artigo?"* Se sim → `uses`.
- **Faltou teoria no pool?** Adicione no campo `theories` (lista livre) —
  é justamente o que queremos medir (o que o pool não viu).
- Recomendado: colar em `quote` o trecho literal que sustenta o veredito.

### Demais seções

Livres, conforme o template. Em conceitos e achados, **cite página/linha**
(`source_refs`) e prefira incluir o `quote` literal — os juízes podem
conferir suas referências diretamente no texto.

## Regras

- Escreva em pt-BR. Nada que não esteja no artigo.
- **Não** consulte o fichamento da IA nem o de colegas — a independência
  é o que torna a comparação válida.

## Após a Rodada 1

Você receberá o [`checklist-students.md`](checklist-students.md), derivado
dos padrões de erro da R1 — é ele que operacionaliza a calibração humana.
