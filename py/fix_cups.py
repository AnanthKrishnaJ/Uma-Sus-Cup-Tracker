import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const INITIAL_DATA = ') + 21
end = html.find('};\n', start) + 1
data = json.loads(html[start:end])

# Fix Dates
for r in data['races']:
    if str(r.get('id')) == '21':
        r['date'] = '03/02/2026'
    if str(r.get('id')) == '26':
        r['date'] = '20 April 2026'

# Fix pos -> position and UMA IDs
for r in data['races']:
    if isinstance(r.get('id'), (int, float, str)):
        if str(r.get('id')).startswith('21') or str(r.get('id')).startswith('22') or str(r.get('id')).startswith('23') or str(r.get('id')).startswith('24') or str(r.get('id')).startswith('25') or str(r.get('id')).startswith('26') or str(r.get('id')).startswith('27'):
            if 'participants' in r:
                for p in r['participants']:
                    if 'pos' in p:
                        p['position'] = p.pop('pos')
                    
                    # Fix position format if it's string like '1st', '2nd'
                    if isinstance(p.get('position'), str):
                        pos_str = p['position']
                        num = ''.join(filter(str.isdigit, pos_str))
                        if num:
                            p['position'] = int(num)
                    
                    # Fix specific umas
                    if p.get('uma') == 'Air Groove':
                        p['umaId'] = '101802'
                    if p.get('uma') == 'Gold Ship':
                        p['umaId'] = '100702'
                    if p.get('uma') == 'Gold City':
                        p['umaId'] = '104002'
                    if p.get('uma') == 'Mihono Bourbon':
                        p['umaId'] = '102602'
                    if p.get('uma') == 'Agnes Digital':
                        p['umaId'] = '101902'
                    if p.get('uma') == 'Taiki Shuttle':
                        p['umaId'] = '101002'
                    if p.get('uma') == 'Nice Nature':
                        p['umaId'] = '106002'

                    if p.get('umaId') in ('None', None, ''):
                        # try to fallback
                        uma = p.get('uma', '')
                        if uma == 'Silence Suzuka': p['umaId'] = '100201'
                        if uma == 'Narita Brian': p['umaId'] = '101601'
                        # ...

# Remove Special Week image from NPC in Cup 25
for r in data['races']:
    if str(r.get('id')) == '25':
        if 'participants' in r:
            for p in r['participants']:
                if p.get('player') == 'NPC':
                    if 'umaId' in p:
                        p.pop('umaId')
                    p['umaId'] = None

new_json = json.dumps(data, indent=4)
new_html = html[:start] + new_json + html[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated INITIAL_DATA in suscup1.html")
