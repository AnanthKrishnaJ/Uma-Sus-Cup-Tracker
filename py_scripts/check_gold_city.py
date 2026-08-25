import json
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
data_str = text[start + 21:text.find('const UMA_DATABASE =')].strip().rstrip(';')
data = json.loads(data_str)

for race in data.get('races', []):
    for p in race.get('participants', []):
        if 'Gold City' in p.get('uma', ''):
            print(f"Found Gold City in Cup {race.get('cupNumber')}: pos={p.get('pos')} no={p.get('number')} url={p.get('characterUrl')}")
