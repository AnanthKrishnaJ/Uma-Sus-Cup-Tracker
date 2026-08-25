import json
import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('const INITIAL_DATA = ') + 21
end_idx = content.find('};', start_idx) + 1

initial_data = json.loads(content[start_idx:end_idx])

# The Medium race for Sus Cup 27 is the other one (2200m or similar)
medium_race = next(r for r in initial_data['races'] if r['cupNumber'] == 'SUS CUP 27' and r.get('distance') != '1600m')

updates = {
    'Mihono Bourbon': '102602',
    'Agnes Digital': '101902',
    'Taiki Shuttle': '101002',
    'Nice Nature': '106002',
    'Gold Ship': '100702'
}

for participant in medium_race['participants']:
    uma_name = participant['uma']
    if uma_name in updates:
        participant['umaId'] = updates[uma_name]

new_content = content[:start_idx] + json.dumps(initial_data, indent=4) + content[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated Sus Cup 27 Medium Umas successfully!")
