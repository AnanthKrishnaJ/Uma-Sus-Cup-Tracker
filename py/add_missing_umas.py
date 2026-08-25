import json
import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

db_start = content.find('const UMA_DATABASE = {') + len('const UMA_DATABASE = {')

missing_entries = """
    "t.m.-opera-o": { id: "t.m.-opera-o", name: "T.M. Opera O", type: "Uma Musume", version: "Standard / Original", url: "https://gametora.com/umamusume/characters/101501-tm-opera-o", image: "https://gametora.com/images/umamusume/characters/chara_stand_1015_101501.png" },
    "air-groove": { id: "air-groove", name: "Air Groove", type: "Uma Musume", version: "Original / Default", url: "https://gametora.com/umamusume/characters/101801-air-groove", image: "https://gametora.com/images/umamusume/characters/chara_stand_1018_101801.png" },
    "rice-shower": { id: "rice-shower", name: "Rice Shower", type: "Uma Musume", version: "Original / Default", url: "https://gametora.com/umamusume/characters/103001-rice-shower", image: "https://gametora.com/images/umamusume/characters/chara_stand_1030_103001.png" },
    "mini-daisy": { id: "mini-daisy", name: "Mini Daisy", type: "NPC", url: null, image: null },
    "takeoff-plane": { id: "takeoff-plane", name: "Takeoff Plane", type: "NPC", url: null, image: null },
    "pan-pacific": { id: "pan-pacific", name: "Pan Pacific", type: "NPC", url: null, image: null },
    "not-shown": { id: "not-shown", name: "Not shown", type: "NPC", url: null, image: null },
    "set-your-record": { id: "set-your-record", name: "Set Your Record", type: "NPC", url: null, image: null },
    "coincidence": { id: "coincidence", name: "Coincidence", type: "NPC", url: null, image: null },
    "torch-and-book": { id: "torch-and-book", name: "Torch and Book", type: "NPC", url: null, image: null },
    "missing-nights": { id: "missing-nights", name: "Missing Nights", type: "NPC", url: null, image: null },
    "maleficus": { id: "maleficus", name: "Maleficus", type: "NPC", url: null, image: null },
    "waltz-step": { id: "waltz-step", name: "Waltz Step", type: "NPC", url: null, image: null },
    "book-of-sugar": { id: "book-of-sugar", name: "Book of Sugar", type: "NPC", url: null, image: null },
    "chief-purser": { id: "chief-purser", name: "Chief Purser", type: "NPC", url: null, image: null },
    "reed-photobook": { id: "reed-photobook", name: "Reed Photobook", type: "NPC", url: null, image: null },
    "out-of-black": { id: "out-of-black", name: "Out of Black", type: "NPC", url: null, image: null },
    "breeze-glider": { id: "breeze-glider", name: "Breeze Glider", type: "NPC", url: null, image: null },
    "farm-volition": { id: "farm-volition", name: "Farm Volition", type: "NPC", url: null, image: null },
"""

new_content = content[:db_start] + '\n' + missing_entries.strip('\n') + content[db_start:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added missing entries!")
