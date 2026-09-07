import json
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const NPC_PROFILES = {};')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

uma_db_start = text.find('const UMA_DATABASE = {')
uma_db_end = text.find('};', uma_db_start)
uma_db_str = text[uma_db_start + 21:uma_db_end+1]

mapping = {}
for match in re.finditer(r'id:\s*\"([^\"]+)\".*?name:\s*\"([^\"]+)\".*?version:\s*\"([^\"]+)\"', uma_db_str):
    name = match.group(2)
    id_ = match.group(1)
    version = match.group(3)
    # Give priority to standard versions if we haven't seen this name yet, or just store all.
    if name not in mapping:
        mapping[name] = {'id': id_, 'version': version}


participants_raw = [
    ("Mayano Top Gun", "Ananth", "Legendary Reprise", "SS", 6, "Front", 1, "1:57.1", 13),
    ("Oguri Cap", "Vilthaar", "Legendary Reprise", "UG Rank 9", 5, "Pace", 2, "3/4 L", 5),
    ("Seiun Sky", "Cruzi", "Independent Learner", "SS", 18, "Front", 3, "Nose", 8),
    ("Oguri Cap", "Cyclobly", "The Key to Success", "UG Rank 3", 9, "Pace", 4, "3/4 L", 14),
    ("Grass Wonder", "agnes", "Nepo Uma", "UG Rank 5", 14, "Late", 5, "1/2 L", 6),
    ("Meisho Doto", "Cyclobly", "Legendary Reprise", "UF Rank 2", 17, "Pace", 6, "Neck", 1),
    ("Gold Ship", "Jiinxye", "Team Player Star Slayer", "SS", 1, "Pace", 7, "2 1/2 L", 16),
    ("Mihono Bourbon", "Cruzi", "Legendary Reprise", "UG Rank 3", 16, "Front", 8, "Neck", 9),
    ("King Halo", "agnes", "Queen of Dance", "UG Rank 3", 3, "Late", 9, "Neck", 3),
    ("Maruzensky", "Ananth", "The Key to Success", "UG", 2, "Front", 10, "3/4 L", 17),
    ("Meisho Doto", "Vilthaar", "Legendary Reprise", "UG Rank 7", 10, "Pace", 11, "3/4 L", 4),
    ("Tokai Teio", "Jiinxye", "Independent Learner", "SS", 8, "Pace", 12, "1/2 L", 10),
    ("Special Week", "agnes", "Powerhouse", "UG Rank 7", 13, "Late", 13, "Nose", 2),
    ("T.M. Opera O", "Jiinxye", "Independent Learner", "SS", 11, "Pace", 14, "2 L", 12),
    ("Kitasan Black", "Ananth", "Legendary Reprise", "UG", 15, "Front", 15, "Neck", 15),
    ("Kitasan Black", "Cruzi", "Legendary Reprise", "SS", 12, "Front", 16, "3/4 L", 11),
    ("Fuji Kiseki", "Vilthaar", "Legendary Reprise", "UG Rank 5", 7, "Pace", 17, "3/4 L", 7),
    ("Agnes Tachyon", "Cyclobly", "Witness to Legend", "S", 4, "Pace", 18, "1 1/2 L", 18)
]

participants = []
for p in participants_raw:
    uma = p[0]
    p_dict = {
        'uma': uma,
        'player': p[1],
        'title': p[2],
        'rank': p[3],
        'number': p[4],
        'strategy': p[5],
        'position': p[6],
        'finishTime': p[7],
        'pop': p[8],
        'participantType': 'Playable Uma'
    }
    if uma in mapping:
        p_dict['umaId'] = mapping[uma]['id']
        p_dict['version'] = mapping[uma]['version']
    participants.append(p_dict)

new_race = {
    'id': '28',
    'cupNumber': 28,
    'cupName': 'Sus Cup 28 - Triple Threat',
    'name': 'Tenno Sho (Autumn)',
    'date': '2026-08-27',
    'roomId': '70312406',
    'race': 'Tenno Sho (Autumn)',
    'course': 'Tokyo',
    'surface': 'Turf',
    'distance': '2000m',
    'distanceType': 'Medium',
    'direction': 'Left',
    'weather': 'Rainy',
    'ground': 'Soft',
    'mood': 'Good',
    'season': 'Fall',
    'rankLimit': 'No Limit',
    'specialRule': '3 runners per person, all 3 runners must use the same strategy (Triple Threat)',
    'result': '5th Place',
    'comment': 'It seems like our trainee had trouble keeping up with the pack.',
    'images': [],
    'registeredRunners': 18,
    'participants': participants
}

new_winner = {
    'cup': 'Sus Cup 28',
    'cupNumber': 28,
    'date': '2026-08-27',
    'uma': 'Mayano Top Gun',
    'trainer': 'Ananth',
    'player': 'Ananth',
    'type': 'Uma Musume'
}

data['races'].append(new_race)
data['winners'].append(new_winner)

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_text = text[:start + 21] + new_json + '\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Sus Cup 28 added successfully!")
