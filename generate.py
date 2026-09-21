import json
import os

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_idx = html.find("const INITIAL_DATA = {")
if start_idx == -1:
    print("Could not find INITIAL_DATA")
    exit(1)

# brace counting
brace_count = 0
end_idx = -1
for i in range(start_idx + 21, len(html)):
    if html[i] == '{':
        brace_count += 1
    elif html[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            end_idx = i + 1
            break

if end_idx == -1:
    print("Could not find end of INITIAL_DATA")
    exit(1)

json_str = html[start_idx + 21 : end_idx]

try:
    data = json.loads(json_str)
except Exception as e:
    print("JSON parse error:", e)
    with open("err.json", "w", encoding="utf-8") as out:
        out.write(json_str)
    exit(1)

# Update winners
winners = data.get("winners", [])
if not any(w.get("cupNumber") == 30 for w in winners):
    winners.append({
        "cup": "Sus Cup 30",
        "cupNumber": 30,
        "date": "2026-09-21",
        "uma": "Meisho Doto",
        "trainer": "Cyclobly",
        "player": "Cyclobly",
        "type": "Uma Musume"
    })

# Update championships
champs = data.get("championships", {})
champs["Meisho Doto"] = champs.get("Meisho Doto", 0) + 1
data["championships"] = champs

# Create Sus Cup 30 Race
cup_30_participants = [
    {"pos": 1, "uma": "Meisho Doto", "player": "Cyclobly", "strategy": "Pace", "gap": "1:31.4", "time": "1:31.4", "pop": 10, "rank": "Unknown", "number": 10},
    {"pos": 2, "uma": "Special Week", "player": "agnes", "strategy": "Late", "gap": "1 1/2 L", "time": "1 1/2 L", "pop": 3, "rank": "Unknown", "number": 3},
    {"pos": 3, "uma": "Mihono Bourbon", "player": "Vilthaar", "strategy": "Front", "gap": "Neck", "time": "Neck", "pop": 8, "rank": "Unknown", "number": 8},
    {"pos": 4, "uma": "Symboli Rudolf", "player": "Jiinxye", "strategy": "Pace", "gap": "1/2 L", "time": "1/2 L", "pop": 5, "rank": "Unknown", "number": 5},
    {"pos": 5, "uma": "Nakayama Festa", "player": "agnes", "strategy": "Late", "gap": "Head", "time": "Head", "pop": 6, "rank": "Unknown", "number": 6},
    {"pos": 6, "uma": "Mejiro Ardan", "player": "Ananth", "strategy": "Pace", "gap": "Head", "time": "Head", "pop": 1, "rank": "Unknown", "number": 1},
    {"pos": 7, "uma": "Seiun Sky", "player": "Vilthaar", "strategy": "Front", "gap": "1 3/4 L", "time": "1 3/4 L", "pop": 4, "rank": "Unknown", "number": 4},
    {"pos": 8, "uma": "Narita Taishin", "player": "Jiinxye", "strategy": "End", "gap": "2 1/2 L", "time": "2 1/2 L", "pop": 7, "rank": "Unknown", "number": 7},
    {"pos": 9, "uma": "Admire Vega", "player": "GohanXGAMER", "strategy": "End", "gap": "1 L", "time": "1 L", "pop": 11, "rank": "Unknown", "number": 11},
    {"pos": 10, "uma": "Kitasan Black", "player": "Ananth", "strategy": "Front", "gap": "1 L", "time": "1 L", "pop": 14, "rank": "Unknown", "number": 14},
    {"pos": 11, "uma": "Seiun Sky", "player": "GohanXGAMER", "strategy": "Front", "gap": "1/2 L", "time": "1/2 L", "pop": 12, "rank": "Unknown", "number": 12},
    {"pos": 12, "uma": "Agnes Tachyon", "player": "Ananth", "strategy": "Pace", "gap": "3/4 L", "time": "3/4 L", "pop": 2, "rank": "Unknown", "number": 2},
    {"pos": 13, "uma": "Tamamo Cross", "player": "Cyclobly", "strategy": "Pace", "gap": "Neck", "time": "Neck", "pop": 9, "rank": "Unknown", "number": 9},
    {"pos": 14, "uma": "Agnes Tachyon", "player": "Cyclobly", "strategy": "End", "gap": "1 1/2 L", "time": "1 1/2 L", "pop": 13, "rank": "Unknown", "number": 13},
    {"pos": 15, "uma": "Meisho Doto", "player": "Vilthaar", "strategy": "Pace", "gap": "5 L", "time": "5 L", "pop": 15, "rank": "Unknown", "number": 15},
    {"pos": 16, "uma": "Tamamo Cross", "player": "GohanXGAMER", "strategy": "End", "gap": "1 1/4 L", "time": "1 1/4 L", "pop": 16, "rank": "Unknown", "number": 16},
    {"pos": 17, "uma": "T.M. Opera O", "player": "agnes", "strategy": "Pace", "gap": "3/4 L", "time": "3/4 L", "pop": 17, "rank": "Unknown", "number": 17},
    {"pos": 18, "uma": "Tokai Teio", "player": "Jiinxye", "strategy": "Pace", "gap": "Head", "time": "Head", "pop": 18, "rank": "Unknown", "number": 18}
]

def make_uma_id(name):
    return name.lower().replace(" ", "-").replace(".", "")

for p in cup_30_participants:
    p["umaId"] = make_uma_id(p["uma"])
    p["title"] = "Unknown"
    p["version"] = "Unknown"

cup_30 = {
    "id": 30,
    "cupNumber": 30,
    "cupName": "Sus Cup 30 - Polar Bear in Arlington Texas",
    "name": "Kyoto Turf 1600m",
    "date": "2026-09-21",
    "roomId": "Unknown",
    "race": "Kyoto Turf 1600m",
    "course": "Kyoto",
    "surface": "Turf",
    "distance": "1600m",
    "distanceType": "Mile",
    "direction": "Right / Outer",
    "weather": "Sunny",
    "ground": "Good",
    "mood": "Great",
    "season": "Fall",
    "rankLimit": "Unknown",
    "specialRule": "Polar Bear in Arlington Texas",
    "result": "6th Place",
    "comment": "",
    "images": [
        "suscupimages21-30/30.1.png",
        "suscupimages21-30/30.2.png",
        "suscupimages21-30/30.3.png",
        "suscupimages21-30/30.4.png"
    ],
    "participants": cup_30_participants
}

races = data.get("races", [])
existing = [r for r in races if r.get("cupNumber") == 30]
if not existing:
    races.append(cup_30)
else:
    for i, r in enumerate(races):
        if r.get("cupNumber") == 30:
            races[i] = cup_30
            break

new_json_str = json.dumps(data, indent=4)
new_html = html[:start_idx + 21] + new_json_str + html[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("index.html updated successfully!")

with open("suscup30.txt", "w", encoding="utf-8") as f:
    f.write("Sus Cup 30 Results\n\n")
    for p in cup_30_participants:
        f.write(f"{p['pos']} - {p['uma']} ({p['player']}) - Strategy: {p['strategy']} - Gap: {p['gap']} - Fav: {p['pop']}\n")

with open("suscup1_to_30.txt", "w", encoding="utf-8") as f:
    for race in data.get("races", []):
        f.write(f"\n{race.get('cupName', f'Sus Cup {race.get('cupNumber')}')}\n")
        for p in race.get("participants", []):
            pos = p.get('pos', 'Unknown')
            uma = p.get('uma', 'Unknown')
            player = p.get('player', 'Unknown')
            strategy = p.get('strategy', 'Unknown')
            f.write(f"{pos} - {uma} ({player}) - Strategy: {strategy}\n")

print("txt files created successfully!")
