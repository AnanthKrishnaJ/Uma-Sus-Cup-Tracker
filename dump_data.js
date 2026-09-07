const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

const INITIAL_DATA_START = html.indexOf('const INITIAL_DATA = ');
const npcProfilesIndex = html.indexOf('const NPC_PROFILES');
let INITIAL_DATA_END = html.lastIndexOf('};', npcProfilesIndex);

let dataStr = html.substring(INITIAL_DATA_START + 'const INITIAL_DATA = '.length, INITIAL_DATA_END + 1);

let data = JSON.parse(dataStr);

// Dump Sus Cup 1 to 20
const cups1to20 = data.races.filter(r => r.id >= 1 && r.id <= 20);
const data1to20 = { races: cups1to20 };
fs.writeFileSync('suscup_1_to_20_data.txt', JSON.stringify(data1to20, null, 2), 'utf8');

// Dump Sus Cup 11 to 20
const cups11to20 = data.races.filter(r => r.id >= 11 && r.id <= 20);
const data11to20 = { races: cups11to20 };
fs.writeFileSync('suscup_11_to_20_data.txt', JSON.stringify(data11to20, null, 2), 'utf8');

console.log('Saved data.');
