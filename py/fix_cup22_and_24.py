import json
import re

def get_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    start_marker = "const INITIAL_DATA ="
    start_idx = html.find(start_marker)
    if start_idx == -1:
        # If it's a JSON file
        return json.loads(html), html, -1, -1
    start_idx += len(start_marker)
    while html[start_idx] != '{': start_idx += 1
    
    stack = []
    end_idx = -1
    for i in range(start_idx, len(html)):
        if html[i] == '{': stack.append('{')
        elif html[i] == '}':
            stack.pop()
            if not stack:
                end_idx = i + 1
                break
                
    json_str = html[start_idx:end_idx]
    json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)
    try:
        data = json.loads(json_str)
        return data, html, start_idx, end_idx
    except Exception as e:
        print("Error parsing", filepath, e)
        return None, html, start_idx, end_idx

temp_data, _, _, _ = get_data('temp_initial_data.json')
live_data, live_html, start_idx, end_idx = get_data('index.html')

temp_races = {r.get('id'): r for r in temp_data['races']}

for race in live_data['races']:
    if race.get('id') in [22, 23, 24]:
        if race.get('id') in temp_races:
            print(f"Restoring Cup {race.get('id')} from temp_initial_data.json")
            # Replace participants and registeredRunners with original temp_data ones
            race['participants'] = temp_races[race.get('id')].get('participants', [])
            race['registeredRunners'] = temp_races[race.get('id')].get('registeredRunners', [])
            
new_json_str = json.dumps(live_data, indent=2)
new_html = live_html[:start_idx] + new_json_str + live_html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Saved to index.html")
