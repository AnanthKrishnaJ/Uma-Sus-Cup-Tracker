import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build Cup 23 object
cup23 = {
    "id": 23,
    "cup": "23",
    "name": "Mixed Rarity Race",
    "track": "Nakayama Turf 2000m (Medium)",
    "direction": "Right / Inner",
    "ground": "Firm",
    "winner": "Narita Taishin",
    "winningTime": "1:56.1",
    "specialRule": "Mixed Rarity Race (3*, 2*, 1* Winners)",
    "scenarioWinners": {
        "3* winner": { "player": "Jinxy", "uma": "Narita Taishin", "pos": 1, "umaId": "narita-taishin" },
        "2* winner": { "player": "agnes", "uma": "Air Groove", "pos": 9, "umaId": "air-groove" },
        "1* winner": { "player": "Shadow Amber", "uma": "Agnes Tachyon", "pos": 2, "umaId": "agnes-tachyon" }
    },
    "participants": [
        {"pos": 1, "player": "Jinxy", "uma": "Narita Taishin", "rank": "SS", "title": "Phenomenal", "strategy": "End", "time": "1:56.1", "pop": 17, "umaId": "narita-taishin"},
        {"pos": 2, "player": "Shadow Amber", "uma": "Agnes Tachyon", "rank": "S", "title": "Leading the Charge", "strategy": "Pace", "time": "1 L", "pop": 8, "umaId": "agnes-tachyon"},
        {"pos": 3, "player": "Cruzi", "uma": "Mihono Bourbon", "rank": "SS", "title": "Leading the Charge", "strategy": "Front", "time": "Head", "pop": 11, "umaId": "mihono-bourbon"},
        {"pos": 4, "player": "agnes", "uma": "King Halo", "rank": "S+", "title": "Goddess", "strategy": "Late", "time": "Head", "pop": 7, "umaId": "king-halo"},
        {"pos": 5, "player": "Cyclobly", "uma": "Nice Nature", "rank": "SS", "title": "Leading the Charge", "strategy": "Late", "time": "1 1/2 L", "pop": 3, "umaId": "nice-nature"},
        {"pos": 6, "player": "Cruzi", "uma": "Agnes Tachyon", "rank": "S+", "title": "Leading the Charge", "strategy": "Pace", "time": "Head", "pop": 5, "umaId": "agnes-tachyon"},
        {"pos": 7, "player": "agnes", "uma": "T.M. Opera O", "rank": "S+", "title": "Centurial Overlord", "strategy": "Pace", "time": "Nose", "pop": 1, "umaId": "tm-opera-o"},
        {"pos": 8, "player": "Shadow Amber", "uma": "Oguri Cap", "rank": "S", "title": "Ideal Idol", "strategy": "Pace", "time": "Nose", "pop": 6, "umaId": "oguri-cap"},
        {"pos": 9, "player": "agnes", "uma": "Air Groove", "rank": "S", "title": "Empress", "strategy": "Late", "time": "Head", "pop": 16, "umaId": "air-groove"},
        {"pos": 10, "player": "Ananth", "uma": "Eishin Flash", "rank": "SS", "title": "Leading the Charge", "strategy": "Pace", "time": "1 L", "pop": 13, "umaId": "eishin-flash"},
        {"pos": 11, "player": "Cruzi", "uma": "Gold Ship", "rank": "S", "title": "Unpredictable", "strategy": "End", "time": "3/4 L", "pop": 9, "umaId": "gold-ship"},
        {"pos": 12, "player": "Jinxy", "uma": "Vodka", "rank": "S", "title": "Goddess", "strategy": "Late", "time": "Neck", "pop": 10, "umaId": "vodka"},
        {"pos": 13, "player": "Cyclobly", "uma": "Oguri Cap", "rank": "SS", "title": "Leading the Charge", "strategy": "Pace", "time": "1/2 L", "pop": 4, "umaId": "oguri-cap"},
        {"pos": 14, "player": "Cyclobly", "uma": "Grass Wonder", "rank": "SS", "title": "Leading the Charge", "strategy": "Late", "time": "Nose", "pop": 2, "umaId": "grass-wonder"},
        {"pos": 15, "player": "Haji", "uma": "Mejiro Ryan", "rank": "A+", "title": "Mesmerizing Muscle", "strategy": "Late", "time": "1/2 L", "pop": 12, "umaId": "mejiro-ryan"},
        {"pos": 16, "player": "Jinxy", "uma": "Winning Ticket", "rank": "S", "title": "Herald of a New Age", "strategy": "Late", "time": "3/4 L", "pop": 14, "umaId": "winning-ticket"},
        {"pos": 17, "player": "Haji", "uma": "Special Week", "rank": "S", "title": "Leading the Charge", "strategy": "Pace", "time": "1 3/4 L", "pop": 15, "umaId": "special-week"},
        {"pos": 18, "player": "Haji", "uma": "Super Creek", "rank": "A+", "title": "Legendary Diva", "strategy": "Pace", "time": "1 1/4 L", "pop": 18, "umaId": "super-creek"}
    ]
}

cup23_json = json.dumps(cup23, indent=6)

# Check if already added
if '"id": 23,' in content and '"cup": "23"' in content:
    print("Cup 23 already exists.")
else:
    # Insert after "races": [
    content = content.replace('"races": [', '"races": [\n' + cup23_json + ',')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Cup 23.")
