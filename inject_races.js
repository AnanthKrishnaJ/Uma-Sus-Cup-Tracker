const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf-8');

let startIdx = html.indexOf('const INITIAL_DATA = ') + 'const INITIAL_DATA = '.length;
let endIdx = startIdx;
let openBraces = 0;
let inString = false;
let escape = false;

for (let i = startIdx; i < html.length; i++) {
    let char = html[i];
    
    if (escape) {
        escape = false;
        continue;
    }
    
    if (char === '\\') {
        escape = true;
        continue;
    }
    
    if (char === '\"') {
        inString = !inString;
        continue;
    }
    
    if (!inString) {
        if (char === '{') {
            openBraces++;
        } else if (char === '}') {
            openBraces--;
            if (openBraces === 0) {
                endIdx = i + 1;
                break;
            }
        }
    }
}

if (endIdx > startIdx && openBraces === 0) {
    let jsonStr = html.substring(startIdx, endIdx);
    let data = JSON.parse(jsonStr);
    let newRaces = JSON.parse(fs.readFileSync('suscup_race_details/suscup_1_to_28_details.txt', 'utf-8')).races;
    data.races = newRaces;
    let newDataStr = JSON.stringify(data, null, 4);
    html = html.substring(0, startIdx) + newDataStr + html.substring(endIdx);
    fs.writeFileSync('index.html', html, 'utf-8');
    console.log('Successfully updated INITIAL_DATA');
} else {
    console.error('Failed to parse INITIAL_DATA bounds.');
}
