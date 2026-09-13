import json
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const NPC_PROFILES = {};')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

race_29 = next(r for r in data['races'] if str(r['id']) == '29')

rank_mapping = {
    1: ('UG3', 11),
    2: ('UG1', 3),
    3: ('UG', 14),
    4: ('UG2', 12),
    5: ('UG8', 5),
    6: ('UG6', 16),
    7: ('UG2', 2),
    8: ('UG7', 8),
    9: ('UG4', 7),
    10: ('UG', 4),
    11: ('A+', 17),
    12: ('A+', 18),
    13: ('A+', 11),
    14: ('A+', 9),
    15: ('A+', 6),
    16: ('A+', 15),
    17: ('S+', 13),
    18: ('UF3', 10)
}

for p in race_29['participants']:
    pos = int(p['pos'])
    if pos in rank_mapping:
        p['rank'] = rank_mapping[pos][0]
        # Also update number if necessary, but the prompt says 'Runner No.' which might be the number
        p['number'] = rank_mapping[pos][1]
    
new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_text = text[:start + 21] + new_json + '\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Ranks updated successfully!")
