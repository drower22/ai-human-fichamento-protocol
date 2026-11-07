# site/ — formulário do fichamento (deploy Vercel)

Estrutura publicada:

- `index.html` — **redirect** para `/r1/` (preserva `?s=token`)
- `r1/index.html` — **cópia publicável** de
  `protocol/forms/fichamento-r1.html` (form da Rodada 1, link pessoal
  `?s=token` → `r1/students/{token}.json`). Edite sempre o original e
  sincronize: `cp protocol/forms/fichamento-r1.html site/r1/index.html`
- `r1/students/{token}.json` — packs individuais (código S + artigo +
  pool de teorias, sem gabarito), gerados por
  `scripts/build_r1_student_packs.py`
- `r1/students/teste.json` — pack demo (`?s=teste`)

O form posta em `/api/send` (não existe neste deploy estático → cai no
fallback: baixa o `.json` e instrui envio por e-mail).

## Publicar na Vercel

Deploy atual: projeto Vercel com root directory = `site/`, integração
GitHub — push em `main` que tocar `site/` faz redeploy automático.

### Variantes de rodada

Para R2: gere `site/r2/` a partir de `fichamento-r2.html` + packs próprios
e aponte o redirect da raiz para `/r2/` quando a rodada abrir.
