import json
import os

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_idx = html.find("const INITIAL_DATA = {")
if start_idx == -1:
    print("Could not find INITIAL_DATA")
    exit(1)

# brace counting
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

if end_idx == -1:
    print("Could not find end of INITIAL_DATA")
    exit(1)

json_str = html[start_idx + 21 : end_idx]

try:
    data = json.loads(json_str)
except Exception as e:
    print("JSON parse error:", e)
    exit(1)

# 1. Replace Cyclobly with Cyciesta in winners
for w in data.get("winners", []):
    if w.get("trainer") == "Cyclobly":
        w["trainer"] = "Cyciesta"
    if w.get("player") == "Cyclobly":
        w["player"] = "Cyciesta"

# 2. Replace in races
for r in data.get("races", []):
    for p in r.get("participants", []):
        if p.get("player") == "Cyclobly":
            p["player"] = "Cyciesta"
            
        # 3. Update Sus Cup 30 specific things
        if r.get("cupNumber") == 30:
            if p.get("uma") == "Nakayama Festa" and p.get("player") == "agnes":
                p["umaId"] = "104901-nakayama-festa"
            if p.get("uma") == "Mejiro Ardan" and p.get("player") == "Ananth":
                p["umaId"] = "107101-mejiro-ardan"
                
            # Update ranks for the special category winners
            if p.get("uma") == "Meisho Doto" and p.get("player") == "Cyciesta" and p.get("pos") == 1:
                p["rank"] = "B"
            if p.get("uma") == "Special Week" and p.get("player") == "agnes" and p.get("pos") == 2:
                p["rank"] = "C"
            if p.get("uma") == "Agnes Tachyon" and p.get("player") == "Ananth" and p.get("pos") == 12:
                p["rank"] = "D↓"

new_json_str = json.dumps(data, indent=4)
new_html = html[:start_idx + 21] + new_json_str + html[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("index.html updated successfully!")

# Write txt files
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
            f.write(f"{p.get('pos', 'Unknown')} - {p.get('uma', 'Unknown')} ({p.get('player', 'Unknown')}) - Strategy: {p.get('strategy', 'Unknown')}\n")

print("txt files created successfully!")
