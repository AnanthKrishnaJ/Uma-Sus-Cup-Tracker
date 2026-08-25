import json

suscup13 = {
  "id": 13,
  "cupNumber": "SUS CUP 13 - Haru Leading",
  "cupName": "Sus Cup 13",
  "name": "Arima Kinen",
  "date": "2025-10-14",
  "time": "18:30",
  "roomId": "7011 0288",
  "race": "Arima Kinen",
  "course": "Nakayama Turf",
  "surface": "Turf",
  "distance": "2500m",
  "distanceType": "Long",
  "direction": "Right / Inner",
  "weather": "Random",
  "ground": "Random",
  "mood": "Random",
  "rankLimit": "No rank limit",
  "specialRule": "No Front Runners allowed. Note: No rank limit was enabled accidentally.",
  "images": [
    "13.1.png"
  ],
  "partialResults": True,
  "participants": [
    {
      "pos": 1,
      "uma": "Gold Ship",
      "umaId": "gold-ship",
      "player": "Cruzi",
      "number": 6,
      "rank": "A",
      "title": "Finals Champion",
      "strategy": "End",
      "time": "2:28.9",
      "pop": 1,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/gold-ship"
    },
    {
      "pos": 2,
      "uma": "Grass Wonder",
      "umaId": "grass-wonder",
      "player": "Agnes",
      "number": 9,
      "rank": "A",
      "title": "The GOAT",
      "strategy": "Late",
      "gap": "1 1/2 L",
      "pop": 2,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/grass-wonder"
    },
    {
      "pos": 3,
      "uma": "Agnes Tachyon",
      "umaId": "agnes-tachyon",
      "player": "Cruzi",
      "number": 15,
      "rank": "A",
      "title": "Finals Champion",
      "strategy": "Pace",
      "gap": "1 1/4 L",
      "pop": 3,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon"
    },
    {
      "pos": 4,
      "uma": "Mejiro McQueen",
      "umaId": "mejiro-mcqueen",
      "player": "GohanXGAMER",
      "number": 4,
      "rank": "B+",
      "title": "Finals Champion",
      "strategy": "Pace",
      "gap": "3 L",
      "pop": 4,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mejiro-mcqueen"
    },
    {
      "pos": 5,
      "uma": "Agnes Tachyon",
      "umaId": "agnes-tachyon",
      "player": "Yves",
      "number": 11,
      "rank": "A",
      "title": "Finals Champion",
      "strategy": "Late",
      "gap": "3/4 L",
      "pop": 5,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon"
    }
  ],
  "submittedEntries": [
    { "player": "Agnes", "uma": "Grass Wonder", "umaId": "grass-wonder" },
    { "player": "Agnes", "uma": "Super Creek", "umaId": "super-creek" },
    { "player": "Yves", "uma": "Hishi Amazon", "umaId": "hishi-amazon" },
    { "player": "GohanXGAMER", "uma": "Special Week", "umaId": "special-week" },
    { "player": "GohanXGAMER", "uma": "Symboli Rudolf", "umaId": "symboli-rudolf" },
    { "player": "Cruzi", "uma": "Agnes Tachyon", "umaId": "agnes-tachyon" },
    { "player": "Cruzi", "uma": "Gold Ship", "umaId": "gold-ship" },
    { "player": "Jiinshi", "uma": "Mejiro McQueen", "umaId": "mejiro-mcqueen" },
    { "player": "Jiinshi", "uma": "Narita Taishin", "umaId": "narita-taishin" },
    { "player": "Cyciesta", "uma": "Narita Taishin", "umaId": "narita-taishin" },
    { "player": "Cyciesta", "uma": "Gold Ship", "umaId": "gold-ship" }
  ]
}

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject JSON Data
start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 13 for r in data['races']):
    data['races'].insert(0, suscup13)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

# 2. Patch UI for partialResults

search_1 = "</div>\n                    ${race.images?.length"
replace_1 = "</div>\n                    ${race.partialResults ? '<div style=\"background:var(--warning, #f39c12); color:white; padding:10px; border-radius:5px; font-weight:bold; margin-bottom:15px;\">⚠️ PARTIAL RESULTS AVAILABLE - Only confirmed top placements are shown below.</div>' : ''}\n                    ${race.images?.length"

if "PARTIAL RESULTS AVAILABLE" not in content:
    content = content.replace(search_1, replace_1)

search_2 = "sorted.forEach(p => {"
replace_2 = """if (race.partialResults) {
                    html += '<h3 style="margin-bottom:10px; color:var(--primary);">CONFIRMED RESULTS</h3>';
                }
                sorted.forEach(p => {"""

if "CONFIRMED RESULTS" not in content:
    content = content.replace(search_2, replace_2)

search_3 = "});\n                document.getElementById('race-detail-content').innerHTML = html;"
replace_3 = """});
                if (race.partialResults && race.submittedEntries) {
                    html += '<h3 style="margin-top:20px; margin-bottom:10px; color:var(--text-muted);">RESULTS NOT AVAILABLE (Submitted Entries)</h3>';
                    race.submittedEntries.forEach(entry => {
                        html += `
                            <div class="list-item" style="opacity: 0.6; background: #fafafa;">
                                <div style="font-size:1.8rem; font-weight:900; width:50px; text-align:center; margin-right:15px; color:#aaa;">?</div>
                                ${this.getUmaImage(entry.umaId)}
                                <div class="item-content">
                                    <div class="item-title">${entry.uma}</div>
                                    <div class="item-subtitle">Trainer: ${entry.player} &bull; Official Submitted Entry</div>
                                </div>
                            </div>
                        `;
                    });
                }
                document.getElementById('race-detail-content').innerHTML = html;"""

if "RESULTS NOT AVAILABLE (Submitted Entries)" not in content:
    content = content.replace(search_3, replace_3)

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 13 data and UI patches applied!")
