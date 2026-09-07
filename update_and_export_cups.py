import json
import os

cup24_ranks = [
    "S", "SS", "SS", "S+", "S+", "S+", "S", "S+", "S+", "S", 
    "A", "A", "A", "A", "A", "A", "A", "A"
]

cup25_ranks = [
    "SS", "S+", "SS", "SS", "S+", "SS", "S+", "S", "S", "S", 
    "S", "S", "SS", "S", "S", "S", "A+", "B+"
]

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data if isinstance(data, list) else data.get('races', [])

all_races = []
all_races.extend(load_json('suscup_1_to_10_data.txt'))
all_races.extend(load_json('suscup_11_to_20_data.txt'))
races_21_28 = load_json('suscup_21_to_28_details.txt')

for race in races_21_28:
    if race['cupNumber'] == 'SUS CUP 24':
        for p in race['participants']:
            pos = p['pos']
            if 1 <= pos <= 18:
                p['rank'] = cup24_ranks[pos - 1]
    if race['cupNumber'] == 'SUS CUP 25':
        for p in race['participants']:
            pos = p['pos']
            if 1 <= pos <= 18:
                p['rank'] = cup25_ranks[pos - 1]

all_races.extend(races_21_28)

with open('suscup_21_to_28_details.txt', 'w', encoding='utf-8') as f:
    json.dump({"races": races_21_28}, f, indent=2)

out_dir = 'suscup_race_details'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

with open(os.path.join(out_dir, 'suscup_1_to_28_details.txt'), 'w', encoding='utf-8') as f:
    json.dump({"races": all_races}, f, indent=2)

for race in all_races:
    cup_num = race['id']
    with open(os.path.join(out_dir, f'suscup_{cup_num}.txt'), 'w', encoding='utf-8') as f:
        json.dump(race, f, indent=2)

print("Done exporting races.")

# Check cyciesta wins
cy_wins = 0
for race in all_races:
    for p in race.get('participants', []):
        player = p['player'].strip()
        if player.lower() in ['cyciesta', 'cyclobly'] and p['pos'] == 1:
            cy_wins += 1
            print(f"Won {race['cupNumber']} with {p['uma']}")

print(f"Cyciesta total wins: {cy_wins}")
