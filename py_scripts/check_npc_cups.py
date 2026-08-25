import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
db_start = text.find('const UMA_DATABASE = ')
end = text.rfind('};', start, db_start)
data = json.loads(text[start + 21:end + 1])

for race in data['races']:
    if race['cupNumber'] in [16, 17]:
        print(f"Cup {race['cupNumber']}")
        for p in race.get('participants', []):
            if p['player'] == 'NPC' or 'npc' in p.get('umaId', '').lower() or p.get('umaId', '') == 'special-week':
                print(f"  {p['pos']} {p['player']} - {p['uma']} (umaId: {p.get('umaId', 'NOT SET')})")
