import re
import json

cup_26_data = {
    "id": 26,
    "cupNumber": 26,
    "cupName": "Sus Cup 26 — Satsuki Sho",
    "subtitle": "Satsuki Sho",
    "images": [
        "suscupimages21-30/26.1.png",
        "suscupimages21-30/26.2.png",
        "suscupimages21-30/26.3.png",
        "suscupimages21-30/26.4.png"
    ],
    "name": "Satsuki Sho",
    "date": "Not specified",
    "time": "Not specified",
    "roomId": "Not specified",
    "grade": "G1",
    "course": "Nakayama",
    "surface": "Turf",
    "distance": 2000,
    "distanceType": "Medium",
    "direction": "Right / Inner",
    "weather": "Sunny",
    "ground": "Not specified",
    "condition": "Firm",
    "mood": "Great",
    "season": "Not specified",
    "restriction": "None",
    "entryRule": "None",
    "participants": [
        {"pos": 1, "uma": "Special Week", "umaId": "special-week", "player": "agnes", "number": 15, "rank": "SS", "title": "Derby Dreamer", "strategy": "Pace", "gap": "", "time": "1:58.0", "pop": 8},
        {"pos": 2, "uma": "Oguri Cap", "umaId": "oguri-cap", "player": "Ananth", "number": 9, "rank": "UG", "title": "Legendary Reprise", "strategy": "Pace", "gap": "1 1/2 L", "time": "1 1/2 L", "pop": 1},
        {"pos": 3, "uma": "Agnes Tachyon", "umaId": "agnes-tachyon", "player": "Cruzi", "number": 14, "rank": "UG3", "title": "Faster than Light", "strategy": "Pace", "gap": "1 3/4 L", "time": "1 3/4 L", "pop": 10},
        {"pos": 4, "uma": "Mejiro Dober", "umaId": "mejiro-dober", "player": "GohanXGAMER", "number": 16, "rank": "SS", "title": "Independent Learner", "strategy": "Late", "gap": "1/2 L", "time": "1/2 L", "pop": 15},
        {"pos": 5, "uma": "Silence Suzuka", "umaId": "silence-suzuka", "player": "agnes", "number": 11, "rank": "SS", "title": "Otherworldly Front-Runner", "strategy": "Front", "gap": "Nose", "time": "Nose", "pop": 2},
        {"pos": 6, "uma": "Agnes Digital", "umaId": "agnes-digital", "player": "Cruzi", "number": 18, "rank": "SS+", "title": "The Key to Success", "strategy": "Pace", "gap": "Neck", "time": "Neck", "pop": 13},
        {"pos": 7, "uma": "Maruzensky", "umaId": "maruzensky", "player": "Ananth", "number": 6, "rank": "UG", "title": "The Key to Success", "strategy": "Front", "gap": "1/2 L", "time": "1/2 L", "pop": 3},
        {"pos": 8, "uma": "Tokai Teio", "umaId": "tokai-teio", "player": "Jiinxye", "number": 3, "rank": "S+", "title": "Independent Learner", "strategy": "Pace", "gap": "3/4 L", "time": "3/4 L", "pop": 4},
        {"pos": 9, "uma": "Seiun Sky", "umaId": "seiun-sky", "player": "GohanXGAMER", "number": 12, "rank": "SS+", "title": "The Key to Success", "strategy": "Front", "gap": "1 L", "time": "1 L", "pop": 12},
        {"pos": 10, "uma": "Admire Vega", "umaId": "admire-vega", "player": "GohanXGAMER", "number": 2, "rank": "UG", "title": "Brightest Star", "strategy": "End", "gap": "Nose", "time": "Nose", "pop": 7},
        {"pos": 11, "uma": "Mayano Top Gun", "umaId": "mayano-top-gun", "player": "Cruzi", "number": 10, "rank": "SS+", "title": "Independent Learner", "strategy": "Pace", "gap": "2 1/2 L", "time": "2 1/2 L", "pop": 6},
        {"pos": 12, "uma": "Gold Ship", "umaId": "gold-ship", "player": "Jiinxye", "number": 17, "rank": "SS", "title": "Cool and Composed", "strategy": "End", "gap": "Neck", "time": "Neck", "pop": 11},
        {"pos": 13, "uma": "T.M. Opera O", "umaId": "tm-opera-o", "player": "Jiinxye", "number": 13, "rank": "S+", "title": "Queen of Dance", "strategy": "Pace", "gap": "1/2 L", "time": "1/2 L", "pop": 9},
        {"pos": 14, "uma": "Air Shakur", "umaId": "air-shakur", "player": "agnes", "number": 5, "rank": "SS", "title": "Independent Learner", "strategy": "End", "gap": "Neck", "time": "Neck", "pop": 5},
        {"pos": 15, "uma": "Gold City", "umaId": "gold-city", "player": "Ananth", "number": 1, "rank": "S+", "title": "Independent Learner", "strategy": "Pace", "gap": "Neck", "time": "Neck", "pop": 14},
        {"pos": 16, "uma": "Oishii Parfait", "umaId": "oishii-parfait", "player": "NPC", "number": 4, "rank": "A", "title": "—", "strategy": "Front", "gap": "5 L", "time": "5 L", "pop": 17},
        {"pos": 17, "uma": "Cornet Rhythm", "umaId": "cornet-rhythm", "player": "NPC", "number": 7, "rank": "A", "title": "—", "strategy": "Pace", "gap": "1/2 L", "time": "1/2 L", "pop": 16},
        {"pos": 18, "uma": "Tropical Sky", "umaId": "tropical-sky", "player": "NPC", "number": 8, "rank": "A", "title": "—", "strategy": "End", "gap": "Head", "time": "Head", "pop": 18}
    ]
}

cup26_str = json.dumps(cup_26_data, indent=4)
# fix title format
cup26_str = cup26_str.replace('"cupName": "Sus Cup 26 \\u2014 Satsuki Sho"', '"cupName": "Sus Cup 26 — Satsuki Sho"')
cup26_str = cup26_str.replace('"title": "\\u2014"', '"title": "—"')
cup26_str = cup26_str.replace('    ', '                ')
# remove outer braces to fit into the array
cup26_str = cup26_str[2:-2] 
# indent the first line
cup26_str = '        {\n          ' + cup26_str + '\n        }'

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'(\{\s*"id":\s*26,\s*"cupNumber":\s*26,[\s\S]*?"participants":\s*)\[[\s\S]*?\](\s*\})'
if re.search(pattern, text):
    text = re.sub(pattern, cup26_str, text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated Cup 26 in index.html")
else:
    print("Pattern not found for Cup 26. Searching for generic id 26")
    pattern = r'\{\s*"id":\s*26,[\s\S]*?\}'
    if re.search(pattern, text):
        print("Found id 26")
    else:
        print("Did not find id 26")
