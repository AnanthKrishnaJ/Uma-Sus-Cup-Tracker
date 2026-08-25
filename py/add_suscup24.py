import json

suscup24 = {
  "id": 24,
  "cupNumber": "SUS CUP 24",
  "cupName": "Sus Cup 24 - Solo Queue Race",
  "name": "Satsuki Sho",
  "date": "05 April 2026, 11:43",
  "roomId": "8244 6062",
  "race": "Satsuki Sho",
  "course": "Nakayama Turf",
  "surface": "Turf",
  "distance": "2000m",
  "distanceType": "Medium",
  "direction": "Right",
  "weather": "Sunny",
  "ground": "Firm",
  "mood": "Great",
  "rankLimit": "No Rank Limit",
  "specialRule": "Solo Queue Race. 1 runner per person. Unique runner only. Taking reservations.",
  "images": [],
  "registeredRunners": [
    {"player": "Agnes", "uma": "Symboli Rudolf"},
    {"player": "Jiinxye", "uma": "Narita Taishin"},
    {"player": "Cyciesta", "uma": "Oguri Cap"},
    {"player": "Ananth", "uma": "Fuji Kiseki"},
    {"player": "Cruzi", "uma": "Agnes Tachyon"},
    {"player": "GohanXGAMER", "uma": "Admire Vega"}
  ],
  "participants": [
    { "pos": 1, "uma": "Mejiro Dober", "umaId": "mejiro-dober", "player": "club member", "rank": "S", "number": 9, "title": "Coolheaded Beauty", "strategy": "Late", "time": "1:56.6", "fav": 8, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/mejiro-dober" },
    { "pos": 2, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "Cyciesta", "rank": "SS", "number": 7, "title": "Leading the Charge", "strategy": "Pace", "margin": "1 3/4 L", "fav": 1, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap" },
    { "pos": 3, "uma": "Maruzensky", "umaId": "maruzensky", "player": "Vilthaar", "rank": "SS", "number": 18, "title": "Leading the Charge", "strategy": "Front", "margin": "1 1/4 L", "fav": 3, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/maruzensky" },
    { "pos": 4, "uma": "Admire Vega", "umaId": "admire-vega", "player": "GohanXGAMER", "rank": "S+", "number": 6, "title": "Leading the Charge", "strategy": "End", "margin": "3/4 L", "fav": 4, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/admire-vega" },
    { "pos": 5, "uma": "Agnes Tachyon", "umaId": "agnes-tachyon", "player": "Cruzi", "rank": "S+", "number": 16, "title": "Leading the Charge", "strategy": "Pace", "margin": "Neck", "fav": 5, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon" },
    { "pos": 6, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "eviskno", "rank": "S+", "number": 2, "title": "Ideal Idol", "strategy": "Pace", "margin": "1 1/4 L", "fav": 6, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap" },
    { "pos": 7, "uma": "Narita Taishin", "umaId": "narita-taishin", "player": "Jiinxye", "rank": "S", "number": 1, "title": "Phenomenal", "strategy": "End", "margin": "1 L", "fav": 10, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/narita-taishin" },
    { "pos": 8, "uma": "Symboli Rudolf", "umaId": "symboli-rudolf", "player": "Agnes", "rank": "S+", "number": 11, "title": "Emperor", "strategy": "Late", "margin": "3/4 L", "fav": 2, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/symboli-rudolf" },
    { "pos": 9, "uma": "Fuji Kiseki", "umaId": "fuji-kiseki", "player": "Ananth", "rank": "S+", "number": 12, "title": "Leading the Charge", "strategy": "Pace", "margin": "1 1/2 L", "fav": 7, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/fuji-kiseki" },
    { "pos": 10, "uma": "Special Week", "umaId": "special-week", "player": "Haji", "rank": "S", "number": 10, "title": "Leading the Charge", "strategy": "Pace", "margin": "3/4 L", "fav": 9, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/special-week" },
    { "pos": 11, "uma": "Mini Daisy", "umaId": "mini-daisy", "player": "NPC", "rank": "A", "number": 17, "strategy": "Pace", "margin": "4 L", "fav": 11, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 12, "uma": "Reed Photobook", "umaId": "reed-photobook", "player": "NPC", "rank": "A", "number": 4, "strategy": "Pace", "margin": "1/2 L", "fav": 13, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 13, "uma": "Chief Purser", "umaId": "chief-purser", "player": "NPC", "rank": "A", "number": 15, "strategy": "Late", "margin": "Nose", "fav": 12, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 14, "uma": "Takeoff Plane", "umaId": "takeoff-plane", "player": "NPC", "rank": "A", "number": 5, "strategy": "End", "margin": "1/2 L", "fav": 17, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 15, "uma": "Farm Volition", "umaId": "farm-volition", "player": "NPC", "rank": "A", "number": 14, "strategy": "Late", "margin": "Nose", "fav": 16, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 16, "uma": "Coincidence", "umaId": "coincidence", "player": "NPC", "rank": "A", "number": 13, "strategy": "Front", "margin": "Head", "fav": 15, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 17, "uma": "Waltz Step", "umaId": "waltz-step", "player": "NPC", "rank": "A", "number": 8, "strategy": "Pace", "margin": "Neck", "fav": 14, "version": "NPC", "participantType": "NPC Uma" },
    { "pos": 18, "uma": "Missing Nights", "umaId": "missing-nights", "player": "NPC", "rank": "A", "number": 3, "strategy": "Front", "margin": "1 1/4 L", "fav": 18, "version": "NPC", "participantType": "NPC Uma" }
  ]
}


with open('../.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

uma_db_addition = ""
if '"mejiro-dober"' not in content:
    uma_db_addition += '  "mejiro-dober": { name: "Mejiro Dober", url: "https://gametora.com/umamusume/characters/mejiro-dober", image: "https://gametora.com/images/umamusume/characters/chara_stand_1059_105901.png" },\n'
if '"fuji-kiseki"' not in content:
    uma_db_addition += '  "fuji-kiseki": { name: "Fuji Kiseki", url: "https://gametora.com/umamusume/characters/fuji-kiseki", image: "https://gametora.com/images/umamusume/characters/chara_stand_1005_100501.png" },\n'

if uma_db_addition:
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + uma_db_addition + content[db_end:]

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

if not any(r.get('id') == 24 for r in data['races']):
    data['races'].append(suscup24)

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('../.vscode/suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 24 data applied!")
