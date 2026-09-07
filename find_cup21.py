import json

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

target_umas = {"Taiki Shuttle", "Curren Chan", "Sakura Bakushin O", "Haru Urara"}

for race in data['races']:
    umas = {p.get('uma') for p in race.get('participants', [])}
    if target_umas.issubset(umas):
        print(f"Match found! Cup {race.get('id')} ({race.get('cupNumber')}): {race.get('name')}")
