# site/ — formulário do fichamento (deploy Vercel)

`index.html` é uma **cópia publicável** de
`protocol/forms/fichamento-piloto.html` (o form gera o `.json` que o
estudante envia por e-mail). Edite sempre o original e sincronize:

```bash
cp protocol/forms/fichamento-piloto.html site/index.html
```

## Publicar na Vercel

### Opção A — CLI (recomendada)

```bash
npm i -g vercel        # uma vez
cd site
vercel --prod        # login na primeira vez; aceite os defaults
```

Saída: uma URL tipo `https://fichamento-piloto.vercel.app`.
Deploys seguintes: editar o HTML, `cp` pra cá, `vercel --prod` de novo.

### Opção B — arrasta-e-solta (sem CLI)

https://vercel.com/new → aba "Deploy" → arraste a pasta `site/`.

### Variantes de rodada

Para R1/R2 com pools diferentes: gere `site/index.html` a partir de um
`fichamento-r{N}.html` (mesmo arquivo, pool diferente) — ou suba pastas
/`r1`, `/r2` cada uma com seu `index.html`.
