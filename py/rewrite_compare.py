import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the HTML layout for Compare View
old_html = """        <!-- COMPARE VIEW -->
        <div id="view-compare" class="view-section">
            <div class="page-header">
                <h2>Compare Players</h2>
                <p>Side-by-side performance comparison</p>
            </div>
            <div class="card" style="margin-bottom:20px;">
                <div class="grid-2">
                    <div>
                        <label class="form-label">Player 1</label>
                        <select class="form-control" id="compare-p1" onchange="App.renderCompare()"></select>
                    </div>
                    <div>
                        <label class="form-label">Player 2</label>
                        <select class="form-control" id="compare-p2" onchange="App.renderCompare()"></select>
                    </div>
                </div>
            </div>
            <div id="compare-content"></div>
        </div>"""

new_html = """        <!-- COMPARE VIEW -->
        <div id="view-compare" class="view-section">
            <div class="page-header">
                <span style="font-size: 0.8rem; letter-spacing: 1.5px; color: var(--text-muted); font-weight: 800; text-transform: uppercase;">PLAYER ANALYTICS / HEAD-TO-HEAD</span>
                <h2 style="margin-top: 5px; margin-bottom: 5px;">Compare Players</h2>
                <p>Side-by-side performance comparison</p>
            </div>
            
            <div class="card compare-selector-card animate-on-scroll">
                <div class="compare-selector-grid">
                    <div class="compare-player-select p1">
                        <label class="form-label">Player 1</label>
                        <select class="form-control compare-select" id="compare-p1" onchange="App.renderCompare()"></select>
                    </div>
                    <div class="vs-badge-container">
                        <div class="vs-badge" id="vs-badge-anim">VS</div>
                    </div>
                    <div class="compare-player-select p2">
                        <label class="form-label">Player 2</label>
                        <select class="form-control compare-select" id="compare-p2" onchange="App.renderCompare()"></select>
                    </div>
                </div>
            </div>
            
            <div id="compare-content"></div>
        </div>"""

if old_html in content:
    content = content.replace(old_html, new_html)
    print("Replaced HTML structure.")
else:
    print("Could not find old HTML structure.")

# 2. Update renderCompare()
pattern_render = re.compile(r'(\s+renderCompare\(\)\s*\{)(.*?)(\n\s+renderProfileView\(\))', re.DOTALL)
match = pattern_render.search(content)

if match:
    new_js = """
        // CSS for Compare Redesign (Injected dynamically)
        if (!document.getElementById('compare-styles')) {
            const style = document.createElement('style');
            style.id = 'compare-styles';
            style.innerHTML = `
                :root {
                    --cp-1: #e63946;
                    --cp-1-light: rgba(230, 57, 70, 0.1);
                    --cp-2: #457b9d;
                    --cp-2-light: rgba(69, 123, 157, 0.1);
                }
                
                .compare-selector-card { margin-bottom: 25px; padding: 25px; }
                .compare-selector-grid {
                    display: grid;
                    grid-template-columns: 1fr 60px 1fr;
                    gap: 15px;
                    align-items: center;
                }
                .compare-player-select label { font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; display: block; color: var(--text-muted); }
                .compare-select {
                    height: 50px;
                    font-size: 1.1rem;
                    font-weight: 600;
                    border: 2px solid var(--border-color);
                    border-radius: var(--radius-md);
                    cursor: pointer;
                    transition: all 0.2s;
                }
                .compare-player-select.p1 .compare-select:focus { border-color: var(--cp-1); box-shadow: 0 0 0 3px var(--cp-1-light); }
                .compare-player-select.p2 .compare-select:focus { border-color: var(--cp-2); box-shadow: 0 0 0 3px var(--cp-2-light); }
                
                .vs-badge-container { display: flex; justify-content: center; align-items: center; margin-top: 25px; }
                .vs-badge {
                    width: 44px; height: 44px; border-radius: 50%;
                    background: var(--text-color); color: #fff;
                    display: flex; justify-content: center; align-items: center;
                    font-weight: 900; font-size: 0.9rem; font-style: italic;
                    letter-spacing: -0.5px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                    transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                }
                .vs-badge.pulse { transform: scale(1.15); }
                
                .compare-cards-grid {
                    display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-bottom: 25px;
                }
                
                .cp-card {
                    background: #fff; border-radius: var(--radius-md); border: 1px solid var(--border-color);
                    padding: 30px 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.02);
                    opacity: 0; transform: translateY(20px);
                    animation: fadeInUp 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) forwards;
                    transition: transform 0.2s, box-shadow 0.2s;
                }
                .cp-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.06); }
                .cp-card.p2 { animation-delay: 0.1s; }
                
                .cp-header { display: flex; flex-direction: column; align-items: center; margin-bottom: 25px; text-align: center; }
                .cp-avatar-wrap {
                    width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
                    font-weight: 800; font-size: 1.8rem; color: #fff; margin-bottom: 15px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    overflow: hidden;
                    position: relative;
                }
                .cp-card.p1 .cp-avatar-wrap { background: linear-gradient(135deg, #e63946, #b01b26); }
                .cp-card.p2 .cp-avatar-wrap { background: linear-gradient(135deg, #457b9d, #1d3557); }
                
                .cp-avatar-wrap img {
                    width: 100%; height: 100%; object-fit: cover;
                }

                .cp-name { font-size: 1.6rem; font-weight: 800; margin: 0 0 5px 0; color: var(--text-color); }
                .cp-rank { font-size: 0.9rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; }
                
                .cp-stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
                .cp-stat-box {
                    background: #fcfcfc; border: 1px solid var(--border-color); border-radius: 8px;
                    padding: 15px; text-align: center; display: flex; flex-direction: column; justify-content: center;
                    transition: 0.2s;
                }
                .cp-stat-box.full-width { grid-column: 1 / -1; }
                .cp-stat-label { font-size: 0.7rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5px; }
                .cp-stat-value { font-size: 1.4rem; font-weight: 800; color: var(--text-color); display: flex; align-items: baseline; justify-content: center; gap: 2px; }
                .cp-stat-value span { font-size: 0.9rem; font-weight: 700; color: var(--text-muted); }
                
                .cp-stat-box.winner.p1 { background: var(--cp-1-light); border-color: rgba(230, 57, 70, 0.3); }
                .cp-stat-box.winner.p2 { background: var(--cp-2-light); border-color: rgba(69, 123, 157, 0.3); }
                .cp-stat-box.winner.p1 .cp-stat-value { color: var(--cp-1); }
                .cp-stat-box.winner.p2 .cp-stat-value { color: var(--cp-2); }
                
                .cp-summary-card { padding: 25px 30px; opacity: 0; transform: translateY(20px); animation: fadeInUp 0.5s ease forwards; animation-delay: 0.2s; margin-bottom: 25px; }
                .cp-bar-container { margin-bottom: 20px; }
                .cp-bar-container:last-child { margin-bottom: 0; }
                .cp-bar-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 8px; }
                .cp-bar-title { font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 1px; }
                .cp-bar-vals { display: flex; font-size: 1.05rem; font-weight: 800; gap: 15px; }
                .cp-bar-vals .v1 { color: var(--cp-1); }
                .cp-bar-vals .v2 { color: var(--cp-2); }
                .cp-bar-track { height: 8px; background: var(--border-color); border-radius: 4px; display: flex; overflow: hidden; }
                .cp-bar-fill-1 { background: var(--cp-1); height: 100%; transition: width 0.6s cubic-bezier(0.165, 0.84, 0.44, 1); }
                .cp-bar-fill-2 { background: var(--cp-2); height: 100%; transition: width 0.6s cubic-bezier(0.165, 0.84, 0.44, 1); }
                
                .cp-chart-card { display: flex; flex-direction: column; opacity: 0; transform: translateY(20px); animation: fadeInUp 0.5s ease forwards; animation-delay: 0.3s; }
                .cp-insights { background: #fcfcfc; border-top: 1px solid var(--border-color); padding: 20px 25px; border-bottom-left-radius: var(--radius-md); border-bottom-right-radius: var(--radius-md); display: flex; flex-wrap: wrap; gap: 15px; justify-content: center; }
                .cp-insight-badge { background: #fff; border: 1px solid var(--border-color); padding: 8px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; display: flex; align-items: center; gap: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.02); }
                
                @media (max-width: 768px) {
                    .compare-selector-grid { grid-template-columns: 1fr; gap: 10px; }
                    .vs-badge-container { margin-top: 0; margin-bottom: 10px; }
                    .compare-cards-grid { grid-template-columns: 1fr; }
                    .cp-bar-header { flex-direction: column; align-items: center; gap: 5px; }
                }
                
                @keyframes fadeInUp { to { opacity: 1; transform: translateY(0); } }
            `;
            document.head.appendChild(style);
        }

        const p1Select = document.getElementById('compare-p1');
        const p2Select = document.getElementById('compare-p2');
        const badge = document.getElementById('vs-badge-anim');
        if (badge) {
            badge.classList.remove('pulse');
            void badge.offsetWidth; // trigger reflow
            badge.classList.add('pulse');
        }

        if (p1Select.options.length === 0 && this.stats && this.stats.players) {
            const sortedPlayers = [...this.stats.players].sort((a, b) => a.name.localeCompare(b.name));
            const optionsHTML = sortedPlayers.map(p => `<option value="${p.name}">${p.name}</option>`).join('');
            p1Select.innerHTML = '<option value="">Select Player 1</option>' + optionsHTML;
            p2Select.innerHTML = '<option value="">Select Player 2</option>' + optionsHTML;

            if (sortedPlayers.length >= 2) {
                p1Select.value = sortedPlayers[0].name;
                p2Select.value = sortedPlayers[1].name;
            }
        }

        const p1Name = p1Select.value;
        const p2Name = p2Select.value;

        const p1 = this.stats.players.find(x => x.name === p1Name);
        const p2 = this.stats.players.find(x => x.name === p2Name);

        const container = document.getElementById('compare-content');
        if (!p1 || !p2) {
            container.innerHTML = '<div class="card" style="text-align:center; padding: 50px; color: var(--text-muted); font-weight: 600;">Select two players to compare.</div>';
            return;
        }

        // Safe metric calculation helper
        const getMetrics = (p) => {
            const r = p.runs || 0;
            const w = p.w || 0;
            const winRate = r > 0 ? ((w / r) * 100).toFixed(1) : 0;
            const pods = p.podiums || 0;
            const podRate = r > 0 ? ((pods / r) * 100).toFixed(1) : 0;
            const avgFin = (p.avgFinish === '—' || p.avgFinish === undefined || isNaN(p.avgFinish)) ? '—' : parseFloat(p.avgFinish).toFixed(1);
            const consis = p.consistencyScore || '—';
            
            return { r, w, winRate: parseFloat(winRate), pods, podRate: parseFloat(podRate), avgFin, consis };
        };

        const m1 = getMetrics(p1);
        const m2 = getMetrics(p2);

        // Winner determination helper
        const getWinnerClass = (val1, val2, reverse = false) => {
            if (val1 === '—' || val2 === '—') return { p1: '', p2: '' };
            const v1 = parseFloat(val1);
            const v2 = parseFloat(val2);
            if (v1 === v2) return { p1: '', p2: '' };
            if (reverse) {
                return v1 < v2 ? { p1: 'winner p1', p2: '' } : { p1: '', p2: 'winner p2' };
            }
            return v1 > v2 ? { p1: 'winner p1', p2: '' } : { p1: '', p2: 'winner p2' };
        };

        const winsWin = getWinnerClass(m1.w, m2.w);
        const winRateWin = getWinnerClass(m1.winRate, m2.winRate);
        const podWin = getWinnerClass(m1.pods, m2.pods);
        const podRateWin = getWinnerClass(m1.podRate, m2.podRate);
        const avgFinWin = getWinnerClass(m1.avgFin, m2.avgFin, true); // lower is better
        const consisWin = getWinnerClass(m1.consis, m2.consis);

        // Helper for animating numbers
        window.animateCompareNum = (elId, val, isFloat) => {
            setTimeout(() => {
                const el = document.getElementById(elId);
                if (!el || val === '—') return;
                const end = parseFloat(val);
                let start = 0;
                const duration = 600;
                const startTime = performance.now();
                const step = (now) => {
                    const prog = Math.min((now - startTime) / duration, 1);
                    const ease = 1 - Math.pow(1 - prog, 3);
                    const current = (end * ease);
                    el.innerText = isFloat ? current.toFixed(1) : Math.floor(current);
                    if (prog < 1) requestAnimationFrame(step);
                    else el.innerText = val;
                };
                requestAnimationFrame(step);
            }, 50);
        };

        const generateAvatarHTML = (p) => {
            // Find most recent top uma for avatar
            let bestUma = null;
            let bestWins = -1;
            if (p.umaStats) {
                for (const [uma, stats] of Object.entries(p.umaStats)) {
                    if (stats.w > bestWins) {
                        bestWins = stats.w;
                        bestUma = uma;
                    }
                }
            }
            
            if (bestUma) {
                const umaId = window.getUmaId(bestUma);
                if (umaId) {
                    return \`<img src="https://gametora.com/images/umamusume/characters/chara_stand_\${umaId}_1060.png" onerror="this.style.display='none'; this.parentElement.innerText='\${p.name.substring(0,2).toUpperCase()}';" alt="\${bestUma}">\`;
                }
            }
            return p.name.substring(0, 2).toUpperCase();
        };

        container.innerHTML = `
            <div class="compare-cards-grid">
                <!-- Player 1 Card -->
                <div class="cp-card p1">
                    <div class="cp-header">
                        <div class="cp-avatar-wrap">\${generateAvatarHTML(p1)}</div>
                        <h3 class="cp-name">\${p1.name}</h3>
                        <div class="cp-rank">Rank #\${p1.rank || '—'}</div>
                    </div>
                    <div class="cp-stats-grid">
                        <div class="cp-stat-box full-width">
                            <div class="cp-stat-label">Total Races</div>
                            <div class="cp-stat-value"><span id="anim-r1">\${m1.r}</span></div>
                        </div>
                        <div class="cp-stat-box \${winsWin.p1}">
                            <div class="cp-stat-label">Wins</div>
                            <div class="cp-stat-value"><span id="anim-w1">\${m1.w}</span></div>
                        </div>
                        <div class="cp-stat-box \${winRateWin.p1}">
                            <div class="cp-stat-label">Win Rate</div>
                            <div class="cp-stat-value"><span id="anim-wr1">\${m1.winRate}</span><span>%</span></div>
                        </div>
                        <div class="cp-stat-box \${podWin.p1}">
                            <div class="cp-stat-label">Podiums</div>
                            <div class="cp-stat-value"><span id="anim-p1">\${m1.pods}</span></div>
                        </div>
                        <div class="cp-stat-box \${podRateWin.p1}">
                            <div class="cp-stat-label">Podium Rate</div>
                            <div class="cp-stat-value"><span id="anim-pr1">\${m1.podRate}</span><span>%</span></div>
                        </div>
                        <div class="cp-stat-box \${avgFinWin.p1}">
                            <div class="cp-stat-label">Avg Finish</div>
                            <div class="cp-stat-value">\${m1.avgFin}</div>
                        </div>
                        <div class="cp-stat-box \${consisWin.p1}">
                            <div class="cp-stat-label">Consistency</div>
                            <div class="cp-stat-value">\${m1.consis}</div>
                        </div>
                    </div>
                </div>
                
                <!-- Player 2 Card -->
                <div class="cp-card p2">
                    <div class="cp-header">
                        <div class="cp-avatar-wrap">\${generateAvatarHTML(p2)}</div>
                        <h3 class="cp-name">\${p2.name}</h3>
                        <div class="cp-rank">Rank #\${p2.rank || '—'}</div>
                    </div>
                    <div class="cp-stats-grid">
                        <div class="cp-stat-box full-width">
                            <div class="cp-stat-label">Total Races</div>
                            <div class="cp-stat-value"><span id="anim-r2">\${m2.r}</span></div>
                        </div>
                        <div class="cp-stat-box \${winsWin.p2}">
                            <div class="cp-stat-label">Wins</div>
                            <div class="cp-stat-value"><span id="anim-w2">\${m2.w}</span></div>
                        </div>
                        <div class="cp-stat-box \${winRateWin.p2}">
                            <div class="cp-stat-label">Win Rate</div>
                            <div class="cp-stat-value"><span id="anim-wr2">\${m2.winRate}</span><span>%</span></div>
                        </div>
                        <div class="cp-stat-box \${podWin.p2}">
                            <div class="cp-stat-label">Podiums</div>
                            <div class="cp-stat-value"><span id="anim-p2">\${m2.pods}</span></div>
                        </div>
                        <div class="cp-stat-box \${podRateWin.p2}">
                            <div class="cp-stat-label">Podium Rate</div>
                            <div class="cp-stat-value"><span id="anim-pr2">\${m2.podRate}</span><span>%</span></div>
                        </div>
                        <div class="cp-stat-box \${avgFinWin.p2}">
                            <div class="cp-stat-label">Avg Finish</div>
                            <div class="cp-stat-value">\${m2.avgFin}</div>
                        </div>
                        <div class="cp-stat-box \${consisWin.p2}">
                            <div class="cp-stat-label">Consistency</div>
                            <div class="cp-stat-value">\${m2.consis}</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Comparison Bars Summary -->
            <div class="card cp-summary-card">
                <h3 style="margin-bottom: 25px; text-align: center; font-size: 1.2rem;">Head-to-Head Balance</h3>
                
                <div class="cp-bar-container">
                    <div class="cp-bar-header">
                        <div class="cp-bar-vals"><span class="v1">\${m1.w} W</span></div>
                        <div class="cp-bar-title">Total Wins</div>
                        <div class="cp-bar-vals"><span class="v2">\${m2.w} W</span></div>
                    </div>
                    <div class="cp-bar-track">
                        <div class="cp-bar-fill-1" style="width: \${(m1.w / Math.max(1, m1.w + m2.w)) * 100}%"></div>
                        <div class="cp-bar-fill-2" style="width: \${(m2.w / Math.max(1, m1.w + m2.w)) * 100}%"></div>
                    </div>
                </div>
                
                <div class="cp-bar-container">
                    <div class="cp-bar-header">
                        <div class="cp-bar-vals"><span class="v1">\${m1.winRate}%</span></div>
                        <div class="cp-bar-title">Win Rate</div>
                        <div class="cp-bar-vals"><span class="v2">\${m2.winRate}%</span></div>
                    </div>
                    <div class="cp-bar-track">
                        <div class="cp-bar-fill-1" style="width: \${(m1.winRate / Math.max(1, m1.winRate + m2.winRate)) * 100}%"></div>
                        <div class="cp-bar-fill-2" style="width: \${(m2.winRate / Math.max(1, m1.winRate + m2.winRate)) * 100}%"></div>
                    </div>
                </div>
                
                <div class="cp-bar-container">
                    <div class="cp-bar-header">
                        <div class="cp-bar-vals"><span class="v1">\${m1.pods}</span></div>
                        <div class="cp-bar-title">Podiums</div>
                        <div class="cp-bar-vals"><span class="v2">\${m2.pods}</span></div>
                    </div>
                    <div class="cp-bar-track">
                        <div class="cp-bar-fill-1" style="width: \${(m1.pods / Math.max(1, m1.pods + m2.pods)) * 100}%"></div>
                        <div class="cp-bar-fill-2" style="width: \${(m2.pods / Math.max(1, m1.pods + m2.pods)) * 100}%"></div>
                    </div>
                </div>
            </div>

            <!-- Radar Chart -->
            <div class="card cp-chart-card" style="padding: 0; overflow: hidden;">
                <div style="padding: 30px;">
                    <h3 style="text-align:center; margin-bottom: 5px;">Performance Radar</h3>
                    <p style="text-align:center; font-size:0.85rem; color:var(--text-muted); margin-bottom: 25px;">Overall performance across key tournament metrics</p>
                    <div style="max-width: 600px; margin: 0 auto; min-height: 350px;">
                        <canvas id="compareRadarChart"></canvas>
                    </div>
                </div>
                
                <div class="cp-insights" id="cp-insights-container">
                    <!-- Insights injected here -->
                </div>
            </div>
        `;

        // Trigger animations
        window.animateCompareNum('anim-r1', m1.r, false);
        window.animateCompareNum('anim-w1', m1.w, false);
        window.animateCompareNum('anim-wr1', m1.winRate, true);
        window.animateCompareNum('anim-p1', m1.pods, false);
        window.animateCompareNum('anim-pr1', m1.podRate, true);
        
        window.animateCompareNum('anim-r2', m2.r, false);
        window.animateCompareNum('anim-w2', m2.w, false);
        window.animateCompareNum('anim-wr2', m2.winRate, true);
        window.animateCompareNum('anim-p2', m2.pods, false);
        window.animateCompareNum('anim-pr2', m2.podRate, true);

        // Generate Insights
        const insights = [];
        if (m1.w > m2.w) insights.push(`🏆 \${p1.name} leads in total wins`);
        else if (m2.w > m1.w) insights.push(`🏆 \${p2.name} leads in total wins`);
        
        if (m1.avgFin !== '—' && m2.avgFin !== '—') {
            if (parseFloat(m1.avgFin) < parseFloat(m2.avgFin)) insights.push(`📊 \${p1.name} has a better average finish`);
            else if (parseFloat(m2.avgFin) < parseFloat(m1.avgFin)) insights.push(`📊 \${p2.name} has a better average finish`);
        }
        
        if (m1.consis !== '—' && m2.consis !== '—') {
            if (parseFloat(m1.consis) > parseFloat(m2.consis)) insights.push(`🔥 \${p1.name} is a more consistent player`);
            else if (parseFloat(m2.consis) > parseFloat(m1.consis)) insights.push(`🔥 \${p2.name} is a more consistent player`);
        }
        
        const insightsContainer = document.getElementById('cp-insights-container');
        if (insights.length > 0) {
            insightsContainer.innerHTML = insights.map(i => `<div class="cp-insight-badge">\${i}</div>`).join('');
        } else {
            insightsContainer.innerHTML = `<div class="cp-insight-badge" style="margin: 0 auto; color: var(--text-muted);">Matches are closely contested</div>`;
        }

        // Render Chart
        const p1Data = [p1.winRate || 0, p1.top3Rate || 0, p1.consistencyScore || 0, p1.experienceScore || 0, p1.top5Rate || 0, Math.min(100, ((p1.podiums||0) / Math.max(1, p1.runs||0)) * 100)];
        const p2Data = [p2.winRate || 0, p2.top3Rate || 0, p2.consistencyScore || 0, p2.experienceScore || 0, p2.top5Rate || 0, Math.min(100, ((p2.podiums||0) / Math.max(1, p2.runs||0)) * 100)];

        if (window.compareRadarInstance) {
            window.compareRadarInstance.data.datasets[0].label = p1.name;
            window.compareRadarInstance.data.datasets[0].data = p1Data;
            window.compareRadarInstance.data.datasets[1].label = p2.name;
            window.compareRadarInstance.data.datasets[1].data = p2Data;
            window.compareRadarInstance.update();
        } else {
            const ctx = document.getElementById('compareRadarChart').getContext('2d');
            window.compareRadarInstance = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['Win Rate', 'Podium Rate', 'Consistency', 'Experience', 'Top 5 Rate', 'Podium/Race Ratio'],
                    datasets: [{
                        label: p1.name,
                        data: p1Data,
                        backgroundColor: 'rgba(230, 57, 70, 0.25)',
                        borderColor: '#e63946',
                        pointBackgroundColor: '#e63946',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: '#e63946',
                        borderWidth: 2
                    }, {
                        label: p2.name,
                        data: p2Data,
                        backgroundColor: 'rgba(69, 123, 157, 0.25)',
                        borderColor: '#457b9d',
                        pointBackgroundColor: '#457b9d',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: '#457b9d',
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        r: {
                            angleLines: { color: 'rgba(0,0,0,0.1)' },
                            grid: { color: 'rgba(0,0,0,0.1)' },
                            pointLabels: { font: { size: 12, family: "'Inter', sans-serif", weight: 'bold' }, color: '#666' },
                            ticks: { display: false, min: 0, max: 100 }
                        }
                    },
                    plugins: { 
                        legend: { 
                            position: 'top',
                            labels: { usePointStyle: true, padding: 20, font: { family: "'Inter', sans-serif", size: 13, weight: 'bold' } }
                        } 
                    }
                }
            });
        }
    }
"""

    content = content[:match.start(1)] + new_js + content[match.start(3):]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Rewritten Compare View.")
else:
    print("Could not find renderCompare function.")
