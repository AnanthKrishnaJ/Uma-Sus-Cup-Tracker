import json

with open(r'c:/Users/anant/OneDrive/Desktop/guess/Uma race tracker/.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

json_start = html.find('const INITIAL_DATA = ') + len('const INITIAL_DATA = ')
json_end = html.find('};\n', json_start) + 1
data = json.loads(html[json_start:json_end])

with open('check_21_27.txt', 'w', encoding='utf-8') as out:
    for race in data['races']:
        if 21 <= race.get('id', 0) <= 27:
            for p in race.get('participants', []):
                out.write(f"Cup {race['id']} | {p['uma']} | umaId: {p.get('umaId')} | characterUrl: {p.get('characterUrl')}\n")
