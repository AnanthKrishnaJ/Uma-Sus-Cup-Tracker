import json
import re
import os

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix missing semicolon after INITIAL_DATA
start = text.find('const INITIAL_DATA = ')
end = text.find('const NPC_PROFILES = {};')
data_str = text[start + 21:end].strip()
if data_str.endswith(';'):
    data_str = data_str[:-1]
data = json.loads(data_str)

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n        ' + text[end:]

# 2. Fix UMA_DATABASE
db_start = text.find('const UMA_DATABASE = {')
db_end = text.find('};', db_start)
db_str = text[db_start:db_end + 2]

umas_to_add = [
    ('"106001": { id: "106001", name: "Nice Nature", type: "Uma Musume", version: "Standard / Original", url: "https://gametora.com/umamusume/characters/106001-nice-nature", image: "https://gametora.com/images/umamusume/characters/chara_stand_1060_106001.png" }', '106001'),
    ('"103701": { id: "103701", name: "Eishin Flash", type: "Uma Musume", version: "Standard / Original", url: "https://gametora.com/umamusume/characters/103701-eishin-flash", image: "https://gametora.com/images/umamusume/characters/chara_stand_1037_103701.png" }', '103701'),
    ('"101301": { id: "101301", name: "Mejiro McQueen", type: "Uma Musume", version: "Standard / Original", url: "https://gametora.com/umamusume/characters/101301-mejiro-mcqueen", image: "https://gametora.com/images/umamusume/characters/chara_stand_1013_101301.png" }', '101301'),
    ('"100401": { id: "100401", name: "Maruzensky", type: "Uma Musume", version: "Standard / Original", url: "https://gametora.com/umamusume/characters/100401-maruzensky", image: "https://gametora.com/images/umamusume/characters/chara_stand_1004_100401.png" }', '100401')
]

for uma_line, uma_id in umas_to_add:
    if f'"{uma_id}"' not in db_str:
        # insert right after the opening bracket
        insert_pos = db_str.find('{') + 1
        db_str = db_str[:insert_pos] + '\n      ' + uma_line + ',' + db_str[insert_pos:]
        print(f"Added {uma_id} to UMA_DATABASE")

text = text[:db_start] + db_str + text[db_end + 2:]

# 3. Remove Upcoming Race Schedule safely
upcoming_idx = text.find('Upcoming Race Schedule')
if upcoming_idx != -1:
    section_start = text.rfind('<section class="card"', 0, upcoming_idx)
    section_end = text.find('</section>', upcoming_idx) + len('</section>')
    
    if section_start != -1 and section_end != -1:
        # Check if Sus Cup 29 is within this block
        block = text[section_start:section_end]
        if "Sus Cup 29" in block:
            text = text[:section_start] + text[section_end:]
            print("Successfully removed the Upcoming Race Schedule section.")
        else:
            print("Found Upcoming Race Schedule but it did not contain Sus Cup 29")
else:
    print("Upcoming Race Schedule not found.")


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("HTML updated.")

# Let's also update the txt export since the original JSON might have been exported without semicolon, but that shouldn't matter for JSON
