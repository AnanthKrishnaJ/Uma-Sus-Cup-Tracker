import json
import re

mapping = {
    1: {"number": 11, "pop": 5},
    2: {"number": 2, "pop": 7},
    3: {"number": 17, "pop": 4},
    4: {"number": 9, "pop": 2},
    5: {"number": 5, "pop": 1},
    6: {"number": 1, "pop": 3},
    7: {"number": 10, "pop": 9},
    8: {"number": 4, "pop": 12},
    9: {"number": 15, "pop": 10},
    10: {"number": 6, "pop": 15},
    11: {"number": 18, "pop": 8},
    12: {"number": 7, "pop": 16},
    13: {"number": 3, "pop": 6},
    14: {"number": 16, "pop": 14},
    15: {"number": 14, "pop": 13},
    16: {"number": 12, "pop": 11},
    17: {"number": 13, "pop": 17},
    18: {"number": 8, "pop": 18}
}

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('const INITIAL_DATA = {') + 21
end_idx = text.find('};\n', start_idx) + 1
json_str = text[start_idx:end_idx]

data = json.loads(json_str)

for race in data['races']:
    if race['cupNumber'] == 26 or race['id'] == 26:
        for p in race.get('participants', []):
            pos = p.get('pos', p.get('position', 99))
            if pos in mapping:
                p['number'] = mapping[pos]['number']
                p['pop'] = mapping[pos]['pop']

new_json_str = json.dumps(data, indent=2)
text = text[:start_idx] + new_json_str + text[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Cup 26 missing values.")
