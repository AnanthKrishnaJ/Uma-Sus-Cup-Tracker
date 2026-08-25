import json
import os

suscup20 = {
  "id": 20,
  "cupNumber": "SUS CUP 20",
  "cupName": "Sus Cup 20 - All Style",
  "name": "Tenno Sho (Autumn)",
  "date": "01 January 2026, 18:51",
  "roomId": "2003 3988",
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
  "specialRule": "1 runner for each style, Unique runners only, 3 entries per person",
  "styleWinners": {
    "Front": { "player": "Ananth", "uma": "Mihono Bourbon", "pos": 11 },
    "Pace": { "player": "Cyciesta", "uma": "Mejiro McQueen", "pos": 1 },
    "Late": { "player": "Yves", "uma": "Eishin Flash", "pos": 2 },
    "End": { "player": "Yves", "uma": "Mayano Top Gun", "pos": 3 }
  },
  "images": [],
  "participants": [
    {
      "pos": 1,
      "uma": "Mejiro McQueen",
      "umaId": "mejiro-mcqueen",
      "player": "Cyciesta",
      "strategy": "Pace",
      "title": "Pace Style Winner",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mejiro-mcqueen"
    },
    {
      "pos": 2,
      "uma": "Eishin Flash",
      "umaId": "eishin-flash",
      "player": "Yves",
      "strategy": "Late",
      "title": "Late Style Winner",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/eishin-flash"
    },
    {
      "pos": 3,
      "uma": "Mayano Top Gun",
      "umaId": "mayano-top-gun",
      "player": "Yves",
      "strategy": "End",
      "title": "End Style Winner",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mayano-top-gun"
    },
    {
      "pos": 4,
      "uma": "Agnes Digital",
      "umaId": "agnes-digital",
      "player": "Cruzi",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/agnes-digital"
    },
    {
      "pos": 5,
      "uma": "Narita Taishin",
      "umaId": "narita-taishin",
      "player": "Cyciesta",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/narita-taishin"
    },
    {
      "pos": 6,
      "uma": "Gold City",
      "umaId": "gold-city",
      "player": "Ananth",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/gold-city"
    },
    {
      "pos": 7,
      "uma": "Symboli Rudolf",
      "umaId": "symboli-rudolf",
      "player": "Cyciesta",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/symboli-rudolf"
    },
    {
      "pos": 8,
      "uma": "Agnes Tachyon",
      "umaId": "agnes-tachyon",
      "player": "Agnes",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon"
    },
    {
      "pos": 9,
      "uma": "Mejiro Ryan",
      "umaId": "mejiro-ryan",
      "player": "Ananth",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mejiro-ryan"
    },
    {
      "pos": 10,
      "uma": "Gold Ship",
      "umaId": "gold-ship",
      "player": "Cruzi",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/gold-ship"
    },
    {
      "pos": 11,
      "uma": "Mihono Bourbon",
      "umaId": "mihono-bourbon",
      "player": "Ananth",
      "strategy": "Front",
      "title": "Front Style Winner",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/mihono-bourbon"
    },
    {
      "pos": 12,
      "uma": "Meisho Doto",
      "umaId": "meisho-doto",
      "player": "Yves",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/meisho-doto"
    },
    {
      "pos": 13,
      "uma": "King Halo",
      "umaId": "king-halo",
      "player": "Agnes",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/king-halo"
    },
    {
      "pos": 14,
      "uma": "Silence Suzuka",
      "umaId": "silence-suzuka",
      "player": "Agnes",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/silence-suzuka"
    },
    {
      "pos": 15,
      "uma": "Seiun Sky",
      "umaId": "seiun-sky",
      "player": "Cruzi",
      "version": "Original / Default",
      "participantType": "Playable Uma",
      "characterUrl": "https://gametora.com/umamusume/characters/seiun-sky"
    },
    {
      "pos": 16,
      "uma": "Neptunus",
      "umaId": "neptunus",
      "player": "NPC",
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 17,
      "uma": "Maleficus",
      "umaId": "maleficus",
      "player": "NPC",
      "version": "NPC",
      "participantType": "NPC Uma"
    },
    {
      "pos": 18,
      "uma": "Ribbon Virelai",
      "umaId": "ribbon-virelai",
      "player": "NPC",
      "version": "NPC",
      "participantType": "NPC Uma"
    }
  ]
}

folder = 'suscupimages11-20'
for i in range(1, 5):
    filename = f"20.{i}.png"
    if os.path.exists(os.path.join(folder, filename)):
        suscup20["images"].append(f"{folder}/{filename}")


with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

uma_db_addition = ""
if '"eishin-flash"' not in content:
    uma_db_addition += '  "eishin-flash": { name: "Eishin Flash", url: "https://gametora.com/umamusume/characters/eishin-flash", image: "https://gametora.com/images/umamusume/characters/chara_stand_1032_103201.png" },\n'
if '"mejiro-ryan"' not in content:
    uma_db_addition += '  "mejiro-ryan": { name: "Mejiro Ryan", url: "https://gametora.com/umamusume/characters/mejiro-ryan", image: "https://gametora.com/images/umamusume/characters/chara_stand_1027_102701.png" },\n'
if '"meisho-doto"' not in content:
    uma_db_addition += '  "meisho-doto": { name: "Meisho Doto", url: "https://gametora.com/umamusume/characters/meisho-doto", image: "https://gametora.com/images/umamusume/characters/chara_stand_1058_105801.png" },\n'
if '"neptunus"' not in content:
    uma_db_addition += '  "neptunus": { id: "neptunus", name: "Neptunus", type: "NPC", url: null, image: null },\n'
if '"ribbon-virelai"' not in content:
    uma_db_addition += '  "ribbon-virelai": { id: "ribbon-virelai", name: "Ribbon Virelai", type: "NPC", url: null, image: null },\n'

if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 20 for r in data['races']):
    data['races'].append(suscup20)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 20 data applied!")
