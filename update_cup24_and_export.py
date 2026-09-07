import json
import os
import re

cup_24_ranks = {
    1: "S", 2: "SS", 3: "SS", 4: "S+", 5: "S+", 6: "S+", 7: "S", 8: "S+", 9: "S+",
    10: "S", 11: "A", 12: "A", 13: "A", 14: "A", 15: "A", 16: "A", 17: "A", 18: "A"
}

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('const INITIAL_DATA = {') + 21
end_idx = text.find('};\n', start_idx) + 1
if end_idx == 0: end_idx = text.find('};\r\n', start_idx) + 1
try:
    data = json.loads(text[start_idx:end_idx])
except:
    data = json.loads(text[start_idx:text.find('};', start_idx) + 1])

# Update Cup 24 ranks
for race in data['races']:
    if race['cupNumber'] == 24 or race['id'] == 24:
        for p in race.get('participants', []):
            pos = p.get('pos', p.get('position', 99))
            if pos in cup_24_ranks:
                p['rank'] = cup_24_ranks[pos]

# Save index.html
new_json_str = json.dumps(data, indent=2)
text = text[:start_idx] + new_json_str + text[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Create backup folder
backup_dir = 'backup_exports'
os.makedirs(backup_dir, exist_ok=True)

# 1. Export ALL races 1 to 28
def get_cup_num(race_or_winner):
    cup_str = str(race_or_winner.get('cupNumber', race_or_winner.get('id', race_or_winner.get('cup', ''))))
    match = re.search(r'\d+', cup_str)
    if match:
        return int(match.group())
    return None

all_races = [r for r in data['races'] if get_cup_num(r) and 1 <= get_cup_num(r) <= 28]
all_winners = [w for w in data.get('winners', []) if get_cup_num(w) and 1 <= get_cup_num(w) <= 28]

with open(os.path.join(backup_dir, 'suscup_1_to_28_details.txt'), 'w', encoding='utf-8') as f:
    json.dump({'races': all_races, 'winners': all_winners}, f, indent=2)

# 2. Export INDIVIDUAL races 1 to 28
for cup_id in range(1, 29):
    races_for_cup = [r for r in data['races'] if get_cup_num(r) == cup_id]
    winners_for_cup = [w for w in data.get('winners', []) if get_cup_num(w) == cup_id]
    
    if races_for_cup or winners_for_cup:
        filepath = os.path.join(backup_dir, f'suscup_{cup_id}_details.txt')
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({'races': races_for_cup, 'winners': winners_for_cup}, f, indent=2)

print("Updated Cup 24 ranks and created backup_exports folder with all txt files.")
