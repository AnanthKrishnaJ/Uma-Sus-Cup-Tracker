import sys

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

if '"hishi-amazon":' not in content and 'hishi-amazon:' not in content:
    db_marker = 'const UMA_DATABASE = {'
    insert_str = '\n    "hishi-amazon": { id: "hishi-amazon", name: "Hishi Amazon", type: "Uma Musume", version: "Original / Default", url: "https://gametora.com/umamusume/characters/hishi-amazon", image: "https://gametora.com/images/umamusume/characters/chara_stand_1012_101201.png" },'
    content = content.replace(db_marker, db_marker + insert_str)
    
    with open('suscup1.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Hishi Amazon added to UMA_DATABASE.")
else:
    print("Hishi Amazon already in UMA_DATABASE.")
