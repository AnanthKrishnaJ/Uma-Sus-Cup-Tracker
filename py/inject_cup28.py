import json
import re

participants_data = [
    {"pos": 1, "uma": "Mayano Top Gun", "player": "Ananth", "title": "Legendary Reprise", "rank": "SS", "number": 6, "strategy": "Front", "time": "1:57.1", "pop": 13, "umaId": "mayano-top-gun", "version": "Standard / Original"},
    {"pos": 2, "uma": "Oguri Cap", "player": "Vilthaar", "title": "Legendary Reprise", "rank": "UG Rank 9", "number": 5, "strategy": "Pace", "gap": "3/4 L", "time": "3/4 L", "pop": 5, "umaId": "100602", "version": "Ashen Miracle"},
    {"pos": 3, "uma": "Seiun Sky", "player": "Cruzi", "title": "Independent Learner", "rank": "SS", "number": 18, "strategy": "Front", "gap": "Nose", "time": "Nose", "pop": 8, "umaId": "seiun-sky", "version": "Standard / Original"},
    {"pos": 4, "uma": "Oguri Cap", "player": "Cyclobly", "title": "The Key to Success", "rank": "UG Rank 3", "number": 9, "strategy": "Pace", "gap": "3/4 L", "time": "3/4 L", "pop": 14, "umaId": "100602", "version": "Ashen Miracle"},
    {"pos": 5, "uma": "Grass Wonder", "player": "Agnes", "title": "Nepo Uma", "rank": "UG Rank 5", "number": 14, "strategy": "Late", "gap": "1/2 L", "time": "1/2 L", "pop": 6, "umaId": "grass-wonder", "version": "Standard / Original"},
    {"pos": 6, "uma": "Meisho Doto", "player": "Cyclobly", "title": "Legendary Reprise", "rank": "UF Rank 2", "number": 17, "strategy": "Pace", "gap": "Neck", "time": "Neck", "pop": 1, "umaId": "105802-meisho-doto", "version": "Dot-o'-Lantern"},
    {"pos": 7, "uma": "Gold Ship", "player": "Jiinxye", "title": "Team Player Star Slayer", "rank": "SS", "number": 1, "strategy": "Pace", "gap": "2 1/2 L", "time": "2 1/2 L", "pop": 16, "umaId": "gold-ship", "version": "Standard / Original"},
    {"pos": 8, "uma": "Mihono Bourbon", "player": "Cruzi", "title": "Legendary Reprise", "rank": "UG Rank 3", "number": 16, "strategy": "Front", "gap": "Neck", "time": "Neck", "pop": 9, "umaId": "mihono-bourbon", "version": "Standard / Original"},
    {"pos": 9, "uma": "King Halo", "player": "Agnes", "title": "Queen of Dance", "rank": "UG Rank 3", "number": 3, "strategy": "Late", "gap": "Neck", "time": "Neck", "pop": 3, "umaId": "king-halo", "version": "Standard / Original"},
    {"pos": 10, "uma": "Maruzensky", "player": "Ananth", "title": "The Key to Success", "rank": "UG", "number": 2, "strategy": "Front", "gap": "3/4 L", "time": "3/4 L", "pop": 17, "umaId": "maruzensky", "version": "Standard / Original"},
    {"pos": 11, "uma": "Meisho Doto", "player": "Vilthaar", "title": "Legendary Reprise", "rank": "UG Rank 7", "number": 10, "strategy": "Pace", "gap": "3/4 L", "time": "3/4 L", "pop": 4, "umaId": "105802-meisho-doto", "version": "Dot-o'-Lantern"},
    {"pos": 12, "uma": "Tokai Teio", "player": "Jiinxye", "title": "Independent Learner", "rank": "SS", "number": 8, "strategy": "Pace", "gap": "1/2 L", "time": "1/2 L", "pop": 10, "umaId": "tokai-teio", "version": "Standard / Original"},
    {"pos": 13, "uma": "Special Week", "player": "Agnes", "title": "Powerhouse", "rank": "UG Rank 7", "number": 13, "strategy": "Late", "gap": "Nose", "time": "Nose", "pop": 2, "umaId": "special-week", "version": "Standard / Original"},
    {"pos": 14, "uma": "T.M. Opera O", "player": "Jiinxye", "title": "Independent Learner", "rank": "SS", "number": 11, "strategy": "Pace", "gap": "2 L", "time": "2 L", "pop": 12, "umaId": "tm-opera-o", "version": "Standard / Original"},
    {"pos": 15, "uma": "Kitasan Black", "player": "Ananth", "title": "Legendary Reprise", "rank": "UG", "number": 15, "strategy": "Front", "gap": "Neck", "time": "Neck", "pop": 15, "umaId": "kitasan-black", "version": "Standard / Original"},
    {"pos": 16, "uma": "Kitasan Black", "player": "Cruzi", "title": "Legendary Reprise", "rank": "SS", "number": 12, "strategy": "Front", "gap": "3/4 L", "time": "3/4 L", "pop": 11, "umaId": "kitasan-black", "version": "Standard / Original"},
    {"pos": 17, "uma": "Fuji Kiseki", "player": "Vilthaar", "title": "Legendary Reprise", "rank": "UG Rank 5", "number": 7, "strategy": "Pace", "gap": "3/4 L", "time": "3/4 L", "pop": 7, "umaId": "100502-fuji-kiseki", "version": "Succès Étoilé"},
    {"pos": 18, "uma": "Agnes Tachyon", "player": "Cyclobly", "title": "Witness to Legend", "rank": "S", "number": 4, "strategy": "Pace", "gap": "1 1/2 L", "time": "1 1/2 L", "pop": 18, "umaId": "agnes-tachyon", "version": "Standard / Original"}
]

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find Cup 28
cup28_idx = text.rfind('"cupNumber": 28')
participants_start = text.find('"participants": [', cup28_idx)
participants_end = text.find(']', participants_start) + 1

# Convert list to JSON string with 6 space indent to match the file roughly, 
# but python json.dumps doesn't easily let us indent the first line differently, 
# so we format it carefully.
json_str = json.dumps(participants_data, indent=2)
# Indent the whole block by 6 spaces (except the first line if it's placed after `"participants": `)
indented = '\n'.join('      ' + line if i > 0 else line for i, line in enumerate(json_str.split('\n')))

new_text = text[:participants_start] + '"participants": ' + indented + text[participants_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Injected 18 participants for Cup 28.")
