import json

suscup15 = {
  "id": 15,
  "cupNumber": "SUS CUP 15 - Triple Front Runners",
  "cupName": "Sus Cup 15",
  "name": "G1 Takarazuka Kinen",
  "date": "Not specified",
  "roomId": "8401 3487",
  "race": "G1 Takarazuka Kinen",
  "course": "Hanshin Turf",
  "surface": "Turf",
  "distance": "2200m",
  "distanceType": "Medium",
  "direction": "Right / Inner",
  "weather": "Random",
  "ground": "Random",
  "mood": "Random",
  "rankLimit": "Not specified",
  "specialRule": "Triple Front Runners",
  "images": [
    "15.1.png", "15.2.png", "15.3.png", "15.4.png"
  ],
  "participants": [
    {
      "pos": 1,
      "uma": "Silence Suzuka",
      "umaId": "silence-suzuka",
      "player": "Agnes",
      "number": 9,
      "rank": "A",
      "title": "Legendary Diva",
      "strategy": "Front",
      "time": "2:11.1",
      "pop": 6,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/silence-suzuka"
    },
    {
      "pos": 2,
      "uma": "Maruzensky",
      "umaId": "maruzensky",
      "player": "Cyciesta",
      "number": 10,
      "rank": "A",
      "title": "The GOAT",
      "strategy": "Front",
      "gap": "2 L",
      "pop": 3,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/maruzensky"
    },
    {
      "pos": 3,
      "uma": "Daiwa Scarlet",
      "umaId": "daiwa-scarlet",
      "player": "Agnes",
      "number": 11,
      "rank": "A",
      "title": "The GOAT",
      "strategy": "Front",
      "gap": "3/4 L",
      "pop": 1,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/daiwa-scarlet"
    },
    {
      "pos": 4,
      "uma": "Daiwa Scarlet",
      "umaId": "daiwa-scarlet",
      "player": "Cyciesta",
      "number": 15,
      "rank": "A",
      "title": "Legendary Diva",
      "strategy": "Front",
      "gap": "1 3/4 L",
      "pop": 2,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/daiwa-scarlet"
    },
    {
      "pos": 5,
      "uma": "Mayano Top Gun",
      "umaId": "mayano-top-gun",
      "player": "Ananth",
      "number": 14,
      "rank": "B+",
      "title": "Finals Champion",
      "strategy": "Front",
      "gap": "2 1/2 L",
      "pop": 7,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mayano-top-gun"
    },
    {
      "pos": 6,
      "uma": "Mayano Top Gun",
      "umaId": "mayano-top-gun",
      "player": "Agnes",
      "number": 3,
      "rank": "A",
      "title": "Free Spirit",
      "strategy": "Front",
      "gap": "1 L",
      "pop": 4,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mayano-top-gun"
    },
    { "pos": 7, "uma": "Ribbon Lullaby", "player": "NPC", "number": 5, "rank": "C+", "strategy": "Late", "gap": "7 L", "pop": 13, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 8, "uma": "Chalemie Rhythm", "player": "NPC", "number": 6, "rank": "C+", "strategy": "Pace", "gap": "1 L", "pop": 12, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 9, "uma": "Shout My Name", "player": "NPC", "number": 16, "rank": "C+", "strategy": "End", "gap": "1/2 L", "pop": 17, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 10, "uma": "Weiss Grimoire", "player": "NPC", "number": 17, "rank": "C+", "strategy": "Front", "gap": "1 1/2 L", "pop": 9, "version": "NPC", "participantType": "NPC Uma" },
    {
      "pos": 11,
      "uma": "Mihono Bourbon",
      "umaId": "mihono-bourbon",
      "player": "Cyciesta",
      "number": 8,
      "rank": "A+",
      "title": "Finals Champion",
      "strategy": "Front",
      "gap": "1/2 L",
      "pop": 5,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mihono-bourbon"
    },
    { "pos": 12, "uma": "Cymbal Rhythm", "player": "NPC", "number": 1, "rank": "C+", "strategy": "Pace", "gap": "Neck", "pop": 11, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 13, "uma": "Salsa Step", "player": "NPC", "number": 2, "rank": "C+", "strategy": "Late", "gap": "Neck", "pop": 15, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 14, "uma": "Thousand Voltaire", "player": "NPC", "number": 13, "rank": "C+", "strategy": "Pace", "gap": "Neck", "pop": 8, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 15, "uma": "Spring Happy", "player": "NPC", "number": 4, "rank": "C+", "strategy": "Late", "gap": "1/2 L", "pop": 16, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 16, "uma": "Faster than Ray", "player": "NPC", "number": 12, "rank": "C+", "strategy": "End", "gap": "Nose", "pop": 14, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 17, "uma": "Izcalli", "player": "NPC", "number": 7, "rank": "C+", "strategy": "Front", "gap": "Head", "pop": 18, "version": "NPC", "participantType": "NPC Uma" },
    {
      "pos": 18,
      "uma": "Smart Falcon",
      "umaId": "smart-falcon",
      "player": "Ananth",
      "number": 18,
      "rank": "B+",
      "title": "Sand Falcon",
      "strategy": "Front",
      "gap": "1 1/2 L",
      "pop": 10,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/smart-falcon"
    }
  ]
}

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 15 for r in data['races']):
    data['races'].insert(0, suscup15)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 15 data applied!")
