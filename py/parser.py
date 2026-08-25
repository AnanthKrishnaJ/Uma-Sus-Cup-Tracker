
import re
import json

def parse_raw():
    with open('../data/suscup_11_20_raw_data.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    cups = text.split('?? Sus Cup ')[1:]
    results = {}
    for cup in cups:
        lines = cup.strip().split('\n')
        cup_num = int(lines[0].strip())
        
        # parse participants
        participants = []
        pos = 1
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Match positional markers like ?? 1st or 4th
            if re.match(r'^(??|??|??)?\s*\d+th|st|nd|rd', line) or re.match(r'^\d+th(–\d+th)?', line):
                if 'Not Shown' in line and '6th–18th' in line:
                    for _ in range(6, 19):
                        participants.append({
                            'pos': _,
                            'uma': 'Not Shown',
                            'player': '—',
                            'number': '-',
                            'pop': '-',
                            'strategy': '-',
                            'gap': 'Not Shown',
                            'time': 'Not Shown'
                        })
                    break

                pos_match = re.search(r'\d+', line)
                current_pos = int(pos_match.group(0))
                
                # Check next line for Uma name
                i += 1
                uma_name = lines[i].strip()
                
                # Next line: Trainer
                i += 1
                trainer = lines[i].strip()
                if trainer == '—':
                    trainer = 'NPC'
                
                # Next line: Race No.
                i += 1
                race_no_str = lines[i].strip()
                race_no = int(race_no_str) if race_no_str.isdigit() else race_no_str
                
                # Next line: Fav (e.g., No. 2)
                i += 1
                fav_str = lines[i].strip().replace('No. ', '')
                fav = int(fav_str) if fav_str.isdigit() else fav_str
                
                # Next line: Style
                i += 1
                style = lines[i].strip()
                
                # Next line: Finish Stat
                i += 1
                finish = lines[i].strip()
                
                participants.append({
                    'pos': current_pos,
                    'uma': uma_name,
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
print(json.dumps({k: len(v) for k, v in parsed.items()}, indent=2))
with open('../data/parsed_11_20.json', 'w', encoding='utf-8') as f:
    json.dump(parsed, f, indent=2)

