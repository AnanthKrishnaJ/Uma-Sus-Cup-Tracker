const fs = require('fs');

const content = fs.readFileSync('suscup1.html', 'utf8');
const start = content.indexOf('const UMA_PROFILES = {');
const end = content.indexOf('const NPC_PROFILES = {');
const profilesText = content.substring(start, end);

const images = {};
for (const line of profilesText.split('\n')) {
    const match = line.match(/"([^"]+)":\s*\{[^}]*id:\s*(\d+)/);
    if (match) {
        const name = match[1];
        const id = match[2];
        images[name] = 'https://gametora.com/images/umamusume/characters/chara_stand_' + id.substring(0,4) + '_' + id + '.png';
    }
}
console.log(JSON.stringify(images, null, 2));
