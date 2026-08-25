import json
import os

suscup25 = {
  "id": 25,
  "cupNumber": "SUS CUP 25",
  "cupName": "Sus Cup 25 - Fashion Statement Race",
  "name": "Satsuki Sho",
  "date": "12 April 2026, 21:35",
  "roomId": "7366 5085",
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
  "specialRule": "Alt Costume Only. 3 runners per person.",
  "images": [],
  "registeredRunners": [
    {"player": "Agnes", "uma": "Gold City"},
    {"player": "Agnes", "uma": "Super Creek"},
    {"player": "Agnes", "uma": "Special Week"},
    {"player": "GohanXGAMER", "uma": "Seiun Sky"},
    {"player": "GohanXGAMER", "uma": "Special Week"},
    {"player": "GohanXGAMER", "uma": "Biwa Hayahide"},
    {"player": "Cruzi", "uma": "Symboli Rudolf"},
    {"player": "Cruzi", "uma": "Mihono Bourbon"},
    {"player": "Cruzi", "uma": "Mayano Top Gun"},
    {"player": "Jiinxye", "uma": "Tokai Teio"},
    {"player": "Jiinxye", "uma": "El Condor Pasa"},
    {"player": "Jiinxye", "uma": "Gold City"},
    {"player": "Ananth", "uma": "Gold City"},
    {"player": "Ananth", "uma": "Grass Wonder"},
    {"player": "Ananth", "uma": "Air Groove"},
    {"player": "Cyciesta", "uma": "Seiun Sky"},
    {"player": "Cyciesta", "uma": "Rice Shower"},
    {"player": "Cyciesta", "uma": "Oguri Cap"}
  ],
  "participants": [
    { "pos": 1, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "Cyciesta", "strategy": "Pace", "margin": "1 1/4 L", "time": "1:56.4", "number": 5, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 2, "uma": "Seiun Sky", "umaId": "seiun-sky", "player": "Cyciesta", "strategy": "Front", "margin": "3/4 L", "number": 7, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 3, "uma": "Mihono Bourbon", "umaId": "mihono-bourbon", "player": "Cruzi", "strategy": "Front", "margin": "1 L", "number": 4, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 4, "uma": "Symboli Rudolf", "umaId": "symboli-rudolf", "player": "Cruzi", "strategy": "Pace", "margin": "1 1/2 L", "number": 2, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 5, "uma": "Seiun Sky", "umaId": "seiun-sky", "player": "GohanXGAMER", "strategy": "Front", "margin": "Neck", "number": 1, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 6, "uma": "Rice Shower", "umaId": "rice-shower", "player": "Cyciesta", "strategy": "Front", "margin": "1 3/4 L", "number": 3, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 7, "uma": "Special Week", "umaId": "special-week", "player": "Agnes", "strategy": "Late", "margin": "3/4 L", "number": 9, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 8, "uma": "Gold City", "umaId": "gold-city", "player": "Jiinxye", "strategy": "Late", "margin": "3/4 L", "number": 12, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 9, "uma": "Super Creek", "umaId": "super-creek", "player": "Agnes", "strategy": "Pace", "margin": "Neck", "number": 10, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 10, "uma": "Tokai Teio", "umaId": "tokai-teio", "player": "Jiinxye", "strategy": "Pace", "margin": "Nose", "number": 15, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 11, "uma": "Gold City", "umaId": "gold-city", "player": "Agnes", "strategy": "Late", "margin": "2 L", "number": 8, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 12, "uma": "Gold City", "umaId": "gold-city", "player": "Ananth", "strategy": "Pace", "margin": "Nose", "number": 16, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 13, "uma": "Mayano Top Gun", "umaId": "mayano-top-gun", "player": "Cruzi", "strategy": "Pace", "margin": "Neck", "number": 6, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 14, "uma": "Air Groove", "umaId": "air-groove", "player": "Ananth", "strategy": "Pace", "margin": "1/2 L", "number": 14, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 15, "uma": "El Condor Pasa", "umaId": "el-condor-pasa", "player": "Jiinxye", "strategy": "Late", "margin": "Nose", "number": 13, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 16, "uma": "Special Week", "umaId": "special-week", "player": "GohanXGAMER", "strategy": "Late", "margin": "Nose", "number": 11, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 17, "uma": "Biwa Hayahide", "umaId": "biwa-hayahide", "player": "GohanXGAMER", "strategy": "Pace", "margin": "Neck", "number": 17, "version": "Alt Costume", "participantType": "Playable Uma" },
    { "pos": 18, "uma": "Tamaxchi", "umaId": "tamaxchi", "player": "Unknown", "strategy": "Pace", "margin": "6 L", "number": 18, "version": "Alt Costume", "participantType": "Playable Uma" }
  ]
}

folder25 = 'suscupimages21-30'
for i in range(1, 5):
    filename = f"25.{i}.png"
    if os.path.exists(os.path.join("..", ".vscode", folder25, filename)):
        suscup25["images"].append(f"{folder25}/{filename}")

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

uma_db_addition = ""
if '"tamaxchi"' not in content:
    # Adding tamaxchi with a default image so it doesn't break
    uma_db_addition += '  "tamaxchi": { name: "Tamaxchi", url: "#", image: "https://gametora.com/images/umamusume/characters/chara_stand_1001_100101.png" },\n'

if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 25 for r in data['races']):
    data['races'].append(suscup25)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 25 data applied!")
