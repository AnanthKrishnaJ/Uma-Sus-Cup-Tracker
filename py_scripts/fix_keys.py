import json
import os

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const NPC_PROFILES = {};')
data_str = text[start + 21:end].strip()
if data_str.endswith(';'):
    data_str = data_str[:-1]
data = json.loads(data_str)

race_29 = next(r for r in data['races'] if r['id'] == '29')

for p in race_29['participants']:
    if 'position' in p:
        p['pos'] = p.pop('position')
    if 'finishTime' in p:
        p['time'] = p.pop('finishTime')

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed participant keys (position -> pos, finishTime -> time).")
