import json
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('const INITIAL_DATA = {') + 21
end_idx = text.find('};\n', start_idx) + 1
if end_idx == 0: end_idx = text.find('};\r\n', start_idx) + 1
data = json.loads(text[start_idx:end_idx])

for race in data['races']:
    if race['cupNumber'] == 25 or race['id'] == 25:
        print('Cup 25:')
        for p in sorted(race.get('participants', []), key=lambda x: x.get('pos', 99)):
            print(f"{p.get('pos')} | {p.get('uma')}")
    if race['cupNumber'] == 26 or race['id'] == 26:
        print('Cup 26:')
        for p in sorted(race.get('participants', []), key=lambda x: x.get('pos', 99)):
            print(f"{p.get('pos')} | {p.get('uma')}")
    if race['cupNumber'] == 24 or race['id'] == 24:
        print('Cup 24:')
        for p in sorted(race.get('participants', []), key=lambda x: x.get('pos', 99)):
            print(f"{p.get('pos')} | {p.get('uma')}")
