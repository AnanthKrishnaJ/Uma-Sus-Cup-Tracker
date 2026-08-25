import json
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
data_str = text[start + 21:text.find('const UMA_DATABASE =')].strip().rstrip(';')
data = json.loads(data_str)

for race in data.get('races', []):
    if str(race.get('cupNumber')) == 'SUS CUP 18' or str(race.get('cupNumber')) == '18':
        for p in race.get('participants', []):
            if 'Symboli' in p.get('uma', ''):
                print(f"uma={p.get('uma')} pos={p.get('pos')} no={p.get('number')}")
