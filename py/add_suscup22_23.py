import json
import os

suscup22 = {
  "id": 22,
  "cupNumber": "SUS CUP 22",
  "cupName": "Sus Cup 22 - Cross Career Race",
  "name": "Tenno Sho (Spring)",
  "date": "15 March 2026, 18:30",
  "roomId": "8386 3137",
  "race": "Tenno Sho (Spring)",
  "course": "Kyoto Turf",
  "surface": "Turf",
  "distance": "3200m",
  "distanceType": "Long",
  "direction": "Right",
  "weather": "Rainy",
  "ground": "Heavy",
  "mood": "Good",
  "rankLimit": "No Rank Limit",
  "specialRule": "1 URA Finale, 1 Unity Cup, 1 Trackblazer runner. 3 entries per person.",
  "scenarioWinners": {
    "URA Finale": { "player": "ARN", "uma": "Gold Ship", "pos": 4 },
    "Unity Cup": { "player": "Cyciesta", "uma": "Oguri Cap", "pos": 3 },
    "Trackblazer": { "player": "Cyciesta", "uma": "Agnes Tachyon", "pos": 1 }
  },
  "images": [],
  "participants": [
    { "pos": 1, "uma": "Agnes Tachyon", "umaId": "agnes-tachyon", "player": "Cyciesta", "strategy": "Pace", "number": 18, "fav": 8, "title": "Trackblazer Scenario Winner", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon" },
    { "pos": 2, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "GohanXGAMER", "strategy": "Pace", "number": 11, "fav": 3, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap" },
    { "pos": 3, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "Cyciesta", "strategy": "Pace", "number": 10, "fav": 6, "title": "Unity Cup Scenario Winner", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap" },
    { "pos": 4, "uma": "Gold Ship", "umaId": "gold-ship", "player": "ARN", "strategy": "End", "number": 14, "fav": 17, "title": "URA Finale Scenario Winner", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/gold-ship" },
    { "pos": 5, "uma": "Gold Ship", "umaId": "gold-ship", "player": "Agnes", "strategy": "End", "number": 2, "fav": 7, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/gold-ship" },
    { "pos": 6, "uma": "Admire Vega", "umaId": "admire-vega", "player": "GohanXGAMER", "strategy": "End", "number": 3, "fav": 2, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/admire-vega" },
    { "pos": 7, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "Yves", "strategy": "Pace", "number": 13, "fav": 15, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap" },
    { "pos": 8, "uma": "Narita Taishin", "umaId": "narita-taishin", "player": "Yves", "strategy": "End", "number": 4, "fav": 8, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/narita-taishin" },
    { "pos": 9, "uma": "Tamamo Cross", "umaId": "tamamo-cross", "player": "GohanXGAMER", "strategy": "End", "number": 9, "fav": 5, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/tamamo-cross" },
    { "pos": 10, "uma": "Mayano Top Gun", "umaId": "mayano-top-gun", "player": "Yves", "strategy": "Front", "number": 6, "fav": 16, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/mayano-top-gun" },
    { "pos": 11, "uma": "Tokai Teio", "umaId": "tokai-teio", "player": "Jiinxye", "strategy": "Pace", "number": 8, "fav": 4, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/tokai-teio" },
    { "pos": 12, "uma": "T.M. Opera O", "umaId": "t-m-opera-o", "player": "Agnes", "strategy": "Pace", "number": 15, "fav": 9, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/t-m-opera-o" },
    { "pos": 13, "uma": "Mejiro McQueen", "umaId": "mejiro-mcqueen", "player": "ARN", "strategy": "Pace", "number": 16, "fav": 11, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/mejiro-mcqueen" },
    { "pos": 14, "uma": "Matikanefukukitaru", "umaId": "matikanefukukitaru", "player": "Jiinxye", "strategy": "Late", "number": 18, "fav": 10, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/matikanefukukitaru" },
    { "pos": 15, "uma": "Grass Wonder", "umaId": "grass-wonder", "player": "Agnes", "strategy": "Late", "number": 12, "fav": 14, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/grass-wonder" },
    { "pos": 16, "uma": "Meisho Doto", "umaId": "meisho-doto", "player": "Cyciesta", "strategy": "Pace", "number": 5, "fav": 12, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/meisho-doto" },
    { "pos": 17, "uma": "Seiun Sky", "umaId": "seiun-sky", "player": "ARN", "strategy": "Front", "number": 1, "fav": 13, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/seiun-sky" },
    { "pos": 18, "uma": "Nice Nature", "umaId": "nice-nature", "player": "Jiinxye", "strategy": "Late", "number": 7, "fav": 18, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/nice-nature" }
  ]
}

suscup23 = {
  "id": 23,
  "cupNumber": "SUS CUP 23",
  "cupName": "Sus Cup 23 - Mixed Rarity Race",
  "name": "Satsuki Sho",
  "date": "03 April 2026, 18:32",
  "roomId": "7419 1111",
  "race": "Satsuki Sho",
  "course": "Nakayama Turf",
  "surface": "Turf",
  "distance": "2000m",
  "distanceType": "Medium",
  "direction": "Right",
  "weather": "Sunny",
  "ground": "Firm",
  "mood": "Good",
  "rankLimit": "No Rank Limit",
  "specialRule": "1x 1★, 1x 2★, 1x 3★ initial rarity runners. Unique runners only.",
  "rarityWinners": {
    "3-Star": { "player": "Jiinxye", "uma": "Narita Taishin", "pos": 1 },
    "2-Star": { "player": "Agnes", "uma": "Air Groove", "pos": 9 },
    "1-Star": { "player": "Shadow Amber", "uma": "Agnes Tachyon", "pos": 2 }
  },
  "images": [],
  "participants": [
    { "pos": 1, "uma": "Narita Taishin", "umaId": "narita-taishin", "player": "Jiinxye", "strategy": "End", "number": 16, "fav": 17, "title": "3-Star Initial Rarity Winner", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/narita-taishin" },
    { "pos": 2, "uma": "Agnes Tachyon", "umaId": "agnes-tachyon", "player": "Shadow Amber", "strategy": "Pace", "number": 18, "fav": 8, "title": "1-Star Initial Rarity Winner", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon" },
    { "pos": 3, "uma": "Mihono Bourbon", "umaId": "mihono-bourbon", "player": "Cruzi", "strategy": "Front", "number": 5, "fav": 11, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/mihono-bourbon" },
    { "pos": 4, "uma": "King Halo", "umaId": "king-halo", "player": "Agnes", "strategy": "Late", "number": 1, "fav": 7, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/king-halo" },
    { "pos": 5, "uma": "Nice Nature", "umaId": "nice-nature", "player": "Cyciesta", "strategy": "Late", "number": 9, "fav": 3, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/nice-nature" },
    { "pos": 6, "uma": "Agnes Tachyon", "umaId": "agnes-tachyon", "player": "Cruzi", "strategy": "Pace", "number": 6, "fav": 5, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon" },
    { "pos": 7, "uma": "T.M. Opera O", "umaId": "t-m-opera-o", "player": "Agnes", "strategy": "Pace", "number": 10, "fav": 1, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/t-m-opera-o" },
    { "pos": 8, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "Shadow Amber", "strategy": "Pace", "number": 13, "fav": 6, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap" },
    { "pos": 9, "uma": "Air Groove", "umaId": "air-groove", "player": "Agnes", "strategy": "Late", "number": 12, "fav": 16, "title": "2-Star Initial Rarity Winner", "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/air-groove" },
    { "pos": 10, "uma": "Eishin Flash", "umaId": "eishin-flash", "player": "Ananth", "strategy": "Pace", "number": 4, "fav": 13, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/eishin-flash" },
    { "pos": 11, "uma": "Gold Ship", "umaId": "gold-ship", "player": "Cruzi", "strategy": "End", "number": 11, "fav": 9, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/gold-ship" },
    { "pos": 12, "uma": "Vodka", "umaId": "vodka", "player": "Jiinxye", "strategy": "Late", "number": 14, "fav": 10, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/vodka" },
    { "pos": 13, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "Cyciesta", "strategy": "Pace", "number": 7, "fav": 4, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap" },
    { "pos": 14, "uma": "Grass Wonder", "umaId": "grass-wonder", "player": "Cyciesta", "strategy": "Late", "number": 15, "fav": 2, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/grass-wonder" },
    { "pos": 15, "uma": "Mejiro Ryan", "umaId": "mejiro-ryan", "player": "Haji", "strategy": "Late", "number": 8, "fav": 12, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/mejiro-ryan" },
    { "pos": 16, "uma": "Winning Ticket", "umaId": "winning-ticket", "player": "Jiinxye", "strategy": "Late", "number": 17, "fav": 14, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/winning-ticket" },
    { "pos": 17, "uma": "Special Week", "umaId": "special-week", "player": "Haji", "strategy": "Pace", "number": 3, "fav": 15, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/special-week" },
    { "pos": 18, "uma": "Super Creek", "umaId": "super-creek", "player": "Haji", "strategy": "Pace", "number": 2, "fav": 18, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/super-creek" }
  ]
}

folder22 = 'suscupimages21-30'
for i in range(1, 5):
    filename = f"22.{i}.png"
    if os.path.exists(os.path.join("..", folder22, filename)):
        suscup22["images"].append(f"{folder22}/{filename}")

for i in range(1, 5):
    filename = f"23.{i}.png"
    if os.path.exists(os.path.join("..", folder22, filename)):
        suscup23["images"].append(f"{folder22}/{filename}")

with open('../.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

uma_db_addition = ""
if '"admire-vega"' not in content:
    uma_db_addition += '  "admire-vega": { name: "Admire Vega", url: "https://gametora.com/umamusume/characters/admire-vega", image: "https://gametora.com/images/umamusume/characters/chara_stand_1033_103301.png" },\n'
if '"tamamo-cross"' not in content:
    uma_db_addition += '  "tamamo-cross": { name: "Tamamo Cross", url: "https://gametora.com/umamusume/characters/tamamo-cross", image: "https://gametora.com/images/umamusume/characters/chara_stand_1021_102101.png" },\n'

if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 22 for r in data['races']):
    data['races'].append(suscup22)
if not any(r.get('id') == 23 for r in data['races']):
    data['races'].append(suscup23)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('../.vscode/suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 22 and 23 data applied!")
