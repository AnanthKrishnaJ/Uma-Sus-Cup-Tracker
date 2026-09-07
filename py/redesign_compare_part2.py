import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the new renderCompare function without backslash syntax error
new_render_compare = """            renderCompare() {
        if (!this.stats || !this.stats.players) return;
        
        // --- CSS INJECTION ---
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
                
                .cp-btn-swap {
                    background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 50%;
                    width: 44px; height: 44px; display: flex; align-items: center; justify-content: center;
                    cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.05); transition: 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                }
                .cp-btn-swap:hover { transform: rotate(180deg) scale(1.1); box-shadow: 0 6px 15px rgba(0,0,0,0.1); }
                .cp-btn-swap svg { width: 20px; height: 20px; fill: var(--text-color); }
                
                .compare-selector-card { margin-bottom: 25px; padding: 25px; }
                .compare-selector-grid {
                    display: grid; grid-template-columns: 1fr auto 1fr; gap: 20px; align-items: center;
                }
                .compare-player-select label { font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; display: block; color: var(--text-muted); }
                .compare-select {
                    height: 50px; font-size: 1.1rem; font-weight: 600; border: 2px solid var(--border-color); border-radius: var(--radius-md); cursor: pointer; transition: all 0.2s; width: 100%;
                }
                .compare-player-select.p1 .compare-select:focus { border-color: var(--cp-1); box-shadow: 0 0 0 3px var(--cp-1-light); }
                .compare-player-select.p2 .compare-select:focus { border-color: var(--cp-2); box-shadow: 0 0 0 3px var(--cp-2-light); }
                
                .vs-badge-container { display: flex; flex-direction: column; justify-content: center; align-items: center; margin-top: 25px; gap: 10px; }
                .vs-badge {
                    width: 44px; height: 44px; border-radius: 50%; background: var(--text-color); color: #fff;
                    display: flex; justify-content: center; align-items: center; font-weight: 900; font-size: 0.9rem; font-style: italic;
                    letter-spacing: -0.5px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); transition: transform 0.3s;
                }
                
                .compare-cards-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-bottom: 25px; }
                @media(max-width: 768px) { .compare-cards-grid { grid-template-columns: 1fr; } .compare-selector-grid { grid-template-columns: 1fr; } .vs-badge-container { flex-direction: row; margin-top:0; margin-bottom: 15px;} }
                
                .cp-card {
                    background: #fff; border-radius: var(--radius-md); border: 1px solid var(--border-color);
                    padding: 30px 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.02); opacity: 0; transform: translateY(20px);
                    animation: fadeInUp 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) forwards; transition: transform 0.3s, box-shadow 0.3s;
                }
                .cp-card:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0,0,0,0.06); }
                .cp-card.p2 { animation-delay: 0.1s; }
                
                .cp-header { display: flex; flex-direction: column; align-items: center; margin-bottom: 25px; text-align: center; }
                .cp-avatar-wrap {
                    width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
                    font-weight: 800; font-size: 1.8rem; color: #fff; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                    overflow: hidden; position: relative;
                }
                .cp-card.p1 .cp-avatar-wrap { background: linear-gradient(135deg, #e63946, #b01b26); }
                .cp-card.p2 .cp-avatar-wrap { background: linear-gradient(135deg, #457b9d, #1d3557); }
                .cp-avatar-wrap img { width: 100%; height: 100%; object-fit: cover; }
                .cp-name { font-size: 1.6rem; font-weight: 800; margin: 0 0 5px 0; color: var(--text-color); }
                .cp-rank { font-size: 0.9rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; }
                
                .cp-stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px;}
                .cp-stat-box {
                    background: #fcfcfc; border: 1px solid var(--border-color); border-radius: 8px;
                    padding: 15px; text-align: center; display: flex; flex-direction: column; justify-content: center; transition: 0.2s;
                }
                .cp-stat-box.full-width { grid-column: 1 / -1; }
                .cp-stat-label { font-size: 0.7rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5px; }
                .cp-stat-value { font-size: 1.4rem; font-weight: 800; color: var(--text-color); display: flex; align-items: baseline; justify-content: center; gap: 2px; }
                .cp-stat-value span { font-size: 0.9rem; font-weight: 700; color: var(--text-muted); }
                
                .cp-best-uma { background: #f9f9f9; border: 1px solid var(--border-color); border-radius: 8px; padding: 15px; text-align: center; }
                .cp-best-uma-label { font-size: 0.75rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }
                .cp-best-uma-name { font-size: 1.2rem; font-weight: 800; color: var(--text-color); margin-bottom: 5px; }
                .cp-best-uma-stats { font-size: 0.85rem; font-weight: 600; color: var(--text-dim); }
                
                .cp-summary-card { padding: 25px 30px; opacity: 0; transform: translateY(20px); animation: fadeInUp 0.5s ease forwards; animation-delay: 0.2s; margin-bottom: 25px; }
                .cp-section-title { font-size: 1.2rem; font-weight: 800; color: var(--text-color); margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px; text-align: center;}
                
                .cp-bar-container { margin-bottom: 20px; }
                .cp-bar-container:last-child { margin-bottom: 0; }
                .cp-bar-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 8px; }
                .cp-bar-title { font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 1px; }
                .cp-bar-vals { display: flex; font-size: 1.05rem; font-weight: 800; gap: 15px; }
                .cp-bar-vals .v1 { color: var(--cp-1); }
                .cp-bar-vals .v2 { color: var(--cp-2); }
                .cp-bar-track { width: 100%; height: 8px; background: #eee; border-radius: 4px; display: flex; overflow: hidden; }
                .cp-bar-fill-1 { height: 100%; background: var(--cp-1); transition: width 1s cubic-bezier(0.22, 1, 0.36, 1); }
                .cp-bar-fill-2 { height: 100%; background: var(--cp-2); transition: width 1s cubic-bezier(0.22, 1, 0.36, 1); }
                
                .cp-breakdown-row { display: flex; margin-bottom: 15px; align-items: center; }
                .cp-breakdown-label { width: 60px; font-weight: 800; font-size: 0.9rem; color: var(--text-muted); }
                .cp-breakdown-bars { flex-grow: 1; display: flex; flex-direction: column; gap: 6px; }
                .cp-bd-bar-wrap { display: flex; align-items: center; gap: 10px; }
                .cp-bd-bar-track { flex-grow: 1; height: 16px; background: #f0f0f0; border-radius: 4px; overflow: hidden; }
                .cp-bd-bar-fill { height: 100%; border-radius: 4px; transition: width 1s cubic-bezier(0.22, 1, 0.36, 1); }
                .cp-bd-bar-fill.p1 { background: var(--cp-1); }
                .cp-bd-bar-fill.p2 { background: var(--cp-2); }
                .cp-bd-stats { width: 140px; font-size: 0.8rem; font-weight: 700; color: var(--text-dim); text-align: right; }
                .cp-bd-stats span { font-weight: 800; color: var(--text-color); display: inline-block; width: 45px; text-align: left; }
                
                .cp-standings-wrap { overflow-x: auto; margin-bottom: 25px; }
                .cp-standings-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
                .cp-standings-table th { background: #f8f9fa; padding: 12px 15px; font-weight: 800; color: var(--text-muted); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.5px; border-bottom: 2px solid var(--border-color); text-align: right; white-space: nowrap; }
                .cp-standings-table th:nth-child(1), .cp-standings-table th:nth-child(2) { text-align: left; }
                .cp-standings-table td { padding: 12px 15px; border-bottom: 1px solid var(--border-color); text-align: right; font-weight: 600; color: var(--text-color); transition: background 0.2s;}
                .cp-standings-table td:nth-child(1), .cp-standings-table td:nth-child(2) { text-align: left; }
                .cp-standings-table tr:hover td { background: #fcfcfc; }
                .cp-standings-table tr.highlight-p1 td { background: var(--cp-1-light); border-bottom: 1px solid rgba(230, 57, 70, 0.3); }
                .cp-standings-table tr.highlight-p2 td { background: var(--cp-2-light); border-bottom: 1px solid rgba(69, 123, 157, 0.3); }
                
                .cp-insights-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }
                .cp-insight-box { background: #fcfcfc; border: 1px solid var(--border-color); border-radius: 8px; padding: 20px; }
                .cp-insight-name { font-size: 1rem; font-weight: 800; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 0.5px; }
                .cp-insight-box.p1 .cp-insight-name { color: var(--cp-1); }
                .cp-insight-box.p2 .cp-insight-name { color: var(--cp-2); }
                .cp-insight-list { list-style: none; padding: 0; margin: 0; }
                .cp-insight-list li { font-size: 0.9rem; font-weight: 600; color: var(--text-dim); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
                .cp-insight-list li:before { content: "✓"; font-weight: 900; }
                .cp-insight-box.p1 .cp-insight-list li:before { color: var(--cp-1); }
                .cp-insight-box.p2 .cp-insight-list li:before { color: var(--cp-2); }
                
                .cp-overall-edge { background: #fff; border: 2px solid var(--border-color); border-radius: 8px; padding: 20px; text-align: center; margin-top: 15px;}
                .cp-edge-label { font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 1px; margin-bottom: 5px;}
                .cp-edge-winner { font-size: 1.8rem; font-weight: 900; margin-bottom: 5px; }
                .cp-edge-desc { font-size: 0.9rem; font-weight: 600; color: var(--text-dim); }
                
                .cp-gen-btn-wrap { text-align: center; margin-top: 30px; margin-bottom: 20px; }
                .cp-gen-btn {
                    background: var(--text-color); color: #fff; border: none; padding: 15px 30px; font-size: 1rem; font-weight: 800; border-radius: var(--radius-md);
                    cursor: pointer; display: inline-flex; align-items: center; gap: 10px; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-transform: uppercase; letter-spacing: 1px;
                }
                .cp-gen-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.15); }
                .cp-gen-btn svg { width: 18px; height: 18px; fill: #fff; }
                
                /* Generator overlay styling */
                #cp-gen-card {
                    background: #fff; width: 600px; padding: 40px; box-sizing: border-box; position: absolute; left: -9999px; top: -9999px;
                    border: 1px solid #ddd; font-family: 'Inter', sans-serif;
                }
                .gen-header { text-align: center; margin-bottom: 30px; border-bottom: 2px solid #f0f0f0; padding-bottom: 20px; }
                .gen-title { font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 800; color: #111; margin: 0 0 5px 0; }
                .gen-subtitle { font-size: 0.9rem; font-weight: 700; color: #666; text-transform: uppercase; letter-spacing: 2px; }
                .gen-vs-grid { display: grid; grid-template-columns: 1fr 40px 1fr; align-items: center; margin-bottom: 30px; text-align: center; }
                .gen-p-name { font-size: 1.8rem; font-weight: 900; color: #111; }
                .gen-p-rank { font-size: 1rem; font-weight: 700; color: #888; text-transform: uppercase; }
                .gen-vs-text { font-size: 1.2rem; font-weight: 900; color: #111; font-style: italic; }
                .gen-stats-table { width: 100%; border-collapse: collapse; margin-bottom: 30px; }
                .gen-stats-table td { padding: 12px 10px; border-bottom: 1px solid #f0f0f0; font-size: 1.2rem; font-weight: 800; color: #111; }
                .gen-stats-table td.label { text-align: center; font-size: 0.9rem; color: #666; text-transform: uppercase; letter-spacing: 1px; width: 33%; font-weight: 700; }
                .gen-stats-table td.v1 { text-align: right; width: 33%; color: #e63946; }
                .gen-stats-table td.v2 { text-align: left; width: 33%; color: #457b9d; }
                .gen-footer { text-align: center; margin-top: 30px; padding-top: 20px; border-top: 2px solid #f0f0f0; }
                .gen-edge { font-size: 1.4rem; font-weight: 900; color: #111; margin-bottom: 10px; }
                .gen-brand { font-size: 0.8rem; font-weight: 700; color: #888; text-transform: uppercase; letter-spacing: 1px; }
                
                @keyframes fadeInUp { to { opacity: 1; transform: translateY(0); } }
            `;
            document.head.appendChild(style);
        }

        const container = document.getElementById('compare-content');
        const p1Select = document.getElementById('compare-p1');
        const p2Select = document.getElementById('compare-p2');

        const sortedPlayers = [...this.stats.players].sort((a, b) => a.name.localeCompare(b.name));
        
        if (!p1Select.options.length) {
            sortedPlayers.forEach(p => {
                p1Select.add(new Option(p.name, p.name));
                p2Select.add(new Option(p.name, p.name));
            });
            if (sortedPlayers.length >= 2) {
                p2Select.selectedIndex = 1;
            }
        }

        const p1Name = p1Select.value;
        const p2Name = p2Select.value;
        const p1 = this.stats.players.find(p => p.name === p1Name);
        const p2 = this.stats.players.find(p => p.name === p2Name);

        if (!p1 || !p2) return;

        // Animate VS badge
        const badge = document.getElementById('vs-badge-anim');
        if (badge) {
            badge.classList.remove('pulse');
            void badge.offsetWidth;
            badge.classList.add('pulse');
        }

        // Metrics Extraction
        const getMetrics = (p) => {
            const r = p.runs || 0;
            const w = p.w || 0;
            const winRate = r > 0 ? ((w / r) * 100).toFixed(1) : 0;
            const pods = p.podiums || 0;
            const podRate = r > 0 ? ((pods / r) * 100).toFixed(1) : 0;
            const top5 = p.top5 || 0;
            const top5Rate = r > 0 ? ((top5 / r) * 100).toFixed(1) : 0;
            const avgFin = (p.avgFinish === '—' || p.avgFinish === undefined || isNaN(p.avgFinish)) ? '—' : parseFloat(p.avgFinish).toFixed(2);
            const consis = (p.consistencyScore === '—' || p.consistencyScore === undefined || isNaN(p.consistencyScore)) ? '—' : parseFloat(p.consistencyScore).toFixed(2);
            return { r, w, winRate: parseFloat(winRate), pods, podRate: parseFloat(podRate), top5, top5Rate: parseFloat(top5Rate), avgFin, consis };
        };

        const m1 = getMetrics(p1);
        const m2 = getMetrics(p2);

        // Helper for Winner Classes
        const getWinnerClass = (val1, val2, reverse = false) => {
            if (val1 === '—' || val2 === '—') return { p1: '', p2: '' };
            const v1 = parseFloat(val1);
            const v2 = parseFloat(val2);
            if (v1 === v2) return { p1: '', p2: '' };
            if (reverse) return v1 < v2 ? { p1: 'winner p1', p2: '' } : { p1: '', p2: 'winner p2' };
            return v1 > v2 ? { p1: 'winner p1', p2: '' } : { p1: '', p2: 'winner p2' };
        };

        const wWins = getWinnerClass(m1.w, m2.w);
        const wWinRate = getWinnerClass(m1.winRate, m2.winRate);
        const wPods = getWinnerClass(m1.pods, m2.pods);
        const wPodRate = getWinnerClass(m1.podRate, m2.podRate);
        const wTop5 = getWinnerClass(m1.top5, m2.top5);
        const wTop5Rate = getWinnerClass(m1.top5Rate, m2.top5Rate);
        const wAvgFin = getWinnerClass(m1.avgFin, m2.avgFin, true);
        const wConsis = getWinnerClass(m1.consis, m2.consis, true);

        // Animation Helper
        window.animateCompareNum = (elId, val, isFloat) => {
            setTimeout(() => {
                const el = document.getElementById(elId);
                if (!el || val === '—') return;
                const end = parseFloat(val);
                let start = 0;
                const duration = 800;
                const startTime = performance.now();
                const step = (now) => {
                    const prog = Math.min((now - startTime) / duration, 1);
                    const ease = 1 - Math.pow(1 - prog, 3); // easeOutCubic
                    const current = (end * ease);
                    el.innerText = isFloat ? current.toFixed(isFloat === 2 ? 2 : 1) : Math.floor(current);
                    if (prog < 1) requestAnimationFrame(step);
                    else el.innerText = isFloat ? end.toFixed(isFloat === 2 ? 2 : 1) : end;
                };
                requestAnimationFrame(step);
            }, 50);
        };
        
        const getBestUma = (p) => {
            let best = { name: '—', runs: 0, wins: 0, pods: 0, umaId: null };
            if (!p.umaStats) return best;
            for (const [umaId, stats] of Object.entries(p.umaStats)) {
                if (stats.wins > best.wins || (stats.wins === best.wins && stats.podiums > best.pods) || (stats.wins === best.wins && stats.podiums === best.pods && stats.runs > best.runs)) {
                    best = { name: stats.name, runs: stats.runs, wins: stats.wins, pods: stats.podiums, umaId: umaId };
                }
            }
            return best;
        };
        
        const bestUma1 = getBestUma(p1);
        const bestUma2 = getBestUma(p2);
        const bu1_wr = bestUma1.runs > 0 ? ((bestUma1.wins / bestUma1.runs) * 100).toFixed(1) : 0;
        const bu1_pr = bestUma1.runs > 0 ? ((bestUma1.pods / bestUma1.runs) * 100).toFixed(1) : 0;
        const bu2_wr = bestUma2.runs > 0 ? ((bestUma2.wins / bestUma2.runs) * 100).toFixed(1) : 0;
        const bu2_pr = bestUma2.runs > 0 ? ((bestUma2.pods / bestUma2.runs) * 100).toFixed(1) : 0;

        const generateAvatarHTML = (p, bestUma) => {
            if (bestUma && bestUma.umaId) {
                let imgUmaId = window.getUmaId(bestUma.name) || bestUma.umaId;
                if (UMA_DATABASE[bestUma.umaId]) {
                    if (UMA_DATABASE[bestUma.umaId].image) return `<img src="${UMA_DATABASE[bestUma.umaId].image}" onerror="this.style.display='none'; this.parentElement.innerText='${p.name.substring(0,2).toUpperCase()}';" alt="${bestUma.name}">`;
                }
                return `<img src="https://gametora.com/images/umamusume/characters/chara_stand_${imgUmaId}_1060.png" onerror="this.style.display='none'; this.parentElement.innerText='${p.name.substring(0,2).toUpperCase()}';" alt="${bestUma.name}">`;
            }
            return p.name.substring(0, 2).toUpperCase();
        };

        const renderBar = (title, val1, val2, rev = false) => {
            const v1 = parseFloat(val1) || 0;
            const v2 = parseFloat(val2) || 0;
            const total = rev ? (1/v1 + 1/v2) : (v1 + v2);
            let pct1 = 50, pct2 = 50;
            if (total > 0 && total !== Infinity) {
                pct1 = rev ? ((1/v1) / total * 100) : (v1 / total * 100);
                pct2 = rev ? ((1/v2) / total * 100) : (v2 / total * 100);
            }
            if (rev && (val1 === '—' || val2 === '—' || isNaN(v1) || isNaN(v2))) { pct1 = 50; pct2 = 50; }
            return `
                <div class="cp-bar-container">
                    <div class="cp-bar-header">
                        <div class="cp-bar-title">${title}</div>
                        <div class="cp-bar-vals"><span class="v1">${val1}</span><span class="v2">${val2}</span></div>
                    </div>
                    <div class="cp-bar-track">
                        <div class="cp-bar-fill-1" style="width: 0%" onload="this.style.width='${pct1}%'" data-width="${pct1}%"></div>
                        <div class="cp-bar-fill-2" style="width: 0%" onload="this.style.width='${pct2}%'" data-width="${pct2}%"></div>
                    </div>
                </div>
            `;
        };
        
        const renderBreakdownRow = (label, p1Data, p2Data, r1, r2) => {
            const pct1 = r1 > 0 ? ((p1Data/r1)*100).toFixed(1) : 0;
            const pct2 = r2 > 0 ? ((p2Data/r2)*100).toFixed(1) : 0;
            return `
                <div class="cp-breakdown-row">
                    <div class="cp-breakdown-label">${label}</div>
                    <div class="cp-breakdown-bars">
                        <div class="cp-bd-bar-wrap">
                            <div class="cp-bd-stats"><span>${p1.name.substring(0,5)}</span> ${p1Data}/${r1} &bull; ${pct1}%</div>
                            <div class="cp-bd-bar-track"><div class="cp-bd-bar-fill p1" style="width:0%" data-width="${pct1}%"></div></div>
                        </div>
                        <div class="cp-bd-bar-wrap">
                            <div class="cp-bd-stats"><span>${p2.name.substring(0,5)}</span> ${p2Data}/${r2} &bull; ${pct2}%</div>
                            <div class="cp-bd-bar-track"><div class="cp-bd-bar-fill p2" style="width:0%" data-width="${pct2}%"></div></div>
                        </div>
                    </div>
                </div>
            `;
        };

        container.innerHTML = `
            <div class="compare-cards-grid">
                <!-- Player 1 Card -->
                <div class="cp-card p1">
                    <div class="cp-header">
                        <div class="cp-avatar-wrap">${generateAvatarHTML(p1, bestUma1)}</div>
                        <h3 class="cp-name">${p1.name}</h3>
                        <div class="cp-rank">Rank #${p1.rank || '—'}</div>
                    </div>
                    <div class="cp-stats-grid">
                        <div class="cp-stat-box full-width">
                            <div class="cp-stat-label">Total Races</div>
                            <div class="cp-stat-value"><span id="anim-r1">${m1.r}</span></div>
                        </div>
                        <div class="cp-stat-box ${wWins.p1}">
                            <div class="cp-stat-label">Wins</div>
                            <div class="cp-stat-value"><span id="anim-w1">${m1.w}</span></div>
                        </div>
                        <div class="cp-stat-box ${wWinRate.p1}">
                            <div class="cp-stat-label">Win Rate</div>
                            <div class="cp-stat-value"><span id="anim-wr1">${m1.winRate}</span><span>%</span></div>
                        </div>
                        <div class="cp-stat-box ${wPods.p1}">
                            <div class="cp-stat-label">Podiums</div>
                            <div class="cp-stat-value"><span id="anim-p1">${m1.pods}</span></div>
                        </div>
                        <div class="cp-stat-box ${wPodRate.p1}">
                            <div class="cp-stat-label">Podium Rate</div>
                            <div class="cp-stat-value"><span id="anim-pr1">${m1.podRate}</span><span>%</span></div>
                        </div>
                        <div class="cp-stat-box ${wTop5.p1}">
                            <div class="cp-stat-label">Top 5</div>
                            <div class="cp-stat-value"><span id="anim-t51">${m1.top5}</span></div>
                        </div>
                        <div class="cp-stat-box ${wTop5Rate.p1}">
                            <div class="cp-stat-label">Top 5 Rate</div>
                            <div class="cp-stat-value"><span id="anim-t5r1">${m1.top5Rate}</span><span>%</span></div>
                        </div>
                        <div class="cp-stat-box ${wAvgFin.p1}">
                            <div class="cp-stat-label">Avg Finish</div>
                            <div class="cp-stat-value"><span id="anim-af1">${m1.avgFin}</span></div>
                        </div>
                        <div class="cp-stat-box ${wConsis.p1}">
                            <div class="cp-stat-label">Consistency</div>
                            <div class="cp-stat-value"><span id="anim-c1">${m1.consis}</span></div>
                        </div>
                    </div>
                    <div class="cp-best-uma">
                        <div class="cp-best-uma-label">Best Uma</div>
                        <div class="cp-best-uma-name">${bestUma1.name}</div>
                        <div class="cp-best-uma-stats">${bestUma1.runs} Races &bull; ${bestUma1.wins} Wins &bull; ${bestUma1.pods} Podiums<br>${bu1_wr}% Win Rate &bull; ${bu1_pr}% Podium Rate</div>
                    </div>
                </div>
                
                <!-- Player 2 Card -->
                <div class="cp-card p2">
                    <div class="cp-header">
                        <div class="cp-avatar-wrap">${generateAvatarHTML(p2, bestUma2)}</div>
                        <h3 class="cp-name">${p2.name}</h3>
                        <div class="cp-rank">Rank #${p2.rank || '—'}</div>
                    </div>
                    <div class="cp-stats-grid">
                        <div class="cp-stat-box full-width">
                            <div class="cp-stat-label">Total Races</div>
                            <div class="cp-stat-value"><span id="anim-r2">${m2.r}</span></div>
                        </div>
                        <div class="cp-stat-box ${wWins.p2}">
                            <div class="cp-stat-label">Wins</div>
                            <div class="cp-stat-value"><span id="anim-w2">${m2.w}</span></div>
                        </div>
                        <div class="cp-stat-box ${wWinRate.p2}">
                            <div class="cp-stat-label">Win Rate</div>
                            <div class="cp-stat-value"><span id="anim-wr2">${m2.winRate}</span><span>%</span></div>
                        </div>
                        <div class="cp-stat-box ${wPods.p2}">
                            <div class="cp-stat-label">Podiums</div>
                            <div class="cp-stat-value"><span id="anim-p2">${m2.pods}</span></div>
                        </div>
                        <div class="cp-stat-box ${wPodRate.p2}">
                            <div class="cp-stat-label">Podium Rate</div>
                            <div class="cp-stat-value"><span id="anim-pr2">${m2.podRate}</span><span>%</span></div>
                        </div>
                        <div class="cp-stat-box ${wTop5.p2}">
                            <div class="cp-stat-label">Top 5</div>
                            <div class="cp-stat-value"><span id="anim-t52">${m2.top5}</span></div>
                        </div>
                        <div class="cp-stat-box ${wTop5Rate.p2}">
                            <div class="cp-stat-label">Top 5 Rate</div>
                            <div class="cp-stat-value"><span id="anim-t5r2">${m2.top5Rate}</span><span>%</span></div>
                        </div>
                        <div class="cp-stat-box ${wAvgFin.p2}">
                            <div class="cp-stat-label">Avg Finish</div>
                            <div class="cp-stat-value"><span id="anim-af2">${m2.avgFin}</span></div>
                        </div>
                        <div class="cp-stat-box ${wConsis.p2}">
                            <div class="cp-stat-label">Consistency</div>
                            <div class="cp-stat-value"><span id="anim-c2">${m2.consis}</span></div>
                        </div>
                    </div>
                    <div class="cp-best-uma">
                        <div class="cp-best-uma-label">Best Uma</div>
                        <div class="cp-best-uma-name">${bestUma2.name}</div>
                        <div class="cp-best-uma-stats">${bestUma2.runs} Races &bull; ${bestUma2.wins} Wins &bull; ${bestUma2.pods} Podiums<br>${bu2_wr}% Win Rate &bull; ${bu2_pr}% Podium Rate</div>
                    </div>
                </div>
            </div>

            <!-- Head to Head Bars -->
            <div class="card cp-summary-card">
                <h3 class="cp-section-title">Head-to-Head Balance</h3>
                ${renderBar('Wins', m1.w, m2.w)}
                ${renderBar('Win Rate %', m1.winRate, m2.winRate)}
                ${renderBar('Podiums', m1.pods, m2.pods)}
                ${renderBar('Podium Rate %', m1.podRate, m2.podRate)}
                ${renderBar('Top 5 Count', m1.top5, m2.top5)}
                ${renderBar('Top 5 Rate %', m1.top5Rate, m2.top5Rate)}
                ${renderBar('Average Finish', m1.avgFin, m2.avgFin, true)}
                ${renderBar('Consistency', m1.consis, m2.consis, true)}
            </div>
            
            <!-- Top 1-5 Breakdown -->
            <div class="card cp-summary-card" style="animation-delay: 0.3s">
                <h3 class="cp-section-title">Finishing Position Breakdown</h3>
                ${renderBreakdownRow('TOP 1', p1.w, p2.w, m1.r, m2.r)}
                ${renderBreakdownRow('TOP 2', (p1.w||0)+(p1.secondPlaces||0), (p2.w||0)+(p2.secondPlaces||0), m1.r, m2.r)}
                ${renderBreakdownRow('TOP 3', p1.podiums, p2.podiums, m1.r, m2.r)}
                ${renderBreakdownRow('TOP 4', p1.top4||0, p2.top4||0, m1.r, m2.r)}
                ${renderBreakdownRow('TOP 5', p1.top5, p2.top5, m1.r, m2.r)}
            </div>

            <div class="compare-cards-grid" style="margin-bottom:0">
                <div class="card cp-summary-card" style="margin-bottom:25px; animation-delay:0.4s">
                    <h3 class="cp-section-title">Performance Radar</h3>
                    <div style="position: relative; height: 350px; width: 100%; display: flex; justify-content: center;">
                        <canvas id="cpRadarChart"></canvas>
                    </div>
                </div>
                
                <div class="card cp-summary-card" id="cp-insights-container" style="margin-bottom:25px; animation-delay:0.5s">
                    <!-- Insights will be injected here -->
                </div>
            </div>
            
            <!-- Full Standings Table -->
            <div class="card cp-summary-card" style="animation-delay: 0.6s">
                <h3 class="cp-section-title">Full Player Standings</h3>
                <div class="cp-standings-wrap">
                    <table class="cp-standings-table">
                        <thead>
                            <tr>
                                <th>Rank</th>
                                <th>Player</th>
                                <th>Races</th>
                                <th>Wins</th>
                                <th>Top 2</th>
                                <th>Top 3</th>
                                <th>Top 4</th>
                                <th>Top 5</th>
                                <th>Win %</th>
                                <th>Pod %</th>
                                <th>Top 5 %</th>
                                <th>Avg Fin</th>
                                <th>Consis</th>
                            </tr>
                        </thead>
                        <tbody id="cp-standings-body">
                        </tbody>
                    </table>
                </div>
            </div>
            
            <div class="cp-gen-btn-wrap">
                <button class="cp-gen-btn" onclick="window.generateCompareCard()">
                    <svg viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
                    Generate Comparison Card
                </button>
            </div>
            
            <!-- Hidden Canvas Overlay for Generation -->
            <div id="cp-gen-card">
                <div class="gen-header">
                    <h2 class="gen-title">SUS CUP RACE TRACKER</h2>
                    <div class="gen-subtitle">Player Comparison</div>
                </div>
                <div class="gen-vs-grid">
                    <div>
                        <div class="gen-p-name" style="color:var(--cp-1)">${p1.name}</div>
                        <div class="gen-p-rank">RANK #${p1.rank||'—'}</div>
                    </div>
                    <div class="gen-vs-text">VS</div>
                    <div>
                        <div class="gen-p-name" style="color:var(--cp-2)">${p2.name}</div>
                        <div class="gen-p-rank">RANK #${p2.rank||'—'}</div>
                    </div>
                </div>
                <table class="gen-stats-table">
                    <tr><td class="v1">${m1.r}</td><td class="label">Races</td><td class="v2">${m2.r}</td></tr>
                    <tr><td class="v1">${m1.w}</td><td class="label">Wins</td><td class="v2">${m2.w}</td></tr>
                    <tr><td class="v1">${m1.winRate}%</td><td class="label">Win Rate</td><td class="v2">${m2.winRate}%</td></tr>
                    <tr><td class="v1">${m1.pods}</td><td class="label">Podiums</td><td class="v2">${m2.pods}</td></tr>
                    <tr><td class="v1">${m1.podRate}%</td><td class="label">Podium Rate</td><td class="v2">${m2.podRate}%</td></tr>
                    <tr><td class="v1">${m1.top5}</td><td class="label">Top 5 Count</td><td class="v2">${m2.top5}</td></tr>
                    <tr><td class="v1">${m1.avgFin}</td><td class="label">Avg Finish</td><td class="v2">${m2.avgFin}</td></tr>
                    <tr>
                        <td class="v1" style="font-size:1rem; font-weight:700">${bestUma1.name}<br>${bestUma1.runs}R &bull; ${bestUma1.wins}W &bull; ${bestUma1.pods}P</td>
                        <td class="label">Best Uma</td>
                        <td class="v2" style="font-size:1rem; font-weight:700">${bestUma2.name}<br>${bestUma2.runs}R &bull; ${bestUma2.wins}W &bull; ${bestUma2.pods}P</td>
                    </tr>
                </table>
                <div class="gen-footer">
                    <div class="gen-edge" id="gen-edge-text">OVERALL EDGE: TBD</div>
                    <div class="gen-brand">Sus Cup Tournament Archive</div>
                </div>
            </div>
        `;

        // Trigger Animations
        setTimeout(() => {
            window.animateCompareNum('anim-r1', m1.r, false); window.animateCompareNum('anim-w1', m1.w, false);
            window.animateCompareNum('anim-wr1', m1.winRate, 1); window.animateCompareNum('anim-p1', m1.pods, false);
            window.animateCompareNum('anim-pr1', m1.podRate, 1); window.animateCompareNum('anim-t51', m1.top5, false);
            window.animateCompareNum('anim-t5r1', m1.top5Rate, 1); window.animateCompareNum('anim-af1', m1.avgFin, 2);
            window.animateCompareNum('anim-c1', m1.consis, 2);
            
            window.animateCompareNum('anim-r2', m2.r, false); window.animateCompareNum('anim-w2', m2.w, false);
            window.animateCompareNum('anim-wr2', m2.winRate, 1); window.animateCompareNum('anim-p2', m2.pods, false);
            window.animateCompareNum('anim-pr2', m2.podRate, 1); window.animateCompareNum('anim-t52', m2.top5, false);
            window.animateCompareNum('anim-t5r2', m2.top5Rate, 1); window.animateCompareNum('anim-af2', m2.avgFin, 2);
            window.animateCompareNum('anim-c2', m2.consis, 2);
            
            document.querySelectorAll('.cp-bar-fill-1, .cp-bar-fill-2, .cp-bd-bar-fill').forEach(el => {
                el.style.width = el.getAttribute('data-width');
            });
        }, 100);
        
        // Render Standings Table
        const standingsTbody = document.getElementById('cp-standings-body');
        let standingsHTML = '';
        this.stats.players.forEach(p => {
            let trClass = '';
            if (p.name === p1.name) trClass = 'highlight-p1';
            else if (p.name === p2.name) trClass = 'highlight-p2';
            
            const r = p.runs||0;
            const t2 = (p.w||0) + (p.secondPlaces||0);
            const wr = r > 0 ? ((p.w||0)/r*100).toFixed(1)+'%' : '0%';
            const pr = r > 0 ? ((p.podiums||0)/r*100).toFixed(1)+'%' : '0%';
            const t5r = r > 0 ? ((p.top5||0)/r*100).toFixed(1)+'%' : '0%';
            const af = (p.avgFinish === '—' || p.avgFinish === undefined || isNaN(p.avgFinish)) ? '—' : parseFloat(p.avgFinish).toFixed(2);
            const c = (p.consistencyScore === '—' || p.consistencyScore === undefined || isNaN(p.consistencyScore)) ? '—' : parseFloat(p.consistencyScore).toFixed(2);
            
            let rankStr = p.rank;
            if (p.rank === 1) rankStr = '🥇 1';
            if (p.rank === 2) rankStr = '🥈 2';
            if (p.rank === 3) rankStr = '🥉 3';
            
            standingsHTML += `<tr class="${trClass}">
                <td>${rankStr}</td>
                <td style="font-weight:800">${p.name}</td>
                <td>${r}</td>
                <td>${p.w||0}</td>
                <td>${t2}</td>
                <td>${p.podiums||0}</td>
                <td>${p.top4||0}</td>
                <td>${p.top5||0}</td>
                <td>${wr}</td>
                <td>${pr}</td>
                <td>${t5r}</td>
                <td>${af}</td>
                <td>${c}</td>
            </tr>`;
        });
        standingsTbody.innerHTML = standingsHTML;

        // Insights Generation
        let p1Adv = [];
        let p2Adv = [];
        if (m1.winRate > m2.winRate) p1Adv.push("Higher Win Rate"); else if (m2.winRate > m1.winRate) p2Adv.push("Higher Win Rate");
        if (m1.pods > m2.pods) p1Adv.push("More Podiums"); else if (m2.pods > m1.pods) p2Adv.push("More Podiums");
        if (m1.top5Rate > m2.top5Rate) p1Adv.push("Higher Top 5 Rate"); else if (m2.top5Rate > m1.top5Rate) p2Adv.push("Higher Top 5 Rate");
        if (m1.avgFin !== '—' && m2.avgFin !== '—') {
            if (m1.avgFin < m2.avgFin) p1Adv.push("Better Average Finish"); else if (m2.avgFin < m1.avgFin) p2Adv.push("Better Average Finish");
        }
        if (m1.consis !== '—' && m2.consis !== '—') {
            if (m1.consis < m2.consis) p1Adv.push("More Consistent Results"); else if (m2.consis < m1.consis) p2Adv.push("More Consistent Results");
        }
        
        let p1Score = p1Adv.length;
        let p2Score = p2Adv.length;
        let edgeText = "TIE";
        let edgeDesc = "Both players are evenly matched in core metrics.";
        if (p1Score > p2Score) { edgeText = p1.name.toUpperCase(); edgeDesc = `Leads in ${p1Score} of ${p1Score+p2Score} major metrics`; }
        else if (p2Score > p1Score) { edgeText = p2.name.toUpperCase(); edgeDesc = `Leads in ${p2Score} of ${p1Score+p2Score} major metrics`; }
        
        document.getElementById('cp-insights-container').innerHTML = `
            <h3 class="cp-section-title">Player Advantages</h3>
            <div class="cp-insights-grid">
                <div class="cp-insight-box p1">
                    <div class="cp-insight-name">${p1.name}</div>
                    <ul class="cp-insight-list">
                        ${p1Adv.length ? p1Adv.map(a => `<li>${a}</li>`).join('') : '<li style="color:#aaa">No clear metric advantages</li>'}
                    </ul>
                </div>
                <div class="cp-insight-box p2">
                    <div class="cp-insight-name">${p2.name}</div>
                    <ul class="cp-insight-list">
                        ${p2Adv.length ? p2Adv.map(a => `<li>${a}</li>`).join('') : '<li style="color:#aaa">No clear metric advantages</li>'}
                    </ul>
                </div>
            </div>
            <div class="cp-overall-edge">
                <div class="cp-edge-label">Overall Edge</div>
                <div class="cp-edge-winner" style="color: ${p1Score > p2Score ? 'var(--cp-1)' : (p2Score > p1Score ? 'var(--cp-2)' : '#111')}">${edgeText}</div>
                <div class="cp-edge-desc">${edgeDesc}</div>
            </div>
        `;
        
        document.getElementById('gen-edge-text').innerText = `OVERALL EDGE: ${edgeText}`;

        // Generator function
        window.generateCompareCard = () => {
            const el = document.getElementById('cp-gen-card');
            if (typeof html2canvas !== 'undefined') {
                html2canvas(el, { scale: 2, backgroundColor: '#ffffff', useCORS: true }).then(canvas => {
                    const link = document.createElement('a');
                    link.download = `SusCup_Compare_${p1.name}_vs_${p2.name}.png`;
                    link.href = canvas.toDataURL('image/png');
                    link.click();
                });
            } else {
                alert("Generator library not loaded yet. Please try again in a moment.");
            }
        };

        // Render Radar
        setTimeout(() => {
            const ctx = document.getElementById('cpRadarChart');
            if (!ctx) return;
            
            // Normalize values for radar
            const maxWinRate = Math.max(...this.stats.players.map(p => (p.w||0)/(p.runs||1)*100), 1);
            const maxPodRate = Math.max(...this.stats.players.map(p => (p.podiums||0)/(p.runs||1)*100), 1);
            const maxTop5Rate = Math.max(...this.stats.players.map(p => (p.top5||0)/(p.runs||1)*100), 1);
            const minAvgFin = Math.min(...this.stats.players.filter(p => !isNaN(p.avgFinish)).map(p => parseFloat(p.avgFinish)));
            const maxAvgFin = Math.max(...this.stats.players.filter(p => !isNaN(p.avgFinish)).map(p => parseFloat(p.avgFinish)));
            const minConsis = Math.min(...this.stats.players.filter(p => !isNaN(p.consistencyScore)).map(p => parseFloat(p.consistencyScore)));
            const maxConsis = Math.max(...this.stats.players.filter(p => !isNaN(p.consistencyScore)).map(p => parseFloat(p.consistencyScore)));
            
            const norm = (val, max, min = 0, inv = false) => {
                if (val === '—' || isNaN(val)) return 0;
                let pct = (parseFloat(val) - min) / (max - min) * 100;
                if (inv) pct = 100 - pct; // lower is better
                return Math.max(0, Math.min(100, pct));
            };

            const d1 = [
                norm(m1.winRate, maxWinRate),
                norm(m1.podRate, maxPodRate),
                norm(m1.top5Rate, maxTop5Rate),
                norm(m1.avgFin, maxAvgFin, minAvgFin, true),
                norm(m1.consis, maxConsis, minConsis, true)
            ];
            
            const d2 = [
                norm(m2.winRate, maxWinRate),
                norm(m2.podRate, maxPodRate),
                norm(m2.top5Rate, maxTop5Rate),
                norm(m2.avgFin, maxAvgFin, minAvgFin, true),
                norm(m2.consis, maxConsis, minConsis, true)
            ];

            if (window.cpChart) window.cpChart.destroy();
            window.cpChart = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: ['Win Rate', 'Podium Rate', 'Top 5 Rate', 'Avg Finish (Inv)', 'Consistency (Inv)'],
                    datasets: [
                        { label: p1.name, data: d1, backgroundColor: 'rgba(230, 57, 70, 0.2)', borderColor: '#e63946', pointBackgroundColor: '#e63946', borderWidth: 2 },
                        { label: p2.name, data: d2, backgroundColor: 'rgba(69, 123, 157, 0.2)', borderColor: '#457b9d', pointBackgroundColor: '#457b9d', borderWidth: 2 }
                    ]
                },
                options: {
                    responsive: true, maintainAspectRatio: false,
                    scales: { r: { angleLines: { color: 'rgba(0,0,0,0.1)' }, grid: { color: 'rgba(0,0,0,0.1)' }, pointLabels: { font: { family: "'Inter', sans-serif", size: 11, weight: 'bold' }, color: '#666' }, ticks: { display: false, min: 0, max: 100 } } },
                    plugins: { legend: { position: 'top', labels: { font: { family: "'Inter', sans-serif", weight: 'bold' } } }, tooltip: { callbacks: { label: function(context) { return context.dataset.label + ': ' + Math.round(context.raw) + ' / 100'; } } } }
                }
            });
        }, 100);
    }"""

start_str = "            renderCompare() {"
end_str = "            renderProfileView() {"

start_idx = html.find(start_str)
end_idx = html.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + new_render_compare + "\n\n" + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully replaced renderCompare.")
else:
    print("Could not find start or end markers.", start_idx, end_idx)
