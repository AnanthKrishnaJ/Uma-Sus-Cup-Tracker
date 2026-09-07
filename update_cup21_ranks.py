import json

mapping = {
    1: 'A+',
    2: 'S',
    3: 'A+',
    4: 'A+',
    5: 'A+',
    6: 'S+',
    7: 'A+',
    8: 'A+',
    9: 'S+',
    10: 'A+',
    11: 'A+',
    12: 'A+',
    13: 'B+',
    14: 'B+',
    15: 'B+',
    16: 'A+',
    17: 'A',
    18: 'S'
}

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('const INITIAL_DATA = {') + 21
end_idx = text.find('};\n', start_idx) + 1
if end_idx == 0:
    end_idx = text.find('};\r\n', start_idx) + 1
try:
    data = json.loads(text[start_idx:end_idx])
except:
    data = json.loads(text[start_idx:text.find('};', start_idx) + 1])

for race in data['races']:
    if race['cupNumber'] == 21 or race['id'] == 21:
        for p in race.get('participants', []):
            # Normalize names
            if p.get('player') == 'Cyclobly':
                p['player'] = 'Cyciesta'
            if p.get('player') == 'agnes':
                p['player'] = 'Agnes'
            
            # Apply ranks
            pos = p.get('pos', p.get('position', 99))
            if pos in mapping:
                p['rank'] = mapping[pos]
        
        # Normalize special winners
        if 'specialWinners' in race:
            for k, v in race['specialWinners'].items():
                if v.get('player') == 'Cyclobly':
                    v['player'] = 'Cyciesta'
                if v.get('player') == 'agnes':
                    v['player'] = 'Agnes'

# Normalize winner for Cup 21
for w in data.get('winners', []):
    if w.get('cup') == 'Sus Cup 21':
        if w.get('trainer') == 'Cyclobly':
            w['trainer'] = 'Cyciesta'
        if w.get('trainer') == 'agnes':
            w['trainer'] = 'Agnes'

new_json_str = json.dumps(data, indent=2)
text = text[:start_idx] + new_json_str + text[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Cup 21 ranks and normalized names.")
