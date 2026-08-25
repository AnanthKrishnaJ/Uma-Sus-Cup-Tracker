import json
import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

db_start = content.find('const UMA_DATABASE = ') + 21
db_end = content.find('};', db_start) + 1
uma_db_str = content[db_start:db_end]
# This is JS object, not strict JSON. Let's extract keys and images using regex.
uma_db = {}
for match in re.finditer(r'"([^"]+)":\s*{(.*?)}', uma_db_str):
    key = match.group(1)
    val_str = match.group(2)
    # Extract image
    img_match = re.search(r'image:\s*(null|"[^"]+")', val_str)
    if img_match:
        img_val = img_match.group(1)
        if img_val == 'null':
            uma_db[key] = None
        else:
            uma_db[key] = img_val.strip('"')
    else:
        uma_db[key] = None

start = content.find('const INITIAL_DATA = ') + 21
end = content.find('};', start) + 1
initial_data = json.loads(content[start:end])

missing_images = set()

for race in initial_data['races']:
    if 'participants' in race:
        for p in race['participants']:
            uma_id = p.get('umaId')
            if not uma_id:
                # generate id from name
                uma_id = p['uma'].lower().replace(' ', '-').replace('.', '').replace('\'', '')
            
            # Check if image exists
            if uma_id not in uma_db or uma_db[uma_id] is None:
                # ignore npcs
                if p.get('player') == 'NPC' or p.get('player') == 'Unknown' or p.get('player') == '' or p.get('player') == '':
                    continue
                missing_images.add((p['uma'], uma_id))

print("Missing Images for non-NPCs:")
for name, uid in missing_images:
    print(f"- {name} (ID: {uid})")
