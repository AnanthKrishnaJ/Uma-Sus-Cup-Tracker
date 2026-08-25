import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

for race in data['races']:
    if '27' in str(race.get('cupNumber', '')):
        print(race['name'])
        print('Images:', race.get('images', []))
        for p in race['participants']:
            time_str = p.get('time', 'MISSING')
            pop = p.get('pop', 'MISSING')
            print(f"{p.get('uma')} (Player: {p.get('player')}) - Pos: {p.get('pos')} - Time: {time_str} - Pop: {pop}")
