import json

suscup16 = {
  "id": 16,
  "cupNumber": "SUS CUP 16 - Mixed Class Race",
  "cupName": "Sus Cup 16",
  "name": "Oka Sho",
  "date": "16 November 2025, 18:31",
  "roomId": "3647 0681",
  "race": "Oka Sho",
  "course": "Hanshin Turf",
  "surface": "Turf",
  "distance": "1600m",
  "distanceType": "Mile",
  "direction": "Right",
  "weather": "Sunny",
  "ground": "Firm",
  "mood": "Good",
  "rankLimit": "Not specified",
  "specialRule": "Mixed Class Race",
  "images": [
    "16.1.png", "16.2.png", "16.3.png", "16.4.png"
  ],
  "participants": [
    {
      "pos": 1,
      "uma": "Vodka",
      "umaId": "vodka",
      "player": "Agnes",
      "number": 14,
      "rank": "A+",
      "title": "Finals Champion",
      "strategy": "Late",
      "time": "1:29.9",
      "pop": 8,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/vodka"
    },
    {
      "pos": 2,
      "uma": "Oguri Cap",
      "umaId": "oguri-cap",
      "player": "GohanXGAMER",
      "number": 5,
      "rank": "A+",
      "title": "Ideal Idol",
      "strategy": "Pace",
      "gap": "1 1/2 L",
      "pop": 3,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap"
    },
    {
      "pos": 3,
      "uma": "Silence Suzuka",
      "umaId": "silence-suzuka",
      "player": "GohanXGAMER",
      "number": 9,
      "rank": "A",
      "title": "Witness to Legend",
      "strategy": "Front",
      "gap": "Neck",
      "pop": 4,
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/silence-suzuka"
    },
    { "pos": 4, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "Jiinxye", "number": 6, "rank": "B+", "title": "The GOAT", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap" },
    { "pos": 5, "uma": "Hishi Amazon", "umaId": "hishi-amazon", "player": "Yves", "number": 18, "rank": "A", "title": "Queen of the Amazons", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/hishi-amazon" },
    { "pos": 6, "uma": "El Condor Pasa", "umaId": "el-condor-pasa", "player": "Cruzi", "number": 15, "rank": "B+", "title": "Finals Champion", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/el-condor-pasa" },
    { "pos": 7, "uma": "Silence Suzuka", "umaId": "silence-suzuka", "player": "Cruzi", "number": 12, "rank": "A+", "title": "Otherworldly Front-Runner", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/silence-suzuka" },
    { "pos": 8, "uma": "Sakura Bakushin O", "umaId": "sakura-bakushin-o", "player": "Agnes", "number": 3, "rank": "B+", "title": "Undefeated", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/sakura-bakushin-o" },
    { "pos": 9, "uma": "Narita Brian", "umaId": "narita-brian", "player": "Jiinxye", "number": 2, "rank": "A+", "title": "Way of Kings", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/narita-brian" },
    { "pos": 10, "uma": "Silence Suzuka", "umaId": "silence-suzuka", "player": "Yves", "number": 8, "rank": "B+", "title": "Steamy Solidarity", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/silence-suzuka" },
    { "pos": 11, "uma": "Book of Sugar", "player": "NPC", "number": 11, "rank": "B", "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 12, "uma": "El Condor Pasa", "umaId": "el-condor-pasa", "player": "Agnes", "number": 7, "rank": "A", "title": "Phantom Bird", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/el-condor-pasa" },
    { "pos": 13, "uma": "Grass Wonder", "umaId": "grass-wonder", "player": "GohanXGAMER", "number": 16, "rank": "B+", "title": "Steamy Solidarity", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/grass-wonder" },
    { "pos": 14, "uma": "Smart Falcon", "umaId": "smart-falcon", "player": "Yves", "number": 4, "rank": "A+", "title": "Epoch Pioneer", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/smart-falcon" },
    { "pos": 15, "uma": "Pan Pacific", "player": "NPC", "number": 17, "rank": "B", "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 16, "uma": "Grass Wonder", "umaId": "grass-wonder", "player": "Cruzi", "number": 1, "rank": "A", "title": "Witness to Legend", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/grass-wonder" },
    { "pos": 17, "uma": "Maruzensky (Summer)", "umaId": "maruzensky-summer", "player": "Jiinxye", "number": 10, "rank": "A", "title": "Finals Champion", "version": "Summer Variant", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/maruzensky" },
    { "pos": 18, "uma": "Mihono Bourbon", "umaId": "mihono-bourbon", "player": "Ananth", "number": 13, "rank": "B+", "title": "Finals Champion", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/mihono-bourbon" }
  ]
}

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ADD UMAS IF NOT EXISTS
import re

uma_db_addition = ""
if '"narita-brian"' not in content:
    uma_db_addition += '  "narita-brian": { name: "Narita Brian", url: "https://gametora.com/umamusume/characters/narita-brian", image: "https://gametora.com/images/umamusume/characters/chara_stand_1007_100701.png" },\n'
if '"maruzensky-summer"' not in content:
    uma_db_addition += '  "maruzensky-summer": { name: "Maruzensky (Summer)", url: "https://gametora.com/umamusume/characters/maruzensky", image: "https://gametora.com/images/umamusume/characters/chara_stand_1004_100402.png" },\n'

if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

# ADD RACE DATA
start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 16 for r in data['races']):
    data['races'].insert(0, suscup16)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 16 data applied!")
