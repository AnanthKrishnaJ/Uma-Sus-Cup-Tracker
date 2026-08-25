import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

db_start = text.find('const UMA_DATABASE = ')
db_end = text.rfind('};', db_start)
db_str = text[db_start + 21:db_end + 1]

# We need to ensure the following keys exist in db_str:
# '103601', '102402', '104002', '100702'

def add_to_db(key, obj_str):
    global text, db_str, db_end
    if f"'{key}':" not in db_str and f'"{key}":' not in db_str and f'\n            {key}:' not in db_str:
        insert_pos = db_end
        text = text[:insert_pos] + f",\n            '{key}': {obj_str}" + text[insert_pos:]
        
        # update db_end and db_str for next potential insert
        db_end = text.rfind('};', db_start)
        db_str = text[db_start + 21:db_end + 1]
        print(f"Added {key} to UMA_DATABASE")

add_to_db('103601', "{ name: 'Air Shakur', version: 'Original / Default', image: 'https://gametora.com/images/umamusume/characters/profile/chara_stand_103601_air-shakur.png', icon: 'https://gametora.com/images/umamusume/characters/icons/chara_icon_103601_air-shakur.png' }")

add_to_db('102402', "{ name: 'Mayano Top Gun', version: 'Sunlight Bouquet', image: 'https://gametora.com/images/umamusume/characters/profile/chara_stand_102402_mayano-top-gun.png', icon: 'https://gametora.com/images/umamusume/characters/icons/chara_icon_102402_mayano-top-gun.png' }")

add_to_db('104002', "{ name: 'Gold City', version: 'Autumn Cosmos', image: 'https://gametora.com/images/umamusume/characters/profile/chara_stand_104002_gold-city.png', icon: 'https://gametora.com/images/umamusume/characters/icons/chara_icon_104002_gold-city.png' }")

add_to_db('100702', "{ name: 'Gold Ship', version: 'RUN! RUIN! LAUNCHER!', image: 'https://gametora.com/images/umamusume/characters/profile/chara_stand_100702_gold-ship.png', icon: 'https://gametora.com/images/umamusume/characters/icons/chara_icon_100702_gold-ship.png' }")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Checked UMA_DATABASE.")
