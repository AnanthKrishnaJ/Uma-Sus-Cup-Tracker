import re, json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update UMA_DATABASE string in the HTML
# We need to insert the entries for 100602 (Oguri Cap Christmas) and 100402 (Maruzensky Summer)
new_entries = """
      "100602": { id: "100602", name: "Oguri Cap", type: "Uma Musume", version: "Miracle of Starlight", url: "https://gametora.com/umamusume/characters/100602-oguri-cap", image: "https://gametora.com/images/umamusume/characters/chara_stand_1006_100602.png" },
      "100402": { id: "100402", name: "Maruzensky", type: "Uma Musume", version: "Bubbly Brilliant", url: "https://gametora.com/umamusume/characters/100402-maruzensky", image: "https://gametora.com/images/umamusume/characters/chara_stand_1004_100402.png" },
"""
content = re.sub(r'(const UMA_DATABASE = \{)', r'\1\n' + new_entries, content, count=1)

# 2. Update INITIAL_DATA to assign umaId to these participants
match = re.search(r'const INITIAL_DATA = (\{[\s\S]*?\});\n', content)
if match:
    db_str = match.group(1)
    data = json.loads(db_str)
    
    for race in data.get('races', []):
        for p in race.get('participants', []):
            if p.get('uma') == 'Oguri Cap (Christmas)':
                p['umaId'] = '100602'
            elif p.get('uma') == 'Maruzensky (Summer)':
                p['umaId'] = '100402'
                
    new_db_str = json.dumps(data, indent=2)
    content = content[:match.start(1)] + new_db_str + content[match.end(1):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated UMA_DATABASE and INITIAL_DATA with xmas oguri and summer maruzensky.")
