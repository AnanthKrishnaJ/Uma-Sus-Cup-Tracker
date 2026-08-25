import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data = json.loads(text[start + 21:end].strip().rstrip(';'))

markdown_input = """
## 🏆 Sus Cup 11
| 🥇 1st | Narita Taishin   | Cyclobly    |        1 |  No. 2 | End   | **2:21.4**   |
| 🥈 2nd | Symboli Rudolf   | Cyclobly    |       11 |  No. 1 | Pace  | **1 1/4 L**  |
| 🥉 3rd | El Condor Pasa   | agnes       |        4 |  No. 3 | Late  | **2 L**      |
| 4th    | Grass Wonder     | agnes       |       17 |  No. 4 | Late  | **1 L**      |
| 5th    | Tokai Teio       | Jinxye      |        8 |  No. 9 | Pace  | **1 1/4 L**  |
| 6th    | Oguri Cap        | GohanXGAMER |       13 |  No. 5 | Pace  | **1/2 L**    |
| 7th    | Agnes Tachyon    | Cruzi       |       14 |  No. 7 | Pace  | **4 L**      |
| 8th    | Super Creek      | GohanXGAMER |        5 | No. 11 | Pace  | **3 L**      |
| 9th    | Mejiro McQueen   | Ananth      |       16 | No. 10 | Pace  | **3/4 L**    |
| 10th   | T.M. Opera O     | Jinxye      |       12 |  No. 6 | Pace  | **1 1/4 L**  |
| 11th   | Encore One More  | —           |        9 | No. 16 | Pace  | **1 3/4 L**  |
| 12th   | Seiun Sky        | Cruzi       |       15 |  No. 8 | Front | **1 L**      |
| 13th   | Sidecar          | —           |       10 | No. 14 | Late  | **1/2 L**    |
| 14th   | Chalemie Rhythm  | —           |        6 | No. 13 | End   | **Head**     |
| 15th   | Mechanical Vapor | —           |       18 | No. 12 | Front | **1 L**      |
| 16th   | Aeneas           | —           |        7 | No. 17 | Late  | **2 L**      |
| 17th   | Leaf Leaf        | —           |        3 | No. 15 | Pace  | **1/2 L**    |
| 18th   | Curren Chan      | Ananth      |        2 | No. 18 | Front | **Distance** |

## 🏆 Sus Cup 12
| 🥇 1st | Narita Taishin | Cyclobly    |        1 |  No. 1 | End   | **1:56.1**   |
| 🥈 2nd | Hishi Amazon   | Jinxye      |        8 |  No. 6 | End   | **1 3/4 L**  |
| 🥉 3rd | Gold Ship      | Cruzi       |        7 |  No. 7 | End   | **3/4 L**    |
| 4th    | Silence Suzuka | agnes       |        2 |  No. 5 | Front | **Nose**     |
| 5th    | Gold Ship      | GohanXGAMER |       11 | No. 10 | End   | **2 L**      |
| 6th    | Silence Suzuka | GohanXGAMER |       16 | No. 11 | Front | **3/4 L**    |
| 7th    | Seiun Sky      | Cruzi       |        5 |  No. 4 | Front | **3/4 L**    |
| 8th    | Bella Prateria | —           |        6 | No. 12 | Pace  | **1 3/4 L**  |
| 9th    | Mayano Top Gun | Ananth      |        4 |  No. 8 | Front | **1 1/2 L**  |
| 10th   | Arcade Champ   | —           |       12 | No. 15 | End   | **1/2 L**    |
| 11th   | Gold Ship      | agnes       |       17 |  No. 3 | End   | **Nose**     |
| 12th   | Oishii Parfait | —           |       10 | No. 13 | Front | **Head**     |
| 13th   | Ogress         | —           |        9 | No. 14 | Front | **3/4 L**    |
| 14th   | Silence Suzuka | Jinxye      |       18 |  No. 9 | Front | **Nose**     |
| 15th   | Ribbon Etude   | —           |       15 | No. 16 | End   | **3/4 L**    |
| 16th   | Mihono Bourbon | Cyclobly    |       14 |  No. 2 | Front | **1 3/4 L**  |
| 17th   | Gray Chouchou  | —           |       13 | No. 17 | Late  | **3/4 L**    |
| 18th   | Oguri Cap      | Ananth      |        3 | No. 18 | Late  | **Distance** |

## 🏆 Sus Cup 13
| 🥇 1st   | Gold Ship      | Cruzi       |        6 | No. 6 | End   | **2:28.9**    |
| 🥈 2nd   | Grass Wonder   | agnes       |        9 | No. 2 | Late  | **1 1/2 L**   |
| 🥉 3rd   | Agnes Tachyon  | Cruzi       |       15 | No. 4 | Pace  | **1 1/4 L**   |
| 4th      | Mejiro McQueen | GohanXGAMER |        4 | No. 7 | Pace  | **3 L**       |
| 5th      | Agnes Tachyon  | Yves        |       11 | No. 3 | Late  | **3/4 L**     |

## 🏆 Sus Cup 14
| 🥇 1st | Special Week     | GohanXGAMER |       15 | No. 11 | Pace  | **2:09.4**  |
| 🥈 2nd | Oguri Cap        | GohanXGAMER |       11 |  No. 7 | Pace  | **2 1/2 L** |
| 🥉 3rd | Oguri Cap        | Yves        |       13 |  No. 8 | Pace  | **1 L**     |
| 4th    | Mejiro McQueen   | Yves        |       12 |  No. 4 | Front | **1 L**     |
| 5th    | Mejiro McQueen   | GohanXGAMER |        6 |  No. 2 | Pace  | **4 L**     |
| 6th    | Oguri Cap        | Ananth      |       17 |  No. 6 | Late  | **1 1/4 L** |
| 7th    | T.M. Opera O     | agnes       |       16 |  No. 5 | Pace  | **1 1/2 L** |
| 8th    | Tap Step         | —           |        4 |  No. 9 | Pace  | **3/4 L**   |
| 9th    | Ribbon Scherzo   | —           |       10 | No. 15 | Late  | **2 1/2 L** |
| 10th   | Ney Rhythm       | —           |        9 | No. 13 | End   | **Neck**    |
| 11th   | King Halo        | agnes       |        1 |  No. 3 | Late  | **Head**    |
| 12th   | Zamburak         | —           |        3 | No. 10 | Late  | **Nose**    |
| 13th   | Short Sleeper    | —           |        7 | No. 16 | Pace  | **Nose**    |
| 14th   | Belongings       | —           |        2 | No. 17 | End   | **1 1/4 L** |
| 15th   | Ribbon Rondo     | —           |        8 | No. 12 | Pace  | **2 L**     |
| 16th   | Grass Wonder     | Ananth      |       14 |  No. 1 | Late  | **1 3/4 L** |
| 17th   | Nice Nature      | Yves        |        5 | No. 14 | Late  | **Neck**    |
| 18th   | Mechanical Vapor | —           |       18 | No. 18 | Front | **6 L**     |

## 🏆 Sus Cup 15
| 🥇 1st | Silence Suzuka    | agnes    |        9 |  No. 6 | Front | **2:11.1**  |
| 🥈 2nd | Maruzensky        | Cyclobly |       10 |  No. 3 | Front | **2 L**     |
| 🥉 3rd | Daiwa Scarlet     | agnes    |       11 |  No. 1 | Front | **3/4 L**   |
| 4th    | Daiwa Scarlet     | Cyclobly |       15 |  No. 2 | Front | **1 3/4 L** |
| 5th    | Mayano Top Gun    | Ananth   |       14 |  No. 7 | Front | **2 1/2 L** |
| 6th    | Mayano Top Gun    | agnes    |        3 |  No. 4 | Front | **1 L**     |
| 7th    | Ribbon Lullaby    | —        |        5 | No. 13 | Late  | **7 L**     |
| 8th    | Chalemie Rhythm   | —        |        6 | No. 12 | Pace  | **1 L**     |
| 9th    | Shout My Name     | —        |       16 | No. 17 | End   | **1/2 L**   |
| 10th   | Weiss Grimoire    | —        |       17 |  No. 9 | Front | **1 1/2 L** |
| 11th   | Mihono Bourbon    | Cyclobly |        8 |  No. 5 | Front | **1/2 L**   |
| 12th   | Cymbal Rhythm     | —        |        1 | No. 11 | Pace  | **Neck**    |
| 13th   | Salsa Step        | —        |        2 | No. 15 | Late  | **Neck**    |
| 14th   | Thousand Voltaire | —        |       13 |  No. 8 | Pace  | **Neck**    |
| 15th   | Spring Happy      | —        |        4 | No. 16 | Late  | **1/2 L**   |
| 16th   | Faster than Ray   | —        |       12 | No. 14 | End   | **Nose**    |
| 17th   | Izcalli           | —        |        7 | No. 18 | Front | **Head**    |
| 18th   | Smart Falcon      | Ananth   |       18 | No. 10 | Front | **1/2 L**   |
"""

cup_updates = {}
current_cup = None

for line in markdown_input.strip().split('\n'):
    if line.startswith('## 🏆 Sus Cup '):
        current_cup = line.replace('## 🏆 Sus Cup ', '').strip()
        cup_updates[current_cup] = {}
    elif line.startswith('|') and 'Pos.' not in line and '---' not in line:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) > 5 and 'Not Shown' not in parts[1]:
            pos_str = parts[1].strip()
            if '1st' in pos_str: pos = 1
            elif '2nd' in pos_str: pos = 2
            elif '3rd' in pos_str: pos = 3
            else:
                m = re.search(r'\d+', pos_str)
                if m: pos = int(m.group())
                else: continue
            
            uma = parts[2]
            player = parts[3]
            if player == '—': player = 'NPC'
            if player == 'Jinxye': player = 'Jiinxye'
            if player == 'Cyclobly': player = 'Cyciesta'
            if player == 'agnes': player = 'Agnes'
            
            number = int(parts[4])
            pop = int(re.search(r'\d+', parts[5]).group())
            style = parts[6]
            gap = parts[7].replace('**', '')
            
            cup_updates[current_cup][pos] = {
                'gap': gap,
                'pop': pop,
                'number': number,
                'strategy': style,
                'uma': uma,
                'player': player
            }

for r in data['races']:
    cn = str(r.get('cupNumber'))
    # Extract just the number from e.g. "SUS CUP 11 - GP Round 3/3"
    m = re.search(r'SUS CUP (\d+)', cn)
    if not m:
        continue
    cup_num = m.group(1)
    
    if cup_num in cup_updates:
        updates = cup_updates[cup_num]
        
        # In Cup 13, some participants were not shown. So we only update the ones we have in updates.
        for p in r['participants']:
            pos = p.get('pos')
            if pos in updates:
                upd = updates[pos]
                
                # Check if it's the winner
                if pos == 1:
                    p['time'] = upd['gap'] # 1st place gets time instead of gap
                
                p['gap'] = upd['gap']
                p['pop'] = upd['pop']
                p['number'] = upd['number']
                p['strategy'] = upd['strategy']
                p['player'] = upd['player']

                # Also Tokai Teio should be 'tokai-teio-beyond' globally based on earlier user requests, let's enforce that
                if 'Tokai Teio' in p.get('uma', ''):
                    p['umaId'] = 'tokai-teio-beyond'

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Cups 11-15 with Markdown table data.")
