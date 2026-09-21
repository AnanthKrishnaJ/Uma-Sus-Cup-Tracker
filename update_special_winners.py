import json

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

special_winners_29 = {
    "Red Skills Winner": {
        "player": "Cruzi",
        "uma": "Grass Wonder",
        "pos": 3
    },
    "Green Skills Winner": {
        "player": "agnes",
        "uma": "Silence Suzuka",
        "pos": 2
    },
    "Blue Skills Winner": {
        "player": "Cyciesta",
        "uma": "Oguri Cap",
        "pos": 1
    }
}

special_winners_30 = {
    "B Winner": {
        "player": "Cyciesta",
        "uma": "Meisho Doto",
        "pos": 1
    },
    "C Winner": {
        "player": "agnes",
        "uma": "Special Week",
        "pos": 2
    },
    "D or Worse Winner": {
        "player": "Ananth",
        "uma": "Agnes Tachyon",
        "pos": 12
    }
}

cup29 = None
cup30 = None

for r in data.get("races", []):
    if r.get("cupNumber") == 29:
        r["specialWinners"] = special_winners_29
        cup29 = r
    if r.get("cupNumber") == 30:
        r["specialWinners"] = special_winners_30
        cup30 = r

new_json_str = json.dumps(data, indent=4)
new_html = html[:start_idx + 21] + new_json_str + html[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("index.html updated successfully!")

# Write suscup29.txt
if cup29:
    with open("suscup29.txt", "w", encoding="utf-8") as f:
        f.write("Sus Cup 29 Results\n\n")
        f.write("Special Category Winners:\n")
        for category, winner in special_winners_29.items():
            f.write(f"  {category}: {winner['player']} ({winner['pos']} - {winner['uma']})\n")
        f.write("\nAll Participants:\n")
        for p in cup29.get("participants", []):
            f.write(f"{p.get('pos', 'Unknown')} - {p.get('uma', 'Unknown')} ({p.get('player', 'Unknown')}) - Strategy: {p.get('strategy', 'Unknown')} - Gap: {p.get('gap', 'Unknown')} - Fav: {p.get('pop', 'Unknown')} - Rank: {p.get('rank', 'Unknown')}\n")

# Write suscup30.txt
if cup30:
    with open("suscup30.txt", "w", encoding="utf-8") as f:
        f.write("Sus Cup 30 Results\n\n")
        f.write("Special Category Winners:\n")
        for category, winner in special_winners_30.items():
            f.write(f"  {category}: {winner['player']} ({winner['pos']} - {winner['uma']})\n")
        f.write("\nAll Participants:\n")
        for p in cup30.get("participants", []):
            f.write(f"{p.get('pos', 'Unknown')} - {p.get('uma', 'Unknown')} ({p.get('player', 'Unknown')}) - Strategy: {p.get('strategy', 'Unknown')} - Gap: {p.get('gap', 'Unknown')} - Fav: {p.get('pop', 'Unknown')} - Rank: {p.get('rank', 'Unknown')}\n")

print("txt files created successfully!")
