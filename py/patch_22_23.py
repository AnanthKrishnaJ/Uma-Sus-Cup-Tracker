import json
import re

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

cup_22 = [
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

cup_23 = [
  {"pos": 1, "number": 16, "uma": "Narita Taishin", "player": "Jiinxye", "strategy": "End", "time": "1:56.1", "gap": "", "pop": 17, "rank": "S", "title": "Phenomenal"},
  {"pos": 2, "number": 18, "uma": "Agnes Tachyon", "player": "Shadow Amber", "strategy": "Pace", "time": "", "gap": "1 L", "pop": 8, "rank": "S", "title": "Leading the Charge"},
  {"pos": 3, "number": 5, "uma": "Mihono Bourbon", "player": "Cruzi", "strategy": "Front", "time": "", "gap": "Head", "pop": 11, "rank": "SS", "title": "Leading the Charge"},
  {"pos": 4, "number": 1, "uma": "King Halo", "player": "agnes", "strategy": "Late", "time": "", "gap": "Head", "pop": 7, "rank": "S+", "title": "Goddess"},
  {"pos": 5, "number": 9, "uma": "Nice Nature", "player": "Cyclobly", "strategy": "Late", "time": "", "gap": "1 1/2 L", "pop": 3, "rank": "SS", "title": "Leading the Charge"},
  {"pos": 6, "number": 6, "uma": "Agnes Tachyon", "player": "Cruzi", "strategy": "Pace", "time": "", "gap": "Head", "pop": 5, "rank": "S+", "title": "Leading the Charge"},
  {"pos": 7, "number": 10, "uma": "T.M. Opera O", "player": "agnes", "strategy": "Pace", "time": "", "gap": "Nose", "pop": 1, "rank": "S+", "title": "Centurial Overlord"},
  {"pos": 8, "number": 13, "uma": "Oguri Cap", "player": "Shadow Amber", "strategy": "Pace", "time": "", "gap": "Nose", "pop": 6, "rank": "S", "title": "Ideal Idol"},
  {"pos": 9, "number": 12, "uma": "Air Groove", "player": "agnes", "strategy": "Late", "time": "", "gap": "Head", "pop": 16, "rank": "S", "title": "Empress"},
  {"pos": 10, "number": 4, "uma": "Eishin Flash", "player": "Ananth", "strategy": "Pace", "time": "", "gap": "1 L", "pop": 13, "rank": "SS", "title": "Leading the Charge"},
  {"pos": 11, "number": 11, "uma": "Gold Ship", "player": "Cruzi", "strategy": "End", "time": "", "gap": "3/4 L", "pop": 9, "rank": "S+", "title": "Unpredictable"},
  {"pos": 12, "number": 14, "uma": "Vodka", "player": "Jiinxye", "strategy": "Late", "time": "", "gap": "Neck", "pop": 10, "rank": "S", "title": "Goddess"},
  {"pos": 13, "number": 7, "uma": "Oguri Cap", "player": "Cyclobly", "strategy": "Pace", "time": "", "gap": "1/2 L", "pop": 4, "rank": "SS", "title": "Leading the Charge"},
  {"pos": 14, "number": 15, "uma": "Grass Wonder", "player": "Cyclobly", "strategy": "Late", "time": "", "gap": "Nose", "pop": 2, "rank": "SS+", "title": "Leading the Charge"},
  {"pos": 15, "number": 8, "uma": "Mejiro Ryan", "player": "Haji", "strategy": "Late", "time": "", "gap": "1/2 L", "pop": 12, "rank": "A+", "title": "Mesmerizing Muscle"},
  {"pos": 16, "number": 17, "uma": "Winning Ticket", "player": "Jiinxye", "strategy": "Late", "time": "", "gap": "3/4 L", "pop": 14, "rank": "S", "title": "Herald of a New Age"},
  {"pos": 17, "number": 3, "uma": "Special Week", "player": "Haji", "strategy": "Pace", "time": "", "gap": "1 3/4 L", "pop": 15, "rank": "S", "title": "Leading the Charge"},
  {"pos": 18, "number": 2, "uma": "Super Creek", "player": "Haji", "strategy": "Pace", "time": "", "gap": "1 1/4 L", "pop": 18, "rank": "A", "title": "Legendary Diva"}
]

for p in cup_22: p['umaId'] = slugify(p['uma'])
for p in cup_23: p['umaId'] = slugify(p['uma'])

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Cup 22
pattern_22 = r'(\{\s*"id":\s*22,\s*"cupNumber":\s*22,[\s\S]*?"participants":\s*)\[[\s\S]*?\](\s*\})'
text = re.sub(pattern_22, lambda m: m.group(1) + json.dumps(cup_22, indent=16) + m.group(2), text)

# Replace Cup 23
pattern_23 = r'(\{\s*"id":\s*23,\s*"cupNumber":\s*23,[\s\S]*?"participants":\s*)\[[\s\S]*?\](\s*\})'
text = re.sub(pattern_23, lambda m: m.group(1) + json.dumps(cup_23, indent=16) + m.group(2), text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Cup 22 and 23")
