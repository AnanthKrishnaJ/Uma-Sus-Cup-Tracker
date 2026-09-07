const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const INITIAL_DATA_START = html.indexOf('const INITIAL_DATA = ');
const npcProfilesIndex = html.indexOf('const NPC_PROFILES');
let INITIAL_DATA_END = html.lastIndexOf('};', npcProfilesIndex);

let dataStr = html.substring(INITIAL_DATA_START + 'const INITIAL_DATA = '.length, INITIAL_DATA_END + 1);

let data = JSON.parse(dataStr);
const cups = [17, 18, 19, 20];
cups.forEach(cupNum => {
    const race = data.races.find(r => r.cupNumber === cupNum);
    console.log(`Sus Cup ${cupNum}:`, race.specialWinners);
});
