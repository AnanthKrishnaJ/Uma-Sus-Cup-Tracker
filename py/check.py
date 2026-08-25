import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'c:/Users/anant/OneDrive/Desktop/guess/Uma race tracker/.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()
    json_start = html.find('const INITIAL_DATA = ') + len('const INITIAL_DATA = ')
    json_end = html.find('};\n', json_start) + 1
    data = json.loads(html[json_start:json_end])
    for race in data['races']:
        if 'scenarioWinners' in race or 'specialWinners' in race:
            print(f'Cup {race.get("id")} has winners')
