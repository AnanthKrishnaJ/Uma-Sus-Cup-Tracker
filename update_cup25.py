import json

cup_25_data = [
    {"pos": 1, "uma": "Oguri Cap", "rank": "SS"},
    {"pos": 2, "uma": "Seiun Sky", "rank": "S+"},
    {"pos": 3, "uma": "Mihono Bourbon", "rank": "SS"},
    {"pos": 4, "uma": "Symboli Rudolf", "rank": "SS"},
    {"pos": 5, "uma": "Seiun Sky", "rank": "S+"},
    {"pos": 6, "uma": "Rice Shower", "rank": "SS"},
    {"pos": 7, "uma": "Special Week", "rank": "S+"},
    {"pos": 8, "uma": "Gold City", "rank": "S"},
    {"pos": 9, "uma": "Super Creek", "rank": "S"},
    {"pos": 10, "uma": "Tokai Teio", "rank": "S"},
    {"pos": 11, "uma": "Gold City", "rank": "S"},
    {"pos": 12, "uma": "Gold City", "rank": "S"},
    {"pos": 13, "uma": "Mayano Top Gun", "rank": "SS"},
    {"pos": 14, "uma": "Air Groove", "rank": "S"},
    {"pos": 15, "uma": "El Condor Pasa", "rank": "S"},
    {"pos": 16, "uma": "Special Week", "rank": "S"},
    {"pos": 17, "uma": "Biwa Hayahide", "rank": "A+"},
    {"pos": 18, "uma": "Tamaxchi", "rank": "B+"}
]

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

for race in data['races']:
    if race['cupNumber'] == 25 or race['id'] == 25:
        # Match by uma name, but since there are duplicate uma names in the list (e.g., Seiun Sky x2, Gold City x3), 
        # it's better to just assign them in order if we can. Or we can just map the array entirely.
        # But wait, participants currently in Cup 25 have player names, numbers, etc.
        # Let's match by name, and if multiple, pop from the list of updates for that uma.
        
        updates_by_uma = {}
        for update in cup_25_data:
            if update['uma'] not in updates_by_uma:
                updates_by_uma[update['uma']] = []
            updates_by_uma[update['uma']].append(update)
            
        for p in race.get('participants', []):
            uma_name = p.get('uma')
            if uma_name in updates_by_uma and len(updates_by_uma[uma_name]) > 0:
                update = updates_by_uma[uma_name].pop(0)
                p['pos'] = update['pos']
                p['rank'] = update['rank']

new_json_str = json.dumps(data, indent=2)
text = text[:start_idx] + new_json_str + text[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Re-export cups 21 to 28
cups_21_28 = [r for r in data['races'] if r.get('id') in range(21, 29) or (isinstance(r.get('cupNumber'), int) and r.get('cupNumber') in range(21, 29)) or (isinstance(r.get('cupNumber'), str) and any(str(i) in r.get('cupNumber') for i in range(21, 29)))]
winners_21_28 = [w for w in data.get('winners', []) if any(str(i) in w.get('cup', '') for i in range(21, 29))]
export_data = {"races": cups_21_28, "winners": winners_21_28}
with open('suscup_21_to_28_details.txt', 'w', encoding='utf-8') as f:
    json.dump(export_data, f, indent=2)

print("Updated Cup 25 and exported 21-28.")
