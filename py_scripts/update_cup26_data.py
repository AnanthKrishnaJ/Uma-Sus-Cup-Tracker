import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

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
| 16th | Oishii Parfait |  4 | A    | —                         | —           | Front         | 5 L        | No. 17 |
| 17th | Conet Rhythm   |  7 | A    | —                         | —           | Pace          | 1/2 L      | No. 16 |
| 18th | Tropical Sky   |  8 | A    | —                         | —           | End           | Head       | No. 18 |
"""

parsed_data = {}
for line in table_str.strip().split('\n'):
    cols = [c.strip() for c in line.split('|')[1:-1]]
    if not cols:
        continue
    pos = int(cols[0].replace('st','').replace('nd','').replace('rd','').replace('th',''))
    uma = cols[1]
    no = int(cols[2])
    rank = cols[3]
    title = cols[4] if cols[4] != '—' else ''
    trainer = cols[5] if cols[5] != '—' else 'NPC'
    style = cols[6]
    finish = cols[7].replace('**', '')
    fav = cols[8].replace('No. ', '')
    fav = int(fav) if fav.isdigit() else None
    
    parsed_data[pos] = {
        'no': no,
        'rank': rank,
        'title': title,
        'trainer': trainer,
        'style': style,
        'finish': finish,
        'fav': fav
    }

start = text.find('const INITIAL_DATA = ')
db_start = text.find('const UMA_DATABASE = ')
end = text.rfind('};', start, db_start)
data = json.loads(text[start + 21:end + 1])

for race in data['races']:
    if race['cupNumber'] == 26 or race['id'] == 26:
        for p in race.get('participants', []):
            if p['pos'] in parsed_data:
                pd = parsed_data[p['pos']]
                p['no'] = pd['no']
                p['rank'] = pd['rank']
                p['style'] = pd['style']
                p['finish'] = pd['finish']
                p['fav'] = pd['fav']
                # The user wants to keep the existing title if it has scenario winners?
                # The user said "add whats important and nothing else". The table has actual titles (like "Derby Dreamer").
                # Let's keep the user's title, but maybe append the scenario winner stuff if it exists?
                # Actually, the user's HTML might already display scenario winners differently, let's just set the title to the new one!
                if pd['title']:
                    p['title'] = pd['title']

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_text = text[:start + 21] + new_json + text[end + 1:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated Cup 26 participants with new table data!")
