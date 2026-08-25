import json
import os

suscup21 = {
  "id": 21,
  "cupNumber": "SUS CUP 21",
  "cupName": "Sus Cup 21 - Spark Race",
  "name": "Takamatsunomiya Kinen",
  "date": "Not provided",
  "roomId": "2818 6716",
  "race": "Takamatsunomiya Kinen",
  "course": "Chukyo Turf",
  "surface": "Turf",
  "distance": "1200m",
  "distanceType": "Sprint",
  "direction": "Left",
  "weather": "Sunny",
  "ground": "Firm",
  "mood": "Good",
  "rankLimit": "No Rank Limit",
  "specialRule": "3 entries per participant. Blue Spark format (1x 3★, 1x 2★, 1x 1★)",
  "sparkWinners": {
    "3★ Blue Spark": { "player": "Cyciesta", "uma": "Curren Chan", "pos": 2 },
    "2★ Blue Spark": { "player": "Agnes", "uma": "Taiki Shuttle", "pos": 1 },
    "1★ Blue Spark": { "player": "Jiinxye", "uma": "Sakura Bakushin O", "pos": 4 }
  },
  "images": [],
  "participants": [
    {
      "pos": 1,
      "uma": "Taiki Shuttle",
      "umaId": "taiki-shuttle",
      "player": "Agnes",
      "strategy": "Pace",
      "number": 11,
      "fav": 4,
      "title": "2★ Blue Spark Champion",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/taiki-shuttle"
    },
    {
      "pos": 2,
      "uma": "Curren Chan",
      "umaId": "curren-chan",
      "player": "Cyciesta",
      "strategy": "Pace",
      "number": 9,
      "fav": 2,
      "title": "3★ Blue Spark Champion",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/curren-chan"
    },
    {
      "pos": 3,
      "uma": "Curren Chan",
      "umaId": "curren-chan",
      "player": "Jiinxye",
      "strategy": "Front",
      "number": 15,
      "fav": 12,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/curren-chan"
    },
    {
      "pos": 4,
      "uma": "Sakura Bakushin O",
      "umaId": "sakura-bakushin-o",
      "player": "Jiinxye",
      "strategy": "Front",
      "number": 16,
      "fav": 14,
      "title": "1★ Blue Spark Champion",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/sakura-bakushin-o"
    },
    {
      "pos": 5,
      "uma": "Haru Urara",
      "umaId": "haru-urara",
      "player": "Cyciesta",
      "strategy": "Late",
      "number": 5,
      "fav": 13,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/haru-urara"
    },
    {
      "pos": 6,
      "uma": "Taiki Shuttle",
      "umaId": "taiki-shuttle",
      "player": "Cyciesta",
      "strategy": "Pace",
      "number": 12,
      "fav": 1,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/taiki-shuttle"
    },
    {
      "pos": 7,
      "uma": "Sakura Bakushin O",
      "umaId": "sakura-bakushin-o",
      "player": "Yves",
      "strategy": "Front",
      "number": 4,
      "fav": 5,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/sakura-bakushin-o"
    },
    {
      "pos": 8,
      "uma": "Maruzensky",
      "umaId": "maruzensky",
      "player": "Jiinxye",
      "strategy": "Front",
      "number": 17,
      "fav": 10,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/maruzensky"
    },
    {
      "pos": 9,
      "uma": "Maruzensky",
      "umaId": "maruzensky",
      "player": "Cruzi",
      "strategy": "Front",
      "number": 7,
      "fav": 6,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/maruzensky"
    },
    {
      "pos": 10,
      "uma": "Sakura Bakushin O",
      "umaId": "sakura-bakushin-o",
      "player": "Agnes",
      "strategy": "Front",
      "number": 1,
      "fav": 11,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/sakura-bakushin-o"
    },
    {
      "pos": 11,
      "uma": "Air Groove",
      "umaId": "air-groove",
      "player": "Agnes",
      "strategy": "Pace",
      "number": 18,
      "fav": 9,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/air-groove"
    },
    {
      "pos": 12,
      "uma": "Silence Suzuka",
      "umaId": "silence-suzuka",
      "player": "Cruzi",
      "strategy": "Front",
      "number": 8,
      "fav": 8,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/silence-suzuka"
    },
    {
      "pos": 13,
      "uma": "Pastime Joy",
      "umaId": "pastime-joy",
      "player": "NPC",
      "strategy": "Pace",
      "number": 3,
      "fav": 17,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 14,
      "uma": "Ribbon Virelai",
      "umaId": "ribbon-virelai",
      "player": "NPC",
      "strategy": "Front",
      "number": 2,
      "fav": 15,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 15,
      "uma": "Battle of Elah",
      "umaId": "battle-of-elah",
      "player": "NPC",
      "strategy": "End",
      "number": 14,
      "fav": 16,
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 16,
      "uma": "Oguri Cap",
      "umaId": "oguri-cap",
      "player": "Yves",
      "strategy": "Pace",
      "number": 13,
      "fav": 7,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap"
    },
    {
      "pos": 17,
      "uma": "Smart Falcon",
      "umaId": "smart-falcon",
      "player": "Yves",
      "strategy": "Front",
      "number": 6,
      "fav": 18,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/smart-falcon"
    },
    {
      "pos": 18,
      "uma": "Daiwa Scarlet",
      "umaId": "daiwa-scarlet",
      "player": "Cruzi",
      "strategy": "Pace",
      "number": 10,
      "fav": 3,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/daiwa-scarlet"
    }
  ]
}

folder = 'suscupimages21-30'
for i in range(1, 5):
    filename = f"21.{i}.png"
    if os.path.exists(os.path.join("..", folder, filename)):
        suscup21["images"].append(f"{folder}/{filename}")


with open('../.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

uma_db_addition = ""
if '"pastime-joy"' not in content:
    uma_db_addition += '  "pastime-joy": { id: "pastime-joy", name: "Pastime Joy", type: "NPC", url: null, image: null },\n'
if '"battle-of-elah"' not in content:
    uma_db_addition += '  "battle-of-elah": { id: "battle-of-elah", name: "Battle of Elah", type: "NPC", url: null, image: null },\n'

if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 21 for r in data['races']):
    data['races'].append(suscup21)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('../.vscode/suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 21 data applied!")
