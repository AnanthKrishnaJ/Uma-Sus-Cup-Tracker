import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Move the dangling Air Shakur and Gold Ship to UMA_DATABASE
dangling_str = """
            '103601': { name: 'Air Shakur', version: 'Original / Default', image: 'https://gametora.com/images/umamusume/characters/profile/chara_stand_103601_air-shakur.png', icon: 'https://gametora.com/images/umamusume/characters/icons/chara_icon_103601_air-shakur.png' },
            '100702': { name: 'Gold Ship', version: 'RUN! RUIN! LAUNCHER!', image: 'https://gametora.com/images/umamusume/characters/profile/chara_stand_100702_gold-ship.png', icon: 'https://gametora.com/images/umamusume/characters/icons/chara_icon_100702_gold-ship.png' }"""

if '103601' not in content[:364173]: # if not already in UMA_DATABASE
    # Find the end of UMA_DATABASE
    db_end = content.find('};', content.find('const UMA_DATABASE ='))
    content = content[:db_end] + ',\n' + dangling_str.strip() + '\n' + content[db_end:]

# Fix 2: Repair the end of the file
corrupted_end = """    this.navigate('race-detail');
,
            '103601': { name: 'Air Shakur', version: 'Original / Default', image: 'https://gametora.com/images/umamusume/characters/profile/chara_stand_103601_air-shakur.png', icon: 'https://gametora.com/images/umamusume/characters/icons/chara_icon_103601_air-shakur.png' },
            '100702': { name: 'Gold Ship', version: 'RUN! RUIN! LAUNCHER!', image: 'https://gametora.com/images/umamusume/characters/profile/chara_stand_100702_gold-ship.png', icon: 'https://gametora.com/images/umamusume/characters/icons/chara_icon_100702_gold-ship.png' }};"""

fixed_end = """    this.navigate('race-detail');
};"""

content = content.replace(corrupted_end, fixed_end)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Syntax fixed!")
