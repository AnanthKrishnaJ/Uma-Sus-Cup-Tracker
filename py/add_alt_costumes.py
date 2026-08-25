import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

db_start = content.find('const UMA_DATABASE = {') + len('const UMA_DATABASE = {')

missing_entries = """
    "101902": { id: "101902", name: "Agnes Digital", type: "Uma Musume", version: "Fanatic♡Jiangshi", url: "https://gametora.com/umamusume/characters/101902-agnes-digital", image: "https://gametora.com/images/umamusume/characters/chara_stand_1019_101902.png" },
    "101002": { id: "101002", name: "Taiki Shuttle", type: "Uma Musume", version: "Bubblegum☆Memories", url: "https://gametora.com/umamusume/characters/101002-taiki-shuttle", image: "https://gametora.com/images/umamusume/characters/chara_stand_1010_101002.png" },
    "106002": { id: "106002", name: "Nice Nature", type: "Uma Musume", version: "Run & Win", url: "https://gametora.com/umamusume/characters/106002-nice-nature", image: "https://gametora.com/images/umamusume/characters/chara_stand_1060_106002.png" },
"""

new_content = content[:db_start] + '\n' + missing_entries.strip('\n') + content[db_start:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added missing alt costumes to UMA_DATABASE!")
