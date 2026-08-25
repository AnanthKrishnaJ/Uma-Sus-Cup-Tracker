import re
import json
import sys

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Load the data we want to insert from add_suscup6.py (we can just import it dynamically or copy-paste it here)
suscup6_race = {
    "id": 6,
    "cupNumber": "SUS CUP 6",
    "name": "UNIQUE EPITHETS / STEAMY SOLIDARITY",
    "date": "2025-09-03",
    "images": ["suscupimages1-10/suscup6.1.png", "suscupimages1-10/suscup6.2.png", "suscupimages1-10/suscup6.3.png", "suscupimages1-10/suscup6.4.png"],
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
    "participants": [
        { "pos": 1, "uma": "Gold Ship", "player": "Cyclobly", "number": 14, "rank": "A", "title": "The GOAT", "strategy": "End", "time": "2:29.0", "pop": 5, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/gold-ship", "umaId": "100101" },
        { "pos": 2, "uma": "Mejiro McQueen", "player": "Jiinxye", "number": 7, "rank": "B+", "title": "Steamy Solidarity", "strategy": "Pace", "gap": "1 1/4 L", "pop": 2, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/mejiro-mcqueen", "umaId": "101301" },
        { "pos": 3, "uma": "Symboli Rudolf", "player": "agnes", "number": 12, "rank": "A", "title": "Emperor", "strategy": "Pace", "gap": "1 1/4 L", "pop": 3, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/symboli-rudolf", "umaId": "101701" },
        { "pos": 4, "uma": "Gold Ship", "player": "Yves", "number": 10, "rank": "A", "title": "The GOAT", "strategy": "End", "gap": "2 L", "pop": 7, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/gold-ship", "umaId": "100101" },
        { "pos": 5, "uma": "Mayano Top Gun", "player": "agnes", "number": 1, "rank": "A", "title": "Free Spirit", "strategy": "End", "gap": "3/4 L", "pop": 6, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/mayano-top-gun", "umaId": "102401" },
        { "pos": 6, "uma": "Keyboard Rhythm", "player": "NPC", "number": 8, "rank": "B", "title": "Keyboard Rhythm", "strategy": "End", "gap": "5 L", "pop": 11, "version": "NPC", "participantType": "NPC Uma", "characterUrl": None, "umaId": "Keyboard Rhythm" },
        { "pos": 7, "uma": "Tokai Teio", "player": "Jiinxye", "number": 5, "rank": "A", "title": "Steamy Solidarity", "strategy": "Pace", "gap": "3/4 L", "pop": 4, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/tokai-teio", "umaId": "100301" },
        { "pos": 8, "uma": "Ogress", "player": "NPC", "number": 3, "rank": "B", "title": "Ogress", "strategy": "End", "gap": "2 1/2 L", "pop": 9, "version": "NPC", "participantType": "NPC Uma", "characterUrl": None, "umaId": "Ogress" },
        { "pos": 9, "uma": "Oguri Cap", "player": "Cyclobly", "number": 13, "rank": "A", "title": "Legendary Diva", "strategy": "Pace", "gap": "3 L", "pop": 1, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap", "umaId": "100601" },
        { "pos": 10, "uma": "Agnes Tachyon", "player": "Cruzi", "number": 15, "rank": "B+", "title": "Steamy Solidarity", "strategy": "Pace", "gap": "Head", "pop": 13, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/agnes-tachyon", "umaId": "103201" },
        { "pos": 11, "uma": "Ribbon Nocturne", "player": "NPC", "number": 9, "rank": "B", "title": "Ribbon Nocturne", "strategy": "Pace", "gap": "Head", "pop": 12, "version": "NPC", "participantType": "NPC Uma", "characterUrl": None, "umaId": "Ribbon Nocturne" },
        { "pos": 12, "uma": "Maleficus", "player": "NPC", "number": 4, "rank": "B", "title": "Maleficus", "strategy": "Late", "gap": "1 3/4 L", "pop": 15, "version": "NPC", "participantType": "NPC Uma", "characterUrl": None, "umaId": "Maleficus" },
        { "pos": 13, "uma": "Nice Nature", "player": "Yves", "number": 16, "rank": "A", "title": "Finals Champion", "strategy": "Late", "gap": "5 L", "pop": 8, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/106001-nice-nature", "umaId": "106001" },
        { "pos": 14, "uma": "Oguri Cap", "player": "GohanXGAMER", "number": 6, "rank": "A", "title": "Finals Champion", "strategy": "Pace", "gap": "2 1/2 L", "pop": 10, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap", "umaId": "100601" },
        { "pos": 15, "uma": "Super Creek", "player": "GohanXGAMER", "number": 2, "rank": "B", "title": "Speedy Stayer", "strategy": "Pace", "gap": "2 L", "pop": 16, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/super-creek", "umaId": "104501" },
        { "pos": 16, "uma": "Tokai Teio", "player": "Cruzi", "number": 11, "rank": "B+", "title": "Monarch", "strategy": "Pace", "gap": "3/4 L", "pop": 14, "version": "Original / Default", "participantType": "Playable Uma", "characterUrl": "https://gametora.com/umamusume/characters/tokai-teio", "umaId": "100301" }
    ]
}

new_cup6_str = json.dumps(suscup6_race, indent=12)

# Fix indentation so it aligns well
formatted_str = ""
for line in new_cup6_str.split('\n'):
    if formatted_str == "":
        formatted_str = "        " + line
    else:
        formatted_str += "\n" + line

pattern = r'\{\s*"id":\s*6,\s*"cupNumber":\s*"SUS CUP 6"[\s\S]*?"participants":\s*\[\]\s*\}'
new_html = re.sub(pattern, formatted_str, html)

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Replaced Cup 6!")
