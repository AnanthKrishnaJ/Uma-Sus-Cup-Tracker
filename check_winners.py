import json
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()
start_idx = text.find('const INITIAL_DATA = {') + 21
try:
    end_idx = text.find('};\n', start_idx) + 1
    if end_idx == 0: end_idx = text.find('};\r\n', start_idx) + 1
    data = json.loads(text[start_idx:end_idx])
except:
    end_idx = text.find('};', start_idx) + 1
    data = json.loads(text[start_idx:end_idx])

print('Winners of Cups 21-28:')
for race in data.get('races', []):
    cup = str(race.get('cupNumber', race.get('id', 'Unknown')))
    for p in race.get('participants', []):
        if p.get('pos', p.get('position')) == 1:
            print(f"Cup {cup}: {p.get('player')} ({p.get('uma')})")
