import re

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Trainer Profile Modal HTML
modal_html = """
    <div id="trainer-profile-modal" class="modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:9999; justify-content:center; align-items:center;">
        <div class="card" style="max-width: 600px; width: 90%; max-height: 90vh; overflow-y: auto; position: relative;">
            <button onclick="document.getElementById('trainer-profile-modal').style.display='none'" style="position:absolute; top:15px; right:15px; background:transparent; border:none; color:white; font-size:1.5rem; cursor:pointer;">&times;</button>
            <div id="trainer-profile-content"></div>
        </div>
    </div>
"""
if 'id="trainer-profile-modal"' not in content:
    content = content.replace('<!-- Add New Race Form -->', modal_html + '\n    <!-- Add New Race Form -->')

# 2. Add showTrainerProfile function to App
show_trainer_func = """
            showTrainerProfile(playerName) {
                const player = this.stats.players.find(p => p.name.toLowerCase() === playerName.toLowerCase());
                if (!player) return;

                let firstRace = null;
                let latestRace = null;
                let bestPos = 99;
                let uniqueUmas = new Set();
                let second = 0;
                let third = 0;

                [...this.data.races].sort((a,b) => new Date(a.date) - new Date(b.date)).forEach(race => {
                    const p = race.participants.find(part => part.player.toLowerCase() === playerName.toLowerCase());
                    if (p) {
                        if (!firstRace) firstRace = `Sus Cup ${race.cupNumber}`;
                        latestRace = `Sus Cup ${race.cupNumber}`;
                        if (p.pos < bestPos) bestPos = p.pos;
                        uniqueUmas.add(p.uma);
                        if (p.pos === 2) second++;
                        if (p.pos === 3) third++;
                    }
                });

                const html = `
                    <div style="text-align: center; border-bottom: 1px solid var(--glass-border); padding-bottom: 20px; margin-bottom: 20px;">
                        <div class="avatar-circle" style="width:100px; height:100px; margin:0 auto 15px; font-size:2.5rem; background:var(--primary); color:white;">
                            ${player.name.substring(0,2).toUpperCase()}
                        </div>
                        <h2 style="font-size: 2rem; margin: 0; color: var(--gold);">${player.name}</h2>
                        <span class="badge" style="background:var(--accent-dark); font-size: 1rem; margin-top: 10px;">SUS CUP TRAINER</span>
                    </div>
                    
                    <div class="grid-2">
                        <div>
                            <p style="color:var(--text-dim); font-size:0.9rem; text-transform:uppercase; margin-bottom:5px;">Career Stats</p>
                            <table class="data-table" style="text-align:left;">
                                <tr><td>Races Attempted</td><td style="text-align:right;"><strong>${player.runs}</strong></td></tr>
                                <tr><td>Wins 🏆</td><td style="text-align:right;"><strong>${player.w}</strong></td></tr>
                                <tr><td>Second Places 🥈</td><td style="text-align:right;"><strong>${second}</strong></td></tr>
                                <tr><td>Third Places 🥉</td><td style="text-align:right;"><strong>${third}</strong></td></tr>
                                <tr><td>Total Podiums</td><td style="text-align:right;"><strong>${player.podiums}</strong></td></tr>
                                <tr><td>Best Finish</td><td style="text-align:right;"><strong>${bestPos === 99 ? 'N/A' : bestPos}</strong></td></tr>
                            </table>
                        </div>
                        <div>
                            <p style="color:var(--text-dim); font-size:0.9rem; text-transform:uppercase; margin-bottom:5px;">Uma Stats</p>
                            <table class="data-table" style="text-align:left;">
                                <tr><td>Unique Umas Used</td><td style="text-align:right;"><strong>${uniqueUmas.size}</strong></td></tr>
                                <tr><td>First Appearance</td><td style="text-align:right;"><strong>${firstRace || 'N/A'}</strong></td></tr>
                                <tr><td>Latest Appearance</td><td style="text-align:right;"><strong>${latestRace || 'N/A'}</strong></td></tr>
                            </table>
                            <div style="margin-top: 15px;">
                                <p style="color:var(--text-dim); font-size:0.9rem; text-transform:uppercase; margin-bottom:5px;">Umas Raced</p>
                                <div style="display:flex; flex-wrap:wrap; gap:5px;">
                                    ${Array.from(uniqueUmas).map(u => `<span class="badge" style="background:rgba(255,255,255,0.1);">${u}</span>`).join('')}
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                
                document.getElementById('trainer-profile-content').innerHTML = html;
                document.getElementById('trainer-profile-modal').style.display = 'flex';
            },
"""
if 'showTrainerProfile' not in content:
    content = content.replace('renderCompare() {', show_trainer_func + '\n            renderCompare() {')

# 3. Fix compare dropdowns
render_compare_replacement = """renderCompare() {
                const p1Select = document.getElementById('compare-p1');
                const p2Select = document.getElementById('compare-p2');
                
                if (p1Select.options.length === 0 && this.stats && this.stats.players) {
                    const sortedPlayers = [...this.stats.players].sort((a,b) => a.name.localeCompare(b.name));
                    const optionsHTML = sortedPlayers.map(p => `<option value="${p.name}">${p.name}</option>`).join('');
                    p1Select.innerHTML = '<option value="">Select Player 1</option>' + optionsHTML;
                    p2Select.innerHTML = '<option value="">Select Player 2</option>' + optionsHTML;
                    
                    if (sortedPlayers.length >= 2) {
                        p1Select.value = sortedPlayers[0].name;
                        p2Select.value = sortedPlayers[1].name;
                    }
                }

                const p1Name = p1Select.value;
                const p2Name = p2Select.value;"""
content = content.replace("""renderCompare() {
                const p1Name = document.getElementById('compare-p1').value;
                const p2Name = document.getElementById('compare-p2').value;""", render_compare_replacement)

# 4. Make names clickable in leaderboards
# In renderLeaderboard(), change <td>${player.name}</td> to clickable
# Using regex to replace `${player.name}` inside <td>
content = re.sub(r'<td>(\$\{player\.name\})</td>', r'<td style="cursor:pointer; color:var(--gold);" onclick="App.showTrainerProfile(\'\1\')">\1</td>', content)
content = re.sub(r'<td><div style="display:flex; align-items:center; gap:10px;">', r'<td><div style="display:flex; align-items:center; gap:10px; cursor:pointer;" onclick="App.showTrainerProfile(\'${player.name}\')">', content)


with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected trainer profile and compare fixes.")
