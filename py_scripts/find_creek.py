import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

for race in data['races']:
    for p in race['participants']:
        if p.get('player') == 'Agnes' and 'Super Creek' in p.get('uma', ''):
            print(f"Found in cup: {race.get('cupNumber')}")
