import json
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('\n};', start)
data = json.loads(text[start + 21:end + 2])

# Cup 26 data
table_str = """
|  1st | Special Week   | 15 | SS   | Derby Dreamer             | agnes       | Pace          | **1:58.0** | No. 8  |
|  2nd | Oguri Cap      |  9 | UG   | Legendary Reprise         | Ananth      | Pace          | 1 1/2 L    | No. 1  |
|  3rd | Agnes Tachyon  | 14 | UG   | Faster than Light         | Cruzi       | Pace          | 1 3/4 L    | No. 10 |
|  4th | Mejiro Dober   | 16 | SS   | Independent Learner       | GohanXGAMER | Late          | 1/2 L      | No. 15 |
|  5th | Silence Suzuka | 11 | SS   | Otherworldly Front-Runner | agnes       | Front         | Nose       | No. 2  |
|  6th | Agnes Digital  | 18 | SS   | The Key to Success        | Cruzi       | Pace          | Neck       | No. 13 |
|  7th | Maruzensky     |  6 | UG   | The Key to Success        | Ananth      | Front         | 1/2 L      | No. 3  |
|  8th | Tokai Teio     |  3 | S+   | Independent Learner       | Jiinxye     | Pace          | 3/4 L      | No. 4  |
|  9th | Seiun Sky      | 12 | SS   | The Key to Success        | GohanXGAMER | Front         | 1 L        | No. 12 |
| 10th | Admire Vega    |  2 | UG   | Brightest Star            | GohanXGAMER | End           | Nose       | No. 7  |
| 11th | Mayano Top Gun | 10 | SS   | Independent Learner       | Cruzi       | Pace          | 2 1/2 L    | No. 6  |
| 12th | Gold Ship      | 17 | SS   | Cool and Composed         | Jiinxye     | End           | Neck       | No. 11 |
| 13th | T.M. Opera O   | 13 | S+   | Queen of Dance            | Jiinxye     | Pace          | 1/2 L      | No. 9  |
| 14th | Air Shakur     |  5 | SS   | Independent Learner       | agnes       | End           | Neck       | No. 5  |
| 15th | Gold City      |  1 | S+   | Independent Learner       | Ananth      | Pace          | Neck       | No. 14 |
| 16th | Oishii Parfait |  4 | A    | \u2014                    | \u2014      | Front         | 5 L        | No. 17 |
| 17th | Cornet Rhythm  |  7 | A    | \u2014                    | \u2014      | Pace          | 1/2 L      | No. 16 |
| 18th | Tropical Sky   |  8 | A    | \u2014                    | \u2014      | End           | Head       | No. 18 |
"""

parsed_data = {}
for line in table_str.strip().split('\n'):
    cols = [c.strip() for c in line.split('|')[1:-1]]
    if not cols: continue
    pos = int(cols[0].replace('st','').replace('nd','').replace('rd','').replace('th',''))
    no = int(cols[2])
    rank = cols[3]
    title = cols[4] if cols[4] != '\u2014' else ''
    style = cols[6]
    finish = cols[7].replace('**', '')
    fav = cols[8].replace('No. ', '')
    fav = int(fav) if fav.isdigit() else None
    
    parsed_data[pos] = { 'no': no, 'rank': rank, 'title': title, 'style': style, 'finish': finish, 'fav': fav }

# Find and update Cup 26
for race in data['races']:
    if race.get('id') == 26:
        for p in race.get('participants', []):
            if p.get('position') in parsed_data:
                pd = parsed_data[p['position']]
                p['no'] = pd['no']
                p['rank'] = pd['rank']
                p['style'] = pd['style']
                p['finish'] = pd['finish']
                p['fav'] = pd['fav']
                if pd['title']:
                    p['title'] = pd['title']

# Build Cup 28 participants
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
    'id': 28,
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
    'rankLimit': 'No Rank Limit',
    'specialRule': '3 runners per person, all 3 runners must use the same strategy (Triple Threat)',
    'images': [
        'suscupimages21-30/28.1.png',
        'suscupimages21-30/28.2.png',
        'suscupimages21-30/28.3.png',
        'suscupimages21-30/28.4.png'
    ],
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

if not any(r.get('id') == 28 for r in data['races']):
    data['races'].append(new_race)
if not any(w.get('cupNumber') == 28 for w in data['winners']):
    data['winners'].append(new_winner)

new_json = json.dumps(data, indent=2, ensure_ascii=False)
new_text = text[:start + 21] + new_json + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Safely updated Cup 26 and added Cup 28!")
