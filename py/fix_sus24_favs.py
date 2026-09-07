import re, json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the INITIAL_DATA object
match = re.search(r'const INITIAL_DATA = (\{[\s\S]*?\});\n', content)
if not match:
    print("Could not find INITIAL_DATA")
    exit(1)

db_str = match.group(1)
data = json.loads(db_str)

# Mapping pos -> fav number for Sus Cup 24
fav_map = {
    1: 8,
    2: 1,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 10,
    8: 2,
    9: 7,
    10: 9,
    11: 11,
    12: 13,
    13: 12,
    14: 17,
    15: 16,
    16: 15,
    17: 14,
    18: 18
}

for race in data.get('races', []):
    if str(race.get('cupNumber')) == '24':
        if 'participants' in race:
            for p in race['participants']:
                if 'pos' in p:
                    pos = int(p['pos'])
                    if pos in fav_map:
                        p['pop'] = fav_map[pos]
        break

# Write back the modified JSON
new_db_str = json.dumps(data, indent=2)
new_content = content[:match.start(1)] + new_db_str + content[match.end(1):]
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated Sus Cup 24 favourites.")
