import json

with open('suscup_1_to_20_data.txt', 'r', encoding='utf-8') as f:
    data = json.load(f)

for r in data['races']:
    for p in r.get('participants', []):
        if p.get('player') == 'agnes':
            print(f"Found agnes in Cup {r['cupNumber']}")
