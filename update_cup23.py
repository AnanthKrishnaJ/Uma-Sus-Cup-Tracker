import json

mapping = {
    1: {"number": 16, "rank": "SS", "title": "Phenomenal", "player": "Jiinxye", "strategy": "End", "time": "1:56.1", "pop": 17},
    2: {"number": 18, "rank": "S", "title": "Leading the Charge", "player": "Shadow Amber", "strategy": "Pace", "time": "1 L", "pop": 8},
    3: {"number": 5, "rank": "SS", "title": "Leading the Charge", "player": "Cruzi", "strategy": "Front", "time": "Head", "pop": 11},
    4: {"number": 1, "rank": "S+", "title": "Goddess", "player": "Agnes", "strategy": "Late", "time": "Head", "pop": 7},
    5: {"number": 9, "rank": "SS", "title": "Leading the Charge", "player": "Cyciesta", "strategy": "Late", "time": "1 1/2 L", "pop": 3},
    6: {"number": 6, "rank": "S+", "title": "Leading the Charge", "player": "Cruzi", "strategy": "Pace", "time": "Head", "pop": 5},
    7: {"number": 10, "rank": "S+", "title": "Centurial Overlord", "player": "Agnes", "strategy": "Pace", "time": "Nose", "pop": 1},
    8: {"number": 13, "rank": "S", "title": "Ideal Idol", "player": "Shadow Amber", "strategy": "Pace", "time": "Nose", "pop": 6},
    9: {"number": 12, "rank": "S", "title": "Empress", "player": "Agnes", "strategy": "Late", "time": "Head", "pop": 16},
    10: {"number": 4, "rank": "SS", "title": "Leading the Charge", "player": "Ananth", "strategy": "Pace", "time": "1 L", "pop": 13},
    11: {"number": 11, "rank": "S", "title": "Unpredictable", "player": "Cruzi", "strategy": "End", "time": "3/4 L", "pop": 9},
    12: {"number": 14, "rank": "S", "title": "Goddess", "player": "Jiinxye", "strategy": "Late", "time": "Neck", "pop": 10},
    13: {"number": 7, "rank": "SS", "title": "Leading the Charge", "player": "Cyciesta", "strategy": "Pace", "time": "1/2 L", "pop": 4},
    14: {"number": 15, "rank": "SS", "title": "Leading the Charge", "player": "Cyciesta", "strategy": "Late", "time": "Nose", "pop": 2},
    15: {"number": 8, "rank": "A+", "title": "Mesmerizing Muscle", "player": "Haji", "strategy": "Late", "time": "1/2 L", "pop": 12},
    16: {"number": 17, "rank": "S", "title": "Herald of a New Age", "player": "Jiinxye", "strategy": "Late", "time": "3/4 L", "pop": 14},
    17: {"number": 3, "rank": "S", "title": "Leading the Charge", "player": "Haji", "strategy": "Pace", "time": "1 3/4 L", "pop": 15},
    18: {"number": 2, "rank": "A+", "title": "Legendary Diva", "player": "Haji", "strategy": "Pace", "time": "1 1/4 L", "pop": 18}
}

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('const INITIAL_DATA = {') + 21
end_idx = text.find('};\n', start_idx) + 1
if end_idx == 0:
    end_idx = text.find('};\r\n', start_idx) + 1
try:
    data = json.loads(text[start_idx:end_idx])
except:
    data = json.loads(text[start_idx:text.find('};', start_idx) + 1])

for race in data['races']:
    if race['cupNumber'] == 23 or race['id'] == 23:
        for p in race.get('participants', []):
            pos = p.get('pos', p.get('position', 99))
            if pos in mapping:
                for key, value in mapping[pos].items():
                    p[key] = value
                p['gap'] = mapping[pos]['time'] # Set gap to time as well

# Also check Cup 23 Winner and update its time
for w in data.get('winners', []):
    if w.get('cup') == 'Sus Cup 23':
        w['result'] = '1:56.1'

new_json_str = json.dumps(data, indent=2)
text = text[:start_idx] + new_json_str + text[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Cup 23 full details.")
