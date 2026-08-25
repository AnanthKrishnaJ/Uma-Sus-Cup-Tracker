import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
db_start = text.find('const UMA_DATABASE = ')
end = text.rfind('};', start, db_start)
data = json.loads(text[start + 21:end + 1])

# Extract DB
db_end = text.rfind('};', db_start)
db_str = text[db_start + 21:db_end + 1]

for race in data['races']:
    if race['cupNumber'] == 26 or race['id'] == 26:
        for p in race.get('participants', []):
            if p['uma'] == 'Air Shakur':
                p['umaId'] = '103601'
            elif p['uma'] == 'Mayano Top Gun':
                p['umaId'] = '102402'
            elif p['uma'] == 'Gold City':
                p['umaId'] = '104002'
            elif p['uma'] == 'Gold Ship':
                p['umaId'] = '100702'

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_text = text[:start + 21] + new_json + text[end + 1:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated Cup 26 participants!")
