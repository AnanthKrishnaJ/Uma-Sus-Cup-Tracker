const fs = require('fs');

const ranks = {
    1: { uma: 'Agnes Tachyon', rank: 'SS', umaId: 'agnes-tachyon' },
    2: { uma: 'Oguri Cap', rank: 'S+', umaId: 'oguri-cap' },
    3: { uma: 'Oguri Cap', rank: 'SS', umaId: 'oguri-cap' },
    4: { uma: 'Gold Ship', rank: 'S', umaId: '100702' },
    5: { uma: 'Gold Ship', rank: 'SS', umaId: '100702' },
    6: { uma: 'Admire Vega', rank: 'S', umaId: 'admire-vega' },
    7: { uma: 'Oguri Cap', rank: 'A+', umaId: 'oguri-cap' },
    8: { uma: 'Narita Taishin', rank: 'A+', umaId: 'narita-taishin' },
    9: { uma: 'Tamamo Cross', rank: 'S', umaId: 'tamamo-cross' },
    10: { uma: 'Mayano Top Gun', rank: 'A+', umaId: 'mayano-top-gun' },
    11: { uma: 'Meisho Doto', rank: 'A+', umaId: 'meisho-doto' },
    12: { uma: 'Silence Suzuka', rank: 'A+', umaId: 'silence-suzuka', player: '—', strategy: '—', time: '—', gap: '—', pop: 0, title: '' },
    13: { uma: 'Pastime Joy', rank: 'B+', umaId: 'pastime-joy', player: '—', strategy: '—', time: '—', gap: '—', pop: 0, title: '' },
    14: { uma: 'Matikanefukukitaru', rank: 'A+', umaId: 'matikanefukukitaru' },
    15: { uma: 'Grass Wonder', rank: 'A', umaId: 'grass-wonder' },
    16: { uma: 'Meisho Doto', rank: 'A', umaId: 'meisho-doto' },
    17: { uma: 'Seiun Sky', rank: 'A+', umaId: 'seiun-sky' },
    18: { uma: 'Nice Nature', rank: 'B+', umaId: '106002' }
};

let data = fs.readFileSync('index.html', 'utf8');
const startMarker = 'const INITIAL_DATA = ';
const startIndex = data.indexOf(startMarker) + startMarker.length;
const endMarker = '};';
const endIndex = data.indexOf(endMarker, startIndex) + 1;
const jsonStr = data.substring(startIndex, endIndex);

try {
    const initialData = JSON.parse(jsonStr);
    const cup21 = initialData.races.find(r => r.cupNumber === 21);
    
    if (!cup21) throw new Error('Cup 21 not found');
    
    cup21.participants.forEach(p => {
        const update = ranks[p.position];
        if (update) {
            Object.assign(p, update);
        }
    });

    const newJsonStr = JSON.stringify(initialData, null, 2);
    
    // Replace the old JSON string with the new one
    data = data.substring(0, startIndex) + newJsonStr + data.substring(endIndex);
    
    fs.writeFileSync('index.html', data, 'utf8');
    console.log('Successfully updated index.html');
} catch (e) {
    console.error(e);
}
