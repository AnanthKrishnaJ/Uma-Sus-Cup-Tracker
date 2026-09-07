import re

with open('index.html', 'r', encoding='utf8') as f:
    html = f.read()

# 1. Fix the image bug in Dashboard table
old_img = """                                        <td>
                                            <div style="display:flex; align-items:center; gap:8px;">
                                                <img src="${App.getUmaImage(p.umaId || p.uma)}" style="width:30px; height:30px; border-radius:50%; object-fit:cover;">
                                                <span>${p.uma}</span>
                                            </div>
                                        </td>"""
new_img = """                                        <td>
                                            <div style="display:flex; align-items:center; gap:8px;">
                                                ${App.getUmaImage(p.umaId || p.uma).replace('border-radius:4px', 'border-radius:50%; width:30px; height:30px; object-fit:cover;')}
                                                <span>${p.uma}</span>
                                            </div>
                                        </td>"""
if old_img in html:
    html = html.replace(old_img, new_img)
    print("Fixed dashboard table image")
else:
    print("Could not find dashboard table image code")


# 2. Fix the Championship History 'undefined' values
# Current code:
old_history = """                const winnerRows = championshipWinners.map(winner => `
                    <div><strong>${winner.cup}</strong><span>${winner.date}</span></div>
                    <div><strong>${winner.uma}</strong><br><small style="color:var(--text-muted)">${winner.player}</small></div>
                `).join('');"""

# We need to look up the date from the race if it's missing from the winner, and use winner.trainer
new_history = """                const winnerRows = championshipWinners.map(winner => {
                    const race = this.data.races.find(r => 'Sus Cup ' + r.cupNumber === winner.cup);
                    const dateStr = winner.date || (race ? race.date : '');
                    const playerStr = winner.trainer || winner.player || '';
                    return `
                    <div><strong>${winner.cup}</strong><span style="font-size:0.85rem; color:var(--text-muted); float:right; margin-top:2px;">${dateStr}</span></div>
                    <div style="margin-top:5px;"><strong>${winner.uma}</strong><br><small style="color:var(--text-muted)">${playerStr}</small></div>
                    `;
                }).join('<div style="height:15px;"></div>');"""

if old_history in html:
    html = html.replace(old_history, new_history)
    print("Fixed championship history undefined values")
else:
    print("Could not find championship history code")

with open('index.html', 'w', encoding='utf8') as f:
    f.write(html)
