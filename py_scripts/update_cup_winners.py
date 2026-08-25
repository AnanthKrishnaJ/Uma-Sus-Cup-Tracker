import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove the "New Race" button from HTML
text = re.sub(r'<li><a href="#" data-nav="add-race".*?</li>', '', text, flags=re.DOTALL)

# 2. Extract INITIAL_DATA
start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

# 3. Update Cup 24 participants
updated_cup24 = 0
for race in data.get('races', []):
    if str(race.get('cupNumber')) == 'SUS CUP 24' or str(race.get('cupNumber')) == '24':
        for p in race.get('participants', []):
            if 'Oguri Cap' in p.get('uma', ''):
                p['umaId'] = '100602'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/100602-oguri-cap'
                updated_cup24 += 1
            if 'Maruzensky' in p.get('uma', ''):
                p['umaId'] = '100402'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/100402-maruzensky'
                updated_cup24 += 1

print(f"Updated {updated_cup24} records in Cup 24")

# 4. Add new winners
new_winners = [
    # Cup 21
    {
        "cup": "Sus Cup 21",
        "trainer": "Cyciesta",
        "uma": "Curren Chan",
        "rankLabel": "3* spark winner"
    },
    {
        "cup": "Sus Cup 21",
        "trainer": "Agnes",
        "uma": "Taiki Shuttle",
        "rankLabel": "2* spark winner"
    },
    {
        "cup": "Sus Cup 21",
        "trainer": "Jiinxye",
        "uma": "Sakura Bakushin O",
        "rankLabel": "1* spark winner"
    },
    # Cup 22
    {
        "cup": "Sus Cup 22",
        "trainer": "guest club member",
        "uma": "Gold Ship",
        "rankLabel": "URA Finale scenario winner"
    },
    {
        "cup": "Sus Cup 22",
        "trainer": "Cyciesta",
        "uma": "Oguri Cap",
        "rankLabel": "Unity Cup scenario winner"
    },
    {
        "cup": "Sus Cup 22",
        "trainer": "Cyciesta",
        "uma": "Agnes Tachyon",
        "rankLabel": "Trackblazer scenario winner"
    },
    # Cup 23
    {
        "cup": "Sus Cup 23",
        "trainer": "Jiinxye",
        "uma": "Narita Taishin",
        "rankLabel": "3* winner"
    },
    {
        "cup": "Sus Cup 23",
        "trainer": "Agnes",
        "uma": "Air Groove",
        "rankLabel": "2* winner"
    },
    {
        "cup": "Sus Cup 23",
        "trainer": "Shadow Amber",
        "uma": "Agnes Tachyon",
        "rankLabel": "1* winner"
    }
]

# Ensure we don't duplicate winners if script is run multiple times
existing_winner_keys = {(w.get('cup'), w.get('trainer'), w.get('uma'), w.get('rankLabel')) for w in data.get('winners', [])}

added_winners = 0
for nw in new_winners:
    key = (nw['cup'], nw['trainer'], nw['uma'], nw['rankLabel'])
    if key not in existing_winner_keys:
        data['winners'].append(nw)
        added_winners += 1

print(f"Added {added_winners} new winners")

# 5. Write back to HTML
new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Done.")
