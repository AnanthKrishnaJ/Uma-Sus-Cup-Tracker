import json
import os

suscup27_mile = {
  "id": 27.1,
  "cupNumber": "SUS CUP 27",
  "cupName": "Sus Cup 27 - MULTI CM SUSSING (MILE)",
  "name": "Asahi Hai Futurity Stakes",
  "date": "22 August 2026, 12:19",
  "roomId": "4967 8054",
  "race": "Asahi Hai Futurity Stakes",
  "course": "Hanshin Turf",
  "surface": "Turf",
  "distance": "1600m",
  "distanceType": "Mile",
  "direction": "Right-handed / Outer",
  "weather": "Cloudy",
  "ground": "Firm",
  "mood": "Good",
  "rankLimit": "No Rank Limit",
  "specialRule": "Multi-CM format. 3 runners per person. This is the Mile round (2 Mile runners used per person).",
  "images": [],
  "registeredRunners": [
    {"player": "agnes", "uma": "Fuji Kiseki"},
    {"player": "agnes", "uma": "Taiki Shuttle"},
    {"player": "agnes", "uma": "Eishin Flash"},
    {"player": "Jiinxye", "uma": "Nishino Flower"},
    {"player": "Jiinxye", "uma": "Seeking the Pearl"},
    {"player": "Jiinxye", "uma": "Gold Ship"},
    {"player": "GohanXGAMER", "uma": "Daiwa Scarlet"},
    {"player": "GohanXGAMER", "uma": "Nice Nature"},
    {"player": "GohanXGAMER", "uma": "Seiun Sky"},
    {"player": "Vilthaar", "uma": "Nishino Flower"},
    {"player": "Vilthaar", "uma": "Taiki Shuttle"},
    {"player": "Vilthaar", "uma": "Meisho Doto"},
    {"player": "Cruzi", "uma": "Mihono Bourbon"},
    {"player": "Cruzi", "uma": "Air Groove"},
    {"player": "Cruzi", "uma": "Fine Motion"},
    {"player": "Ananth", "uma": "Kitasan Black"},
    {"player": "Ananth", "uma": "Agnes Digital"},
    {"player": "Ananth", "uma": "Taiki Shuttle"}
  ],
  "participants": [
    { "pos": 1, "uma": "Nishino Flower", "umaId": "nishino-flower", "player": "Vilthaar", "title": "", "rank": "UG4", "number": 4, "strategy": "Pace", "pop": 6, "gap": "—", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 2, "uma": "Mihono Bourbon", "umaId": "mihono-bourbon", "player": "Cruzi", "title": "", "rank": "UG7", "number": 5, "strategy": "Front", "pop": 4, "gap": "2 L", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 3, "uma": "Taiki Shuttle", "umaId": "taiki-shuttle", "player": "agnes", "title": "", "rank": "UG5", "number": 10, "strategy": "Pace", "pop": 1, "gap": "1 1/2 L", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 4, "uma": "Daiwa Scarlet", "umaId": "daiwa-scarlet", "player": "GohanXGAMER", "title": "", "rank": "UG6", "number": 13, "strategy": "Front", "pop": 2, "gap": "Neck", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 5, "uma": "Taiki Shuttle", "umaId": "taiki-shuttle", "player": "Vilthaar", "title": "", "rank": "UG8", "number": 9, "strategy": "Pace", "pop": 7, "gap": "Neck", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 6, "uma": "Fine Motion", "umaId": "fine-motion", "player": "Cruzi", "title": "", "rank": "SS", "number": 14, "strategy": "Pace", "pop": 5, "gap": "1 L", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 7, "uma": "Nice Nature", "umaId": "nice-nature", "player": "GohanXGAMER", "title": "", "rank": "UG5", "number": 8, "strategy": "Late", "pop": 11, "gap": "Nose", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 8, "uma": "Taiki Shuttle", "umaId": "taiki-shuttle", "player": "Ananth", "title": "", "rank": "UG3", "number": 16, "strategy": "Pace", "pop": 13, "gap": "3 L", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 9, "uma": "Nishino Flower", "umaId": "nishino-flower", "player": "Jiinxye", "title": "", "rank": "UG", "number": 1, "strategy": "Pace", "pop": 15, "gap": "Neck", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 10, "uma": "Fuji Kiseki", "umaId": "fuji-kiseki", "player": "agnes", "title": "", "rank": "UG7", "number": 6, "strategy": "Pace", "pop": 3, "gap": "1 1/2 L", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 11, "uma": "Agnes Digital", "umaId": "agnes-digital", "player": "Ananth", "title": "", "rank": "SS", "number": 7, "strategy": "Pace", "pop": 14, "gap": "3/4 L", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 12, "uma": "Seeking the Pearl", "umaId": "seeking-the-pearl", "player": "Jiinxye", "title": "", "rank": "SS", "number": 3, "strategy": "Pace", "pop": 9, "gap": "Nose", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 13, "uma": "Seiun Sky", "umaId": "seiun-sky", "player": "GohanXGAMER", "title": "", "rank": "SS", "number": 12, "strategy": "Front", "pop": 17, "gap": "1 1/2 L", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 14, "uma": "Air Groove", "umaId": "air-groove", "player": "Cruzi", "title": "", "rank": "UG", "number": 15, "strategy": "Pace", "pop": 8, "gap": "Head", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 15, "uma": "Gold Ship", "umaId": "gold-ship", "player": "Jiinxye", "title": "", "rank": "SS", "number": 2, "strategy": "End", "pop": 16, "gap": "1 1/4 L", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 16, "uma": "Kitasan Black", "umaId": "kitasan-black", "player": "Ananth", "title": "", "rank": "SS", "number": 18, "strategy": "Front", "pop": 12, "gap": "1 3/4 L", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 17, "uma": "Meisho Doto", "umaId": "meisho-doto", "player": "Vilthaar", "title": "", "rank": "UG4", "number": 17, "strategy": "Pace", "pop": 10, "gap": "5 L", "version": "Original / Default", "participantType": "Playable Uma" },
    { "pos": 18, "uma": "Eishin Flash", "umaId": "eishin-flash", "player": "agnes", "title": "", "rank": "SS", "number": 11, "strategy": "Late", "pop": 18, "gap": "2 L", "version": "Original / Default", "participantType": "Playable Uma" }
  ]
}

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 27.1 for r in data['races']):
    data['races'].append(suscup27_mile)
    data['races'].sort(key=lambda x: x['id'])

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 27 (Mile) data applied!")
