import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

for race in data['races']:
    if str(race.get('cupNumber')) == 'SUS CUP 6':
        for p in race['participants']:
            print(f"{p.get('pos')} | {p.get('uma')} | ID: {p.get('umaId')}")
