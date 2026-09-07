import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build Cup 24 object
cup24 = {
    "id": 24,
    "cup": "24",
    "name": "G1 Satsuki Sho",
    "track": "Nakayama Turf 2000m (Medium)",
    "direction": "Right / Inner",
    "ground": "Firm",
    "winner": "Mejiro Dober",
    "winningTime": "1:56.6",
    "specialRule": "",
    "images": [],
    "participants": [
        {"pos": 1, "player": "jayreative", "uma": "Mejiro Dober", "rank": "?", "title": "Coolheaded Beauty", "strategy": "Late", "time": "1:56.6", "pop": 8, "umaId": "mejiro-dober"},
        {"pos": 2, "player": "Cyclobly", "uma": "Oguri Cap", "rank": "?", "title": "Leading the Charge", "strategy": "Pace", "time": "1 3/4 L", "pop": 1, "umaId": "oguri-cap"},
        {"pos": 3, "player": "Vilthaar", "uma": "Maruzensky", "rank": "?", "title": "Leading the Charge", "strategy": "Front", "time": "1 1/4 L", "pop": 3, "umaId": "maruzensky"},
        {"pos": 4, "player": "GohanXGAMER", "uma": "Admire Vega", "rank": "?", "title": "Leading the Charge", "strategy": "End", "time": "3/4 L", "pop": 4, "umaId": "admire-vega"},
        {"pos": 5, "player": "Cruzi", "uma": "Agnes Tachyon", "rank": "?", "title": "Leading the Charge", "strategy": "Pace", "time": "Neck", "pop": 5, "umaId": "agnes-tachyon"},
        {"pos": 6, "player": "eviskno", "uma": "Oguri Cap", "rank": "?", "title": "Ideal Idol", "strategy": "Pace", "time": "1 1/4 L", "pop": 6, "umaId": "oguri-cap"},
        {"pos": 7, "player": "Jiinxye", "uma": "Narita Taishin", "rank": "?", "title": "Phenomenal", "strategy": "End", "time": "1 L", "pop": 10, "umaId": "narita-taishin"},
        {"pos": 8, "player": "agnes", "uma": "Symboli Rudolf", "rank": "?", "title": "Emperor", "strategy": "Late", "time": "3/4 L", "pop": 2, "umaId": "symboli-rudolf"},
        {"pos": 9, "player": "Ananth", "uma": "Fuji Kiseki", "rank": "?", "title": "Leading the Charge", "strategy": "Pace", "time": "1 1/2 L", "pop": 7, "umaId": "fuji-kiseki"},
        {"pos": 10, "player": "Haji", "uma": "Special Week", "rank": "?", "title": "Leading the Charge", "strategy": "Pace", "time": "3/4 L", "pop": 9, "umaId": "special-week"},
        {"pos": 11, "player": "Not shown", "uma": "Mini Daisy", "rank": "?", "title": "", "strategy": "Pace", "time": "4 L", "pop": 11, "umaId": "mini-daisy"},
        {"pos": 12, "player": "Not shown", "uma": "Reed Photobook", "rank": "?", "title": "", "strategy": "Pace", "time": "1/2 L", "pop": 13, "umaId": "reed-photobook"},
        {"pos": 13, "player": "Not shown", "uma": "Chief Purser", "rank": "?", "title": "", "strategy": "Late", "time": "Nose", "pop": 12, "umaId": "chief-purser"},
        {"pos": 14, "player": "Not shown", "uma": "Takeoff Plane", "rank": "?", "title": "", "strategy": "End", "time": "1/2 L", "pop": 17, "umaId": "takeoff-plane"},
        {"pos": 15, "player": "Not shown", "uma": "Farm Volition", "rank": "?", "title": "", "strategy": "Late", "time": "Nose", "pop": 16, "umaId": "farm-volition"},
        {"pos": 16, "player": "Not shown", "uma": "Coincidence", "rank": "?", "title": "", "strategy": "Front", "time": "Head", "pop": 15, "umaId": "coincidence"},
        {"pos": 17, "player": "Not shown", "uma": "Waltz Step", "rank": "?", "title": "", "strategy": "Pace", "time": "Neck", "pop": 14, "umaId": "waltz-step"},
        {"pos": 18, "player": "Not shown", "uma": "Missing Nights", "rank": "?", "title": "", "strategy": "Front", "time": "1 1/4 L", "pop": 18, "umaId": "missing-nights"}
    ]
}

cup24_json = json.dumps(cup24, indent=6)

if '"id": 24,' in content and '"cup": "24"' in content:
    print("Cup 24 already exists.")
else:
    # Insert after "races": [
    content = content.replace('"races": [', '"races": [\n' + cup24_json + ',')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Cup 24.")
