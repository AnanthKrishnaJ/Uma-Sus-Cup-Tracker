import re
import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add to UMA_DATABASE
entries = """
            "104201": { id: "104201", name: "Seeking the Pearl", type: "Uma Musume", version: "Original / Default", url: "https://gametora.com/umamusume/characters/104201-seeking-the-pearl", image: "https://gametora.com/images/umamusume/characters/chara_stand_1042_104201.png" },
            "101901": { id: "101901", name: "Agnes Digital", type: "Uma Musume", version: "Original / Default", url: "https://gametora.com/umamusume/characters/101901-agnes-digital", image: "https://gametora.com/images/umamusume/characters/chara_stand_1019_101901.png" },
"""

pattern = r'(const UMA_DATABASE = \{\s*)'
new_html = re.sub(pattern, r'\1' + entries.lstrip('\n'), html, count=1)

# 2. Update INITIAL_DATA umaIds
start = new_html.find('const INITIAL_DATA = ')
end = new_html.find('};\n', start) + 1
if start != -1:
    data_str = new_html[start + len('const INITIAL_DATA = '):end]
    data = json.loads(data_str)
    
    for i, race in enumerate(data.get('races', [])):
        for j, p in enumerate(race.get('participants', [])):
            if p.get('uma') == 'Seeking the Pearl':
                data['races'][i]['participants'][j]['umaId'] = '104201'
            elif p.get('uma') == 'Agnes Digital':
                data['races'][i]['participants'][j]['umaId'] = '101901'

    new_data_str = json.dumps(data, indent=8)
    new_html = new_html[:start + len('const INITIAL_DATA = ')] + new_data_str + new_html[end:]

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Added Seeking the Pearl and Agnes Digital to UMA_DATABASE and INITIAL_DATA.")
