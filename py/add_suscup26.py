import json
import os

suscup26 = {
  "id": 26,
  "cupNumber": "SUS CUP 26",
  "cupName": "Sus Cup 26 - GRAND LIVE SUSSERY",
  "name": "Satsuki Sho",
  "date": "Not provided",
  "roomId": "5887 5481",
  "race": "Satsuki Sho",
  "course": "Nakayama Turf",
  "surface": "Turf",
  "distance": "2000m",
  "distanceType": "Medium",
  "direction": "Right",
  "weather": "Sunny",
  "ground": "Firm",
  "mood": "Normal",
  "rankLimit": "No Rank Limit",
  "specialRule": "3 runners per participant. All trained in Grand Live scenario. Conditions: 1. Speed SSR Agnes Tachyon (No Light Hello) 2. Light Hello (No Speed SSR Agnes Tachyon) 3. Auto Train (No deck restrictions).",
  "scenarioWinners": {
    "Speed Tachyon Deck": { "player": "Agnes", "uma": "Special Week", "pos": 1 },
    "Light Hello Deck": { "player": "Ananth", "uma": "Oguri Cap", "pos": 2 },
    "Auto Train": { "player": "GohanXGAMER", "uma": "Mejiro Dober", "pos": 4 }
  },
  "images": [],
  "participants": [
    { "pos": 1, "uma": "Special Week", "umaId": "special-week", "player": "Agnes", "title": "Speed Tachyon Deck Winner", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 2, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "Ananth", "title": "Light Hello Deck Winner", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 3, "uma": "Agnes Tachyon", "umaId": "agnes-tachyon", "player": "Cruzi", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 4, "uma": "Mejiro Dober", "umaId": "mejiro-dober", "player": "GohanXGAMER", "title": "Auto Train Winner", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 5, "uma": "Silence Suzuka", "umaId": "silence-suzuka", "player": "Agnes", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 6, "uma": "Agnes Digital", "umaId": "agnes-digital", "player": "Cruzi", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 7, "uma": "Maruzensky", "umaId": "maruzensky", "player": "Ananth", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 8, "uma": "Tokai Teio", "umaId": "tokai-teio", "player": "Jiinxye", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 9, "uma": "Seiun Sky", "umaId": "seiun-sky", "player": "GohanXGAMER", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 10, "uma": "Admire Vega", "umaId": "admire-vega", "player": "GohanXGAMER", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 11, "uma": "Mayano Top Gun", "umaId": "mayano-top-gun", "player": "Cruzi", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 12, "uma": "Gold Ship", "umaId": "gold-ship", "player": "Jiinxye", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 13, "uma": "T.M. Opera O", "umaId": "t-m-opera-o", "player": "Jiinxye", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 14, "uma": "Air Shakur", "umaId": "air-shakur", "player": "Agnes", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 15, "uma": "Gold City", "umaId": "gold-city", "player": "Ananth", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 16, "uma": "Oishii Parfait", "umaId": "oishii-parfait", "player": "NPC", "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 17, "uma": "Coronet Rhythm", "umaId": "coronet-rhythm", "player": "NPC", "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 18, "uma": "Tropical Sky", "umaId": "tropical-sky", "player": "NPC", "version": "NPC", "participantType": "NPC Uma" }
  ]
}

folder26 = 'suscupimages21-30'
for i in range(1, 5):
    filename = f"26.{i}.png"
    if os.path.exists(os.path.join("..", ".vscode", folder26, filename)):
        suscup26["images"].append(f"{folder26}/{filename}")

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

uma_db_addition = ""
if '"air-shakur"' not in content:
    uma_db_addition += '  "air-shakur": { name: "Air Shakur", url: "https://gametora.com/umamusume/characters/air-shakur", image: "https://gametora.com/images/umamusume/characters/chara_stand_1025_102501.png" },\n'
if '"oishii-parfait"' not in content:
    uma_db_addition += '  "oishii-parfait": { name: "Oishii Parfait", url: "#", image: "https://gametora.com/images/umamusume/characters/chara_stand_1001_100101.png" },\n'
if '"coronet-rhythm"' not in content:
    uma_db_addition += '  "coronet-rhythm": { name: "Coronet Rhythm", url: "#", image: "https://gametora.com/images/umamusume/characters/chara_stand_1001_100101.png" },\n'
if '"tropical-sky"' not in content:
    uma_db_addition += '  "tropical-sky": { name: "Tropical Sky", url: "#", image: "https://gametora.com/images/umamusume/characters/chara_stand_1001_100101.png" },\n'

if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 26 for r in data['races']):
    data['races'].append(suscup26)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 26 data applied!")
