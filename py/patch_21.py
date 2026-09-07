import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Define the new participants array for Sus Cup 21
cup_21_participants = [
    {"pos": 1, "number": 11, "uma": "Taiki Shuttle", "player": "agnes", "strategy": "Pace", "time": "1:07.3", "gap": "", "pop": 4, "rank": "A+", "title": "Mightiest Miler"},
    {"pos": 2, "number": 9, "uma": "Curren Chan", "player": "Cyclobly", "strategy": "Pace", "time": "", "gap": "1 L", "pop": 2, "rank": "S", "title": "Sprint Sweetheart"},
    {"pos": 3, "number": 15, "uma": "Curren Chan", "player": "Jiinxye", "strategy": "Front", "time": "", "gap": "1/2 L", "pop": 12, "rank": "A+", "title": "Team Player Star Slayer"},
    {"pos": 4, "number": 16, "uma": "Sakura Bakushin O", "player": "Jiinxye", "strategy": "Front", "time": "", "gap": "1 L", "pop": 14, "rank": "A", "title": "Team Player Star Slayer"},
    {"pos": 5, "number": 5, "uma": "Haru Urara", "player": "Cyclobly", "strategy": "Late", "time": "", "gap": "1/2 L", "pop": 13, "rank": "A+", "title": "Finals Champion"},
    {"pos": 6, "number": 12, "uma": "Taiki Shuttle", "player": "Cyclobly", "strategy": "Pace", "time": "", "gap": "1/2 L", "pop": 1, "rank": "S+", "title": "Witness to Legend"},
    {"pos": 7, "number": 4, "uma": "Sakura Bakushin O", "player": "Yves", "strategy": "Front", "time": "", "gap": "3/4 L", "pop": 5, "rank": "A+", "title": "Witness to Legend"},
    {"pos": 8, "number": 17, "uma": "Maruzensky", "player": "Jiinxye", "strategy": "Front", "time": "", "gap": "1 L", "pop": 10, "rank": "A", "title": "Team Player Star Slayer"},
    {"pos": 9, "number": 7, "uma": "Maruzensky", "player": "Cruzi", "strategy": "Front", "time": "", "gap": "1/2 L", "pop": 6, "rank": "S", "title": "Dream Team"},
    {"pos": 10, "number": 1, "uma": "Sakura Bakushin O", "player": "agnes", "strategy": "Front", "time": "", "gap": "1/2 L", "pop": 11, "rank": "A+", "title": "Finals Champion"},
    {"pos": 11, "number": 18, "uma": "Air Groove", "player": "agnes", "strategy": "Pace", "time": "", "gap": "1 3/4 L", "pop": 9, "rank": "A+", "title": "Triple Tiara"},
    {"pos": 12, "number": 8, "uma": "Silence Suzuka", "player": "Cruzi", "strategy": "Front", "time": "", "gap": "1 1/4 L", "pop": 8, "rank": "A+", "title": "Otherworldly Front-Runner"},
    {"pos": 13, "number": 3, "uma": "Pastime Joy", "player": "", "strategy": "Pace", "time": "", "gap": "Neck", "pop": 17, "rank": "B+", "title": ""},
    {"pos": 14, "number": 2, "uma": "Ribbon Virelai", "player": "", "strategy": "Front", "time": "", "gap": "1/2 L", "pop": 15, "rank": "B+", "title": ""},
    {"pos": 15, "number": 14, "uma": "Battle of Elah", "player": "", "strategy": "End", "time": "", "gap": "1/2 L", "pop": 16, "rank": "B+", "title": ""},
    {"pos": 16, "number": 13, "uma": "Oguri Cap", "player": "Yves", "strategy": "Pace", "time": "", "gap": "Nose", "pop": 7, "rank": "A", "title": "Witness to Legend"},
    {"pos": 17, "number": 6, "uma": "Smart Falcon", "player": "Yves", "strategy": "Front", "time": "", "gap": "1 3/4 L", "pop": 18, "rank": "A", "title": "Record Holder"},
    {"pos": 18, "number": 10, "uma": "Daiwa Scarlet", "player": "Cruzi", "strategy": "Pace", "time": "", "gap": "5 L", "pop": 3, "rank": "S", "title": "Miss Perfect"}
]

# We need to add umaId based on Uma name
import re
def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

for p in cup_21_participants:
    p['umaId'] = slugify(p['uma'])

# We'll use a regex to match the race block for cupNumber: 21
pattern_to_replace = r'(\{\s*"id":\s*21,\s*"cupNumber":\s*21,[\s\S]*?"participants":\s*)\[[\s\S]*?\](\s*\})'

match = re.search(pattern_to_replace, text)
if match:
    text = re.sub(pattern_to_replace, lambda m: m.group(1) + json.dumps(cup_21_participants, indent=16) + m.group(2), text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully updated Sus Cup 21")
else:
    print("Could not find Sus Cup 21 block")
