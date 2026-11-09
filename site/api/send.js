// POST /api/send — recebe {filename, json} do form e envia o .json
// em anexo por e-mail via Resend. Env vars: RESEND_API_KEY, TO_EMAIL.
// Sem domínio verificado, from=onboarding@resend.dev só entrega ao
// e-mail da própria conta Resend (limitação conhecida do piloto).
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
  return res.status(200).json({ ok: true });
}
