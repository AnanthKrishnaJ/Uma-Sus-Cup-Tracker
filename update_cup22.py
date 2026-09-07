import json

mapping = {
    1: {'rank': 'S', 'time': '3:13.4'},
    2: {'rank': 'S', 'time': '1 3/4 L'},
    3: {'rank': 'S', 'time': '3 1/2 L'},
    4: {'rank': 'A', 'time': '1 1/2 L'},
    5: {'rank': 'S', 'time': '1/2 L'},
    6: {'rank': 'S', 'time': '1 1/4 L'},
    7: {'rank': 'A', 'time': '4 L'},
    8: {'rank': 'A+', 'time': '5 L'},
    9: {'rank': 'S', 'time': '2 1/2 L'},
    10: {'rank': 'A', 'time': '2 L'},
    11: {'rank': 'S', 'time': 'Head'},
    12: {'rank': 'A+', 'time': '3 1/2 L'},
    13: {'rank': 'A', 'time': '3 1/2 L'},
    14: {'rank': 'A+', 'time': '5 L'},
    15: {'rank': 'A', 'time': 'Distance'},
    16: {'rank': 'A+', 'time': '1/2 L'},
    17: {'rank': 'A+', 'time': '5 L'},
    18: {'rank': 'B+', 'time': '6 L'}
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
    if race['cupNumber'] == 22 or race['id'] == 22:
        for p in race.get('participants', []):
            pos = p.get('pos', p.get('position', 99))
            if pos in mapping:
                p['rank'] = mapping[pos]['rank']
                p['time'] = mapping[pos]['time']
                p['gap'] = mapping[pos]['time']

# Also check Cup 22 Winner and update its time
for w in data.get('winners', []):
    if w.get('cup') == 'Sus Cup 22':
        w['result'] = '3:13.4'

new_json_str = json.dumps(data, indent=2)
text = text[:start_idx] + new_json_str + text[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Cup 22 ranks and times.")
