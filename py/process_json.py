import json
import re

with open('extracted.json', 'r', encoding='utf-8') as f:
    initial_data = json.load(f)

def parse_raw():
    with open('../data/suscup_11_20_raw_data.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    cups = text.split('🏆 Sus Cup ')[1:]
    results = {}
    for cup in cups:
        lines = [l.strip() for l in cup.strip().split('\n') if l.strip()]
        cup_num = int(lines[0])
        
        participants = []
        i = 0
        while i < len(lines):
            line = lines[i]
            
            if re.match(r'^(🥇|🥈|🥉)?\s*\d+(st|nd|rd|th)', line) or re.match(r'^\d+th(–\d+th)?', line):
                if 'Not Shown' in line and '6th–18th' in line:
                    for pos in range(6, 19):
                        participants.append({
                            'pos': pos,
                            'uma': "Not Shown",
                            'player': "—",
                            'number': "-",
                            'pop': "-",
                            'strategy': "-",
                            'gap': "Not Shown",
                            'time': "Not Shown"
                        })
                    break

                pos_match = re.search(r'\d+', line)
                current_pos = int(pos_match.group(0))
                
                i += 1; uma = lines[i]
                i += 1; trainer = lines[i]
                if trainer == '—' or trainer == '-': trainer = 'NPC'
                
                i += 1; race_no = lines[i]
                race_no = int(race_no) if race_no.isdigit() else race_no
                
                i += 1; fav = lines[i].replace('No. ', '')
                fav = int(fav) if fav.isdigit() else fav
                
                i += 1; style = lines[i]
                i += 1; finish = lines[i]
                
                participants.append({
                    'pos': current_pos,
                    'uma': uma,
                    'player': trainer,
                    'number': race_no,
                    'pop': fav,
                    'strategy': style,
                    'gap': finish,
                    'time': finish
                })
            i += 1
        
        results[cup_num] = participants
    return results

parsed = parse_raw()

for race in initial_data['races']:
    rid = race.get('id')
    if rid in parsed:
        new_participants = []
        for np in parsed[rid]:
            ep = next((p for p in race.get('participants', []) if p.get('pos') == np['pos']), {})
            ep.update({
                'pos': np['pos'],
                'uma': np['uma'],
                'player': np['player'],
                'number': np['number'],
                'pop': np['pop'],
                'strategy': np['strategy'],
                'gap': np['gap'],
                'time': np['time']
            })
            new_participants.append(ep)
        race['participants'] = new_participants

with open('../.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const INITIAL_DATA = {')
if start != -1:
    brace_count = 0
    in_string = False
    escape = False
    end = -1
    for i in range(start + 21, len(html)):
        char = html[i]
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
            continue
        if char == '"':
            in_string = not in_string
        if not in_string:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    end = i + 1
                    break
    
    new_json_str = json.dumps(initial_data, indent=4, ensure_ascii=False)
    new_html = html[:start+21] + new_json_str + html[end:]
    with open('../.vscode/suscup1.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("suscup1.html successfully updated with cups 11-20 data")
