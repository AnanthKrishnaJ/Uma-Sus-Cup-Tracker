import json

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
    if race['cupNumber'] == 21 or race['id'] == 21:
        print(f"Cup 21 found! Name: {race.get('name')}")
        for p in sorted(race.get('participants', []), key=lambda x: x.get('pos', x.get('position', 99))):
            print(f"{p.get('pos', p.get('position', 99))} | {p.get('uma')} | rank: {p.get('rank')}")
