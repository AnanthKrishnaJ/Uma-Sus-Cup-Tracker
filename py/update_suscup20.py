import json

updates = {
    1: {"rank": "A+", "number": 11, "title": "Witness to Legend", "strategy": "Pace", "time": "1:56.3", "fav": 6},
    2: {"rank": "A+", "number": 4, "title": "Blinding Flash", "strategy": "Late", "margin": "1/2 L", "fav": 10},
    3: {"rank": "A+", "number": 17, "title": "Witness to Legend", "strategy": "End", "margin": "1 L", "fav": 2},
    4: {"rank": "A+", "number": 3, "title": "Witness to Legend", "strategy": "Late", "margin": "1 L", "fav": 5},
    5: {"rank": "S", "number": 1, "title": "Witness to Legend", "strategy": "End", "margin": "Neck", "fav": 8},
    6: {"rank": "A+", "number": 16, "title": "Dream Team", "strategy": "Pace", "margin": "Head", "fav": 12},
    7: {"rank": "S", "number": 18, "title": "Witness to Legend", "strategy": "Late", "margin": "Head", "fav": 1},
    8: {"rank": "A+", "number": 5, "title": "Witness to Legend", "strategy": "Pace", "margin": "Head", "fav": 3},
    9: {"rank": "A+", "number": 15, "title": "Mesmerizing Muscle", "strategy": "Late", "margin": "1/2 L", "fav": 9},
    10: {"rank": "A+", "number": 10, "title": "Witness to Legend", "strategy": "End", "margin": "1/2 L", "fav": 4},
    11: {"rank": "A+", "number": 2, "title": "Spirit Burst", "strategy": "Front", "margin": "Neck", "fav": 14},
    12: {"title": "Finals Champion", "strategy": "Pace", "margin": "Head", "fav": 13},
    13: {"rank": "A+", "number": 12, "title": "Spirit Burst", "strategy": "Late", "margin": "1 1/4 L", "fav": 11},
    14: {"rank": "A", "number": 6, "title": "Legendary Diva", "strategy": "Front", "margin": "3/4 L", "fav": 15},
    15: {"rank": "A+", "number": 9, "title": "Witness to Legend", "strategy": "Front", "margin": "1/2 L", "fav": 7},
    16: {"rank": "B", "number": 14, "strategy": "End", "margin": "4 L", "fav": 18},
    17: {"rank": "B", "number": 8, "strategy": "Front", "margin": "4 L", "fav": 16},
    18: {"rank": "B", "number": 13, "strategy": "Front", "margin": "1 3/4 L", "fav": 17}
}

with open('../.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

for race in data['races']:
    if race.get('id') == 20:
        for p in race['participants']:
            pos = p['pos']
            if pos in updates:
                upd = updates[pos]
                if 'rank' in upd: p['rank'] = upd['rank']
                if 'number' in upd: p['number'] = upd['number']
                
                # Keep the style winner title if one existed and was more specific, or just append it
                # Actually earlier I assigned "Pace Style Winner" to 1st place.
                # Let's keep the existing title logic but append or replace.
                # The user explicitly says "Title: Witness to Legend"
                if 'title' in upd:
                    # check if p['title'] contains "Style Winner"
                    existing_title = p.get('title', '')
                    if "Style Winner" in existing_title:
                        p['title'] = upd['title'] + " / " + existing_title
                    else:
                        p['title'] = upd['title']
                
                if 'strategy' in upd: p['strategy'] = upd['strategy']
                if 'time' in upd: p['time'] = upd['time']
                if 'margin' in upd: p['margin'] = upd['margin']
                if 'fav' in upd: p['fav'] = upd['fav']

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('../.vscode/suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUS CUP 20 details updated!")
