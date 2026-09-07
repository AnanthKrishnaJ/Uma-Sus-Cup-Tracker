import json
import re

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

import re
def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

for p in cup_22_participants:
    p['umaId'] = slugify(p['uma'])

pattern_to_replace = r'(\{\s*"id":\s*22,\s*"cupNumber":\s*22,[\s\S]*?"participants":\s*)\[[\s\S]*?\](\s*\})'

match = re.search(pattern_to_replace, text)
if match:
    text = re.sub(pattern_to_replace, lambda m: m.group(1) + json.dumps(cup_22_participants, indent=16) + m.group(2), text)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully updated Sus Cup 22")
else:
    print("Could not find Sus Cup 22 block")
