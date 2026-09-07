const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');
const normalizedHtml = html.replace(/\r\n/g, '\n');

const searchStr = "pl.history.push({ race: race.name, cup: race.cupNumber, uma: p.uma, pos: p.pos, time: p.time, strategy: style });";
const replaceStr = "pl.history.push({ race: race.name, cup: race.cupNumber, uma: p.uma, pos: p.pos, time: p.time, strategy: style, pop: p.pop });";

if (normalizedHtml.includes(searchStr)) {
    html = normalizedHtml.replace(searchStr, replaceStr);
    console.log('Successfully injected pop to pl.history.push (calculateStats)');
} else {
    console.log('Failed to find pl.history.push in calculateStats');
}

fs.writeFileSync('index.html', html, 'utf8');
