import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data = json.loads(text[start + 21:end].strip().rstrip(';'))

# Helpers
def get_participant(cup_num, pos_or_uma, player=None):
    for r in data['races']:
        if str(cup_num) in str(r.get('cupNumber')):
            for p in r.get('participants', []):
                if isinstance(pos_or_uma, int):
                    if p['pos'] == pos_or_uma: return r, p
                else:
                    if p['uma'] == pos_or_uma and (not player or p['player'] == player): return r, p
    return None, None

# Build new winners
winners_to_add = []

cup_specs = [
    (16, [
        (1, "A+ Winner"),
        (3, "A Winner"),
        (4, "B+ Winner")
    ]),
    (17, [
        (1, "Triple Guts Winner"),
        (2, "Double Guts Winner"),
        (4, "Single Guts Winner")
    ]),
    (18, [
        (1, "Triple SSR Winner"),
        (2, "Double SSR Winner"),
        (10, "Single SSR Winner")
    ])
]

for cup_num, specs in cup_specs:
    for pos, rank_label in specs:
        race, p = get_participant(cup_num, pos)
        if race and p:
            winner = {
                "cup": f"Sus Cup {cup_num}",
                "trainer": p['player'],
                "uma": p['uma'],
                "version": p.get('version', 'Original / Default'),
                "url": p.get('characterUrl', ''),
                "race": race['name'],
                "date": race['date'],
                "result": p.get('time', p.get('gap', '')),
                "umaId": p.get('umaId'),
                "rankLabel": rank_label
            }
            winners_to_add.append(winner)

# Remove existing winners for 16, 17, 18 and add new ones
data['winners'] = [w for w in data.get('winners', []) if not any(str(c) in str(w.get('cup', '')) for c in [16, 17, 18])]
data['winners'].extend(winners_to_add)

# Update Cup 17 Tokai Teio to normal
for r in data['races']:
    if '17' in str(r.get('cupNumber')):
        for p in r.get('participants', []):
            if 'Tokai Teio' in p.get('uma', ''):
                p['umaId'] = 'tokai-teio'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/tokai-teio'
    if '18' in str(r.get('cupNumber')):
        for p in r.get('participants', []):
            if 'Symboli Rudolf' in p.get('uma', ''):
                p['umaId'] = '101702'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/101702-symboli-rudolf'

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

# Modify JS rendering
# 1. renderHistory
history_orig = '''const winner = winners.find(item => item.cup === `Sus Cup ${race.cupNumber}`) || race.participants.find(p => p.pos === 1);
                    return `<div class="timeline-item"><div class="card" style="margin-bottom:0; cursor:pointer;" onclick="App.showRaceDetail(${race.id})">
                        <span class="badge" style="background:var(--accent-dark);">SUS CUP ${race.cupNumber}</span>
                        <h3 style="font-size:1.35rem; margin:12px 0 5px;">${race.name}</h3>
                        <p style="color:var(--text-muted); font-weight:700;">${race.date}  ${race.course} ${race.distance}m ${race.surface}</p>
                        <p style="margin-top:12px; font-weight:800;">Winner: ${winner?.trainer || winner?.player || 'Not recorded'}  ${winner?.uma || 'Not recorded'}</p>'''

history_new = '''const cupWinners = winners.filter(item => item.cup === `Sus Cup ${race.cupNumber}`);
                    let winnersHtml = '';
                    if (cupWinners.length > 0) {
                        winnersHtml = cupWinners.map(w => `<p style="margin-top:6px; font-weight:800;">${w.rankLabel || 'Winner'}: ${w.trainer} <span style="opacity:0.7">&mdash;</span> ${w.uma}</p>`).join('');
                    } else {
                        const winner = race.participants.find(p => p.pos === 1);
                        winnersHtml = `<p style="margin-top:12px; font-weight:800;">Winner: ${winner?.player || 'Not recorded'} <span style="opacity:0.7">&mdash;</span> ${winner?.uma || 'Not recorded'}</p>`;
                    }
                    
                    return `<div class="timeline-item"><div class="card" style="margin-bottom:0; cursor:pointer;" onclick="App.showRaceDetail(${race.id})">
                        <span class="badge" style="background:var(--accent-dark);">SUS CUP ${race.cupNumber}</span>
                        <h3 style="font-size:1.35rem; margin:12px 0 5px;">${race.name}</h3>
                        <p style="color:var(--text-muted); font-weight:700;">${race.date}  ${race.course} ${race.distance}m ${race.surface}</p>
                        <div style="margin-top:12px;">${winnersHtml}</div>'''

text = text.replace(history_orig, history_new)

# 2. renderDashboard - Championship Trainer
dashboard_orig = '''<div><strong>${winner.trainer}</strong><span>Champion Trainer</span></div>'''
dashboard_new = '''<div><strong>${winner.trainer}</strong><span>${winner.rankLabel || 'Champion Trainer'}</span></div>'''
text = text.replace(dashboard_orig, dashboard_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Update script successful!")
