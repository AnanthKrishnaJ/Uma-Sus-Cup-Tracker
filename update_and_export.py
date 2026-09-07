import json

mapping_27_med = {
    1: '2:10.5', 2: '1 1/4 L', 3: '1 1/2 L', 4: '1/2 L', 5: 'Nose',
    6: '3 1/2 L', 7: '3/4 L', 8: '3/4 L', 9: '1 L', 10: '1 L',
    11: '4 L', 12: '1/2 L', 13: 'Nose', 14: '1/2 L', 15: 'Nose',
    16: 'Head', 17: 'Neck', 18: '1 1/4 L'
}

mapping_24_num = {
    1: 9, 2: 7, 3: 18, 4: 6, 5: 16, 6: 2, 7: 1, 8: 11, 9: 12,
    10: 10, 11: 17, 12: 4, 13: 15, 14: 5, 15: 14, 16: 13, 17: 8, 18: 3
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
    # Update Cup 24 Numbers
    if race['cupNumber'] == 24 or race['id'] == 24:
        for p in race.get('participants', []):
            pos = p.get('pos', p.get('position', 99))
            if pos in mapping_24_num:
                p['number'] = mapping_24_num[pos]
    
    # Update Cup 27 Medium finish time / gap
    if (race['cupNumber'] == 27 or race['id'] == 27) and race.get('distanceType') == 'Medium':
        for p in race.get('participants', []):
            pos = p.get('pos', p.get('position', 99))
            if pos in mapping_27_med:
                p['time'] = mapping_27_med[pos]
                p['gap'] = mapping_27_med[pos]

# Also check Cup 27 Medium Winner and update its time
for w in data.get('winners', []):
    if w.get('cup') == 'Sus Cup 27' and w.get('race') == 'Queen Elizabeth II Cup':
        w['result'] = '2:10.5'

new_json_str = json.dumps(data, indent=2)
text = text[:start_idx] + new_json_str + text[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Save cups 21 to 28 in a text file
cups_21_28 = [r for r in data['races'] if r.get('id') in range(21, 29) or (isinstance(r.get('cupNumber'), int) and r.get('cupNumber') in range(21, 29)) or (isinstance(r.get('cupNumber'), str) and any(str(i) in r.get('cupNumber') for i in range(21, 29)))]
winners_21_28 = [w for w in data.get('winners', []) if any(str(i) in w.get('cup', '') for i in range(21, 29))]

export_data = {
    "races": cups_21_28,
    "winners": winners_21_28
}

with open('suscup_21_to_28_details.txt', 'w', encoding='utf-8') as f:
    json.dump(export_data, f, indent=2)

print("Updated Cup 27 Medium and Cup 24. Exported Cups 21-28.")
