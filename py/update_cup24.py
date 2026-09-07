import json
import re

def get_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    start_marker = "const INITIAL_DATA ="
    start_idx = html.find(start_marker)
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

live_data, live_html, start_idx, end_idx = get_data('index.html')

participants_data = [
    {"pos": 1, "uma": "Mejiro Dober", "player": "jayreative", "title": "Coolheaded Beauty", "strategy": "Late", "time": "1:56.6", "pop": 8, "rank": "-"},
    {"pos": 2, "uma": "Oguri Cap (Christmas)", "player": "Cyclobly", "title": "Leading the Charge", "strategy": "Pace", "time": "1 3/4 L", "pop": 1, "rank": "-"},
    {"pos": 3, "uma": "Maruzensky (Summer)", "player": "Vilthaar", "title": "Leading the Charge", "strategy": "Front", "time": "1 1/4 L", "pop": 3, "rank": "-"},
    {"pos": 4, "uma": "Admire Vega", "player": "GohanXGAMER", "title": "Leading the Charge", "strategy": "End", "time": "3/4 L", "pop": 4, "rank": "-"},
    {"pos": 5, "uma": "Agnes Tachyon", "player": "Cruzi", "title": "Leading the Charge", "strategy": "Pace", "time": "Neck", "pop": 5, "rank": "-"},
    {"pos": 6, "uma": "Oguri Cap", "player": "eviskno", "title": "Ideal Idol", "strategy": "Pace", "time": "1 1/4 L", "pop": 6, "rank": "-"},
    {"pos": 7, "uma": "Narita Taishin", "player": "Jiinxye", "title": "Phenomenal", "strategy": "End", "time": "1 L", "pop": 10, "rank": "-"},
    {"pos": 8, "uma": "Symboli Rudolf", "player": "agnes", "title": "Emperor", "strategy": "Late", "time": "3/4 L", "pop": 2, "rank": "-"},
    {"pos": 9, "uma": "Fuji Kiseki", "player": "Ananth", "title": "Leading the Charge", "strategy": "Pace", "time": "1 1/2 L", "pop": 7, "rank": "-"},
    {"pos": 10, "uma": "Special Week", "player": "Haji", "title": "Leading the Charge", "strategy": "Pace", "time": "3/4 L", "pop": 9, "rank": "-"},
    {"pos": 11, "uma": "Mini Daisy", "player": "NPC Uma", "title": "—", "strategy": "Pace", "time": "4 L", "pop": 11, "rank": "-"},
    {"pos": 12, "uma": "Reed Photobook", "player": "NPC Uma", "title": "—", "strategy": "Pace", "time": "1/2 L", "pop": 13, "rank": "-"},
    {"pos": 13, "uma": "Chief Purser", "player": "NPC Uma", "title": "—", "strategy": "Late", "time": "Nose", "pop": 12, "rank": "-"},
    {"pos": 14, "uma": "Takeoff Plane", "player": "NPC Uma", "title": "—", "strategy": "End", "time": "1/2 L", "pop": 17, "rank": "-"},
    {"pos": 15, "uma": "Farm Volition", "player": "NPC Uma", "title": "—", "strategy": "Late", "time": "Nose", "pop": 16, "rank": "-"},
    {"pos": 16, "uma": "Coincidence", "player": "NPC Uma", "title": "—", "strategy": "Front", "time": "Head", "pop": 15, "rank": "-"},
    {"pos": 17, "uma": "Waltz Step", "player": "NPC Uma", "title": "—", "strategy": "Pace", "time": "Neck", "pop": 14, "rank": "-"},
    {"pos": 18, "uma": "Missing Nights", "player": "NPC Uma", "title": "—", "strategy": "Front", "time": "1 1/4 L", "pop": 18, "rank": "-"}
]

for race in live_data['races']:
    if race.get('id') == 24:
        race['participants'] = participants_data
        
new_json_str = json.dumps(live_data, indent=2)
new_html = live_html[:start_idx] + new_json_str + live_html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Saved to index.html with Cup 24 participants updated")
