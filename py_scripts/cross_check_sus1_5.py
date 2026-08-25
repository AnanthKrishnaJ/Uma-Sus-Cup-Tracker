import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

markdown_text = """
## Sus Cup 1
| Pos.   | Uma            | Trainer     | Race No. |   Fav. | Finish Stat |
| ------ | -------------- | ----------- | -------: | -----: | ----------- |
| 1st | Oguri Cap      | GohanXGAMER |        7 |  No. 8 | **2:22.5**  |
| 2nd | Mihono Bourbon | Jinxye      |        2 |  No. 7 | 1¾ L        |
| 3rd | T.M. Opera O   | Yves        |       15 |  No. 3 | 1¼ L        |
| 4th    | Gold Ship      | agnes       |        4 |  No. 1 | 3 L         |
| 5th    | Agnes Tachyon  | Cyclobly    |       17 |  No. 5 | 3 L         |
| 6th    | Tokai Teio     | Cruzi       |        8 |  No. 6 | 3 L         |
| 7th    | Symboli Rudolf | agnes       |        9 |  No. 2 | 1 L         |
| 8th    | Narita Taishin | Cyclobly    |       16 |  No. 4 | 1 L         |
| 9th    | Revival Lyric  | —           |        1 | No. 14 | ¾ L         |
| 10th   | Marine Seagull | —           |       13 | No. 17 | ¾ L         |
| 11th   | T.M. Opera O   | Jinxye      |       14 |  No. 9 | ¾ L         |
| 12th   | Reverent       | —           |       18 | No. 15 | ¾ L         |
| 13th   | Cithara Rhythm | —           |        5 | No. 12 | 1½ L        |
| 14th   | Grass Wonder   | GohanXGAMER |        6 | No. 10 | 1¼ L        |
| 15th   | Silence Suzuka | Cruzi       |       11 | No. 11 | 1¼ L        |
| 16th   | Bravo Deux     | —           |       10 | No. 16 | Neck        |
| 17th   | Mejiro McQueen | Nadav       |       12 | No. 18 | Neck        |
| 18th   | Vodka          | Nadav       |        3 | No. 13 | 8 L         |

## Sus Cup 2
| Pos.   | Uma               | Trainer     | Race No. |   Fav. | Finish Stat |
| ------ | ----------------- | ----------- | -------: | -----: | ----------- |
| 1st | Daiwa Scarlet     | GohanXGAMER |        1 |  No. 4 | **1:30.9**  |
| 2nd | Sakura Bakushin O | agnes       |       15 |  No. 7 | 1 L         |
| 3rd | Mihono Bourbon    | Jinxye      |       16 |  No. 2 | 1 L         |
| 4th    | Silence Suzuka    | GohanXGAMER |       12 |  No. 6 | Head        |
| 5th    | Venabulum         | —           |        9 |  No. 9 | Neck        |
| 6th    | Jewel Onyx        | —           |        5 | No. 13 | Neck        |
| 7th    | Maruzensky        | Cruzi       |       10 |  No. 8 | Nose        |
| 8th    | Basal Shoot       | —           |        3 | No. 15 | Neck        |
| 9th    | Keyboard Rhythm   | —           |        2 | No. 10 | Nose        |
| 10th   | Hearty Letter     | —           |        4 | No. 11 | Nose        |
| 11th   | Mihono Bourbon    | Cruzi       |       18 |  No. 5 | Neck        |
| 12th   | Silence Suzuka    | Jinxye      |        8 | No. 14 | Neck        |
| 13th   | Krasnaya          | —           |        7 | No. 16 | ½ L         |
| 14th   | Silence Suzuka    | agnes       |        6 |  No. 3 | 1 L         |
| 15th   | Maruzensky        | Cyclobly    |       17 |  No. 1 | 1½ L        |
| 16th   | Mihono Bourbon    | Nadav       |       13 | No. 18 | 1½ L        |
| 17th   | Daiwa Scarlet     | Nadav       |       11 | No. 17 | 1½ L        |
| 18th   | Sakura Bakushin O | Cyclobly    |       14 | No. 12 | Nose        |

## Sus Cup 3
| Pos.   | Uma             | Trainer     | Race No. |   Fav. | Style | Finish Stat     |
| ------ | --------------- | ----------- | -------: | -----: | ----- | --------------- |
| 1st | Oguri Cap       | Yves        |       15 |  No. 3 | Pace  | **1:48.2**      |
| 2nd | Smart Falcon    | Yves        |        8 |  No. 2 | Front | 2½ L            |
| 3rd | Taiki Shuttle   | agnes       |       11 |  No. 5 | Pace  | 2½ L            |
| 4th    | El Condor Pasa  | Cruzi       |       12 |  No. 7 | Pace  | Neck            |
| 5th    | Haru Urara      | Cyclobly    |        9 |  No. 1 | Late  | 1½ L            |
| 6th    | El Condor Pasa  | agnes       |        2 |  No. 8 | Late  | ½ L             |
| 7th    | Haru Urara      | Cruzi       |        5 |  No. 6 | Late  | 1¼ L            |
| 8th    | Dunna           | —           |        4 | No. 13 | Pace  | 1¼ L            |
| 9th    | Gold Chouchou   | —           |        1 | No. 11 | End   | ¾ L             |
| 10th   | Oguri Cap       | Cyclobly    |        7 |  No. 4 | Pace  | ¾ L             |
| 11th   | Oguri Cap       | GohanXGAMER |       14 | No. 10 | Pace  | Neck            |
| 12th   | Haru Urara      | GohanXGAMER |        6 |  No. 9 | Late  | 1 L             |
| 13th   | Chalemie Rhythm | —           |        3 | No. 12 | Pace  | Neck            |
| 14th   | Haru Urara      | Nadav       |       16 | No. 15 | Late  | 5 L             |
| 15th   | Aqua Spring     | —           |       10 | No. 14 | Front | ¾ L             |
| 16th   | Vodka           | Nadav       |       13 | No. 16 | Pace  | Distance        |
| 17th   | —               | —           |        — |      — | —     | **Not visible** |
| 18th   | —               | —           |        — |      — | —     | **Not visible** |

## Sus Cup 4
| Pos.   | Uma              | Trainer     | Race No. |   Fav. | Style | Finish Stat |
| ------ | ---------------- | ----------- | -------: | -----: | ----- | ----------- |
| 1st | Nice Nature      | Yves        |        8 |  No. 4 | Pace  | **1:56.6**  |
| 2nd | Gold Ship        | Cyclobly    |       14 |  No. 1 | End   | 2½ L        |
| 3rd | El Condor Pasa   | Cruzi       |        4 |  No. 7 | Pace  | 1¾ L        |
| 4th    | Silence Suzuka   | agnes       |        6 |  No. 5 | Front | Head        |
| 5th    | Agnes Tachyon    | Yves        |        5 |  No. 6 | Late  | 5 L         |
| 6th    | Nice Nature      | agnes       |        9 |  No. 2 | Late  | 2 L         |
| 7th    | Bridge Comp      | —           |        7 | No. 15 | End   | 1½ L        |
| 8th    | Muruga           | —           |       11 | No. 10 | Pace  | 1 L         |
| 9th    | Mechanical Vapor | —           |       10 | No. 13 | Late  | Neck        |
| 10th   | Insight Catch    | —           |        3 | No. 12 | Front | ¾ L         |
| 11th   | Ribbon Carol     | —           |        1 | No. 11 | Pace  | ½ L         |
| 12th   | Symboli Rudolf   | Cyclobly    |       12 |  No. 3 | Late  | ½ L         |
| 13th   | Super Creek      | GohanXGAMER |        2 | No. 18 | Pace  | 1¼ L        |
| 14th   | Mayano Top Gun   | GohanXGAMER |       13 |  No. 8 | Front | Head        |
| 15th   | King Halo        | Cruzi       |       15 |  No. 9 | Late  | Nose        |
| 16th   | Navigate Light   | —           |       17 | No. 17 | Front | ¾ L         |
| 17th   | Mini Lotus       | —           |       18 | No. 16 | Front | 4 L         |
| 18th   | Summer Bonfire   | —           |       16 | No. 14 | End   | ¾ L         |

## Sus Cup 5
| Pos.   | Uma             | Trainer     | Race No. |   Fav. | Style | Finish Stat |
| ------ | --------------- | ----------- | -------: | -----: | ----- | ----------- |
| 1st | Super Creek     | agnes       |        5 |  No. 4 | Pace  | **3:15.6**  |
| 2nd | Tokai Teio      | Jinxye      |        1 |  No. 1 | Pace  | Distance    |
| 3rd | Mejiro McQueen  | Nadav       |       18 | No. 17 | Pace  | 7 L         |
| 4th    | Marsyas         | —           |       13 | No. 11 | Late  | 5 L         |
| 5th    | Black Tipped    | —           |       10 |  No. 8 | End   | ¾ L         |
| 6th    | Symboli Rudolf  | Cyclobly    |       11 | No. 15 | Pace  | 3 L         |
| 7th    | Biwa Hayahide   | GohanXGAMER |        4 |  No. 3 | Pace  | 1 L         |
| 8th    | Breeze Chopper  | —           |        3 | No. 12 | Front | Neck        |
| 9th    | Speechless Hack | —           |       17 |  No. 7 | Pace  | 3 L         |
| 10th   | T.M. Opera O    | Jinxye      |        2 |  No. 2 | Pace  | ½ L         |
| 11th   | Yggdra Valley   | —           |       12 | No. 10 | Late  | 1 L         |
| 12th   | Agnes Tachyon   | Cruzi       |        8 | No. 13 | Pace  | 3 L         |
| 13th   | Flute Rhythm    | —           |       14 |  No. 6 | Front | 2½ L        |
| 14th   | Tokai Teio      | Cyclobly    |        7 |  No. 5 | Pace  | Neck        |
| 15th   | Grass Wonder    | agnes       |       15 | No. 14 | Pace  | 1 L         |
| 16th   | Nice Nature     | GohanXGAMER |       16 | No. 16 | Late  | Head        |
| 17th   | Gold Ship       | Cruzi       |        9 |  No. 9 | End   | 8 L         |
| 18th   | Mihono Bourbon  | Nadav       |        6 | No. 18 | Front | ¾ L         |
"""

cup_data = {}
current_cup = None

for line in markdown_text.splitlines():
    line = line.strip()
    if line.startswith('## Sus Cup'):
        current_cup = int(line.split()[-1])
        cup_data[current_cup] = []
    elif line.startswith('|') and current_cup and 'Pos' not in line and '---' not in line:
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if len(parts) >= 6:
            # pos, uma, trainer, race_no, fav, style, finish_stat
            pos_str = parts[0].replace('st', '').replace('nd', '').replace('rd', '').replace('th', '').strip()
            if not pos_str.isdigit():
                continue
            pos = int(pos_str)
            uma = parts[1]
            trainer = parts[2] if parts[2] != '—' else 'NPC'
            number = int(parts[3]) if parts[3].isdigit() else None
            
            fav_str = parts[4].replace('No.', '').replace('Fav', '').strip()
            fav = int(fav_str) if fav_str.isdigit() else None
            
            # for 1 and 2, style is missing in the markdown table, finish stat is 5
            # for 3, 4, 5 style is 5, finish stat is 6
            if len(parts) == 6:
                style = None
                finish_stat = parts[5].replace('**', '')
            else:
                style = parts[5]
                finish_stat = parts[6].replace('**', '')
                
            time = finish_stat if ':' in finish_stat else None
            gap = finish_stat if ':' not in finish_stat else None
            
            cup_data[current_cup].append({
                'pos': pos,
                'uma': uma,
                'player': trainer,
                'number': number,
                'pop': fav,
                'time': time,
                'gap': gap,
                'style': style
            })

updates_made = 0
for race in data.get('races', []):
    cup_num = int(race.get('cupNumber')) if str(race.get('cupNumber')).isdigit() else None
    if cup_num in cup_data:
        # Check participants
        ref_parts = cup_data[cup_num]
        
        for p in race.get('participants', []):
            pos = p.get('pos')
            # find ref
            ref = next((r for r in ref_parts if r['pos'] == pos), None)
            if ref:
                # Cross-check and update
                if 'pop' not in p or p['pop'] != ref['pop']:
                    p['pop'] = ref['pop']
                    updates_made += 1
                if ref['time'] and p.get('time') != ref['time']:
                    p['time'] = ref['time']
                    updates_made += 1
                if ref['gap'] and p.get('gap') != ref['gap']:
                    # Special check: markdown has fraction chars like 1¾ L, JSON might have 1 3/4 L
                    # We will just use the markdown one as it's cleaner
                    p['gap'] = ref['gap']
                    updates_made += 1
                if 'number' not in p or p['number'] != ref['number']:
                    p['number'] = ref['number']
                    updates_made += 1
                
                # Check Uma name just in case (e.g. spelling changes)
                if ref['uma'] != '—' and p['uma'] != ref['uma']:
                    print(f"Mismatch in Uma for Cup {cup_num} Pos {pos}: JSON {p['uma']} vs Markdown {ref['uma']}")
                    # we keep JSON uma name if it's minor, but let's update if the user specifies
                    if p['uma'] != 'Not visible':
                        p['uma'] = ref['uma']
                        updates_made += 1
                
                # Trainer
                if ref['player'] != 'NPC' and p['player'] != ref['player']:
                    # Special check for Agnes/agnes
                    if ref['player'].lower() == p['player'].lower():
                        p['player'] = ref['player']
                        updates_made += 1
                    else:
                        print(f"Trainer mismatch Cup {cup_num} Pos {pos}: {p['player']} vs {ref['player']}")
                        p['player'] = ref['player']
                        updates_made += 1

                if ref['style'] and p.get('strategy') != ref['style']:
                    # Markdown uses 'Pace', 'Late', etc which match 'strategy'
                    p['strategy'] = ref['style']
                    updates_made += 1


if updates_made > 0:
    new_json = json.dumps(data, indent=4)
    # Ensure Unicode fractions are preserved without escaping if possible?
    # Actually json.dumps escapes non-ascii by default unless ensure_ascii=False
    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Successfully applied {updates_made} updates to INITIAL_DATA.")
else:
    print("No discrepancies found, or updates failed.")
