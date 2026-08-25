import json

suscup19 = {
  "id": 19,
  "cupNumber": "SUS CUP 19",
  "cupName": "Sus Cup 19 - Gold Skills",
  "name": "Tenno Sho (Autumn)",
  "date": "30 December 2025, 18:31",
  "roomId": "6799 5179",
  "race": "Tenno Sho (Autumn)",
  "course": "Tokyo Turf",
  "surface": "Turf",
  "distance": "2000m",
  "distanceType": "Medium",
  "direction": "Left",
  "weather": "Rainy",
  "ground": "Soft",
  "mood": "Good",
  "rankLimit": "No Rank Limit",
  "specialRule": "0 Gold Skill, 1-2 Gold Skill, Gold Skill Only",
  "images": [],
  "participants": [
    {
      "pos": 1,
      "uma": "Gold City",
      "umaId": "gold-city",
      "player": "Ananth",
      "number": 6,
      "rank": "A+",
      "title": "Dream Team",
      "strategy": "Pace",
      "time": "1:56.8",
      "pop": 6,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/gold-city"
    },
    {
      "pos": 2,
      "uma": "T.M. Opera O",
      "umaId": "t-m-opera-o",
      "player": "Jiinxye",
      "number": 4,
      "rank": "A+",
      "title": "Team Player Star Slayer",
      "strategy": "Late",
      "gap": "3/4 L",
      "pop": 7,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/t-m-opera-o"
    },
    {
      "pos": 3,
      "uma": "Agnes Tachyon",
      "umaId": "agnes-tachyon",
      "player": "Agnes",
      "number": 13,
      "rank": "A+",
      "title": "Faster than Light",
      "strategy": "Pace",
      "gap": "3 L",
      "pop": 1,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon"
    },
    {
      "pos": 4,
      "uma": "Gold Ship",
      "umaId": "gold-ship",
      "player": "Cruzi",
      "number": 18,
      "rank": "A+",
      "title": "Dream Team",
      "strategy": "End",
      "gap": "Nose",
      "pop": 11,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/gold-ship"
    },
    {
      "pos": 5,
      "uma": "Gold Ship",
      "umaId": "gold-ship",
      "player": "Ananth",
      "number": 15,
      "rank": "A+",
      "title": "Witness to Legend",
      "strategy": "End",
      "gap": "Neck",
      "pop": 8,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/gold-ship"
    },
    {
      "pos": 6,
      "uma": "Gold Ship",
      "umaId": "gold-ship",
      "player": "Jiinxye",
      "number": 12,
      "rank": "A+",
      "title": "Witness to Legend",
      "strategy": "End",
      "gap": "Head",
      "pop": 3,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/gold-ship"
    },
    {
      "pos": 7,
      "uma": "Mayano Top Gun",
      "umaId": "mayano-top-gun",
      "player": "Cruzi",
      "number": 11,
      "rank": "A+",
      "title": "Witness to Legend",
      "strategy": "Late",
      "gap": "1 1/4 L",
      "pop": 2,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mayano-top-gun"
    },
    {
      "pos": 8,
      "uma": "Oguri Cap",
      "umaId": "oguri-cap",
      "player": "Jiinxye",
      "number": 5,
      "rank": "A+",
      "title": "Ideal Idol",
      "strategy": "Pace",
      "gap": "Head",
      "pop": 12,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap"
    },
    {
      "pos": 9,
      "uma": "Daiwa Scarlet",
      "umaId": "daiwa-scarlet",
      "player": "Agnes",
      "number": 8,
      "rank": "A+",
      "title": "Miss Perfect",
      "strategy": "Front",
      "gap": "1 1/2 L",
      "pop": 10,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/daiwa-scarlet"
    },
    {
      "pos": 10,
      "uma": "Seiun Sky",
      "umaId": "seiun-sky",
      "player": "Cruzi",
      "number": 1,
      "rank": "A+",
      "title": "Dream Team",
      "strategy": "Front",
      "gap": "Neck",
      "pop": 4,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/seiun-sky"
    },
    {
      "pos": 11,
      "uma": "Winning Ticket",
      "umaId": "winning-ticket",
      "player": "Agnes",
      "number": 14,
      "rank": "A+",
      "title": "Steamy Solidarity",
      "strategy": "Late",
      "gap": "2 1/2 L",
      "pop": 9,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/winning-ticket"
    },
    {
      "pos": 12,
      "uma": "Mejiro McQueen",
      "umaId": "mejiro-mcqueen",
      "player": "Ananth",
      "number": 7,
      "rank": "A+",
      "title": "Witness to Legend",
      "strategy": "Pace",
      "gap": "2 1/2 L",
      "pop": 5,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mejiro-mcqueen"
    },
    {
      "pos": 13,
      "uma": "Gray Chouchou",
      "umaId": "gray-chouchou",
      "player": "NPC",
      "number": 2,
      "rank": "B",
      "strategy": "Pace",
      "gap": "3 L",
      "pop": 15,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 14,
      "uma": "Jagdplatte",
      "umaId": "jagdplatte",
      "player": "NPC",
      "number": 9,
      "rank": "B",
      "strategy": "End",
      "gap": "1/2 L",
      "pop": 16,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 15,
      "uma": "Mini Narcissus",
      "umaId": "mini-narcissus",
      "player": "NPC",
      "number": 10,
      "rank": "B",
      "strategy": "Late",
      "gap": "3/4 L",
      "pop": 18,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 16,
      "uma": "Turcke",
      "umaId": "turcke",
      "player": "NPC",
      "number": 16,
      "rank": "B",
      "strategy": "Pace",
      "gap": "1 1/2 L",
      "pop": 14,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 17,
      "uma": "Gran Shamal",
      "umaId": "gran-shamal",
      "player": "NPC",
      "number": 17,
      "rank": "B",
      "strategy": "Late",
      "gap": "Nose",
      "pop": 13,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 18,
      "uma": "Circuit Breaker",
      "umaId": "circuit-breaker",
      "player": "NPC",
      "number": 3,
      "rank": "B",
      "strategy": "Front",
      "gap": "4 L",
      "pop": 17,
      "version": "NPC",
      "participantType": "NPC Uma"
    }
  ]
}

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

uma_db_addition = ""
if '"gold-city"' not in content:
    uma_db_addition += '  "gold-city": { name: "Gold City", url: "https://gametora.com/umamusume/characters/gold-city", image: "https://gametora.com/images/umamusume/characters/chara_stand_1040_104001.png" },\n'
if '"gray-chouchou"' not in content:
    uma_db_addition += '  "gray-chouchou": { id: "gray-chouchou", name: "Gray Chouchou", type: "NPC", url: null, image: null },\n'
if '"jagdplatte"' not in content:
    uma_db_addition += '  "jagdplatte": { id: "jagdplatte", name: "Jagdplatte", type: "NPC", url: null, image: null },\n'
if '"mini-narcissus"' not in content:
    uma_db_addition += '  "mini-narcissus": { id: "mini-narcissus", name: "Mini Narcissus", type: "NPC", url: null, image: null },\n'
if '"turcke"' not in content:
    uma_db_addition += '  "turcke": { id: "turcke", name: "Turcke", type: "NPC", url: null, image: null },\n'
if '"gran-shamal"' not in content:
    uma_db_addition += '  "gran-shamal": { id: "gran-shamal", name: "Gran Shamal", type: "NPC", url: null, image: null },\n'
if '"circuit-breaker"' not in content:
    uma_db_addition += '  "circuit-breaker": { id: "circuit-breaker", name: "Circuit Breaker", type: "NPC", url: null, image: null },\n'


if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 19 for r in data['races']):
    data['races'].append(suscup19)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 19 data applied!")
