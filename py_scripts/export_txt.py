import json
import os

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const NPC_PROFILES = {};')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

races = data.get('races', [])

out_dir = 'suscup_race_details'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

all_suscups = []
for race in races:
    cup_name = race.get('cupName', '')
    if 'Sus Cup' in cup_name or 'SUS CUP' in cup_name.upper():
        all_suscups.append(race)
        cup_num = race.get('id')
        if cup_num:
            with open(os.path.join(out_dir, f'suscup_{cup_num}.txt'), 'w', encoding='utf-8') as f:
                json.dump(race, f, indent=2, ensure_ascii=False)

with open(os.path.join(out_dir, 'suscup_1_to_29_details.txt'), 'w', encoding='utf-8') as f:
    json.dump({"races": all_suscups}, f, indent=2, ensure_ascii=False)

print(f"Exported {len(all_suscups)} Sus Cup races to {out_dir}")
