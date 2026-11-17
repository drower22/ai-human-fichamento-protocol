// GET /api/status?r=1 — lista as avaliações já persistidas em
// data/evaluations/round{r}/ (ou data/piloto/evaluations/ para r=0).
// Usado pela página do juiz e pelo painel para marcar "enviado" sem
// depender de rebuild/deploy. Requer GITHUB_TOKEN nas env vars.
export default async function handler(req, res) {
  const gh = process.env.GITHUB_TOKEN;
  const repo = process.env.GITHUB_REPO || 'drower22/ai-human-fichamento-protocol';
  const r = String(req.query.r ?? '1');
  const dir = r === '0' ? 'data/piloto/evaluations'
                        : `data/evaluations/round${r}`;
  const files = [];
  if (gh) {
    try {
      const g = await fetch(
        `https://api.github.com/repos/${repo}/contents/${dir}`,
        { headers: { Authorization: `Bearer ${gh}`,
                     Accept: 'application/vnd.github+json' } });
      if (g.ok) {
        for (const f of await g.json())
          if (f.name?.endsWith('.json')) files.push(f.name.replace(/\.json$/, ''));
      }
    } catch { /* cai no retorno vazio */ }
  }
  res.setHeader('Cache-Control', 'no-store');
  return res.status(200).json({ files });
}
