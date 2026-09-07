const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const INITIAL_DATA_START = html.indexOf('const INITIAL_DATA = ');
const npcProfilesIndex = html.indexOf('const NPC_PROFILES');
let INITIAL_DATA_END = html.lastIndexOf('};', npcProfilesIndex);

let dataStr = html.substring(INITIAL_DATA_START + 'const INITIAL_DATA = '.length, INITIAL_DATA_END + 1);

let data = JSON.parse(dataStr);

const specialImages = {
    17: {
        'Single Guts': 'tm-opera-o',
        'Double Guts': 'agnes-digital',
        'Triple Guts': 'symboli-rudolf'
    },
    18: {
        'Triple SSR': 'nice-nature',
        'Double SSR': 'nice-nature',
        'Single SSR': 'biwa-hayahide'
    },
    19: {
        '0 Gold Skill': 'mayano-top-gun',
        '1-2 Gold Skill': 'gold-city',
        'Gold Skill Only': 'tm-opera-o'
    },
    20: {
        'Front Winner': 'mihono-bourbon',
        'Pace Winner': 'mejiro-mcqueen',
        'Late Winner': 'eishin-flash',
        'End Winner': 'mayano-top-gun'
    }
};

for (const cupNum in specialImages) {
    const race = data.races.find(r => r.cupNumber === parseInt(cupNum));
    if (race && race.specialWinners) {
        for (const cat in specialImages[cupNum]) {
            if (race.specialWinners[cat]) {
                race.specialWinners[cat].umaId = specialImages[cupNum][cat];
            }
        }
    }
}

let newDataStr = JSON.stringify(data, null, 2);
html = html.substring(0, INITIAL_DATA_START + 'const INITIAL_DATA = '.length) + newDataStr + html.substring(INITIAL_DATA_END + 1);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Update complete.');
