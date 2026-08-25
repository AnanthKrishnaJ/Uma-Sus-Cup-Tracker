import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# I want to inject the latest results table into the home screen.
# The `latest-cup-summary` box currently has the 1st place winner.
# Let's see how `latest-cup-summary` is generated inside renderDashboard.

# I will find the renderDashboard() definition inside `App = {`
idx = html.find('renderDashboard() {')
if idx != -1:
    end_idx = html.find('},', idx)
    original_code = html[idx:end_idx]

    new_code = """renderDashboard() {
                const latestRace = [...this.data.races].sort((a, b) => {
                    const d1 = new Date(a.date); const d2 = new Date(b.date);
                    if (isNaN(d1)) return 1; if (isNaN(d2)) return -1;
                    return d2 - d1;
                })[0] || this.data.races[this.data.races.length - 1];
                
                const latestWinner = latestRace?.participants.find(p => p.position === 1 || p.position === '1');
                
                let resultsHtml = '';
                if (latestRace && latestRace.participants) {
                    const sortedParticipants = [...latestRace.participants].sort((a,b) => {
                        let posA = parseInt(a.position); let posB = parseInt(b.position);
                        if(isNaN(posA)) posA = 99; if(isNaN(posB)) posB = 99;
                        return posA - posB;
                    });
                    
                    resultsHtml = `<div style="margin-top:20px; max-height: 300px; overflow-y: auto; background: var(--bg-alt); padding: 10px; border-radius: 8px;">
                        <h4 style="margin-bottom: 10px; font-size: 1rem; color: var(--primary);">Latest Race Results</h4>
                        <table class="table" style="font-size: 0.85rem; width: 100%;">
                            <thead>
                                <tr>
                                    <th>Pos</th>
                                    <th>Uma</th>
                                    <th>Player</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${sortedParticipants.map(p => `
                                    <tr>
                                        <td><strong>${p.position || '-'}</strong></td>
                                        <td>
                                            <div style="display:flex; align-items:center; gap:8px;">
                                                <img src="${App.getUmaImage(p.umaId || p.uma)}" style="width:30px; height:30px; border-radius:50%; object-fit:cover;">
                                                <span>${p.uma}</span>
                                            </div>
                                        </td>
                                        <td>${p.player}</td>
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                    </div>`;
                }

                document.getElementById('latest-cup-summary').innerHTML = `
                    <span class="eyebrow">Latest champion</span>
                    <h3 style="font-size:1.7rem; margin:15px 0 8px;">${latestRace ? `Sus Cup ${latestRace.cupNumber || latestRace.id} / ${latestRace.name || ''}` : 'No races recorded'}</h3>
                    <p style="font-weight:800; margin-bottom:8px;">${latestWinner?.player || 'Not recorded'} — ${latestWinner?.uma || 'Not recorded'}</p>
                    <p style="color:var(--text-muted); font-size:.85rem; margin-bottom:15px;">${latestRace ? `${latestRace.date || ''} — ${latestRace.course || ''} ${latestRace.distance || ''} ${latestRace.surface || ''}` : ''}</p>
                    ${resultsHtml}
                `;
                document.getElementById('dash-stats').innerHTML = `
                    <div class="stat-block"><div class="val">${this.stats.totalRaces}</div><div class="lbl">Total Cups</div></div>
                    <div class="stat-block"><div class="val">${this.stats.totalPlayers}</div><div class="lbl">Active Players</div></div>
                    <div class="stat-block"><div class="val">${this.stats.totalUmas}</div><div class="lbl">Umas Fielded</div></div>
                `;

                const championshipWinners = this.data.winners.filter(winner => !NPC_PROFILES[winner.uma] && winner.type !== 'NPC Uma');
                const winnerRows = championshipWinners.map(winner => `
                    <div><strong>${winner.cup}</strong><span>${winner.date}</span></div>
                    <div><strong>${winner.uma}</strong><br><small style="color:var(--text-muted)">${winner.player}</small></div>
                `).join('');
                document.getElementById('championship-record').innerHTML = `
                    <h3 style="margin-bottom: 20px;"><i class="fa-solid fa-medal" style="color:var(--gold)"></i> Championship History</h3>
                    <div class="grid-4" style="gap:15px;">${winnerRows}</div>
                `;

                document.getElementById('dash-player-list').innerHTML = Object.values(this.stats.players)
                    .sort((a, b) => b.wins - a.wins || b.races - a.races)
                    .slice(0, 5)
                    .map((p, i) => `
                        <div class="list-item">
                            <div class="rank">#${i + 1}</div>
                            <div class="info">
                                <strong>${p.name}</strong>
                                <span>${p.races} races</span>
                            </div>
                            <div class="val">${p.wins} W</div>
                        </div>
                    `).join('');

                document.getElementById('dash-uma-list').innerHTML = Object.values(this.stats.umas)
                    .sort((a, b) => b.wins - a.wins || b.races - a.races)
                    .slice(0, 5)
                    .map((u, i) => `
                        <div class="list-item">
                            <div class="rank">#${i + 1}</div>
                            <div style="width:40px;height:40px;border-radius:50%;overflow:hidden;flex-shrink:0;">
                                <img src="${App.getUmaImage(u.id || u.name)}" style="width:100%;height:100%;object-fit:cover;">
                            </div>
                            <div class="info">
                                <strong>${u.name}</strong>
                                <span>${u.races} races</span>
                            </div>
                            <div class="val">${u.wins} W</div>
                        </div>
                    `).join('');
            """

    new_html = html[:idx] + new_code + html[end_idx:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated renderDashboard")
else:
    print("Could not find renderDashboard()")
