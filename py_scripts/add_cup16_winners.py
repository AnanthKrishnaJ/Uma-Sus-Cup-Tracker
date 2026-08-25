import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data = json.loads(text[start + 21:end].strip().rstrip(';'))

# Get Cup 16 participants
cup16_race = None
for r in data['races']:
    if '16' in str(r.get('cupNumber')):
        cup16_race = r
        break

if cup16_race:
    winners_to_add = []
    # Pos 1, 3, 4
    for p in cup16_race['participants']:
        if p['pos'] in [1, 3, 4]:
            winner = {
                "cup": "Sus Cup 16",
                "trainer": p['player'],
                "uma": p['uma'],
                "version": p['version'],
                "url": p.get('characterUrl', ''),
                "race": cup16_race['name'],
                "date": cup16_race['date'],
                "result": p.get('time', p.get('gap', '')),
                "umaId": p.get('umaId')
            }
            winners_to_add.append(winner)
            
    # Add them to winners array
    # Check if they are already in the winners array
    existing_winners = data.get('winners', [])
    # Remove any existing Cup 16 winners just to be safe
    data['winners'] = [w for w in existing_winners if '16' not in str(w.get('cup', ''))]
    data['winners'].extend(winners_to_add)

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Added Cup 16 winners!")
