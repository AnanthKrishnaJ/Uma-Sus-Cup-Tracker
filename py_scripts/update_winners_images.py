import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

old_winners_block = """    const cupWinners = this.data.winners.filter(w => w.cup === `Sus Cup ${race.cupNumber}`);
    if (cupWinners.length > 1 || (cupWinners.length === 1 && cupWinners[0].rankLabel)) {
        html += `<div class="card" style="margin-top:20px; background:#fafafa; border:1px solid #eee;">
            <h3 style="margin-bottom:15px; font-size:1.4rem; display:flex; align-items:center; gap:10px;"><i class="fa-solid fa-trophy" style="color:var(--gold);"></i> Sus Cup ${race.cupNumber} Winners</h3>
            <div class="grid-3" style="gap:15px;">`;
        cupWinners.forEach(w => {
            html += `<div style="background:white; padding:15px; border-radius:8px; box-shadow:0 2px 4px rgba(0,0,0,0.05); text-align:center;">
                <div style="font-weight:bold; font-size:1.1rem; color:var(--primary); margin-bottom:5px;">${w.rankLabel || 'Winner'}</div>
                <div style="font-weight:800; font-size:1.2rem;">${w.trainer}</div>
                <div style="color:var(--text-muted); margin-top:5px;"><i class="fa-solid fa-horse-head"></i> ${w.uma}</div>
            </div>`;
        });
        html += `</div></div>`;
    }"""

new_winners_block = """    const cupWinners = this.data.winners.filter(w => w.cup === `Sus Cup ${race.cupNumber}`);
    if (cupWinners.length > 1 || (cupWinners.length === 1 && cupWinners[0].rankLabel)) {
        html += `<div class="card" style="margin-top:20px; background:#fafafa; border:1px solid #eee;">
            <h3 style="margin-bottom:15px; font-size:1.4rem; display:flex; align-items:center; gap:10px;"><i class="fa-solid fa-trophy" style="color:var(--gold);"></i> Sus Cup ${race.cupNumber} Winners</h3>
            <div class="grid-3" style="gap:15px;">`;
        cupWinners.forEach(w => {
            let p = race.participants.find(part => part.player === w.trainer && part.uma === w.uma);
            let umaId = w.umaId || (p ? p.umaId : '');
            let imgHtml = umaId ? this.getUmaImage(umaId).replace('width:40px;height:40px', 'width:60px;height:60px;margin:10px auto') : '<i class="fa-solid fa-horse-head" style="font-size:2rem; margin:10px 0;"></i>';
            html += `<div style="background:white; padding:15px; border-radius:8px; box-shadow:0 2px 4px rgba(0,0,0,0.05); text-align:center;">
                <div style="font-weight:bold; font-size:1.1rem; color:var(--primary); margin-bottom:5px;">${w.rankLabel || 'Winner'}</div>
                ${imgHtml}
                <div style="font-weight:800; font-size:1.2rem; margin-top:5px;">${w.trainer}</div>
                <div style="color:var(--text-muted); margin-top:5px;">${w.uma}</div>
            </div>`;
        });
        html += `</div></div>`;
    }"""

if old_winners_block in text:
    new_text = text.replace(old_winners_block, new_winners_block)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced winners block successfully!")
else:
    print("Could not find old winners block.")
