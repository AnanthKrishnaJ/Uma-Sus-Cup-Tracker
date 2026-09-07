const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

const INITIAL_DATA_START = html.indexOf('const INITIAL_DATA = ');
const npcProfilesIndex = html.indexOf('const NPC_PROFILES');
let INITIAL_DATA_END = html.lastIndexOf('};', npcProfilesIndex);

let dataStr = html.substring(INITIAL_DATA_START + 'const INITIAL_DATA = '.length, INITIAL_DATA_END + 1);

let data = JSON.parse(dataStr);

const cup21 = data.races.find(r => r.id === 21);
if (cup21) {
    cup21.name = 'Takamatsunomiya Kinen';
    cup21.date = '2026-04-05'; // Guessing based on timeline, leaving as is if not provided
    cup21.race = 'Takamatsunomiya Kinen';
    cup21.course = 'Chukyo Turf';
    cup21.surface = 'Turf';
    cup21.distance = '1200m';
    cup21.distanceType = 'Sprint';
    cup21.direction = 'Left';
    cup21.weather = 'Sunny';
    cup21.ground = 'Firm';
    cup21.details = 'Chukyo Turf 1200m (Sprint) Left | Firm';

    cup21.participants = [
        { number: 4, uma: 'Taiki Shuttle', player: 'agnes', strategy: 'Pace', time: '1:07.3', gap: '1:07.3', pop: 4, rank: 'A+', title: 'Mightiest Miler', umaId: 'taiki-shuttle', position: 1, pos: 1 },
        { number: 2, uma: 'Curren Chan', player: 'Cyclobly', strategy: 'Pace', time: '1 L', gap: '1 L', pop: 2, rank: 'S', title: 'Sprint Sweetheart', umaId: 'curren-chan', position: 2, pos: 2 },
        { number: 12, uma: 'Curren Chan', player: 'Jiinxye', strategy: 'Front', time: '1/2 L', gap: '1/2 L', pop: 12, rank: 'A+', title: 'Team Player Star Slayer', umaId: 'curren-chan', position: 3, pos: 3 },
        { number: 14, uma: 'Sakura Bakushin O', player: 'Jiinxye', strategy: 'Front', time: '1 L', gap: '1 L', pop: 14, rank: 'A+', title: 'Team Player Star Slayer', umaId: 'sakura-bakushin-o', position: 4, pos: 4 },
        { number: 13, uma: 'Haru Urara', player: 'Cyclobly', strategy: 'Late', time: '1/2 L', gap: '1/2 L', pop: 13, rank: 'A+', title: 'Finals Champion', umaId: 'haru-urara', position: 5, pos: 5 },
        { number: 1, uma: 'Taiki Shuttle', player: 'Cyclobly', strategy: 'Pace', time: '1/2 L', gap: '1/2 L', pop: 1, rank: 'S', title: 'Witness to Legend', umaId: 'taiki-shuttle', position: 6, pos: 6 },
        { number: 5, uma: 'Sakura Bakushin O', player: 'Yves', strategy: 'Front', time: '3/4 L', gap: '3/4 L', pop: 5, rank: 'A+', title: 'Witness to Legend', umaId: 'sakura-bakushin-o', position: 7, pos: 7 },
        { number: 10, uma: 'Maruzensky', player: 'Jiinxye', strategy: 'Front', time: '1 L', gap: '1 L', pop: 10, rank: 'A+', title: 'Team Player Star Slayer', umaId: 'maruzensky', position: 8, pos: 8 },
        { number: 6, uma: 'Maruzensky', player: 'Cruzi', strategy: 'Front', time: '1 1/2 L', gap: '1 1/2 L', pop: 6, rank: 'S', title: 'Dream Team', umaId: 'maruzensky', position: 9, pos: 9 },
        { number: 11, uma: 'Sakura Bakushin O', player: 'agnes', strategy: 'Front', time: '1/2 L', gap: '1/2 L', pop: 11, rank: 'A+', title: 'Finals Champion', umaId: 'sakura-bakushin-o', position: 10, pos: 10 },
        { number: 9, uma: 'Air Groove', player: 'agnes', strategy: 'Pace', time: '1 3/4 L', gap: '1 3/4 L', pop: 9, rank: 'A+', title: 'Triple Tiara', umaId: 'air-groove', position: 11, pos: 11 },
        { number: 8, uma: 'Silence Suzuka', player: 'Cruzi', strategy: 'Front', time: '1 1/4 L', gap: '1 1/4 L', pop: 8, rank: 'A+', title: 'Otherworldly Front-Runner', umaId: 'silence-suzuka', position: 12, pos: 12 },
        { number: 17, uma: 'Pastime Joy', player: 'Mob', strategy: 'Pace', time: 'Neck', gap: 'Neck', pop: 17, rank: 'B+', title: 'Not shown', umaId: 'pastime-joy', position: 13, pos: 13 },
        { number: 15, uma: 'Ribbon Virelai', player: 'Mob', strategy: 'Front', time: '1/2 L', gap: '1/2 L', pop: 15, rank: 'B+', title: 'Not shown', umaId: 'ribbon-virelai', position: 14, pos: 14 },
        { number: 16, uma: 'Battle of Elah', player: 'Mob', strategy: 'End', time: '1/2 L', gap: '1/2 L', pop: 16, rank: 'B+', title: 'Not shown', umaId: 'battle-of-elah', position: 15, pos: 15 },
        { number: 7, uma: 'Oguri Cap', player: 'Yves', strategy: 'Pace', time: 'Nose', gap: 'Nose', pop: 7, rank: 'A+', title: 'Witness to Legend', umaId: 'oguri-cap', position: 16, pos: 16 },
        { number: 18, uma: 'Smart Falcon', player: 'Yves', strategy: 'Front', time: '1 3/4 L', gap: '1 3/4 L', pop: 18, rank: 'A', title: 'Record Holder', umaId: 'smart-falcon', position: 17, pos: 17 },
        { number: 3, uma: 'Daiwa Scarlet', player: 'Cruzi', strategy: 'Pace', time: '5 L', gap: '5 L', pop: 3, rank: 'S', title: 'Miss Perfect', umaId: 'daiwa-scarlet', position: 18, pos: 18 }
    ];

    cup21.specialWinners = {
        '3★ Blue Spark': { player: 'Cyciesta', uma: 'Curren Chan', pos: 2, umaId: 'curren-chan' },
        '2★ Blue Spark': { player: 'Agnes', uma: 'Taiki Shuttle', pos: 1, umaId: 'taiki-shuttle' },
        '1★ Blue Spark': { player: 'Jiinxye', uma: 'Sakura Bakushin O', pos: 4, umaId: 'sakura-bakushin-o' }
    };

    // Update winner in data.winners if present
    const cup21Winner = data.winners.find(w => w.cup === 'Sus Cup 21');
    if (cup21Winner) {
        cup21Winner.trainer = 'agnes';
        cup21Winner.uma = 'Taiki Shuttle';
        cup21Winner.umaId = 'taiki-shuttle';
        cup21Winner.race = 'Takamatsunomiya Kinen';
        cup21Winner.result = '1:07.3';
    } else {
        data.winners.push({
            cup: 'Sus Cup 21',
            trainer: 'agnes',
            uma: 'Taiki Shuttle',
            umaId: 'taiki-shuttle',
            version: 'Original / Default',
            url: 'https://gametora.com/umamusume/characters/101401-taiki-shuttle',
            race: 'Takamatsunomiya Kinen',
            date: '2026-04-05',
            result: '1:07.3'
        });
    }
}

let newDataStr = JSON.stringify(data, null, 2);
html = html.substring(0, INITIAL_DATA_START + 'const INITIAL_DATA = '.length) + newDataStr + html.substring(INITIAL_DATA_END + 1);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Update for Cup 21 complete.');
