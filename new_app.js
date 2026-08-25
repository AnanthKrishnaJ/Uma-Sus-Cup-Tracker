const App = {
    data: null, stats: null, runnerCount: 0,
    stylesMap: {
        'Front': 'Front Runner',
        'Pace': 'Pace Chaser',
        'Late': 'Late Surger',
        'End': 'End Closer'
    },

    init() {
        localStorage.removeItem('sus_cup_db');
        this.loadData(); 
        this.setupNavigation();
        this.setupForm();
        this.navigate('dashboard');
    },

    loadData() {
        const local = localStorage.getItem('sus_cup_db');
        if (local) this.data = JSON.parse(local);
        else { this.data = JSON.parse(JSON.stringify(INITIAL_DATA)); this.saveData(); }
        this.migrateHistoricalRecord();
        this.calculateStats();
    },

    migrateHistoricalRecord() {
        this.data.races.forEach(race => {
            if (race.participants) {
                race.participants = race.participants.map(p => {
                    const umaId = p.umaId || Object.keys(UMA_DATABASE).find(k => UMA_DATABASE[k].name === p.uma) || "unknown";
                    return {
                        ...p, umaId: umaId, version: UMA_DATABASE[umaId] ? UMA_DATABASE[umaId].version : p.version
                    };
                });
            }
        });

        const sourceRace = INITIAL_DATA.races[0];
        let race = this.data.races.find(item => item.id === sourceRace.id);
        if (!race) {
            race = JSON.parse(JSON.stringify(sourceRace));
            this.data.races.unshift(race);
        } else {
            Object.assign(race, {
                cupNumber: sourceRace.cupNumber, cupName: sourceRace.cupName, name: sourceRace.name, date: sourceRace.date, images: [...sourceRace.images], time: sourceRace.time, roomId: sourceRace.roomId, course: sourceRace.course, surface: sourceRace.surface, distance: sourceRace.distance, distanceType: sourceRace.distanceType, direction: sourceRace.direction, weather: sourceRace.weather, ground: sourceRace.ground, condition: sourceRace.condition, mood: sourceRace.mood, season: sourceRace.season, restriction: sourceRace.restriction
            });
        }

        INITIAL_DATA.races.slice(1).forEach(sourceRace => {
            const existingRace = this.data.races.find(item => item.id === sourceRace.id);
            if (!existingRace) this.data.races.push(JSON.parse(JSON.stringify(sourceRace)));
            else if (sourceRace.id >= 3) Object.assign(existingRace, JSON.parse(JSON.stringify(sourceRace)));
            else if (sourceRace.images) existingRace.images = [...sourceRace.images];
        });

        this.data.races.forEach(race => {
            if (race.participants) {
                race.participants = race.participants.map(p => {
                    const umaId = p.umaId || Object.keys(UMA_DATABASE).find(k => UMA_DATABASE[k].name === p.uma) || "unknown";
                    return { ...p, umaId: umaId, version: UMA_DATABASE[umaId] ? UMA_DATABASE[umaId].version : p.version };
                });
            }
        });

        const seededCups = new Set(INITIAL_DATA.winners.map(winner => winner.cup));
        const customWinners = (this.data.winners || []).filter(winner => !seededCups.has(winner.cup));
        this.data.winners = [...INITIAL_DATA.winners.map(winner => JSON.parse(JSON.stringify(winner))), ...customWinners];
        this.data.championships = this.data.winners.reduce((championships, winner) => {
            const uma = UMA_DATABASE[winner.umaId];
            if (uma && uma.type !== 'NPC' && winner.type !== 'NPC Uma') {
                championships[winner.umaId] = (championships[winner.umaId] || 0) + 1;
            }
            return championships;
        }, {});
        this.data.winners = this.data.winners.map(winner => {
            const umaId = winner.umaId || Object.keys(UMA_DATABASE).find(k => UMA_DATABASE[k].name === winner.uma) || "unknown";
            return {
                ...winner, umaId: umaId, race: winner.race || (this.data.races.find(r => r.cupName === winner.cup)?.name || ""), result: winner.result || (this.data.races.find(r => r.cupName === winner.cup)?.participants.find(p => p.pos === 1)?.gap || "")
            };
        });
        localStorage.setItem('sus_cup_db', JSON.stringify(this.data));
    },

    saveData() {
        localStorage.setItem('sus_cup_db', JSON.stringify(this.data));
        this.calculateStats();
    },

    resetData() {
        if (confirm("Reset all data back to the demo SUS CUP 1 database?")) {
            localStorage.removeItem('sus_cup_db');
            this.loadData(); this.navigate('dashboard');
        }
    },

    exportData() {
        const str = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(this.data));
        const a = document.createElement('a');
        a.href = str; a.download = "sus_cup_backup.json"; a.click();
    },

    importData(e) {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (ev) => {
            try {
                const parsed = JSON.parse(ev.target.result);
                if (parsed.races) { this.data = parsed; this.saveData(); this.navigate('dashboard'); }
            } catch (err) { alert("Invalid JSON file."); }
            e.target.value = '';
        };
        reader.readAsText(file);
    },

    parseTime(tStr) {
        if (!tStr) return 9999;
        if (typeof tStr !== 'string') return 9999;
        const m = tStr.match(/(\d+):(\d+)\.(\d+)/);
        if (m) return parseInt(m[1]) * 60 + parseInt(m[2]) + parseInt(m[3]) / 10;
        return 9999;
    },

    formatTime(sec) {
        if (sec >= 9999) return '-';
        const m = Math.floor(sec / 60);
        const s = Math.floor(sec % 60);
        const ms = Math.round((sec - Math.floor(sec)) * 10);
        return `${m}:${s.toString().padStart(2, '0')}.${ms}`;
    },

    getPoints(pos) {
        const pts = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1];
        return (pos >= 1 && pos <= 10) ? pts[pos - 1] : 0;
    },

    calculateStats() {
        const players = {}; const umas = {};
        const globalStyles = { 'Front Runner': { runs:0, w:0, pod:0, sumPos:0 }, 'Pace Chaser': { runs:0, w:0, pod:0, sumPos:0 }, 'Late Surger': { runs:0, w:0, pod:0, sumPos:0 }, 'End Closer': { runs:0, w:0, pod:0, sumPos:0 } };
        let totalCourses = new Set();
        
        let allRecords = {
            fastestTime: 9999, fastestUma: '', fastestPlayer: '', fastestCourse: '',
            mostWins: 0, mostWinsPlayer: '',
            mostPodiums: 0, mostPodiumsPlayer: '',
            bestAvg: 99, bestAvgPlayer: '',
            biggestMargin: -1, biggestMarginRace: '',
            closestFinish: 999, closestFinishRace: ''
        };

        this.data.races.forEach(race => {
            if (race.course) totalCourses.add(race.course);
            
            // Record margins
            const p1 = race.participants.find(p => p.pos === 1);
            const p2 = race.participants.find(p => p.pos === 2);
            if (p1 && p2 && p1.time && p2.time) {
                const margin = this.parseTime(p2.time) - this.parseTime(p1.time);
                if (margin > allRecords.biggestMargin && margin < 9000) { allRecords.biggestMargin = margin; allRecords.biggestMarginRace = race.name; }
                if (margin < allRecords.closestFinish && margin >= 0) { allRecords.closestFinish = margin; allRecords.closestFinishRace = race.name; }
            }

            race.participants.forEach(p => {
                if (!players[p.player]) {
                    players[p.player] = {
                        name: p.player, runs: 0, w: 0, secondPlaces: 0, thirdPlaces: 0, podiums: 0, sumPos: 0, 
                        bestFinish: 99, worstFinish: 0, bestTime: 9999, totalTime: 0, timeCount: 0, points: 0,
                        styles: { 'Front Runner': { runs:0, w:0, pod:0, sumPos:0, bestTime:9999 }, 'Pace Chaser': { runs:0, w:0, pod:0, sumPos:0, bestTime:9999 }, 'Late Surger': { runs:0, w:0, pod:0, sumPos:0, bestTime:9999 }, 'End Closer': { runs:0, w:0, pod:0, sumPos:0, bestTime:9999 } },
                        tracks: {}, styleEvolution: [], history: []
                    };
                }
                const pl = players[p.player];
                pl.runs++; pl.sumPos += p.pos;
                pl.points += this.getPoints(p.pos);
                if (p.pos === 1) pl.w++;
                if (p.pos === 2) pl.secondPlaces++;
                if (p.pos === 3) pl.thirdPlaces++;
                if (p.pos <= 3) pl.podiums++;
                if (p.pos < pl.bestFinish) pl.bestFinish = p.pos;
                if (p.pos > pl.worstFinish) pl.worstFinish = p.pos;

                const pTime = this.parseTime(p.time);
                if (pTime < 9000) {
                    if (pTime < pl.bestTime) pl.bestTime = pTime;
                    pl.totalTime += pTime; pl.timeCount++;
                    if (pTime < allRecords.fastestTime) {
                        allRecords.fastestTime = pTime; allRecords.fastestUma = p.uma; allRecords.fastestPlayer = p.player; allRecords.fastestCourse = race.course;
                    }
                }

                const style = this.stylesMap[p.strategy] || 'Unknown';
                if (style !== 'Unknown') {
                    pl.styles[style].runs++;
                    pl.styles[style].sumPos += p.pos;
                    if (p.pos === 1) pl.styles[style].w++;
                    if (p.pos <= 3) pl.styles[style].pod++;
                    if (pTime < 9000 && pTime < pl.styles[style].bestTime) pl.styles[style].bestTime = pTime;
                    
                    globalStyles[style].runs++; globalStyles[style].sumPos += p.pos;
                    if (p.pos === 1) globalStyles[style].w++;
                    if (p.pos <= 3) globalStyles[style].pod++;
                }
                
                pl.styleEvolution.push({ cup: race.cupNumber, style: style });
                
                if (race.course) {
                    if (!pl.tracks[race.course]) pl.tracks[race.course] = { runs:0, w:0, pod:0, sumPos:0, bestTime:9999 };
                    pl.tracks[race.course].runs++;
                    pl.tracks[race.course].sumPos += p.pos;
                    if (p.pos === 1) pl.tracks[race.course].w++;
                    if (p.pos <= 3) pl.tracks[race.course].pod++;
                    if (pTime < 9000 && pTime < pl.tracks[race.course].bestTime) pl.tracks[race.course].bestTime = pTime;
                }

                pl.history.push({ race: race.name, cup: race.cupNumber, uma: p.uma, pos: p.pos, time: p.time, strategy: style });

                // Uma stats
                if (!umas[p.umaId]) umas[p.umaId] = { umaId: p.umaId, name: p.uma, runs: 0, w: 0, podiums: 0, sumPos: 0, users: {} };
                const um = umas[p.umaId];
                um.runs++; um.sumPos += p.pos;
                if (p.pos === 1) um.w++;
                if (p.pos <= 3) um.podiums++;
                if (!um.users[p.player]) um.users[p.player] = 0;
                um.users[p.player]++;
            });
        });

        // Compute Player derived stats
        const sortedPlayers = Object.values(players).map(p => {
            const avgFinish = p.sumPos / p.runs;
            const avgTime = p.timeCount > 0 ? p.totalTime / p.timeCount : 9999;
            
            // Track preference
            let favTrack = { name: '-', runs: 0 };
            let bestTrack = { name: '-', avg: 99, w: 0 };
            Object.keys(p.tracks).forEach(t => {
                if (p.tracks[t].runs > favTrack.runs) { favTrack.name = t; favTrack.runs = p.tracks[t].runs; }
                const tAvg = p.tracks[t].sumPos / p.tracks[t].runs;
                if (tAvg < bestTrack.avg || (tAvg === bestTrack.avg && p.tracks[t].w > bestTrack.w)) {
                    bestTrack.name = t; bestTrack.avg = tAvg; bestTrack.w = p.tracks[t].w;
                }
            });

            // Style preference
            let favStyle = { name: '-', runs: 0 };
            let leastStyle = { name: '-', runs: 999 };
            let bestStyle = { name: '-', avg: 99, w: 0 };
            Object.keys(p.styles).forEach(s => {
                if (p.styles[s].runs > favStyle.runs) { favStyle.name = s; favStyle.runs = p.styles[s].runs; }
                if (p.styles[s].runs < leastStyle.runs) { leastStyle.name = s; leastStyle.runs = p.styles[s].runs; }
                if (p.styles[s].runs > 0) {
                    const sAvg = p.styles[s].sumPos / p.styles[s].runs;
                    if (sAvg < bestStyle.avg || (sAvg === bestStyle.avg && p.styles[s].w > bestStyle.w)) {
                        bestStyle.name = s; bestStyle.avg = sAvg; bestStyle.w = p.styles[s].w;
                    }
                }
            });

            if (p.w > allRecords.mostWins) { allRecords.mostWins = p.w; allRecords.mostWinsPlayer = p.name; }
            if (p.podiums > allRecords.mostPodiums) { allRecords.mostPodiums = p.podiums; allRecords.mostPodiumsPlayer = p.name; }
            if (p.runs >= 3 && avgFinish < allRecords.bestAvg) { allRecords.bestAvg = avgFinish; allRecords.bestAvgPlayer = p.name; }

            return {
                ...p, 
                avgFinish: avgFinish.toFixed(2), 
                avgTime: avgTime,
                winRate: ((p.w / p.runs) * 100).toFixed(1),
                podiumRate: ((p.podiums / p.runs) * 100).toFixed(1),
                favTrack: favTrack.name, bestTrack: bestTrack.name,
                favStyle: favStyle.name, leastStyle: leastStyle.name, bestStyle: bestStyle.name
            };
        }).sort((a, b) => b.points - a.points || b.w - a.w || b.podiums - a.podiums || a.sumPos - b.sumPos);

        sortedPlayers.forEach((p, idx) => p.rank = idx + 1);

        const sortedUmas = Object.values(umas).map(u => ({
            ...u, winRate: ((u.w / u.runs) * 100).toFixed(1), avgFinish: (u.sumPos / u.runs).toFixed(2),
            bestPlayer: Object.keys(u.users).reduce((a, b) => u.users[a] > u.users[b] ? a : b)
        })).sort((a, b) => b.w - a.w || b.podiums - a.podiums || b.runs - a.runs);
        sortedUmas.forEach((u, idx) => u.rank = idx + 1);

        // Global styles
        let bestGlobalStyle = { name: '-', avg: 99 };
        let mostGlobalStyle = { name: '-', runs: 0 };
        let leastGlobalStyle = { name: '-', runs: 9999 };
        let totalStyleRuns = 0;
        Object.keys(globalStyles).forEach(s => {
            const r = globalStyles[s].runs;
            totalStyleRuns += r;
            if (r > mostGlobalStyle.runs) { mostGlobalStyle.name = s; mostGlobalStyle.runs = r; }
            if (r < leastGlobalStyle.runs) { leastGlobalStyle.name = s; leastGlobalStyle.runs = r; }
            if (r > 0) {
                const avg = globalStyles[s].sumPos / r;
                if (avg < bestGlobalStyle.avg) { bestGlobalStyle.name = s; bestGlobalStyle.avg = avg; }
            }
        });

        this.stats = {
            totalCups: new Set(this.data.races.map(r => r.cupNumber)).size,
            totalRaces: this.data.races.length,
            totalPlayers: sortedPlayers.length,
            totalUmas: sortedUmas.length,
            totalTracks: totalCourses.size,
            players: sortedPlayers,
            umas: sortedUmas,
            records: allRecords,
            styles: globalStyles,
            bestGlobalStyle, mostGlobalStyle, leastGlobalStyle, totalStyleRuns
        };
    },

    setupNavigation() {
        document.querySelectorAll('a[data-nav]').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault(); this.navigate(e.currentTarget.dataset.nav);
            });
        });
    },

    navigate(view) {
        if (view === 'compare') this.setupCompareView();
        document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
        document.querySelectorAll('a[data-nav]').forEach(v => v.classList.remove('active'));
        const targetView = document.getElementById(`view-${view}`);
        if (targetView) targetView.classList.add('active');

        const targetLink = document.querySelector(`a[data-nav="${view}"]`);
        if (targetLink) targetLink.classList.add('active');

        if (view === 'dashboard') this.renderDashboard();
        if (view === 'history') this.renderHistory();
        if (view === 'archive') this.renderArchive();
        if (view === 'info') this.renderInfo();
        if (view === 'players') this.renderPlayers();
        if (view === 'umas') this.renderUmas();
        window.scrollTo(0, 0);
    },

    getBadge(rank) {
        const r = (rank || 'C').toUpperCase();
        let cls = 'badge-c';
        if (r.includes('S')) cls = 'badge-s';
        else if (r.includes('A')) cls = 'badge-a';
        else if (r.includes('B')) cls = 'badge-b';
        return `<span class="badge ${cls}">${r}</span>`;
    },

    getUmaImage(umaId, large = false) {
        const uma = UMA_DATABASE[umaId];
        if (uma && uma.image) {
            const cls = `${large ? 'uma-image-large' : 'uma-image'}${uma.type === 'NPC' ? ' npc-face' : ''}`;
            const fallbackSrc = `data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='100' height='100'><rect width='100' height='100' fill='%23eee'/><text x='50' y='50' font-size='12' text-anchor='middle' fill='%23999'>Error</text></svg>`;
            return `<img class="${cls}" src="${uma.image}" alt="${uma.name}" loading="lazy" onerror="this.onerror=null; this.src='${fallbackSrc}'; this.style.border='2px dashed #ccc'; this.style.objectFit='contain';">`;
        }
        return `<div class="avatar-circle" title="IMAGE UNAVAILABLE" style="background:#eee; color:#999; border:2px dashed #ccc; font-size:10px; line-height:1.2; text-align:center;"><div style="font-size:16px;">X</div><div style="font-size:8px; margin-top:2px;">${uma ? uma.name : 'Unknown'}</div></div>`;
    },

    renderDashboard() {
        document.getElementById('dash-stats').innerHTML = `
            <div class="stat-block"><div class="val">${this.stats.totalCups}</div><div class="lbl">Total Cups</div></div>
            <div class="stat-block"><div class="val">${this.stats.totalRaces}</div><div class="lbl">Total Races</div></div>
            <div class="stat-block"><div class="val">${this.stats.totalPlayers}</div><div class="lbl">Total Players</div></div>
            <div class="stat-block"><div class="val">${this.stats.totalTracks}</div><div class="lbl">Total Tracks</div></div>
        `;
        
        const rec = this.stats.records;
        document.getElementById('championship-record').innerHTML = `
            <div class="record-heading"><span class="eyebrow">All-Time Historical Records</span><span class="record-count"><i class="fa-solid fa-star"></i></span></div>
            <div class="record-winner" style="display:grid; grid-template-columns:1fr 1fr; gap:15px; margin-top:15px;">
                <div style="background:#fafafa; padding:15px; border-radius:5px;">
                    <div style="font-size:0.8rem; color:#888; text-transform:uppercase;">Fastest Player/Uma</div>
                    <div style="font-size:1.2rem; font-weight:bold;">${rec.fastestPlayer} - ${rec.fastestUma}</div>
                    <div style="font-size:0.9rem; color:var(--primary);">${this.formatTime(rec.fastestTime)} on ${rec.fastestCourse}</div>
                </div>
                <div style="background:#fafafa; padding:15px; border-radius:5px;">
                    <div style="font-size:0.8rem; color:#888; text-transform:uppercase;">Most Successful Player</div>
                    <div style="font-size:1.2rem; font-weight:bold;">${rec.mostWinsPlayer}</div>
                    <div style="font-size:0.9rem; color:var(--primary);">${rec.mostWins} Wins</div>
                </div>
                <div style="background:#fafafa; padding:15px; border-radius:5px;">
                    <div style="font-size:0.8rem; color:#888; text-transform:uppercase;">Biggest Winning Margin</div>
                    <div style="font-size:1.2rem; font-weight:bold;">+${rec.biggestMargin > 0 ? rec.biggestMargin.toFixed(1) : '-'}s</div>
                    <div style="font-size:0.9rem; color:var(--primary);">${rec.biggestMarginRace}</div>
                </div>
                <div style="background:#fafafa; padding:15px; border-radius:5px;">
                    <div style="font-size:0.8rem; color:#888; text-transform:uppercase;">Closest Finish</div>
                    <div style="font-size:1.2rem; font-weight:bold;">+${rec.closestFinish < 999 ? rec.closestFinish.toFixed(1) : '-'}s</div>
                    <div style="font-size:0.9rem; color:var(--primary);">${rec.closestFinishRace}</div>
                </div>
                <div style="background:#fafafa; padding:15px; border-radius:5px;">
                    <div style="font-size:0.8rem; color:#888; text-transform:uppercase;">Most Used Style</div>
                    <div style="font-size:1.2rem; font-weight:bold;">${this.stats.mostGlobalStyle.name}</div>
                    <div style="font-size:0.9rem; color:var(--primary);">${((this.stats.mostGlobalStyle.runs / this.stats.totalStyleRuns)*100).toFixed(1)}% Usage</div>
                </div>
                <div style="background:#fafafa; padding:15px; border-radius:5px;">
                    <div style="font-size:0.8rem; color:#888; text-transform:uppercase;">Best Performing Style</div>
                    <div style="font-size:1.2rem; font-weight:bold;">${this.stats.bestGlobalStyle.name}</div>
                    <div style="font-size:0.9rem; color:var(--primary);">${this.stats.bestGlobalStyle.avg.toFixed(2)} Avg Finish</div>
                </div>
            </div>
        `;

        let phtml = '';
        this.stats.players.slice(0, 5).forEach(p => {
            phtml += `
                <div class="list-item" onclick="App.showPlayer('${p.name}')">
                    <div class="avatar-circle" style="background:#f4ece1; color:var(--text-main); font-size:1rem;">#${p.rank}</div>
                    <div class="item-content">
                        <div class="item-title">${p.name}</div>
                        <div class="item-subtitle">${p.w} Wins / ${p.points} Pts</div>
                    </div>
                    <div class="item-right">
                        <div class="item-value" style="font-size:0.9rem;">${p.favStyle}</div>
                        <div class="item-label">Fav: ${p.favTrack}</div>
                    </div>
                </div>`;
        });
        document.getElementById('dash-player-list').innerHTML = phtml;

        let uhtml = '';
        this.stats.umas.filter(u => !NPC_PROFILES[u.name]).slice(0, 5).forEach(u => {
            uhtml += `
                <div class="list-item" onclick="App.showUma('${u.name}')">
                    ${this.getUmaImage(u.umaId)}
                    <div class="item-content">
                        <div class="item-title">${u.name}</div>
                        <div class="item-subtitle">Best: ${u.bestPlayer}</div>
                    </div>
                    <div class="item-right">
                        <div class="item-value" style="color:var(--primary)">${u.w} Wins</div>
                        <div class="item-label">${u.winRate}% WR</div>
                    </div>
                </div>`;
        });
        document.getElementById('dash-uma-list').innerHTML = uhtml;
    },

    renderHistory() {
        const winners = this.data.winners || [];
        const html = [...this.data.races].sort((a, b) => new Date(a.date) - new Date(b.date)).map(race => {
            const winner = winners.find(item => item.cup === \`Sus Cup \${race.cupNumber}\`) || race.participants.find(p => p.pos === 1);
            return \`<div class="timeline-item"><div class="card" style="margin-bottom:0; cursor:pointer;" onclick="App.showRaceDetail(\${race.id})">
                <span class="badge" style="background:var(--accent-dark);">SUS CUP \${race.cupNumber}</span>
                <h3 style="font-size:1.35rem; margin:12px 0 5px;">\${race.name}</h3>
                <p style="color:var(--text-muted); font-weight:700;">\${race.date} • \${race.course} \${race.distance}m \${race.surface}</p>
                <p style="margin-top:12px; font-weight:800;">Winner: \${winner?.trainer || winner?.player || 'Not recorded'} • \${winner?.uma || 'Not recorded'}</p>
            </div></div>\`;
        }).join('');
        document.getElementById('history-timeline').innerHTML = html;
    },

    renderInfo() {
        document.getElementById('info-content').innerHTML = \`<section class="card info-section"><h3>About Sus Cup Analytics</h3><p>Upgraded with advanced analytics.</p></section>\`;
    },

    renderArchive() {
        let html = '';
        const searchTxt = (document.getElementById('filter-search')?.value || '').toLowerCase();
        let races = [...this.data.races].filter(r => (!searchTxt || r.name.toLowerCase().includes(searchTxt) || r.cupNumber.toLowerCase().includes(searchTxt)));
        races.sort((a, b) => new Date(a.date || '2099') - new Date(b.date || '2099'));
        races.forEach(race => {
            const winner = race.participants.find(p => p.pos === 1);
            html += \`
                <div class="card" style="cursor:pointer;" onclick="App.showRaceDetail(\${race.id})">
                    <span class="badge" style="background:var(--accent-dark)">SUS CUP \${race.cupNumber}</span>
                    <h3 style="font-size:1.4rem; margin-top:10px;">\${race.name}</h3>
                    <p style="color:var(--text-muted); margin-bottom:15px;">\${race.course} \${race.surface} \${race.distance}m</p>
                    <div class="list-item" style="border-left:4px solid var(--gold); padding:10px;">
                        \${this.getUmaImage(winner?.umaId || '')}
                        <div>
                            <div class="item-title">\${winner?.uma || 'Unknown'}</div>
                            <div class="item-subtitle">\${winner?.player || ''}</div>
                        </div>
                    </div>
                </div>\`;
        });
        document.getElementById('archive-grid').innerHTML = html;
    },

    showRaceDetail(id) {
        const race = this.data.races.find(r => r.id === id);
        if (!race) return;
        const sorted = [...race.participants].sort((a, b) => a.pos - b.pos);
        
        const raceMeta = [
            \`Cup Name/Number: Sus Cup \${race.cupNumber}\`,
            \`Round: \${race.name}\`,
            \`Date & Time: \${race.date} \${race.time || ''}\`,
            \`Track: \${race.course}\`,
            \`Distance: \${race.distance}m (\${race.distanceType})\`,
            \`Surface: \${race.surface}\`,
            \`Direction: \${race.direction || 'N/A'}\`,
            \`Weather: \${race.weather || 'N/A'}\`,
            \`Ground Condition: \${race.ground || 'N/A'}\`,
            \`Mood: \${race.mood || 'N/A'}\`,
            \`Room ID: \${race.roomId || 'N/A'}\`
        ];

        let html = \`
            <div class="card" style="background:var(--accent-dark); color:white;">
                <h2 style="font-size:2rem; margin-bottom:15px;">\${race.name}</h2>
                <div class="grid-2" style="gap:10px;">\${raceMeta.map(item => \`<div style="font-size:0.9rem; opacity:0.9; border-bottom:1px solid rgba(255,255,255,0.2); padding-bottom:5px;">\${item}</div>\`).join('')}</div>
            </div>
        \`;

        sorted.forEach(p => {
            let medal = p.pos;
            let style = '';
            if (p.pos === 1) { style = 'border-left: 5px solid var(--gold); background: #fffcf0;'; medal = '🥇'; }
            else if (p.pos === 2) { style = 'border-left: 5px solid var(--silver);'; medal = '🥈'; }
            else if (p.pos === 3) { style = 'border-left: 5px solid var(--bronze);'; medal = '🥉'; }
            
            html += \`
                <div class="list-item" style="\${style}">
                    <div style="font-size:1.5rem; font-weight:900; width:40px; text-align:center;">\${medal}</div>
                    \${this.getUmaImage(p.umaId)}
                    <div class="item-content">
                        <div class="item-title">\${p.uma}</div>
                        <div class="item-subtitle">Player: \${p.player} &bull; Style: \${this.stylesMap[p.strategy] || p.strategy || 'N/A'}</div>
                    </div>
                    <div class="item-right">
                        <div class="item-value" style="font-size:1.1rem; color:var(--primary);">\${p.time || '-'}</div>
                        <div class="item-label">Pos: \${p.pos}</div>
                    </div>
                </div>
            \`;
        });
        document.getElementById('race-detail-content').innerHTML = html;
        this.navigate('race-detail');
    },

    renderPlayers() {
        const query = (document.getElementById('search-players')?.value || '').toLowerCase();
        let html = '';
        this.stats.players.filter(p => p.name.toLowerCase().includes(query)).forEach(p => {
            html += \`
                <div class="list-item" onclick="App.showPlayer('\${p.name.replace(/'/g, "\\'")}')">
                    <div class="avatar-circle" style="background:white; border:2px solid #eee;">#\${p.rank}</div>
                    <div class="item-content">
                        <div class="item-title">\${p.name}</div>
                        <div class="item-subtitle">\${p.points} Pts | \${p.w} Wins</div>
                    </div>
                </div>\`;
        });
        document.getElementById('full-player-list').innerHTML = html;
    },

    showPlayer(name) {
        const p = this.stats.players.find(x => x.name === name);
        if(!p) return;
        
        let styleStatsHtml = '';
        Object.keys(p.styles).forEach(s => {
            const data = p.styles[s];
            if (data.runs > 0) {
                styleStatsHtml += \`
                <tr>
                    <td>\${s}</td>
                    <td>\${data.runs} (\${((data.runs/p.runs)*100).toFixed(0)}%)</td>
                    <td>\${data.w}</td>
                    <td>\${data.pod}</td>
                    <td>\${(data.sumPos/data.runs).toFixed(2)}</td>
                    <td>\${this.formatTime(data.bestTime)}</td>
                </tr>\`;
            }
        });

        let trackStatsHtml = '';
        Object.keys(p.tracks).forEach(t => {
            const data = p.tracks[t];
            trackStatsHtml += \`
            <tr>
                <td>\${t}</td>
                <td>\${data.runs}</td>
                <td>\${data.w}</td>
                <td>\${data.pod}</td>
                <td>\${(data.sumPos/data.runs).toFixed(2)}</td>
                <td>\${this.formatTime(data.bestTime)}</td>
            </tr>\`;
        });
        
        let evolutionHtml = '';
        p.styleEvolution.forEach(e => {
            evolutionHtml += \`<span class="badge" style="background: #eee; color:#333; margin-right:5px; margin-bottom:5px;">Cup \${e.cup}: \${e.style}</span>\`;
        });

        let html = \`
            <div class="card" style="background:var(--accent-dark); color:white; margin-bottom:20px;">
                <h2 style="font-size:2rem; margin-bottom:10px;">\${p.name}</h2>
                <div class="grid-4" style="gap:15px; margin-top:20px;">
                    <div><div style="font-size:0.8rem; opacity:0.8;">Total Points</div><div style="font-size:1.5rem; font-weight:bold;">\${p.points}</div></div>
                    <div><div style="font-size:0.8rem; opacity:0.8;">Races Entered</div><div style="font-size:1.5rem; font-weight:bold;">\${p.runs}</div></div>
                    <div><div style="font-size:0.8rem; opacity:0.8;">Wins</div><div style="font-size:1.5rem; font-weight:bold;">\${p.w} (\${p.winRate}%)</div></div>
                    <div><div style="font-size:0.8rem; opacity:0.8;">Podiums</div><div style="font-size:1.5rem; font-weight:bold;">\${p.podiums} (\${p.podiumRate}%)</div></div>
                    <div><div style="font-size:0.8rem; opacity:0.8;">2nd / 3rd</div><div style="font-size:1.5rem; font-weight:bold;">\${p.secondPlaces} / \${p.thirdPlaces}</div></div>
                    <div><div style="font-size:0.8rem; opacity:0.8;">Avg / Best / Worst Finish</div><div style="font-size:1.5rem; font-weight:bold;">\${p.avgFinish} / \${p.bestFinish} / \${p.worstFinish}</div></div>
                    <div><div style="font-size:0.8rem; opacity:0.8;">Best / Avg Race Time</div><div style="font-size:1.5rem; font-weight:bold;">\${this.formatTime(p.bestTime)} / \${this.formatTime(p.avgTime)}</div></div>
                </div>
            </div>
            
            <div class="grid-2">
                <div class="card">
                    <h3 style="margin-bottom:15px;">⭐ Track Preferences</h3>
                    <div style="margin-bottom:10px;"><strong>❤️ Favorite Track:</strong> \${p.favTrack}</div>
                    <div style="margin-bottom:15px;"><strong>🏆 Best Track:</strong> \${p.bestTrack}</div>
                    <div class="table-responsive">
                        <table class="table">
                            <thead><tr><th>Track</th><th>Runs</th><th>Wins</th><th>Podiums</th><th>Avg</th><th>Best Time</th></tr></thead>
                            <tbody>\${trackStatsHtml}</tbody>
                        </table>
                    </div>
                </div>
                
                <div class="card">
                    <h3 style="margin-bottom:15px;">🏃 Running Style Usage</h3>
                    <div style="margin-bottom:5px;"><strong>🔥 Most Used:</strong> \${p.favStyle}</div>
                    <div style="margin-bottom:5px;"><strong>📉 Least Used:</strong> \${p.leastStyle}</div>
                    <div style="margin-bottom:15px;"><strong>🏆 Best Performing:</strong> \${p.bestStyle}</div>
                    <div class="table-responsive">
                        <table class="table">
                            <thead><tr><th>Style</th><th>Usage</th><th>Wins</th><th>Podiums</th><th>Avg</th><th>Best Time</th></tr></thead>
                            <tbody>\${styleStatsHtml}</tbody>
                        </table>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h3 style="margin-bottom:15px;">📈 Style Evolution</h3>
                <div style="display:flex; flex-wrap:wrap;">\${evolutionHtml}</div>
            </div>
        \`;
        document.getElementById('profile-content').innerHTML = html;
        this.navigate('profile');
    },

    renderUmas() {
        // Simple uma list, similar to players
        const html = this.stats.umas.map(u => \`
            <div class="list-item" onclick="App.showUma('\${u.name.replace(/'/g, "\\'")}')">
                \${this.getUmaImage(u.umaId)}
                <div class="item-content">
                    <div class="item-title">\${u.name}</div>
                    <div class="item-subtitle">Wins: \${u.w} | Avg Finish: \${u.avgFinish}</div>
                </div>
            </div>\`).join('');
        document.getElementById('full-uma-list').innerHTML = html;
    },

    showUma(name) {
        const u = this.stats.umas.find(x => x.name === name);
        if(!u) return;
        document.getElementById('profile-content').innerHTML = \`
            <div class="card" style="text-align:center;">
                \${this.getUmaImage(u.umaId, true)}
                <h2>\${u.name}</h2>
                <p>\${u.w} Wins / \${u.runs} Runs</p>
            </div>\`;
        this.navigate('profile');
    },

    setupForm() {
        // dummy for legacy setupForm calls
    }
};

document.addEventListener('DOMContentLoaded', () => {
    App.init();
});
