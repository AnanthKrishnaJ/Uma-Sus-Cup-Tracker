import json

suscup11 = {
  "id": 11,
  "cupNumber": "SUS CUP 11 - GP ROUND 3/3",
  "cupName": "Sus Cup 11",
  "name": "Japan Cup",
  "date": "21 September 2025, 19:03",
  "roomId": "3936 9926",
  "race": "Japan Cup",
  "course": "Tokyo Turf",
  "surface": "Turf",
  "distance": "2400m",
  "distanceType": "Medium",
  "direction": "Left",
  "weather": "Random",
  "ground": "Random",
  "mood": "Random",
  "rankLimit": "No Rank Limit",
  "specialRule": "GP Round 3/3",
  "images": [
    "11.1.png", "11.2.png", "11.3.png", "11.4.png"
  ],
  "participants": [
    {
      "pos": 1,
      "uma": "Narita Taishin",
      "umaId": "narita-taishin",
      "player": "Cyciesta",
      "number": 1,
      "rank": "A",
      "title": "The GOAT",
      "strategy": "End",
      "time": "2:21.4",
      "pop": 2,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/narita-taishin"
    },
    {
      "pos": 2,
      "uma": "Symboli Rudolf",
      "umaId": "symboli-rudolf",
      "player": "Cyciesta",
      "number": 11,
      "rank": "A+",
      "title": "Emperor",
      "strategy": "Pace",
      "gap": "1 1/4 L",
      "pop": 1,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/symboli-rudolf"
    },
    {
      "pos": 3,
      "uma": "El Condor Pasa",
      "umaId": "el-condor-pasa",
      "player": "Agnes",
      "number": 4,
      "rank": "A",
      "title": "Finals Champion",
      "strategy": "Late",
      "gap": "2 L",
      "pop": 3,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/el-condor-pasa"
    },
    {
      "pos": 4,
      "uma": "Grass Wonder",
      "umaId": "grass-wonder",
      "player": "Agnes",
      "number": 17,
      "rank": "A",
      "title": "Steamy Solidarity",
      "strategy": "Late",
      "gap": "1 L",
      "pop": 4,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/grass-wonder"
    },
    {
      "pos": 5,
      "uma": "Tokai Teio",
      "umaId": "tokai-teio-beyond-the-horizon",
      "player": "Jiinxye",
      "number": 8,
      "rank": "A",
      "title": "Finals Champion",
      "strategy": "Pace",
      "gap": "1 1/4 L",
      "pop": 9,
      "version": "Beyond the Horizon Variant",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/tokai-teio"
    },
    {
      "pos": 6,
      "uma": "Oguri Cap",
      "umaId": "oguri-cap",
      "player": "GohanXGAMER",
      "number": 13,
      "rank": "A",
      "title": "Ideal Idol",
      "strategy": "Pace",
      "gap": "1/2 L",
      "pop": 5,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap"
    },
    {
      "pos": 7,
      "uma": "Agnes Tachyon",
      "umaId": "agnes-tachyon",
      "player": "Cruzi",
      "number": 14,
      "rank": "A",
      "title": "Finals Champion",
      "strategy": "Pace",
      "gap": "4 L",
      "pop": 7,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon"
    },
    {
      "pos": 8,
      "uma": "Super Creek",
      "umaId": "super-creek",
      "player": "GohanXGAMER",
      "number": 5,
      "rank": "B+",
      "title": "Way of Kings",
      "strategy": "Pace",
      "gap": "3 L",
      "pop": 11,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/super-creek"
    },
    {
      "pos": 9,
      "uma": "Mejiro McQueen",
      "umaId": "mejiro-mcqueen",
      "player": "Ananth",
      "number": 16,
      "rank": "B+",
      "title": "The GOAT",
      "strategy": "Pace",
      "gap": "3/4 L",
      "pop": 10,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mejiro-mcqueen"
    },
    {
      "pos": 10,
      "uma": "T.M. Opera O",
      "umaId": "t-m-opera-o",
      "player": "Jiinxye",
      "number": 12,
      "rank": "A",
      "title": "Undefeated",
      "strategy": "Pace",
      "gap": "1 1/4 L",
      "pop": 6,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/t-m-opera-o"
    },
    { "pos": 11, "uma": "Encore One More", "player": "NPC", "number": 9, "rank": "C+", "strategy": "Pace", "gap": "1 3/4 L", "pop": 16, "version": "NPC", "participantType": "NPC Uma" },
    {
      "pos": 12,
      "uma": "Seiun Sky",
      "umaId": "seiun-sky",
      "player": "Cruzi",
      "number": 15,
      "rank": "A",
      "title": "The GOAT",
      "strategy": "Front",
      "gap": "1 L",
      "pop": 8,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/seiun-sky"
    },
    { "pos": 13, "uma": "Sidecar", "player": "NPC", "number": 10, "rank": "B", "strategy": "Late", "gap": "1/2 L", "pop": 14, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 14, "uma": "Chalemie Rhythm", "player": "NPC", "number": 6, "rank": "C+", "strategy": "End", "gap": "Head", "pop": 13, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 15, "uma": "Mechanical Vapor", "player": "NPC", "number": 18, "rank": "B", "strategy": "Front", "gap": "1 L", "pop": 12, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 16, "uma": "Aeneas", "player": "NPC", "number": 7, "rank": "C+", "strategy": "Late", "gap": "2 L", "pop": 17, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 17, "uma": "Leaf Leaf", "player": "NPC", "number": 3, "rank": "C+", "strategy": "Pace", "gap": "1/2 L", "pop": 15, "version": "NPC", "participantType": "NPC Uma" },
    {
      "pos": 18,
      "uma": "Curren Chan",
      "umaId": "curren-chan",
      "player": "Ananth",
      "number": 2,
      "rank": "B+",
      "title": "Finals Champion",
      "strategy": "Front",
      "gap": "Distance",
      "pop": 18,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/curren-chan"
    }
  ]
}

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

uma_db_addition = ""
if '"tokai-teio-beyond-the-horizon"' not in content:
    uma_db_addition += '  "tokai-teio-beyond-the-horizon": { name: "Tokai Teio (Beyond the Horizon)", url: "https://gametora.com/umamusume/characters/tokai-teio", image: "https://gametora.com/images/umamusume/characters/chara_stand_1003_100302.png" },\n'

if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

# Add Sus Cup 11 based on ID ordering
if not any(r.get('id') == 11 for r in data['races']):
    # Find correct insertion index (descending order by ID usually, so insert after 12)
    insert_idx = len(data['races'])
    for i, r in enumerate(data['races']):
        if r['id'] < 11:
            insert_idx = i
            break
    data['races'].insert(insert_idx, suscup11)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 11 data applied!")
