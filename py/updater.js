const fs = require('fs');

const rawData = fs.readFileSync('../data/suscup_11_20_raw_data.txt', 'utf8');
const html = fs.readFileSync('../.vscode/suscup1.html', 'utf8');

// Parse text
const cups = rawData.split('🏆 Sus Cup ').slice(1);
const parsed = {};

cups.forEach(cupText => {
    const lines = cupText.trim().split('\n').map(l => l.trim()).filter(l => l);
    const cupNum = parseInt(lines[0], 10);
    const participants = [];
    
    for (let i = 0; i < lines.length; i++) {
        let line = lines[i];
        
        // e.g. "🥇 1st", "4th", "6th–18th"
        if (line.match(/^(🥇|🥈|🥉)?\s*\d+(st|nd|rd|th)/) || line.match(/^\d+th(–\d+th)?/)) {
            if (line.includes('Not Shown') && line.includes('6th–18th')) {
                for (let pos = 6; pos <= 18; pos++) {
                    participants.push({
                        pos: pos,
                        uma: "Not Shown",
                        player: "—",
                        number: "-",
                        pop: "-",
                        strategy: "-",
                        gap: "Not Shown",
                        time: "Not Shown"
                    });
                }
                break; // Stop parsing participants for this cup
            }

            const posMatch = line.match(/\d+/);
            const currentPos = parseInt(posMatch[0], 10);
            
            const uma = lines[++i];
            let trainer = lines[++i];
            if (trainer === '—' || trainer === '-') trainer = "NPC";
            
            const raceNoStr = lines[++i];
            const raceNo = isNaN(raceNoStr) ? raceNoStr : parseInt(raceNoStr, 10);
            
            const favStr = lines[++i].replace('No. ', '');
            const fav = isNaN(favStr) ? favStr : parseInt(favStr, 10);
            
            const style = lines[++i];
            const finish = lines[++i];
            
            participants.push({
                pos: currentPos,
                uma: uma,
                player: trainer,
                number: raceNo,
                pop: fav,
                strategy: style,
                gap: finish,
                time: finish
            });
        }
    }
    
    parsed[cupNum] = participants;
});

console.log("Parsed Cups:", Object.keys(parsed));

// Find INITIAL_DATA in HTML
const regex = /const INITIAL_DATA = (\{[\s\S]*?\n\});\s*const UMA_DATABASE/m;
const match = html.match(regex);
if (!match) {
    console.error("INITIAL_DATA not found in HTML!");
    process.exit(1);
}

let initialData;
try {
    // Evaluating the object literal
    initialData = eval('(' + match[1] + ')');
} catch(e) {
    console.error("Failed to parse INITIAL_DATA", e);
    process.exit(1);
}

// Update archive
let updated = false;
initialData.archive.forEach(race => {
    // Cup 11 is id 11, Cup 20 is id 20
    if (race.id >= 11 && race.id <= 20) {
        if (parsed[race.id]) {
            // Need to preserve umaId and characterUrl from existing data if possible
            // Wait, the new participants array doesn't have umaId, version, rank, title, etc.
            // Let's just merge new data into the old participants, or replace completely?
            // The prompt says: "update the suscup reuslts if there are any changes and do nothing else"
            // Let's map existing data to avoid losing umaId/version/rank/etc.
            
            const newParticipants = parsed[race.id].map(np => {
                // Find existing participant by position or name
                const ep = race.participants.find(p => p.pos === np.pos) || {};
                return {
                    ...ep,
                    pos: np.pos,
                    uma: np.uma,
                    player: np.player,
                    number: np.number,
                    pop: np.pop,
                    strategy: np.strategy,
                    time: np.time,
                    gap: np.gap
                };
            });
            race.participants = newParticipants;
            updated = true;
            console.log(`Updated Cup ${race.id}`);
        }
    }
});

if (updated) {
    const newDataString = JSON.stringify(initialData, null, 4);
    const newHtml = html.replace(match[1], newDataString);
    fs.writeFileSync('../.vscode/suscup1.html', newHtml, 'utf8');
    console.log("Successfully updated suscup1.html");
} else {
    console.log("No updates made.");
}
