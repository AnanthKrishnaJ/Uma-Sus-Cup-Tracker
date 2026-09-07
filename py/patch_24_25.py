import json
import re

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

cup_24 = [
  {"pos": 1, "number": 9, "uma": "Mejiro Dober", "player": "jayreative", "strategy": "Late", "time": "1:56.6", "gap": "", "pop": 8, "rank": "S", "title": "Coolheaded Beauty"},
  {"pos": 2, "number": 7, "uma": "Oguri Cap", "player": "Cyclobly", "strategy": "Pace", "time": "", "gap": "1 3/4 L", "pop": 1, "rank": "SS", "title": "Leading the Charge"},
  {"pos": 3, "number": 18, "uma": "Maruzensky", "player": "Vilthaar", "strategy": "Front", "time": "", "gap": "1 1/4 L", "pop": 3, "rank": "SS", "title": "Leading the Charge"},
  {"pos": 4, "number": 6, "uma": "Admire Vega", "player": "GohanXGAMER", "strategy": "End", "time": "", "gap": "3/4 L", "pop": 4, "rank": "S+", "title": "Leading the Charge"},
  {"pos": 5, "number": 16, "uma": "Agnes Tachyon", "player": "Cruzi", "strategy": "Pace", "time": "", "gap": "Neck", "pop": 5, "rank": "S+", "title": "Leading the Charge"},
  {"pos": 6, "number": 2, "uma": "Oguri Cap", "player": "eviskno", "strategy": "Pace", "time": "", "gap": "1 1/4 L", "pop": 6, "rank": "S+", "title": "Ideal Idol"},
  {"pos": 7, "number": 1, "uma": "Narita Taishin", "player": "Jiinxye", "strategy": "End", "time": "", "gap": "1 L", "pop": 10, "rank": "S", "title": "Phenomenal"},
  {"pos": 8, "number": 11, "uma": "Symboli Rudolf", "player": "agnes", "strategy": "Late", "time": "", "gap": "3/4 L", "pop": 2, "rank": "S+", "title": "Emperor"},
  {"pos": 9, "number": 12, "uma": "Fuji Kiseki", "player": "Ananth", "strategy": "Pace", "time": "", "gap": "1 1/2 L", "pop": 7, "rank": "S", "title": "Leading the Charge"},
  {"pos": 10, "number": 10, "uma": "Special Week", "player": "Haji", "strategy": "Pace", "time": "", "gap": "3/4 L", "pop": 9, "rank": "S", "title": "Leading the Charge"}
]

cup_25 = [
  {"pos": 1, "number": 11, "uma": "Oguri Cap", "player": "Cyclobly", "strategy": "Pace", "time": "1:56.4", "gap": "", "pop": 5, "rank": "SS", "title": "Ideal Idol"},
  {"pos": 2, "number": 2, "uma": "Seiun Sky", "player": "Cyclobly", "strategy": "Front", "time": "", "gap": "3/4 L", "pop": 7, "rank": "S+", "title": "Leading the Charge"},
  {"pos": 3, "number": 17, "uma": "Mihono Bourbon", "player": "Cruzi", "strategy": "Front", "time": "", "gap": "1 L", "pop": 4, "rank": "SS", "title": "Leading the Charge"},
  {"pos": 4, "number": 9, "uma": "Symboli Rudolf", "player": "Cruzi", "strategy": "Pace", "time": "", "gap": "1 1/2 L", "pop": 2, "rank": "SS", "title": "Emperor"},
  {"pos": 5, "number": 5, "uma": "Seiun Sky", "player": "GohanXGAMER", "strategy": "Front", "time": "", "gap": "Neck", "pop": 1, "rank": "S+", "title": "Leading the Charge"},
  {"pos": 6, "number": 1, "uma": "Rice Shower", "player": "Cyclobly", "strategy": "Front", "time": "", "gap": "1 3/4 L", "pop": 3, "rank": "SS", "title": "Sable Assassin"},
  {"pos": 7, "number": 10, "uma": "Special Week", "player": "agnes", "strategy": "Late", "time": "", "gap": "3/4 L", "pop": 9, "rank": "S+", "title": "Incredible"},
  {"pos": 8, "number": 4, "uma": "Gold City", "player": "Jiinxye", "strategy": "Late", "time": "", "gap": "3/4 L", "pop": 12, "rank": "S", "title": "Epoch Pioneer"},
  {"pos": 9, "number": 15, "uma": "Super Creek", "player": "agnes", "strategy": "Pace", "time": "", "gap": "Neck", "pop": 10, "rank": "S", "title": "Leading the Charge"},
  {"pos": 10, "number": 6, "uma": "Tokai Teio", "player": "Jiinxye", "strategy": "Pace", "time": "", "gap": "Nose", "pop": 15, "rank": "S", "title": "Leading the Charge"},
  {"pos": 11, "number": 18, "uma": "Gold City", "player": "agnes", "strategy": "Late", "time": "", "gap": "2 L", "pop": 8, "rank": "S+", "title": "Leading the Charge"},
  {"pos": 12, "number": 7, "uma": "Gold City", "player": "Ananth", "strategy": "Pace", "time": "", "gap": "Nose", "pop": 16, "rank": "S", "title": "Leading the Charge"},
  {"pos": 13, "number": 3, "uma": "Mayano Top Gun", "player": "Cruzi", "strategy": "Pace", "time": "", "gap": "Neck", "pop": 6, "rank": "SS", "title": "Leading the Charge"},
  {"pos": 14, "number": 16, "uma": "Air Groove", "player": "Ananth", "strategy": "Pace", "time": "", "gap": "1/2 L", "pop": 14, "rank": "S", "title": "Leading the Charge"},
  {"pos": 15, "number": 14, "uma": "El Condor Pasa", "player": "Jiinxye", "strategy": "Late", "time": "", "gap": "Nose", "pop": 13, "rank": "S", "title": "Leading the Charge"},
  {"pos": 16, "number": 12, "uma": "Special Week", "player": "GohanXGAMER", "strategy": "Late", "time": "", "gap": "Nose", "pop": 11, "rank": "S", "title": "Leading the Charge"},
  {"pos": 17, "number": 13, "uma": "Biwa Hayahide", "player": "GohanXGAMER", "strategy": "Pace", "time": "", "gap": "Neck", "pop": 17, "rank": "A+", "title": "Witness to Legend"}
]

for p in cup_24: p['umaId'] = slugify(p['uma'])
for p in cup_25: p['umaId'] = slugify(p['uma'])

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Cup 24
pattern_24 = r'(\{\s*"id":\s*24,\s*"cupNumber":\s*24,[\s\S]*?"participants":\s*)\[[\s\S]*?\](\s*\})'
text = re.sub(pattern_24, lambda m: m.group(1) + json.dumps(cup_24, indent=16) + m.group(2), text)

# Replace Cup 25
pattern_25 = r'(\{\s*"id":\s*25,\s*"cupNumber":\s*25,[\s\S]*?"participants":\s*)\[[\s\S]*?\](\s*\})'
text = re.sub(pattern_25, lambda m: m.group(1) + json.dumps(cup_25, indent=16) + m.group(2), text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Cup 24 and 25")
