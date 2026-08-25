import json
import os

suscup27_medium = {
  "id": 27.2,
  "cupNumber": "SUS CUP 27",
  "cupName": "Sus Cup 27 - MULTI CM SUSSING (MEDIUM)",
  "name": "Queen Elizabeth II Cup",
  "date": "22 August 2026, 12:19",
  "roomId": "3009 9804",
  "race": "Queen Elizabeth II Cup",
  "course": "Kyoto Turf",
  "surface": "Turf",
  "distance": "2200m",
  "distanceType": "Medium",
  "direction": "Right-handed / Outer",
  "weather": "Cloudy",
  "ground": "Firm",
  "mood": "Good",
  "rankLimit": "No Rank Limit",
  "specialRule": "Multi-CM format. 3 runners per person. This is the Medium round (1 Medium runner used per person).",
  "images": [],
  "registeredRunners": [
    {"player": "Agnes", "uma": "Eishin Flash"},
    {"player": "Jiinxye", "uma": "Nishino Flower"},
    {"player": "GohanXGAMER", "uma": "Seiun Sky"},
    {"player": "Vilthaar", "uma": "Meisho Doto"},
    {"player": "Cruzi", "uma": "Air Groove"},
    {"player": "Ananth", "uma": "Kitasan Black"}
  ],
  "participants": [
    { "pos": 1, "uma": "Air Groove", "umaId": "air-groove", "player": "Cruzi", "title": "The Key to Success", "rank": "UG", "number": 11, "strategy": "Pace", "fav": 9, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 2, "uma": "Nice Nature", "umaId": "nice-nature", "player": "GohanXGAMER", "title": "Legendary Reprise", "rank": "UG", "number": 17, "strategy": "Late", "fav": 10, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 3, "uma": "Kitasan Black", "umaId": "kitasan-black", "player": "Ananth", "title": "Legendary Reprise", "rank": "UG", "number": 5, "strategy": "Front", "fav": 12, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 4, "uma": "Taiki Shuttle", "umaId": "taiki-shuttle", "player": "Ananth", "title": "Mightiest Miler", "rank": "UG", "number": 2, "strategy": "Pace", "fav": 13, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 5, "uma": "Gold Ship", "umaId": "gold-ship", "player": "Jiinxye", "title": "Independent Learner", "rank": "SS", "number": 1, "strategy": "End", "fav": 11, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 6, "uma": "Seiun Sky", "umaId": "seiun-sky", "player": "GohanXGAMER", "title": "Legendary Reprise", "rank": "SS", "number": 6, "strategy": "Front", "fav": 14, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 7, "uma": "Agnes Digital", "umaId": "agnes-digital", "player": "Ananth", "title": "Independent Learner", "rank": "SS", "number": 10, "strategy": "Pace", "fav": 8, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 8, "uma": "Eishin Flash", "umaId": "eishin-flash", "player": "Agnes", "title": "True Way of Kings", "rank": "SS", "number": 4, "strategy": "Late", "fav": 4, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 9, "uma": "Fine Motion", "umaId": "fine-motion", "player": "Cruzi", "title": "Legendary Reprise", "rank": "SS", "number": 9, "strategy": "Pace", "fav": 7, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 10, "uma": "Meisho Doto", "umaId": "meisho-doto", "player": "Vilthaar", "title": "Legendary Reprise", "rank": "UG", "number": 15, "strategy": "Pace", "fav": 5, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 11, "uma": "Fuji Kiseki", "umaId": "fuji-kiseki", "player": "Agnes", "title": "Sprinter Stayer", "rank": "UG", "number": 18, "strategy": "Pace", "fav": 3, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 12, "uma": "Mihono Bourbon", "umaId": "mihono-bourbon", "player": "Cruzi", "title": "Legendary Reprise", "rank": "UG", "number": 3, "strategy": "Front", "fav": 2, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 13, "uma": "Daiwa Scarlet", "umaId": "daiwa-scarlet", "player": "GohanXGAMER", "title": "Legendary Reprise", "rank": "UG", "number": 14, "strategy": "Front", "fav": 1, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 14, "uma": "Seeking the Pearl", "umaId": "seeking-the-pearl", "player": "Jiinxye", "title": "Independent Learner", "rank": "SS", "number": 8, "strategy": "Pace", "fav": 16, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 15, "uma": "Taiki Shuttle", "umaId": "taiki-shuttle", "player": "Vilthaar", "title": "Mightiest Miler", "rank": "UG", "number": 12, "strategy": "Pace", "fav": 6, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 16, "uma": "Nishino Flower", "umaId": "nishino-flower", "player": "Jiinxye", "title": "Queen of Dance", "rank": "UG", "number": 7, "strategy": "Pace", "fav": 17, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 17, "uma": "Taiki Shuttle", "umaId": "taiki-shuttle", "player": "Agnes", "title": "Mightiest Miler", "rank": "UG", "number": 16, "strategy": "Pace", "fav": 18, "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 18, "uma": "Nishino Flower", "umaId": "nishino-flower", "player": "Vilthaar", "title": "Legendary Reprise", "rank": "UG", "number": 13, "strategy": "Pace", "fav": 15, "version": "Original / Default", "participantType": "Playable Uma" }
  ]
}

folder27 = 'suscupimages21-30'
for i in range(1, 5):
    filename = f"27.{i}.png"
    if os.path.exists(os.path.join("..", ".vscode", folder27, filename)):
        suscup27_medium["images"].append(f"{folder27}/{filename}")

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

uma_db_addition = ""
if '"kitasan-black"' not in content:
    uma_db_addition += '  "kitasan-black": { name: "Kitasan Black", url: "https://gametora.com/umamusume/characters/kitasan-black", image: "https://gametora.com/images/umamusume/characters/chara_stand_1068_106801.png" },\n'
if '"fine-motion"' not in content:
    uma_db_addition += '  "fine-motion": { name: "Fine Motion", url: "https://gametora.com/umamusume/characters/fine-motion", image: "https://gametora.com/images/umamusume/characters/chara_stand_1022_102201.png" },\n'
if '"seeking-the-pearl"' not in content:
    uma_db_addition += '  "seeking-the-pearl": { name: "Seeking the Pearl", url: "https://gametora.com/umamusume/characters/seeking-the-pearl", image: "https://gametora.com/images/umamusume/characters/chara_stand_1062_106201.png" },\n'

if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 27.2 for r in data['races']):
    data['races'].append(suscup27_medium)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 27 (Medium) data applied!")
