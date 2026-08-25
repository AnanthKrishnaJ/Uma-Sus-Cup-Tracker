import json
import re

def parse_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    races = []
    
    sections = re.split(r'## Sus Cup (\d+) — ([^\n]+)', content)
    
    for i in range(1, len(sections), 3):
        cup_num = sections[i].strip()
        cup_name = sections[i+1].strip()
        body = sections[i+2]
        
        race_obj = {
            "cupNumber_parsed": cup_num,
            "title": cup_name,
            "participants": []
        }
        
        meta_pattern = r'\*\*(.*?)\*\*:\s*([^\n]+)'
        for m in re.finditer(meta_pattern, body):
            key = m.group(1).strip()
            val = m.group(2).strip()
            if key == 'Date': race_obj['date'] = val
            elif key == 'Race time': race_obj['time'] = val
            elif key == 'Room ID': race_obj['roomId'] = val
            elif key == 'Track': race_obj['track'] = val
            elif key == 'Distance': 
                parts = val.split('—')
                race_obj['distance'] = parts[0].strip()
                if len(parts) > 1:
                    race_obj['distanceCategory'] = parts[1].strip()
            elif key == 'Direction': race_obj['direction'] = val
            elif key == 'Weather': race_obj['weather'] = val
            elif key == 'Ground': race_obj['ground'] = val
            elif key == 'Condition': race_obj['condition'] = val
            elif key == 'Mood': race_obj['mood'] = val
            elif key == 'Season': race_obj['season'] = val
            elif key == 'Subtitle': race_obj['subtitle'] = val
            
        table_lines = [line.strip() for line in body.split('\n') if line.strip().startswith('|')]
        if len(table_lines) > 2:
            headers = [h.strip() for h in table_lines[0].split('|')[1:-1]]
            for line in table_lines[2:]:
                cols = [c.strip() for c in line.split('|')[1:-1]]
                if len(cols) == len(headers):
                    participant = {}
                    for h, c in zip(headers, cols):
                        h_lower = h.lower()
                        c = c.replace('**', '')
                        if h_lower == 'pos': participant['pos'] = int(c) if c.isdigit() else c
                        elif h_lower == 'uma': 
                            participant['uma'] = c
                            participant['umaId'] = c.lower().replace(' ', '-').replace('.', '').replace('\'', '').replace('[', '').replace(']', '')
                        elif h_lower == 'trainer': participant['player'] = c
                        elif h_lower == 'no.': participant['number'] = int(c) if c.isdigit() else c
                        elif h_lower == 'rank': participant['rank'] = c
                        elif h_lower == 'title': participant['title'] = c
                        elif h_lower == 'style': participant['strategy'] = c
                        elif h_lower == 'time/gap': 
                            if ':' in c and 'L' not in c:
                                participant['time'] = c
                                participant['gap'] = ''
                            else:
                                participant['gap'] = c
                                participant['time'] = c
                        elif h_lower == 'fav': participant['pop'] = int(c) if c.isdigit() else c
                    race_obj['participants'].append(participant)
        races.append(race_obj)
    return races

def update_html():
    html_path = '../.vscode/suscup1.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('const INITIAL_DATA = ') + 21
    end_idx = content.find('};', start_idx) + 1
    
    initial_data = json.loads(content[start_idx:end_idx])
    
    parsed_races = parse_markdown('../data/suscup_1_10_raw_data.txt')
    parsed_dict = {r['cupNumber_parsed']: r for r in parsed_races}
    
    updated_count = 0
    for race in initial_data['races']:
        cup = str(race.get('cupNumber', ''))
        # Extract number from cup string (e.g. "SUS CUP 9 - GP Round 1/3" -> "9")
        m = re.search(r'(?:CUP |^)(\d+)', cup, re.IGNORECASE)
        if m:
            cup_num = m.group(1)
            if cup_num in parsed_dict:
                new_r = parsed_dict[cup_num]
                race['participants'] = new_r['participants']
                for k, v in new_r.items():
                    if k not in ['participants', 'cupNumber_parsed', 'cupNumber']:
                        race[k] = v
                updated_count += 1

    new_content = content[:start_idx] + json.dumps(initial_data, indent=4) + content[end_idx:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {updated_count} races in INITIAL_DATA successfully!")

if __name__ == '__main__':
    update_html()
