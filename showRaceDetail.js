showRaceDetail(id) {
                const race = this.data.races.find(r => r.id === id);
                if (!race) return;
                const sorted = [...race.participants].sort((a, b) => a.pos - b.pos);
                const raceMeta = [
                    race.date && `${race.date.split(',')[0]}`,
                    race.roomId && `ROOM ${race.roomId}`,
                    race.grade,
                    race.distanceType && `${race.distanceType} / ${race.direction || 'Direction not recorded'}`,
                    race.courseLayout,
                    race.weather && `WEATHER SETTING: ${race.weather}`,
                    race.ground && `GROUND SETTING: ${race.ground}`,
                    race.condition && `RACE CONDITION: ${race.condition}`,
                    race.mood && `MOOD: ${race.mood}`,
                    race.restriction && `LIMIT: ${race.restriction}`,
                    race.entryRule
                ].filter(Boolean);

                let html = `
                    <div class="card" style="background:var(--accent-dark); color:white;">
                        <span class="badge" style="background:var(--primary); margin-bottom:10px;">${(race.cupName || `SUS CUP ${race.cupNumber}`).toUpperCase()}</span>
                        <h2 style="font-size:2rem; margin-bottom:10px; color:white;">${race.name}</h2>
                        <p style="font-weight:700; opacity:0.8;">${race.cupName || `SUS CUP ${race.cupNumber}`}${race.subtitle ? ` &mdash; ${race.subtitle}` : ''}</p>
                        <p style="font-weight:700; opacity:0.8; margin-top:6px;">${race.course} ${race.surface} ${race.distance}m</p>
                        <div class="race-meta">${raceMeta.map(item => `<span>${item}</span>`).join('')}</div>
                    </div>
                    ${race.partialResults ? '<div style="background:var(--warning, #f39c12); color:white; padding:10px; border-radius:5px; font-weight:bold; margin-bottom:15px;">⚠️ PARTIAL RESULTS AVAILABLE - Only confirmed top placements are shown below.</div>' : ''}
                    ${race.images?.length ? `<div class="race-gallery">${race.images.slice(0, 4).map((image, index) => `<a href="javascript:void(0)" onclick="openGallery('${race.images.join(',')}', ${index})"><img src="${image}" alt="Sus Cup ${race.cupNumber} result screenshot ${index + 1}" loading="lazy" onerror="this.onerror=null; this.src='data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' width=\'300\' height=\'200\'><rect width=\'300\' height=\'200\' fill=\'%23eee\'/><text x=\'150\' y=\'100\' font-size=\'16\' text-anchor=\'middle\' fill=\'%23999\'>Screenshot Missing</text></svg>';"></a>`).join('')}</div>` : ''}
                `;

                const firstPlace = sorted.find(p => p.pos === 1) || sorted[0];
                const displayWinners = race.scenarioWinners || race.specialWinners || (firstPlace ? { 'Overall Winner': { player: firstPlace.player, uma: firstPlace.uma, pos: firstPlace.position ?? firstPlace.pos } } : null);

                if (displayWinners) {
                    const blockTitle = (race.scenarioWinners || race.specialWinners) ? 'Special Category Winners' : 'Race Winner';
                    html += `<div style="margin: 20px 0; background: var(--surface-light); border-radius: 8px; padding: 15px; border-left: 4px solid var(--accent);">
                        <h3 style="margin-bottom: 12px; font-size: 1.2rem; color: var(--accent);">${blockTitle}</h3>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">`;
                    
                    for (const [category, winner] of Object.entries(displayWinners)) {
                        const participant = race.participants.find(p => p.uma === winner.uma && p.player === winner.player);
                        const umaId = winner.umaId || (participant ? participant.umaId : '');
                        const posText = winner.pos ? `${winner.pos}${winner.pos === 1 ? 'st' : winner.pos === 2 ? 'nd' : winner.pos === 3 ? 'rd' : 'th'}` : '';
                        
                        html += `
                            <div style="background: var(--surface); padding: 12px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                                <div style="font-weight: 800; font-size: 0.9rem; color: var(--text-muted); margin-bottom: 5px; text-transform: uppercase;">${category}</div>
                                <div style="display: flex; align-items: center; gap: 10px;">
                                    ${this.getUmaImage(umaId).replace('border-radius:4px', 'border-radius:50%')}
                                    <div>
                                        <div style="font-weight: 700;">${winner.uma}</div>
                                        <div style="font-size: 0.85rem; color: var(--text-muted);"><a href="#" onclick="App.showPlayer('${winner.player}'); return false;" style="color:inherit; font-weight:600; text-decoration:none;" onmouseover="this.style.textDecoration='underline'" onmouseout="this.style.textDecoration='none'">${winner.player}</a>${posText ? ` &bull; ${posText}` : ''}</div>
                                    </div>
                                </div>
                            </div>
                        `;
                    }
                    html += `</div></div>`;
                }

                if (race.partialResults) {
                    html += '<h3 style="margin-bottom:10px; color:var(--primary);">CONFIRMED RESULTS</h3>';
                }
                sorted.forEach(p => {
                    let pos = p.position ?? p.pos;
                    let style = ''; let medal = pos;
                    if (pos === 1) { style = 'border-left: 5px solid var(--gold); background: #fffcf0;'; medal = '🥇'; }
                    else if (pos === 2) { style = 'border-left: 5px solid var(--silver);'; medal = '🥈'; }
                    else if (pos === 3) { style = 'border-left: 5px solid var(--bronze);'; medal = '🥉'; }

                    html += `
                        <div class="list-item" style="${style}">
                            <div style="font-size:1.8rem; font-weight:900; width:50px; text-align:center; margin-right:15px;">${medal}</div>
                            <div class="avatar-circle" style="width:45px;height:45px;font-size:1rem;background:#eee;color:#333;">${p.number || '-'}</div>
                            ${this.getUmaImage(p.umaId)}
                            <div class="item-content">
                                <div style="display:flex; align-items:center; gap:10px; margin-bottom:4px;">
                                    <div class="item-title">
                                        ${p.characterUrl || (UMA_DATABASE[p.umaId] && UMA_DATABASE[p.umaId].url) ? 
                                            `<a href="${p.characterUrl || UMA_DATABASE[p.umaId].url}" target="_blank" style="color:inherit; text-decoration:none;" onmouseover="this.style.textDecoration='underline'" onmouseout="this.style.textDecoration='none'">${p.uma} <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:0.7em; opacity:0.7;"></i></a>` 
                                            : p.uma}
                                    </div>
                                    ${this.getBadge(p.rank)}
                                </div>
                                <div class="item-subtitle">${p.player === 'NPC' ? 'NPC / Mob Uma' : `Trainer: <a href="#" onclick="App.showPlayer('${p.player}'); return false;" style="color:inherit; font-weight:600; text-decoration:none;" onmouseover="this.style.textDecoration='underline'" onmouseout="this.style.textDecoration='none'">${p.player}</a>`} &bull; ${p.strategy || 'Strategy not recorded'} &bull; ${p.version || (UMA_DATABASE[p.umaId]?.type === 'NPC' ? 'NPC Uma' : UMA_DATABASE[p.umaId]?.version || 'Version not recorded')}</div>
                                <div class="item-label" style="margin-top:4px;">${p.title ? `TITLE: ${p.title}` : 'NPC / Mob Uma'} &bull; RUNNER NO. ${p.number}</div>
                            </div>
                            <div class="item-right">
                                <div class="item-value" style="font-size:1.1rem;">${p.time || p.finish || p.gap || ''}</div>
                                <div class="item-label">Fav: ${p.pop}</div>
                            </div>
                        </div>
                    `;
                });
                if (race.partialResults && race.submittedEntries) {
                    html += '<h3 style="margin-top:20px; margin-bottom:10px; color:var(--text-muted);">RESULTS NOT AVAILABLE (Submitted Entries)</h3>';
                    race.submittedEntries.forEach(entry => {
                        html += `
                            <div class="list-item" style="opacity: 0.6; background: #fafafa;">
                                <div style="font-size:1.8rem; font-weight:900; width:50px; text-align:center; margin-right:15px; color:#aaa;">?</div>
                                ${this.getUmaImage(entry.umaId)}
                                <div class="item-content">
                                    <div class="item-title">${entry.uma}</div>
                                    <div class="item-subtitle">Trainer: ${entry.player} &bull; Official Submitted Entry</div>
                                </div>
                            </div>
                        `;
                    });
                }
                


    const raceIndex = this.data.races.findIndex(r => r.id === id);
    const prevRace = raceIndex > 0 ? this.data.races[raceIndex - 1] : null;
    const nextRace = raceIndex < this.data.races.length - 1 ? this.data.races[raceIndex + 1] : null;

    html += `
    <div style="display: flex; justify-content: space-between; margin-top: 30px; gap: 15px;">
        ${prevRace ? `<button class="btn btn-primary" onclick="App.showRaceDetail(${prevRace.id})" style="flex: 1; text-align: left; background: var(--accent-dark); border: none;"><i class="fa-solid fa-arrow-left"></i> Previous: ${(prevRace.cupName || ('Sus Cup ' + prevRace.cupNumber)).toUpperCase()}</button>` : '<div style="flex: 1;"></div>'}
        ${nextRace ? `<button class="btn btn-primary" onclick="App.showRaceDetail(${nextRace.id})" style="flex: 1; text-align: right; background: var(--accent-dark); border: none;">Next: ${(nextRace.cupName || ('Sus Cup ' + nextRace.cupNumber)).toUpperCase()} <i class="fa-solid fa-arrow-right"></i></button>` : '<div style="flex: 1;"></div>'}
    </div>`;

    document.getElementById('race-detail-content').innerHTML = html;

                this.navigate('race-detail');
            },
