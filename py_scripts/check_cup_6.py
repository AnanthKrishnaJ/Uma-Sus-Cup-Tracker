import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

found = False
for race in data['races']:
    if str(race.get('cupNumber')) == '6':
        print(f"Found Cup 6 with {len(race['participants'])} participants")
        print(f"Participant 1: {race['participants'][0]}")
        found = True
if not found:
    print('Cup 6 not found')
