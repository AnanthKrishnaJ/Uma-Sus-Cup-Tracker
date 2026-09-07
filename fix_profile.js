const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf-8');

html = html.replace('firstCup: race.cupNumber, latestCup: race.cupNumber,', 'firstCup: (race.cupNumber || race.id), latestCup: (race.cupNumber || race.id),');
html = html.replace('pl.latestCup = race.cupNumber;', 'pl.latestCup = (race.cupNumber || race.id);');
html = html.replace('race: race.name, cup: race.cupNumber, uma: p.uma, umaId: p.umaId, pos: p.pos,', 'race: race.name, cup: (race.cupNumber || race.id), uma: p.uma, umaId: p.umaId, pos: p.pos,');
html = html.replace("um.history.push({ race: race.name, cup: race.cupNumber, player: p.player, pos: p.pos, strategy: p.strategy || 'Strategy not recorded', time: p.time, pop: p.pop });", "um.history.push({ race: race.name, cup: (race.cupNumber || race.id), player: p.player, pos: p.pos, strategy: p.strategy || 'Strategy not recorded', time: p.time, pop: p.pop });");
html = html.replace('<div><i class="fa-solid fa-horse-head" style="color:var(--text-muted)"></i> <strong>${p.uniqueUmasCount}</strong> Unique Umas</div>', '<div><i class="fa-solid fa-horse-head" style="color:var(--text-muted)"></i> <strong>${p.uniqueUmas.size}</strong> Unique Umas</div>');

fs.writeFileSync('index.html', html, 'utf-8');
console.log('Fixed index.html undefined variables');
