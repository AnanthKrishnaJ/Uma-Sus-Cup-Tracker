import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update INITIAL_DATA
start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data_str = text[start + 21:end].strip().rstrip(';')

data = json.loads(data_str)

for r in data['races']:
    if '18' in str(r.get('cupNumber')):
        for p in r['participants']:
            if p.get('uma') == 'Symboli Rudolf' and p.get('pos') == 17:
                p['umaId'] = 'symboli-rudolf'
    
    if '19' in str(r.get('cupNumber')):
        for p in r['participants']:
            if p.get('uma') == 'Gold City':
                p['umaId'] = '104002'

new_data_str = json.dumps(data, indent=4)
text = text[:start + 21] + new_data_str + ';\n\n    ' + text[end:]

# 2. Update UMA_DATABASE
db_start = text.find('const UMA_DATABASE = {')
db_end = text.find('};', db_start)
db_str = text[db_start + 21:db_end + 1]

if '"104002"' not in db_str:
    # insert before the closing brace
    insertion = ',\n        "104002": "https://gametora.com/umamusume/characters/104002-gold-city"'
    text = text[:db_end] + insertion + text[db_end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated Uma portraits successfully!')
