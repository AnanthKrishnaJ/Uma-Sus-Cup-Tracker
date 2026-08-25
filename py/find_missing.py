import json
import re

with open(r'c:/Users/anant/OneDrive/Desktop/guess/Uma race tracker/.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

json_start = html.find('const INITIAL_DATA = ') + len('const INITIAL_DATA = ')
json_end = html.find('};\n', json_start) + 1
data = json.loads(html[json_start:json_end])

missing = []

for race in data['races']:
    if 21 <= race.get('id', 0) <= 27:
        for p in race.get('participants', []):
            if not p.get('umaId'):
                missing.append(f"Cup {race['id']} - {p['player']} - {p['uma']} missing umaId")
            if '[' in p['uma'] and ']' in p['uma']:
                if not p.get('characterUrl'):
                    missing.append(f"Cup {race['id']} - {p['player']} - {p['uma']} missing characterUrl")
                
for m in missing:
    print(m)

if not missing:
    print('No missing umaId or characterUrls found in Cup 21-27.')
