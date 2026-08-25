import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
db_start = text.find('const UMA_DATABASE = ')
end = text.rfind('};', start, db_start)

data_str = text[start + 21:end + 1]
data = json.loads(data_str)

db_end = text.rfind('};', db_start)
db_str = text[db_start + 21:db_end + 1]

# Poor man's JSON parser for UMA_DATABASE since it's a JS object without quotes on keys sometimes
import re
uma_db = {}
for match in re.finditer(r"'?([a-zA-Z0-9_-]+)'?:\s*{\s*name:\s*['\"](.*?)['\"]", db_str):
    uma_id = match.group(1)
    uma_name = match.group(2)
    # default versions are usually lowercase id
    if uma_id.islower() and '-' in uma_id or uma_id.isalpha():
        if uma_name not in uma_db:
            uma_db[uma_name] = uma_id

print(uma_db)

for race in data['races']:
    for p in race['participants']:
        if 'umaId' not in p or p['umaId'] == 'MISSING' or p['umaId'] == '':
            if p['uma'] in uma_db:
                p['umaId'] = uma_db[p['uma']]
                print(f"Fixed {p['uma']} -> {p['umaId']}")
            else:
                # auto slug
                slug = p['uma'].lower().replace(' ', '-')
                p['umaId'] = slug
                print(f"Auto-slugged {p['uma']} -> {slug}")

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_text = text[:start + 21] + new_json + text[end + 1:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Done fixing missing umaIds.")
