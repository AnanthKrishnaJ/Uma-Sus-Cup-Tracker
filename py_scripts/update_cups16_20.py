import json
import re

with open('full_user_prompt_untruncated.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

cups_data = {}
current_cup = None

for line in md_content.split('\n'):
    line = line.strip()
    if '## 🏆 Sus Cup ' in line:
        # e.g. "without changing anything else ## 🏆 Sus Cup 16"
        num_str = line.split('## 🏆 Sus Cup ')[1].strip()
        if ' ' in num_str:
            num_str = num_str.split(' ')[0]
        current_cup = int(num_str)
        cups_data[current_cup] = {
            'raceName': '',
            'trackInfo': '',
            'groundCondition': '',
            'guestPlacing': 0,
            'participants': []
        }
    elif '## Sus Cup ' in line:
        num_str = line.split('## Sus Cup ')[1].strip()
        if ' ' in num_str:
            num_str = num_str.split(' ')[0]
        current_cup = int(num_str)
        cups_data[current_cup] = {
            'raceName': '',
            'trackInfo': '',
            'groundCondition': '',
            'guestPlacing': 0,
            'participants': []
        }
    elif current_cup and line.startswith('**Race:**'):
        cups_data[current_cup]['raceName'] = line.replace('**Race:**', '').strip()
    elif current_cup and line.startswith('**Track:**'):
        cups_data[current_cup]['trackInfo'] = line.replace('**Track:**', '').strip()
    elif current_cup and line.startswith('**Ground:**'):
        cups_data[current_cup]['groundCondition'] = line.replace('**Ground:**', '').strip()
    elif current_cup and line.startswith('**Result:**'):
        val = line.replace('**Result:**', '').replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').strip()
        if val.isdigit():
            cups_data[current_cup]['guestPlacing'] = int(val)
    elif current_cup and line.startswith('|') and 'Pos' not in line and '---' not in line:
        parts = [p.strip() for p in line.split('|')][1:-1]
        if len(parts) >= 7:
            # Format: | Pos. | Uma | Trainer | No. | Fav. | Style | Finish |
            pos_str = parts[0]
            uma_str = parts[1]
            trainer_str = parts[2]
            no_str = parts[3]
            fav_str = parts[4]
            style_str = parts[5]
            finish_str = parts[6]
            
            finish_str = finish_str.replace('**', '').strip()
            
            if pos_str == '' or pos_str == '—':
                pos = 99
            else:
                pos = int(re.sub(r'\D', '', pos_str))
                
            if no_str == '' or no_str == '—':
                no = 0
            else:
                no = int(re.sub(r'\D', '', no_str))
                
            if fav_str == '' or fav_str == '—':
                fav = 0
            else:
                fav = int(re.sub(r'\D', '', fav_str))
                
            cups_data[current_cup]['participants'].append({
                'pos': pos,
                'number': no,
                'uma': uma_str,
                'player': trainer_str,
                'strategy': style_str,
                'time': finish_str,
                'gap': finish_str,
                'pop': fav,
                'rank': '',
                'title': ''
            })

print(f"Parsed {len(cups_data)} cups: {list(cups_data.keys())}")

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
db_start = text.find('const UMA_DATABASE = ')
end = text.rfind('};', start, db_start)

data_str = text[start + 21:end + 1]
import json
data = json.loads(data_str)
races = data['races']

for cup in races:
    cup_id = cup['id']
    if cup_id in cups_data:
        new_data = cups_data[cup_id]
        if not new_data['participants']:
            continue
            
        cup['name'] = new_data['raceName']
        cup['details'] = new_data['trackInfo'] + ' | ' + new_data['groundCondition']
        if new_data['guestPlacing']:
            cup['guestPlacing'] = new_data['guestPlacing']
            
        existing_umas = {}
        for p in cup['participants']:
            if 'umaId' in p:
                existing_umas[p['uma'] + '_' + p['player']] = p['umaId']
                
        cup['participants'] = new_data['participants']
        for p in cup['participants']:
            key = p['uma'] + '_' + p['player']
            if key in existing_umas:
                p['umaId'] = existing_umas[key]

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_text = text[:start + 21] + new_json + text[end + 1:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated HTML with Cups 16 to 20")
