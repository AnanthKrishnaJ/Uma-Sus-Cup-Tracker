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
    if name not in mapping:
        mapping[name] = {'id': id_, 'version': version}

participants_raw = [
    ("Oguri Cap", "Cyciesta", "The Key to Success", "Unknown", 11, "Pace", 1, "1:56.1", 11),
    ("Silence Suzuka", "agnes", "Otherworldly Front-Runner", "Unknown", 3, "Front", 2, "1/2 L", 8),
    ("Grass Wonder", "Cruzi", "Legendary Reprise", "Unknown", 14, "Late", 3, "2 L", 10),
    ("Nice Nature", "Cruzi", "Legendary Reprise", "Unknown", 12, "Late", 4, "1 1/4 L", 9),
    ("Silence Suzuka", "Cyciesta", "Legendary Reprise", "Unknown", 5, "Front", 5, "Neck", 5),
    ("Eishin Flash", "Ananth", "Legendary Reprise", "Unknown", 16, "Pace", 6, "3/4 L", 1),
    ("Agnes Tachyon", "Cruzi", "Faster than Light", "Unknown", 2, "Pace", 7, "1/2 L", 3),
    ("Grass Wonder", "Ananth", "Legendary Reprise", "Unknown", 8, "Pace", 8, "1/2 L", 2),
    ("Grass Wonder", "agnes", "Shared Smarts", "Unknown", 7, "Late", 9, "1 L", 7),
    ("Mejiro McQueen", "agnes", "Legendary Reprise", "Unknown", 4, "Pace", 10, "1/2 L", 4),
    ("Sunset Groom", "Not shown", "—", "Unknown", 17, "Pace", 11, "1/2 L", 13),
    ("Yggdra Valley", "Not shown", "—", "Unknown", 18, "End", 12, "1 L", 18),
    ("Aqua Oasis", "Not shown", "—", "Unknown", 11, "Late", 13, "1 1/4 L", 15),
    ("Shadow Stalker", "Not shown", "—", "Unknown", 9, "End", 14, "3/4 L", 17),
    ("Tide and Flow", "Not shown", "—", "Unknown", 6, "End", 15, "1 1/2 L", 16),
    ("Code of Heart", "Not shown", "—", "Unknown", 15, "Pace", 16, "1 L", 12),
    ("Agnes Tachyon", "Cyciesta", "Witness to Legend", "Unknown", 13, "End", 17, "Nose", 14),
    ("Maruzensky", "Ananth", "Witness to Legend", "Unknown", 10, "Front", 18, "2 L", 6),
]

participants = []
for i, p in enumerate(participants_raw):
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
    if p[1] == 'Not shown':
        p_dict['participantType'] = 'NPC'
        p_dict['rank'] = '-'
        p_dict['title'] = '-'
    
    if uma in mapping:
        # Special logic for Oguri Cap (1st place)
        if uma == "Oguri Cap" and i == 0:
            p_dict['umaId'] = '100602'
            p_dict['version'] = 'Christmas' # just a guess for version, id is what matters
        else:
            p_dict['umaId'] = mapping[uma]['id']
            p_dict['version'] = mapping[uma]['version']
    participants.append(p_dict)

new_race = {
    'id': '29',
    'cupNumber': 29,
    'cupName': 'Sus Cup 29 — RGB Race',
    'name': 'Niigata Turf 2000m',
    'date': '2026-09-11',
    'roomId': '72085153',
    'race': 'Niigata Turf 2000m',
    'course': 'Niigata',
    'surface': 'Turf',
    'distance': '2000m',
    'distanceType': 'Medium',
    'direction': 'Left / Outer',
    'weather': 'Snow',
    'ground': 'Soft',
    'mood': 'Great',
    'season': 'Spring',
    'rankLimit': 'Unknown',
    'specialRule': 'RGB Race',
    'result': '6th Place', # Ananth got 6th
    'comment': '',
    'images': ['29.1.png', '29.2.png', '29.3.png', '29.4.png'],
    'registeredRunners': 18,
    'participants': participants
}

new_winner = {
    'cup': 'Sus Cup 29',
    'cupNumber': 29,
    'date': '2026-09-11',
    'uma': 'Oguri Cap',
    'trainer': 'Cyciesta',
    'player': 'Cyciesta',
    'type': 'Uma Musume'
}

data['races'].append(new_race)
data['winners'].append(new_winner)

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_text = text[:start + 21] + new_json + '\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Sus Cup 29 added successfully!")
