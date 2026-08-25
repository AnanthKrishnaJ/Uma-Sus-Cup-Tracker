import json

suscup18 = {
  "id": 18,
  "cupNumber": "SUS CUP 18",
  "cupName": "Sus Cup 18 - SSR Race",
  "name": "Kikuka Sho",
  "date": "20 December 2025, 19:03",
  "roomId": "9022 4218",
  "race": "Kikuka Sho",
  "course": "Kyoto Turf",
  "surface": "Turf",
  "distance": "3000m",
  "distanceType": "Long",
  "direction": "Right / Outer",
  "weather": "Cloudy",
  "ground": "Good",
  "mood": "Good",
  "rankLimit": "No Rank Limit",
  "specialRule": "1 Single SSR, 1 Double SSR, 1 Triple SSR",
  "images": [],
  "participants": [
    {
      "pos": 1,
      "uma": "Nice Nature",
      "umaId": "nice-nature",
      "player": "GohanXGAMER",
      "number": 7,
      "rank": "A",
      "title": "Witness to Legend",
      "strategy": "Late",
      "time": "3:02.2",
      "pop": 2,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/nice-nature"
    },
    {
      "pos": 2,
      "uma": "Nice Nature",
      "umaId": "nice-nature",
      "player": "Ananth",
      "number": 13,
      "rank": "A",
      "title": "Witness to Legend",
      "strategy": "Pace",
      "gap": "1 L",
      "pop": 6,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/nice-nature"
    },
    {
      "pos": 3,
      "uma": "Nice Nature",
      "umaId": "nice-nature",
      "player": "Agnes",
      "number": 16,
      "rank": "A",
      "title": "Undefeated",
      "strategy": "Late",
      "gap": "2 L",
      "pop": 9,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/nice-nature"
    },
    {
      "pos": 4,
      "uma": "Gold Ship",
      "umaId": "gold-ship",
      "player": "Cruzi",
      "number": 12,
      "rank": "A+",
      "title": "Witness to Legend",
      "strategy": "End",
      "gap": "Nose",
      "pop": 3,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/gold-ship"
    },
    {
      "pos": 5,
      "uma": "Winning Ticket",
      "umaId": "winning-ticket",
      "player": "Agnes",
      "number": 8,
      "rank": "A",
      "title": "Steamy Solidarity",
      "strategy": "Late",
      "gap": "1 1/2 L",
      "pop": 7,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/winning-ticket"
    },
    {
      "pos": 6,
      "uma": "T.M. Opera O",
      "umaId": "t-m-opera-o",
      "player": "Yves",
      "number": 10,
      "rank": "A+",
      "title": "G1 Hunter",
      "strategy": "Pace",
      "gap": "1 1/4 L",
      "pop": 8,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/t-m-opera-o"
    },
    {
      "pos": 7,
      "uma": "Matikanefukukitaru",
      "umaId": "matikanefukukitaru",
      "player": "GohanXGAMER",
      "number": 14,
      "rank": "A+",
      "title": "Witness to Legend",
      "strategy": "Late",
      "gap": "Nose",
      "pop": 1,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/matikanefukukitaru"
    },
    {
      "pos": 8,
      "uma": "Mayano Top Gun",
      "umaId": "mayano-top-gun",
      "player": "Cruzi",
      "number": 6,
      "rank": "A+",
      "title": "Witness to Legend",
      "strategy": "Late",
      "gap": "3/4 L",
      "pop": 4,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mayano-top-gun"
    },
    {
      "pos": 9,
      "uma": "Mayano Top Gun",
      "umaId": "mayano-top-gun",
      "player": "Yves",
      "number": 4,
      "rank": "A",
      "title": "Finals Champion",
      "strategy": "Pace",
      "gap": "4 L",
      "pop": 13,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mayano-top-gun"
    },
    {
      "pos": 10,
      "uma": "Biwa Hayahide",
      "umaId": "biwa-hayahide",
      "player": "Agnes",
      "number": 1,
      "rank": "A",
      "title": "Team Player",
      "strategy": "Pace",
      "gap": "3 L",
      "pop": 11,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/biwa-hayahide"
    },
    {
      "pos": 11,
      "uma": "Agnes Tachyon",
      "umaId": "agnes-tachyon",
      "player": "Ananth",
      "number": 2,
      "rank": "A+",
      "title": "Witness to Legend",
      "strategy": "Late",
      "gap": "2 1/2 L",
      "pop": 5,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon"
    },
    {
      "pos": 12,
      "uma": "Symboli Rudolf",
      "umaId": "symboli-rudolf",
      "player": "Yves",
      "number": 3,
      "rank": "A",
      "title": "Legendary Diva",
      "strategy": "Pace",
      "gap": "3/4 L",
      "pop": 14,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/symboli-rudolf"
    },
    {
      "pos": 13,
      "uma": "Torch and Book",
      "umaId": "torch-and-book",
      "player": "NPC",
      "number": 9,
      "rank": "B",
      "strategy": "Pace",
      "gap": "8 L",
      "pop": 16,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 14,
      "uma": "Set Your Record",
      "umaId": "set-your-record",
      "player": "NPC",
      "number": 18,
      "rank": "B",
      "strategy": "Pace",
      "gap": "5 L",
      "pop": 17,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 15,
      "uma": "Grass Wonder",
      "umaId": "grass-wonder",
      "player": "Ananth",
      "number": 17,
      "rank": "A",
      "title": "Witness to Legend",
      "strategy": "Late",
      "gap": "1 L",
      "pop": 10,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/grass-wonder"
    },
    {
      "pos": 16,
      "uma": "Breeze Glider",
      "umaId": "breeze-glider",
      "player": "NPC",
      "number": 5,
      "rank": "B",
      "strategy": "Front",
      "gap": "Head",
      "pop": 18,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 17,
      "uma": "Symboli Rudolf",
      "umaId": "symboli-rudolf",
      "player": "Cruzi",
      "number": 11,
      "rank": "A",
      "title": "Witness to Legend",
      "strategy": "Late",
      "gap": "Distance",
      "pop": 12,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/symboli-rudolf"
    },
    {
      "pos": 18,
      "uma": "Out of Black",
      "umaId": "out-of-black",
      "player": "NPC",
      "number": 15,
      "rank": "B",
      "strategy": "Front",
      "gap": "Head",
      "pop": 15,
      "version": "NPC",
      "participantType": "NPC Uma"
    }
  ]
}

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

uma_db_addition = ""
if '"winning-ticket"' not in content:
    uma_db_addition += '  "winning-ticket": { name: "Winning Ticket", url: "https://gametora.com/umamusume/characters/winning-ticket", image: "https://gametora.com/images/umamusume/characters/chara_stand_1035_103501.png" },\n'
if '"matikanefukukitaru"' not in content:
    uma_db_addition += '  "matikanefukukitaru": { name: "Matikanefukukitaru", url: "https://gametora.com/umamusume/characters/matikanefukukitaru", image: "https://gametora.com/images/umamusume/characters/chara_stand_1056_105601.png" },\n'
if '"torch-and-book"' not in content:
    uma_db_addition += '  "torch-and-book": { id: "torch-and-book", name: "Torch and Book", type: "NPC", url: null, image: null },\n'
if '"set-your-record"' not in content:
    uma_db_addition += '  "set-your-record": { id: "set-your-record", name: "Set Your Record", type: "NPC", url: null, image: null },\n'
if '"breeze-glider"' not in content:
    uma_db_addition += '  "breeze-glider": { id: "breeze-glider", name: "Breeze Glider", type: "NPC", url: null, image: null },\n'
if '"out-of-black"' not in content:
    uma_db_addition += '  "out-of-black": { id: "out-of-black", name: "Out of Black", type: "NPC", url: null, image: null },\n'

if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 18 for r in data['races']):
    data['races'].append(suscup18)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 18 data applied!")
