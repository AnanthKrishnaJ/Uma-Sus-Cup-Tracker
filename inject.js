// Analytical Engine Override
App.stylesMap = {
    'Front': 'Front Runner',
    'Pace': 'Pace Chaser',
    'Late': 'Late Surger',
    'End': 'End Closer'
};

App.parseTime = function(tStr) {
    if (!tStr) return 9999;
    if (typeof tStr !== 'string') return 9999;
    const m = tStr.match(/(\d+):(\d+)\.(\d+)/);
    if (m) return parseInt(m[1]) * 60 + parseInt(m[2]) + parseInt(m[3]) / 10;
    return 9999;
};

App.formatTime = function(sec) {
    if (sec >= 9999) return '-';
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);
    const ms = Math.round((sec - Math.floor(sec)) * 10);
    return `${m}:${s.toString().padStart(2, '0')}.${ms}`;
};

App.getPoints = function(pos) {
    const pts = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1];
    return (pos >= 1 && pos <= 10) ? pts[pos - 1] : 0;
};

App.calculateStats = function() {
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

            if (!umas[p.umaId]) umas[p.umaId] = { umaId: p.umaId, name: p.uma, runs: 0, w: 0, podiums: 0, sumPos: 0, users: {}, history: [] };
            const um = umas[p.umaId];
            um.runs++; um.sumPos += p.pos;
            if (p.pos === 1) um.w++;
            if (p.pos <= 3) um.podiums++;
            if (!um.users[p.player]) um.users[p.player] = 0;
            um.users[p.player]++;
            um.history.push({ race: race.name, cup: race.cupNumber, player: p.player, pos: p.pos, time: p.time, strategy: style, date: race.date });
        });
    });

    const sortedPlayers = Object.values(players).map(p => {
        const avgFinish = p.sumPos / p.runs;
        const avgTime = p.timeCount > 0 ? p.totalTime / p.timeCount : 9999;
        
        let favTrack = { name: '-', runs: 0 };
        let bestTrack = { name: '-', avg: 99, w: 0 };
        Object.keys(p.tracks).forEach(t => {
            if (p.tracks[t].runs > favTrack.runs) { favTrack.name = t; favTrack.runs = p.tracks[t].runs; }
            const tAvg = p.tracks[t].sumPos / p.tracks[t].runs;
            if (tAvg < bestTrack.avg || (tAvg === bestTrack.avg && p.tracks[t].w > bestTrack.w)) {
                bestTrack.name = t; bestTrack.avg = tAvg; bestTrack.w = p.tracks[t].w;
            }
        });

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
        if (leastStyle.name === '-') leastStyle.name = 'None';

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

    sortedPlayers.forEach((p, idx) => { p.rank = idx + 1; p.diff = 0; });

    const sortedUmas = Object.values(umas).map(u => ({
        ...u, winRate: ((u.w / u.runs) * 100).toFixed(1), avgFinish: (u.sumPos / u.runs).toFixed(2),
        bestPlayer: Object.keys(u.users).reduce((a, b) => u.users[a] > u.users[b] ? a : b)
    })).sort((a, b) => b.w - a.w || b.podiums - a.podiums || b.runs - a.runs);
    sortedUmas.forEach((u, idx) => u.rank = idx + 1);

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
};

App.renderDashboard = function() {
    document.getElementById('dash-stats').innerHTML = `
        <div class="stat-block"><div class="val">${this.stats.totalCups}</div><div class="lbl">Total Cups</div></div>
        <div class="stat-block"><div class="val">${this.stats.totalRaces}</div><div class="lbl">Total Races</div></div>
        <div class="stat-block"><div class="val">${this.stats.totalPlayers}</div><div class="lbl">Total Players</div></div>
        <div class="stat-block"><div class="val">${this.stats.totalTracks}</div><div class="lbl">Total Tracks</div></div>
    `;
    
    const rec = this.stats.records;
    document.getElementById('championship-record').innerHTML = `
        <div class="record-heading"><span class="eyebrow">All-Time Historical Records</span><span class="record-count"><i class="fa-solid fa-star"></i></span></div>
        <div class="record-winner" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:15px; margin-top:15px; background:transparent;">
            <div style="background:#fafafa; padding:15px; border-radius:5px; border:1px solid #eee;">
                <div style="font-size:0.8rem; color:#888; text-transform:uppercase; margin-bottom:5px;">Fastest Player/Uma</div>
                <div style="font-size:1.1rem; font-weight:bold; color:var(--text-main);">${rec.fastestPlayer} - ${rec.fastestUma}</div>
                <div style="font-size:0.9rem; color:var(--primary); font-weight:bold; margin-top:5px;">${this.formatTime(rec.fastestTime)} on ${rec.fastestCourse}</div>
            </div>
            <div style="background:#fafafa; padding:15px; border-radius:5px; border:1px solid #eee;">
                <div style="font-size:0.8rem; color:#888; text-transform:uppercase; margin-bottom:5px;">Most Successful Player</div>
                <div style="font-size:1.1rem; font-weight:bold; color:var(--text-main);">${rec.mostWinsPlayer}</div>
                <div style="font-size:0.9rem; color:var(--primary); font-weight:bold; margin-top:5px;">${rec.mostWins} Wins</div>
            </div>
            <div style="background:#fafafa; padding:15px; border-radius:5px; border:1px solid #eee;">
                <div style="font-size:0.8rem; color:#888; text-transform:uppercase; margin-bottom:5px;">Biggest Winning Margin</div>
                <div style="font-size:1.1rem; font-weight:bold; color:var(--text-main);">+${rec.biggestMargin > 0 ? rec.biggestMargin.toFixed(1) : '-'}s</div>
                <div style="font-size:0.9rem; color:var(--primary); font-weight:bold; margin-top:5px;">${rec.biggestMarginRace}</div>
            </div>
            <div style="background:#fafafa; padding:15px; border-radius:5px; border:1px solid #eee;">
                <div style="font-size:0.8rem; color:#888; text-transform:uppercase; margin-bottom:5px;">Closest Finish</div>
                <div style="font-size:1.1rem; font-weight:bold; color:var(--text-main);">+${rec.closestFinish < 999 ? rec.closestFinish.toFixed(1) : '-'}s</div>
                <div style="font-size:0.9rem; color:var(--primary); font-weight:bold; margin-top:5px;">${rec.closestFinishRace}</div>
            </div>
            <div style="background:#fafafa; padding:15px; border-radius:5px; border:1px solid #eee;">
                <div style="font-size:0.8rem; color:#888; text-transform:uppercase; margin-bottom:5px;">Most Used Style</div>
                <div style="font-size:1.1rem; font-weight:bold; color:var(--text-main);">${this.stats.mostGlobalStyle.name}</div>
                <div style="font-size:0.9rem; color:var(--primary); font-weight:bold; margin-top:5px;">${((this.stats.mostGlobalStyle.runs / this.stats.totalStyleRuns)*100).toFixed(1)}% Usage</div>
            </div>
            <div style="background:#fafafa; padding:15px; border-radius:5px; border:1px solid #eee;">
                <div style="font-size:0.8rem; color:#888; text-transform:uppercase; margin-bottom:5px;">Best Performing Style</div>
                <div style="font-size:1.1rem; font-weight:bold; color:var(--text-main);">${this.stats.bestGlobalStyle.name}</div>
                <div style="font-size:0.9rem; color:var(--primary); font-weight:bold; margin-top:5px;">${this.stats.bestGlobalStyle.avg.toFixed(2)} Avg Finish</div>
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
                    <div class="item-value" style="font-size:0.9rem; font-weight:bold; color:var(--primary);">${p.favStyle}</div>
                    <div class="item-label">Fav: ${p.favTrack}</div>
                </div>
            </div>`;
    });
    document.getElementById('dash-player-list').innerHTML = phtml;
};

App.showPlayer = function(name) {
    const p = this.stats.players.find(x => x.name === name);
    if(!p) return;
    
    let styleStatsHtml = '';
    Object.keys(p.styles).forEach(s => {
        const data = p.styles[s];
        if (data.runs > 0) {
            styleStatsHtml += `
            <tr>
                <td style="font-weight:bold;">${s}</td>
                <td>${data.runs} (${((data.runs/p.runs)*100).toFixed(0)}%)</td>
                <td>${data.w}</td>
                <td>${data.pod}</td>
                <td>${(data.sumPos/data.runs).toFixed(2)}</td>
                <td>${this.formatTime(data.bestTime)}</td>
            </tr>`;
        }
    });

    let trackStatsHtml = '';
    Object.keys(p.tracks).forEach(t => {
        const data = p.tracks[t];
        trackStatsHtml += `
        <tr>
            <td style="font-weight:bold;">${t}</td>
            <td>${data.runs}</td>
            <td>${data.w}</td>
            <td>${data.pod}</td>
            <td>${(data.sumPos/data.runs).toFixed(2)}</td>
            <td>${this.formatTime(data.bestTime)}</td>
        </tr>`;
    });
    
    let evolutionHtml = '';
    p.styleEvolution.forEach((e, idx) => {
        evolutionHtml += `<div style="background:#f0f0f0; border:1px solid #ddd; padding:5px 10px; border-radius:20px; font-size:0.85rem; font-weight:600;"><span style="color:var(--primary); margin-right:5px;">Cup ${e.cup}</span> ${e.style}</div>
        ${idx < p.styleEvolution.length - 1 ? '<i class="fa-solid fa-arrow-right" style="color:#ccc; font-size:0.8rem; margin-top:8px;"></i>' : ''}`;
    });

    let html = `
        <div class="card" style="background:var(--accent-dark); color:white; margin-bottom:20px;">
            <h2 style="font-size:2.5rem; margin-bottom:15px;">${p.name}</h2>
            <div class="grid-4" style="gap:15px; margin-top:20px;">
                <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:8px;"><div style="font-size:0.8rem; opacity:0.8; text-transform:uppercase;">Total Points</div><div style="font-size:1.8rem; font-weight:bold; color:var(--gold);">${p.points}</div></div>
                <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:8px;"><div style="font-size:0.8rem; opacity:0.8; text-transform:uppercase;">Races Entered</div><div style="font-size:1.8rem; font-weight:bold;">${p.runs}</div></div>
                <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:8px;"><div style="font-size:0.8rem; opacity:0.8; text-transform:uppercase;">Wins</div><div style="font-size:1.8rem; font-weight:bold;">${p.w} <span style="font-size:1rem; opacity:0.8;">(${p.winRate}%)</span></div></div>
                <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:8px;"><div style="font-size:0.8rem; opacity:0.8; text-transform:uppercase;">Podiums</div><div style="font-size:1.8rem; font-weight:bold;">${p.podiums} <span style="font-size:1rem; opacity:0.8;">(${p.podiumRate}%)</span></div></div>
                <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:8px;"><div style="font-size:0.8rem; opacity:0.8; text-transform:uppercase;">2nd / 3rd</div><div style="font-size:1.8rem; font-weight:bold;">${p.secondPlaces} / ${p.thirdPlaces}</div></div>
                <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:8px;"><div style="font-size:0.8rem; opacity:0.8; text-transform:uppercase;">Avg / Best / Worst</div><div style="font-size:1.8rem; font-weight:bold;">${p.avgFinish} / ${p.bestFinish} / ${p.worstFinish}</div></div>
                <div style="background:rgba(255,255,255,0.1); padding:15px; border-radius:8px; grid-column: span 2;"><div style="font-size:0.8rem; opacity:0.8; text-transform:uppercase;">Best / Avg Race Time</div><div style="font-size:1.8rem; font-weight:bold;">${this.formatTime(p.bestTime)} / ${this.formatTime(p.avgTime)}</div></div>
            </div>
        </div>
        
        <div class="card" style="margin-bottom:20px;">
            <h3 style="margin-bottom:15px; font-size:1.4rem; display:flex; align-items:center; gap:10px;"><i class="fa-solid fa-shoe-prints" style="color:var(--primary);"></i> Running Style Usage</h3>
            <div style="display:flex; gap:20px; margin-bottom:20px; background:#fafafa; padding:15px; border-radius:8px; border:1px solid #eee;">
                <div><span style="color:#888; text-transform:uppercase; font-size:0.8rem;">🔥 Most Used</span><br><strong style="font-size:1.1rem;">${p.favStyle}</strong></div>
                <div><span style="color:#888; text-transform:uppercase; font-size:0.8rem;">📉 Least Used</span><br><strong style="font-size:1.1rem;">${p.leastStyle}</strong></div>
                <div><span style="color:#888; text-transform:uppercase; font-size:0.8rem;">🏆 Best Performing</span><br><strong style="font-size:1.1rem;">${p.bestStyle}</strong></div>
            </div>
            <div class="table-responsive">
                <table class="table" style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead style="background:#f4ece1; color:var(--text-main);"><tr><th style="padding:10px;">Style</th><th style="padding:10px;">Usage</th><th style="padding:10px;">Wins</th><th style="padding:10px;">Podiums</th><th style="padding:10px;">Avg Finish</th><th style="padding:10px;">Best Time</th></tr></thead>
                    <tbody>${styleStatsHtml}</tbody>
                </table>
            </div>
        </div>

        <div class="card" style="margin-bottom:20px;">
            <h3 style="margin-bottom:15px; font-size:1.4rem; display:flex; align-items:center; gap:10px;"><i class="fa-solid fa-map-location-dot" style="color:var(--gold);"></i> Track Preferences</h3>
            <div style="display:flex; gap:20px; margin-bottom:20px; background:#fafafa; padding:15px; border-radius:8px; border:1px solid #eee;">
                <div><span style="color:#888; text-transform:uppercase; font-size:0.8rem;">❤️ Favorite Track</span><br><strong style="font-size:1.1rem;">${p.favTrack}</strong></div>
                <div><span style="color:#888; text-transform:uppercase; font-size:0.8rem;">🏆 Best Track</span><br><strong style="font-size:1.1rem;">${p.bestTrack}</strong></div>
            </div>
            <div class="table-responsive">
                <table class="table" style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead style="background:#f4ece1; color:var(--text-main);"><tr><th style="padding:10px;">Track</th><th style="padding:10px;">Runs</th><th style="padding:10px;">Wins</th><th style="padding:10px;">Podiums</th><th style="padding:10px;">Avg Finish</th><th style="padding:10px;">Best Time</th></tr></thead>
                    <tbody>${trackStatsHtml}</tbody>
                </table>
            </div>
        </div>
        
        <div class="card">
            <h3 style="margin-bottom:15px; font-size:1.4rem; display:flex; align-items:center; gap:10px;"><i class="fa-solid fa-timeline" style="color:var(--accent);"></i> Style Evolution</h3>
            <div style="display:flex; flex-wrap:wrap; align-items:center; gap:8px;">${evolutionHtml}</div>
        </div>
    `;
    document.getElementById('profile-content').innerHTML = html;
    this.navigate('profile');
};

App.showRaceDetail = function(id) {
    const race = this.data.races.find(r => r.id === id);
    if (!race) return;
    const sorted = [...race.participants].sort((a, b) => a.pos - b.pos);
    
    const raceMeta = [
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Cup</span><br><strong style="font-size:1.1rem;">Sus Cup ${race.cupNumber}</strong>`,
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Round</span><br><strong style="font-size:1.1rem;">${race.name}</strong>`,
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Date & Time</span><br><strong style="font-size:1.1rem;">${race.date} ${race.time || ''}</strong>`,
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Track</span><br><strong style="font-size:1.1rem;">${race.course}</strong>`,
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Distance</span><br><strong style="font-size:1.1rem;">${race.distance}m (${race.distanceType})</strong>`,
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Surface</span><br><strong style="font-size:1.1rem;">${race.surface}</strong>`,
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Direction</span><br><strong style="font-size:1.1rem;">${race.direction || 'N/A'}</strong>`,
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Weather</span><br><strong style="font-size:1.1rem;">${race.weather || 'N/A'}</strong>`,
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Ground Condition</span><br><strong style="font-size:1.1rem;">${race.ground || 'N/A'}</strong>`,
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Mood</span><br><strong style="font-size:1.1rem;">${race.mood || 'N/A'}</strong>`,
        `<span style="color:#888; font-size:0.8rem; text-transform:uppercase;">Room ID</span><br><strong style="font-size:1.1rem;">${race.roomId || 'N/A'}</strong>`
    ];

    let html = `
        <div class="card" style="background:var(--accent-dark); color:white; padding:30px;">
            <h2 style="font-size:2.5rem; margin-bottom:20px;">${race.name}</h2>
            <div class="grid-4" style="gap:15px; margin-top:20px;">
                ${raceMeta.map(item => `<div style="background:rgba(255,255,255,0.1); padding:10px 15px; border-radius:8px;">${item}</div>`).join('')}
            </div>
        </div>
    `;

    sorted.forEach(p => {
        let medal = p.pos;
        let style = '';
        if (p.pos === 1) { style = 'border-left: 5px solid var(--gold); background: #fffcf0;'; medal = '🥇'; }
        else if (p.pos === 2) { style = 'border-left: 5px solid var(--silver);'; medal = '🥈'; }
        else if (p.pos === 3) { style = 'border-left: 5px solid var(--bronze);'; medal = '🥉'; }
        
        html += `
            <div class="list-item" style="${style}">
                <div style="font-size:1.8rem; font-weight:900; width:50px; text-align:center;">${medal}</div>
                ${this.getUmaImage(p.umaId)}
                <div class="item-content">
                    <div class="item-title" style="font-size:1.2rem;">${p.uma}</div>
                    <div class="item-subtitle" style="margin-top:5px; font-weight:bold; display:flex; gap:15px;">
                        <span><i class="fa-solid fa-user"></i> ${p.player}</span>
                        <span style="color:var(--primary)"><i class="fa-solid fa-shoe-prints"></i> ${this.stylesMap[p.strategy] || p.strategy || 'N/A'}</span>
                    </div>
                </div>
                <div class="item-right" style="text-align:right;">
                    <div class="item-value" style="font-size:1.3rem; font-weight:bold; color:var(--primary);">${p.time || '-'}</div>
                    <div class="item-label" style="font-weight:bold;">Final Pos: ${p.pos}</div>
                </div>
            </div>
        `;
    });
    document.getElementById('race-detail-content').innerHTML = html;
    this.navigate('race-detail');
};
