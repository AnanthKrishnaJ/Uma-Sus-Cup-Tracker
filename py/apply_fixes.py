import json
import re

with open('../.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const INITIAL_DATA = {')
if start == -1:
    print('INITIAL_DATA Not found')
    exit()

brace_count = 0
in_string = False
escape = False
end = -1
for i in range(start + 21, len(html)):
    char = html[i]
    if escape:
        escape = False
        continue
    if char == '\\':
        escape = True
        continue
    if char == '"':
        in_string = not in_string
    if not in_string:
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end = i + 1
                break

json_str = html[start+21:end]
data = json.loads(json_str)

# 1. Sus Cup 25: last uma is NPC, remove special week image
for race in data['races']:
    if race.get('id') == 25:
        parts = race.get('participants', [])
        if parts:
            last_p = parts[-1]
            if last_p.get('player') == 'NPC' or last_p.get('player') == '—':
                # Remove special week image (umaId)
                if 'umaId' in last_p:
                    del last_p['umaId']
                if 'characterUrl' in last_p:
                    del last_p['characterUrl']
                print("Fixed Cup 25 NPC")

# 2. Sus Cup 21 date: 03/02/2026
#    Sus Cup 26 date: 20 April 2026
for race in data['races']:
    if race.get('id') == 21:
        race['date'] = '2026-02-03' # Assuming YYYY-MM-DD
    if race.get('id') == 26:
        race['date'] = '2026-04-20'

# 3. Sus Cup 27 images (Mihono Bourbon ICING, Agnes Digital Fanatic Jiangshi, Air Groove Wedding, Taiki Shuttle Bubblegum, Nice Nature Run & Win, Gold Ship RUN! RUIN! LAUNCHER!)
# The IDs for Sus Cup 27 are 27.1 (Mile) and 27.2 (Medium)
for race in data['races']:
    if race.get('id') in [27.1, 27.2]:
        for p in race.get('participants', []):
            if p.get('uma') == 'Mihono Bourbon':
                p['umaId'] = '102602'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/102602-mihono-bourbon'
            elif p.get('uma') == 'Agnes Digital':
                p['umaId'] = '101902'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/101902-agnes-digital'
            elif p.get('uma') == 'Air Groove':
                p['umaId'] = '101802'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/101802-air-groove'
            elif p.get('uma') == 'Taiki Shuttle':
                p['umaId'] = '101002'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/101002-taiki-shuttle'
            elif p.get('uma') == 'Nice Nature':
                p['umaId'] = '106002'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/106002-nice-nature'
            elif p.get('uma') == 'Gold Ship':
                p['umaId'] = '100702'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/100702-gold-ship'

# Add specialWinners for Sus Cup 16 (Wait, what were the criteria? Let me just search if there's any info in the html or text)
# Actually, the user says "i previouly asled to add three winners from suscup 16 based on some cirite add them in middle of scrrenshots and race results for eveery suscup which had threee winners and nothing else"
# Wait, for Sus Cup 16, they provided criteria in a previous prompt?
# Let's write the modified data back first.

new_json_str = json.dumps(data, indent=4, ensure_ascii=False)
new_html = html[:start+21] + new_json_str + html[end:]
with open('../.vscode/suscup1.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("suscup1.html successfully updated with other fixes")
