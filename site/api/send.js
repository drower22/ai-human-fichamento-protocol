// POST /api/send — recebe {filename, json} do form e envia o .json
// em anexo por e-mail via Resend. Env vars: RESEND_API_KEY, TO_EMAIL.
// Sem domínio verificado, from=onboarding@resend.dev só entrega ao
// e-mail da própria conta Resend (limitação conhecida do piloto).
//
// Persistência definitiva: se GITHUB_TOKEN estiver configurado, o .json
// também é commitado em data/evaluations/round{r}/ (ou data/piloto/
// evaluations/ para r=0) via GitHub Contents API. Aí o status "enviado"
// vira estado real no servidor — /api/status lê o mesmo diretório.
export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'method' });

  const { filename, json } = req.body || {};
  if (typeof filename !== 'string' || typeof json !== 'string' ||
      !/^[\w.\-]+\.json$/.test(filename) || filename.length > 80 ||
      json.length > 5_000_000) {
    return res.status(400).json({ error: 'payload invalido' });
  }

  const key = process.env.RESEND_API_KEY, to = process.env.TO_EMAIL;
  if (!key || !to) return res.status(500).json({ error: 'env vars ausentes' });

  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      from: 'Fichamento <onboarding@resend.dev>',
      to: [to],
      subject: `Fichamento recebido: ${filename}`,
      text: `Arquivo ${filename} segue em anexo (JSON canonico do formulario).`,
      attachments: [{ filename, content: Buffer.from(json).toString('base64') }],
    }),
  });

  if (!r.ok) {
    const detail = await r.text();
    return res.status(502).json({ error: 'resend falhou', detail });
  }

  // grava no repo: data/evaluations/round{r}/{filename}
  let persisted = false;
  const gh = process.env.GITHUB_TOKEN;
  const repo = process.env.GITHUB_REPO || 'drower22/ai-human-fichamento-protocol';
  const m = filename.match(/^E-R(\d+)-[\w.\-]+\.json$/);
  if (gh && m) {
    const dir = m[1] === '0' ? 'data/piloto/evaluations'
                             : `data/evaluations/round${m[1]}`;
    try {
      const g = await fetch(
        `https://api.github.com/repos/${repo}/contents/${dir}/${filename}`,
        { method: 'PUT',
          headers: { Authorization: `Bearer ${gh}`,
                     Accept: 'application/vnd.github+json',
                     'Content-Type': 'application/json' },
          body: JSON.stringify({
            message: `avaliação recebida: ${filename}`,
            content: Buffer.from(json).toString('base64') }) });
      persisted = g.ok || g.status === 422; // 422 = arquivo já existe
    } catch { /* e-mail já é o recibo; persistência falhou silenciosamente */ }
  }
  return res.status(200).json({ ok: true, persisted });
}
