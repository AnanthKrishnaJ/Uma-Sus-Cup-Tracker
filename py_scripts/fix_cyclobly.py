import json

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const NPC_PROFILES = {};')
data_str = text[start + 21:end].strip()
if data_str.endswith(';'):
    data_str = data_str[:-1]
data = json.loads(data_str)

changed = False

# Fix races
for race in data.get('races', []):
    for p in race.get('participants', []):
        player = p.get('player', '')
        if player in ['Cyclobly', 'cyclocly', 'cyclobly']:
            p['player'] = 'Cyciesta'
            changed = True

# Fix winners
for winner in data.get('winners', []):
    trainer = winner.get('trainer', '')
    if trainer in ['Cyclobly', 'cyclocly', 'cyclobly']:
        winner['trainer'] = 'Cyciesta'
        changed = True
        
    player = winner.get('player', '')
    if player in ['Cyclobly', 'cyclocly', 'cyclobly']:
        winner['player'] = 'Cyciesta'
        changed = True

if changed:
    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    text = text[:start + 21] + new_json + ';\n        ' + text[end:]

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed all occurrences of Cyclobly to Cyciesta.")
else:
    print("No occurrences of Cyclobly found.")
