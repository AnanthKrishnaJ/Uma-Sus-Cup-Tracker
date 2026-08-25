import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the bad string entries with proper objects
bad_102402 = '"102402": "https://gametora.com/umamusume/characters/102402-mayano-top-gun",'
bad_104002 = '"104002": "https://gametora.com/umamusume/characters/104002-gold-city"'

good_102402 = '"102402": { id: "102402", name: "Mayano Top Gun", type: "Uma Musume", version: "Sun Kissed Amour", url: "https://gametora.com/umamusume/characters/102402-mayano-top-gun", image: "https://gametora.com/images/umamusume/characters/chara_stand_102402_1060.png" },'
good_104002 = '"104002": { id: "104002", name: "Gold City", type: "Uma Musume", version: "Autumn Cosmos", url: "https://gametora.com/umamusume/characters/104002-gold-city", image: "https://gametora.com/images/umamusume/characters/chara_stand_104002_1060.png" },'
good_103601 = '"103601": { id: "103601", name: "Air Shakur", type: "Uma Musume", version: "Original / Default", url: "https://gametora.com/umamusume/characters/103601-air-shakur", image: "https://gametora.com/images/umamusume/characters/profile/chara_stand_103601_air-shakur.png" },'
good_100702 = '"100702": { id: "100702", name: "Gold Ship", type: "Uma Musume", version: "RUN! RUIN! LAUNCHER!", url: "https://gametora.com/umamusume/characters/100702-gold-ship", image: "https://gametora.com/images/umamusume/characters/profile/chara_stand_100702_gold-ship.png" }'

if bad_102402 in content:
    content = content.replace(bad_102402, good_102402)
if bad_104002 in content:
    content = content.replace(bad_104002, good_104002 + '\n            ' + good_103601 + '\n            ' + good_100702)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("UMA_DATABASE entries fixed!")
