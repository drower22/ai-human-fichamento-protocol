"""Sorteia o par A/B do piloto (estratificado por cobertura) e gera
o pacote anonimizado pairs/PILOTO.json.

Camadas: score = n_conceitos + n_achados.
  alta  >= 9   |   baixa <= 3   |   (meio: resto, fora do sorteio)
Sorteia 1 fichamento de cada cauda, depois embaralha p/ A e B.
Tudo com seed registrada; mapa privado em data/private/piloto-pair-map.json.
"""
import json, glob, random, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESP = ROOT / 'data/piloto/responses'
SEED = 20261030
SECTIONS = ['executive_summary','research_question','theory_verdicts','theories',
            'key_concepts','methodology','main_findings','contribution']

# respostas válidas = X_* (alunos); S18 é teste interno e fica de fora
files = sorted(RESP.glob('X_*.json'))
def score(f):
    d = json.loads(f.read_text())
    return len(d.get('key_concepts',[])) + len(d.get('main_findings',[])), d

scored = [(score(f)[0], f, score(f)[1]) for f in files]
high = [x for x in scored if x[0] >= 9]
low  = [x for x in scored if x[0] <= 3]
assert high and low, 'caudas vazias — reajustar cortes'

rng = random.Random(SEED)
pick_high = rng.choice(sorted(high, key=lambda x: x[1].name))
pick_low  = rng.choice(sorted(low,  key=lambda x: x[1].name))
pair = [pick_high, pick_low]
rng.shuffle(pair)           # pair[0] -> A, pair[1] -> B

def anon(d):
    return {k: d.get(k) for k in SECTIONS if k in d}

meta = {
    'demo': False, 'article_id': 'PILOTO', 'round': 0,
    'title': 'Entre o Planejamento Estratégico Formal e Informal: um Estudo de Caso '
             'Exploratório sobre a Prática de Estratégia nas Organizações',
    'authors': 'Souza, C. M. L.', 'year': 2011, 'venue': 'RAC 15(5), 855-876',
}
pkg = {**meta, 'A': anon(pair[0][2]), 'B': anon(pair[1][2])}
(ROOT / 'data/piloto/pairs').mkdir(parents=True, exist_ok=True)
(ROOT / 'data/piloto/pairs/PILOTO.json').write_text(
    json.dumps(pkg, ensure_ascii=False, indent=2))

# Versão por juiz: orientação A/B balanceada (2 de cada lado) e embaralhada
# com a mesma seed — elimina efeito-ordem confundido entre juízes.
# Arquivos nomeados por slug do juiz (link ?j=<slug>): o J# nunca aparece.
# tokens opacos por juiz (link ?j=<token>): sem nome nem J# no link/arquivo;
# o mapa token↔juiz fica só aqui e no participants.csv
SLUGS = {1: 'nz4f', 2: 'bq8w', 3: 'mv3r', 4: 'gx6t'}
orient = ['high', 'high', 'low', 'low']
rng.shuffle(orient)
judge_map = {}
for i, side in enumerate(orient, 1):
    slug = SLUGS[i]
    a_src, b_src = (pick_high, pick_low) if side == 'high' else (pick_low, pick_high)
    jpkg = {**meta, 'A': anon(a_src[2]), 'B': anon(b_src[2])}
    (ROOT / f'data/piloto/pairs/PILOTO-{slug}.json').write_text(
        json.dumps(jpkg, ensure_ascii=False, indent=2))
    judge_map[f'J{i}'] = {
        'slug': slug,
        'A_from': a_src[1].name, 'A_full_name': a_src[2].get('full_name'),
        'B_from': b_src[1].name, 'B_full_name': b_src[2].get('full_name'),
    }

pmap = {
    'seed': SEED,
    'rule': 'score = n_key_concepts + n_main_findings; cauda alta >=9, baixa <=3; '
            '1 sorteado por cauda; embaralhamento A/B com a mesma seed',
    'tiers': {
        'high': sorted(f.name for _, f, _ in high),
        'low':  sorted(f.name for _, f, _ in low),
        'mid_unsampled': sorted(f.name for s, f, _ in scored if 3 < s < 9),
        'excluded_test': ['S18_PILOTO.json'],
    },
    'draw': {
        'high_pick': pick_high[1].name, 'high_score': pick_high[0],
        'low_pick': pick_low[1].name, 'low_score': pick_low[0],
    },
    'ab_map': {
        'A': {'file': pair[0][1].name,
              'full_name': pair[0][2].get('full_name'), 'tier_score': pair[0][0]},
        'B': {'file': pair[1][1].name,
              'full_name': pair[1][2].get('full_name'), 'tier_score': pair[1][0]},
    },
    'judge_map': judge_map,
    'judge_note': 'Cada juiz recebe pairs/PILOTO-{slug}.json próprio (link ?j={slug}) — '
                  'orientação A/B balanceada 2x2 e embaralhada pela seed. '
                  'O J# não aparece em link, arquivo ou tela.',
    'note': 'Ambos os lados são fichamentos de estudantes (a IA não participa do '
            'piloto — decisão de 15/10). Dados de identificação, tempo, '
            'self_assessment e reflection_log NÃO vão ao par.',
}
(ROOT / 'data/private/piloto-pair-map.json').write_text(
    json.dumps(pmap, ensure_ascii=False, indent=2))
print('A <-', pmap['ab_map']['A']['file'], '| B <-', pmap['ab_map']['B']['file'])
print('high:', [f.name for _, f, _ in high]); print('low :', [f.name for _, f, _ in low])
