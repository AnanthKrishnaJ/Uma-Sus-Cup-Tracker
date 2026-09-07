import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Player Rankings fix
html = html.replace('<span>${p.races} races</span>', '<span>${p.runs} races</span>')
html = html.replace('<div class="val">${p.wins} W</div>', '<div class="val">${p.w} W</div>')
html = html.replace('<div class=\'val\'>${p.wins} W</div>', '<div class=\'val\'>${p.w} W</div>')

# 2. Top Umas fix
html = re.sub(r'<img src=\"\$\{App\.getUmaImage\(u\.id \|\| u\.name\)\}\" style=\"width:100%;height:100%;object-fit:cover;\">', r'${App.getUmaImage(u.id || u.name)}', html)
html = html.replace('<span>${u.races} races</span>', '<span>${u.runs} races</span>')
html = html.replace('<div class="val">${u.wins} W</div>', '<div class="val">${u.w} W</div>')
html = html.replace('<div class=\'val\'>${u.wins} W</div>', '<div class=\'val\'>${u.w} W</div>')

# 3. Stats label fix
html = html.replace('<div class="lbl">Umas Fielded</div>', '<div class="lbl">Total Umas</div>')

# 4. Championship History fix
old_winner_rows = """                const winnerRows = championshipWinners.map(winner => {
                    const race = this.data.races.find(r => 'Sus Cup ' + r.cupNumber === winner.cup);
                    const dateStr = winner.date || (race ? race.date : '');
                    const playerStr = winner.trainer || winner.player || '';
                    return `
                    <div><strong>${winner.cup}</strong><span style="font-size:0.85rem; color:var(--text-muted); float:right; margin-top:2px;">${dateStr}</span></div>
                    <div style="margin-top:5px;"><strong>${winner.uma}</strong><br><small style="color:var(--text-muted)">${playerStr}</small></div>
                    `;
                }).join('<div style="height:15px;"></div>');"""

new_winner_rows = """                const winnerRows = championshipWinners.map(winner => {
                    const race = this.data.races.find(r => 'Sus Cup ' + r.cupNumber === winner.cup);
                    const rawDate = winner.date || (race ? race.date : '');
                    const dateStr = rawDate ? rawDate.split(",")[0].trim() : '';
                    const playerStr = winner.trainer || winner.player || '';
                    return `
                    <div><strong>${winner.cup}</strong><span style="font-size:0.85rem; color:var(--text-muted); float:right; margin-top:2px;">${dateStr}</span></div>
                    <div style="margin-top:5px;"><strong>${playerStr}</strong></div>
                    `;
                }).join('<div style="height:15px;"></div>');"""

html = html.replace(old_winner_rows, new_winner_rows)

# 5. Latest Champion fix (p.pos instead of p.position)
html = html.replace('<td><strong>${p.position || \'-\'}</strong></td>', '<td><strong>${p.pos || \'-\'}</strong></td>')
html = html.replace('ΓÇö', '&mdash;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
