import json

# Load index.html
html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('const INITIAL_DATA = {') + 21
end_idx = text.find('};\n', start_idx) + 1
if end_idx == 0:
    end_idx = text.find('};\r\n', start_idx) + 1

json_str = text[start_idx:end_idx]
try:
    data = json.loads(json_str)
except Exception as e:
    # try fallback
    end_idx = text.find('};', start_idx) + 1
    json_str = text[start_idx:end_idx]
    data = json.loads(json_str)

# Load the text file
with open('suscup_1_to_20_data.txt', 'r', encoding='utf-8') as f:
    text_data = json.load(f)

# Normalize text file data
new_races = text_data.get('races', [])
for r in new_races:
    for p in r.get('participants', []):
        if p.get('player') == 'Cyclobly':
            p['player'] = 'Cyciesta'
        if p.get('player') == 'agnes':
            p['player'] = 'Agnes'

# Remove existing races 1-20
existing_races = [r for r in data.get('races', []) if r.get('id') not in range(1, 21)]

# Combine and sort
combined_races = existing_races + new_races
combined_races.sort(key=lambda x: x.get('id', 999))

data['races'] = combined_races

# Write back
new_json_str = json.dumps(data, indent=2)
text = text[:start_idx] + new_json_str + text[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Merged races 1-20 successfully.")
