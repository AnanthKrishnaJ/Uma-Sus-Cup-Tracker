import re, json

with open('big_prompt.txt', 'r', encoding='utf-8') as f:
    text = f.read()

cups = {}
current_cup = None

lines = text.split('\n')
for i, line in enumerate(lines):
    m = re.search(r'Sus Cup (\d+)', line)
    if '##' in line and m:
        current_cup = m.group(1)
        cups[current_cup] = []
        continue
    
    if current_cup and line.strip().startswith('|') and 'Pos' not in line and '---' not in line:
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if len(parts) >= 6:
            pos_str = parts[0]
            pos_m = re.search(r'\d+', pos_str)
            if pos_m:
                pos = int(pos_m.group(0))
                uma = parts[1]
                player = parts[2]
                no = parts[3]
                fav = parts[4]
                style = parts[5]
                result = parts[6] if len(parts) > 6 else ''
                # Clean up markdown bold
                result = result.replace('**', '')
                cups[current_cup].append({
                    'pos': pos, 'uma': uma, 'player': player, 'number': no, 'fav': fav, 'style': style, 'result': result
                })

with open('parsed_prompt.json', 'w', encoding='utf-8') as f:
    json.dump(cups, f, indent=4)
