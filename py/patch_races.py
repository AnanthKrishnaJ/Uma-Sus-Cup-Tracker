import re
import json

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

cup_22_participants = [
    {"pos": 1, "number": 17, "uma": "Agnes Tachyon", "player": "Cyclobly", "strategy": "Pace", "time": "3:13.4", "gap": "", "pop": 1, "rank": "SS", "title": "Leading the Charge"},
    {"pos": 2, "number": 11, "uma": "Oguri Cap", "player": "Yves", "strategy": "Pace", "time": "", "gap": "1 3/4 L", "pop": 3, "rank": "S+", "title": "Leading the Charge"},
    {"pos": 3, "number": 10, "uma": "Oguri Cap", "player": "Cyclobly", "strategy": "Pace", "time": "", "gap": "3 1/2 L", "pop": 6, "rank": "S", "title": "Witness to Legend"},
    {"pos": 4, "number": 14, "uma": "Gold Ship", "player": "Arn", "strategy": "End", "time": "", "gap": "1 1/2 L", "pop": 17, "rank": "A", "title": "The GOAT"},
    {"pos": 5, "number": 2, "uma": "Gold Ship", "player": "agnes", "strategy": "End", "time": "", "gap": "1/2 L", "pop": 7, "rank": "S", "title": "Unpredictable"},
    {"pos": 6, "number": 3, "uma": "Admire Vega", "player": "GohanXGAMER", "strategy": "End", "time": "", "gap": "1 1/4 L", "pop": 2, "rank": "S", "title": "Leading the Charge"},
    {"pos": 7, "number": 13, "uma": "Oguri Cap", "player": "GohanXGAMER", "strategy": "Pace", "time": "", "gap": "4 L", "pop": 15, "rank": "A", "title": "G1 Hunter"},
    {"pos": 8, "number": 4, "uma": "Narita Taishin", "player": "Yves", "strategy": "End", "time": "", "gap": "5 L", "pop": 8, "rank": "A+", "title": "Witness to Legend"},
    {"pos": 9, "number": 9, "uma": "Tamamo Cross", "player": "GohanXGAMER", "strategy": "End", "time": "", "gap": "2 1/2 L", "pop": 5, "rank": "S", "title": "Now That's White Lightning!"},
    {"pos": 10, "number": 6, "uma": "Mayano Top Gun", "player": "Yves", "strategy": "Front", "time": "", "gap": "2 L", "pop": 16, "rank": "A", "title": "Finals Champion"},
    {"pos": 11, "number": 8, "uma": "Tokai Teio", "player": "Jiinxye", "strategy": "Pace", "time": "", "gap": "Head", "pop": 4, "rank": "S+", "title": "Monarch"},
    {"pos": 12, "number": 15, "uma": "T.M. Opera O", "player": "agnes", "strategy": "Pace", "time": "", "gap": "3 1/2 L", "pop": 9, "rank": "A", "title": "Centurial Overlord"},
    {"pos": 13, "number": 16, "uma": "Mejiro McQueen", "player": "Arn", "strategy": "Pace", "time": "", "gap": "3 1/2 L", "pop": 11, "rank": "A", "title": "Product Power"},
    {"pos": 14, "number": 18, "uma": "Matikanefukukitaru", "player": "Jiinxye", "strategy": "Late", "time": "", "gap": "5 L", "pop": 10, "rank": "A+", "title": "Team Player Star Slayer"},
    {"pos": 15, "number": 12, "uma": "Grass Wonder", "player": "agnes", "strategy": "Late", "time": "", "gap": "Distance", "pop": 14, "rank": "A", "title": "Finals Champion"},
    {"pos": 16, "number": 5, "uma": "Meisho Doto", "player": "Cyclobly", "strategy": "Pace", "time": "", "gap": "1/2 L", "pop": 12, "rank": "A+", "title": "Legendary Diva"},
    {"pos": 17, "number": 1, "uma": "Seiun Sky", "player": "Arn", "strategy": "Front", "time": "", "gap": "5 L", "pop": 13, "rank": "A", "title": "Witness to Legend"},
    {"pos": 18, "number": 7, "uma": "Nice Nature", "player": "Jiinxye", "strategy": "Late", "time": "", "gap": "6 L", "pop": 18, "rank": "B+", "title": "Next-Gen Grandmaster"}
]
for p in cup_22_participants:
    p['umaId'] = slugify(p['uma'])

races_to_add = [
    {
        "id": 22,
        "cupNumber": 22,
        "cupName": "Sus Cup 22 — Cross Career Race",
        "name": "Tenno Sho (Spring)",
        "date": "TBD",
        "roomId": "TBD",
        "race": "Tenno Sho (Spring)",
        "grade": "G1",
        "track": "Kyoto Turf",
        "distance": "3200m",
        "distanceType": "Long",
        "direction": "Right / Outer",
        "weather": "Rainy",
        "ground": "Heavy",
        "mood": "Good",
        "rankLimit": "No Rank Limit",
        "specialRule": "TBD",
        "images": [],
        "participants": cup_22_participants
    }
]

for i in range(23, 28):
    races_to_add.append({
        "id": i,
        "cupNumber": i,
        "cupName": f"Sus Cup {i}",
        "name": "TBD",
        "date": "TBD",
        "roomId": "TBD",
        "race": "TBD",
        "grade": "TBD",
        "track": "TBD",
        "distance": "TBD",
        "distanceType": "TBD",
        "direction": "TBD",
        "weather": "TBD",
        "ground": "TBD",
        "mood": "TBD",
        "rankLimit": "TBD",
        "specialRule": "TBD",
        "images": [],
        "participants": []
    })

# Add 28 based on prompt details
races_to_add.append({
    "id": 28,
    "cupNumber": 28,
    "cupName": "Sus Cup 28 — Triple Threat",
    "name": "Tenno Sho (Autumn)",
    "date": "27 August 2026",
    "roomId": "70312406",
    "race": "Tenno Sho (Autumn)",
    "grade": "G1",
    "track": "Tokyo Turf",
    "distance": "2000m",
    "distanceType": "Medium",
    "direction": "Left",
    "weather": "Rainy",
    "ground": "Soft",
    "mood": "Good",
    "rankLimit": "No Rank Limit",
    "specialRule": "3 runners per person, exactly 3 runners, all 3 runners must use the same running strategy",
    "images": [],
    "participants": []
})

# Find the end of INITIAL_DATA races array
pattern = r'(\{\s*"id":\s*21,[\s\S]*?"participants":\s*\[[\s\S]*?\]\s*\})(\s*\]\s*\})'
match = re.search(pattern, text)
if match:
    replacement = match.group(1) + ",\n" + ",\n".join([json.dumps(r, indent=12) for r in races_to_add]) + match.group(2)
    text = text[:match.start()] + replacement + text[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully added Sus Cups 22-28.")
else:
    print("Could not find insertion point after Sus Cup 21.")
