import json
import re

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the corrupted Sus Cup 6 object and replace it.
# It currently looks like this:
#         {
#             "id": 6,
#             "cupNumber": "SUS CUP 6",
#             "name": "UNIQUE EPITHETS / STEAMY SOLIDARITY",
#             "date": "2025-09-03",
#             "images": [
#                 "suscupimages1-10/suscup6.1.png",
#                 "suscupimages1-10/suscup6.2.png",
#                 "suscupimages1-10/suscup6.3.png",
#                 "suscupimages1-10/suscup6.4.png"
#             ],
#         {
#             "id": 11,

# Let's use a regex to match from `{ "id": 6,` up to just before `{ "id": 11,`
pattern = re.compile(r'\{\s*"id": 6,\s*"cupNumber": "SUS CUP 6",\s*"name": "UNIQUE EPITHETS / STEAMY SOLIDARITY",\s*"date": "2025-09-03",\s*"images": \[\s*"suscupimages1-10/suscup6\.1\.png",\s*"suscupimages1-10/suscup6\.2\.png",\s*"suscupimages1-10/suscup6\.3\.png",\s*"suscupimages1-10/suscup6\.4\.png"\s*\],\s*', re.DOTALL)

match = pattern.search(content)
if match:
    print("Found corrupted Sus Cup 6. Fixing it.")
    
    suscup6_race = {
        "id": 6,
        "cupNumber": "SUS CUP 6",
        "name": "UNIQUE EPITHETS / STEAMY SOLIDARITY",
        "date": "2025-09-03",
        "time": "18:18",
        "roomId": "9075 4387",
        "course": "Nakayama Turf",
        "surface": "Turf",
        "distance": "2500m",
        "distanceType": "Long",
        "direction": "Right-handed / Inner",
        "weather": "Random",
        "ground": "Random",
        "condition": "Great",
        "mood": "Great",
        "season": "Random",
        "restriction": "No rank restriction specified",
        "images": [
            "suscupimages1-10/suscup6.1.png",
            "suscupimages1-10/suscup6.2.png",
            "suscupimages1-10/suscup6.3.png",
            "suscupimages1-10/suscup6.4.png"
        ],
        "participants": [
            { "pos": 1, "uma": "Gold Ship", "player": "Cyclobly", "number": 14, "rank": "A", "title": "The GOAT", "strategy": "End", "time": "2:29.0", "pop": 5, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/gold-ship" },
            { "pos": 2, "uma": "Mejiro McQueen", "player": "Jiinxye", "number": 7, "rank": "B+", "title": "Steamy Solidarity", "strategy": "Pace", "gap": "1 1/4 L", "pop": 2, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/mejiro-mcqueen" },
            { "pos": 3, "uma": "Symboli Rudolf", "player": "agnes", "number": 12, "rank": "A", "title": "Emperor", "strategy": "Pace", "gap": "1 1/4 L", "pop": 3, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/symboli-rudolf" },
            { "pos": 4, "uma": "Gold Ship", "player": "Yves", "number": 10, "rank": "A", "title": "The GOAT", "strategy": "End", "gap": "2 L", "pop": 7, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/gold-ship" },
            { "pos": 5, "uma": "Mayano Top Gun", "player": "agnes", "number": 1, "rank": "A", "title": "Free Spirit", "strategy": "End", "gap": "3/4 L", "pop": 6, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/mayano-top-gun" },
            { "pos": 6, "uma": "Keyboard Rhythm", "player": "NPC", "number": 8, "rank": "B", "title": "Keyboard Rhythm", "strategy": "End", "gap": "5 L", "pop": 11, "version": "NPC", "participantType": "NPC Uma", "characterUrl": None },
            { "pos": 7, "uma": "Tokai Teio", "player": "Jiinxye", "number": 5, "rank": "A", "title": "Steamy Solidarity", "strategy": "Pace", "gap": "3/4 L", "pop": 4, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/tokai-teio" },
            { "pos": 8, "uma": "Ogress", "player": "NPC", "number": 3, "rank": "B", "title": "Ogress", "strategy": "End", "gap": "2 1/2 L", "pop": 9, "version": "NPC", "participantType": "NPC Uma", "characterUrl": None },
            { "pos": 9, "uma": "Oguri Cap", "player": "Cyclobly", "number": 13, "rank": "A", "title": "Legendary Diva", "strategy": "Pace", "gap": "3 L", "pop": 1, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap" },
            { "pos": 10, "uma": "Agnes Tachyon", "player": "Cruzi", "number": 15, "rank": "B+", "title": "Steamy Solidarity", "strategy": "Pace", "gap": "Head", "pop": 13, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon" },
            { "pos": 11, "uma": "Ribbon Nocturne", "player": "NPC", "number": 9, "rank": "B", "title": "Ribbon Nocturne", "strategy": "Pace", "gap": "Head", "pop": 12, "version": "NPC", "participantType": "NPC Uma", "characterUrl": None },
            { "pos": 12, "uma": "Maleficus", "player": "NPC", "number": 4, "rank": "B", "title": "Maleficus", "strategy": "Late", "gap": "1 3/4 L", "pop": 15, "version": "NPC", "participantType": "NPC Uma", "characterUrl": None },
            { "pos": 13, "uma": "Nice Nature", "player": "Yves", "number": 16, "rank": "A", "title": "Finals Champion", "strategy": "Late", "gap": "5 L", "pop": 8, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/106001-nice-nature" },
            { "pos": 14, "uma": "Oguri Cap", "player": "GohanXGAMER", "number": 6, "rank": "A", "title": "Finals Champion", "strategy": "Pace", "gap": "2 1/2 L", "pop": 10, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap" },
            { "pos": 15, "uma": "Super Creek", "player": "GohanXGAMER", "number": 2, "rank": "B", "title": "Speedy Stayer", "strategy": "Pace", "gap": "2 L", "pop": 16, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/super-creek" },
            { "pos": 16, "uma": "Tokai Teio", "player": "Cruzi", "number": 11, "rank": "B+", "title": "Monarch", "strategy": "Pace", "gap": "3/4 L", "pop": 14, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/tokai-teio" }
        ]
    }
    
    # Dump it perfectly.
    race_json = json.dumps(suscup6_race, indent=12)
    
    # We want it to be indented by 8 spaces to match the races array, so let's adjust.
    formatted_lines = []
    for line in race_json.split('\n'):
        if line == '{':
            formatted_lines.append('        {')
        else:
            # We used indent=12, but we can just use indent=4 and add 8 spaces to everything.
            pass
            
    race_json = json.dumps(suscup6_race, indent=4)
    formatted_lines = []
    for line in race_json.split('\n'):
        if line == '{' or line == '}':
            formatted_lines.append('        ' + line)
        else:
            formatted_lines.append('        ' + line)
            
    replacement = '\n'.join(formatted_lines) + ',\n'
    
    content = content[:match.start()] + replacement + content[match.end():]
    
    # Write it back.
    with open('suscup1.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed!")
else:
    print("Corrupted Sus Cup 6 not found via regex!")
