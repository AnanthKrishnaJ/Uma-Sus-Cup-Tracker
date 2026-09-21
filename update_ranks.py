import json

updates = {
    1: {"rank": "UG1", "umaId": "105802-meisho-doto"},
    2: {"rank": "UG7"},
    3: {"rank": "UG5", "umaId": "102602"}, 
    4: {"rank": "UG6", "umaId": "101702"}, 
    5: {"rank": "UG2"}, 
    6: {"rank": "UG9"}, 
    7: {"rank": "UG7"},
    8: {"rank": "SS"},
    9: {"rank": "UG1"},
    10: {"rank": "UG1"},
    11: {"rank": "SS+"},
    12: {"rank": "UG"},
    13: {"rank": "UG9", "umaId": "102102"}, 
    14: {"rank": "S+"},
    15: {"rank": "UG7", "umaId": "105802-meisho-doto"},
    16: {"rank": "SS+", "umaId": "102102"}, 
    17: {"rank": "UG5"},
    18: {"rank": "SS", "umaId": "100302"}, 
}

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_idx = html.find("const INITIAL_DATA = {")
if start_idx == -1:
    print("Could not find INITIAL_DATA")
    exit(1)

brace_count = 0
end_idx = -1
for i in range(start_idx + 21, len(html)):
    if html[i] == '{':
        brace_count += 1
    elif html[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            end_idx = i + 1
            break

json_str = html[start_idx + 21 : end_idx]
data = json.loads(json_str)

for r in data.get("races", []):
    if r.get("cupNumber") == 30:
        for p in r.get("participants", []):
            pos = p.get("pos")
            if pos in updates:
                upd = updates[pos]
                p["rank"] = upd["rank"]
                if "umaId" in upd:
                    p["umaId"] = upd["umaId"]

new_json_str = json.dumps(data, indent=4)
new_html = html[:start_idx + 21] + new_json_str + html[end_idx:]

# Part 1: UPDATE UMA_DATABASE
new_uma_str = '      "102102": { id: "102102", name: "Tamamo Cross", type: "Uma Musume", version: "Standard / Original", url: "https://gametora.com/umamusume/characters/102102-tamamo-cross", image: "https://gametora.com/images/umamusume/characters/chara_stand_1021_102102.png" },\n'
if "102102" not in new_html:
    insert_pos = new_html.find('"104901-nakayama-festa"')
    if insert_pos != -1:
        # Wait, finding "104901-nakayama-festa" will find the one inside INITIAL_DATA! 
        # I need to find the one inside UMA_DATABASE.
        # Let's search for '"104901-nakayama-festa": {'
        insert_pos = new_html.find('"104901-nakayama-festa": {')
        if insert_pos != -1:
            new_html = new_html[:insert_pos] + new_uma_str + new_html[insert_pos:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("index.html updated successfully!")

cup_30_participants = []
for r in data.get("races", []):
    if r.get("cupNumber") == 30:
        cup_30_participants = r.get("participants", [])

if cup_30_participants:
    with open("suscup30.txt", "w", encoding="utf-8") as f:
        f.write("Sus Cup 30 Results\n\n")
        for p in cup_30_participants:
            f.write(f"{p.get('pos', 'Unknown')} - {p.get('uma', 'Unknown')} ({p.get('player', 'Unknown')}) - Strategy: {p.get('strategy', 'Unknown')} - Gap: {p.get('gap', 'Unknown')} - Fav: {p.get('pop', 'Unknown')} - Rank: {p.get('rank', 'Unknown')}\n")

with open("suscup1_to_30.txt", "w", encoding="utf-8") as f:
    for race in data.get("races", []):
        f.write(f"\n{race.get('cupName', f'Sus Cup {race.get('cupNumber')}')}\n")
        for p in race.get("participants", []):
            f.write(f"{p.get('pos', 'Unknown')} - {p.get('uma', 'Unknown')} ({p.get('player', 'Unknown')}) - Strategy: {p.get('strategy', 'Unknown')} - Rank: {p.get('rank', 'Unknown')}\n")

print("txt files created successfully!")
