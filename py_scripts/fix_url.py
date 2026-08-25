import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data = json.loads(text[start + 21:end].strip().rstrip(';'))

db_start = end
db_end = text.find('const SKILLS_DATABASE =')
db_str = text[db_start + 20:db_end].strip().rstrip(';')

# Basic regex parser for UMA_DATABASE since it is not standard JSON
db_dict = {}
for m in re.finditer(r'([\'"a-zA-Z0-9_-]+):\s*\{([^}]+)\}', db_str):
    key = m.group(1).strip("'\"")
    content = m.group(2)
    # find characterUrl
    url_m = re.search(r'characterUrl:\s*([\'"])(.*?)\1', content)
    if url_m:
        db_dict[key] = url_m.group(2)
    elif 'url:' in content:
        url_m = re.search(r'url:\s*([\'"])(.*?)\1', content)
        if url_m:
            db_dict[key] = url_m.group(2)

for r in data['races']:
    if str(r.get('cupNumber')) == 'SUS CUP 6':
        for p in r['participants']:
            uma_id = p.get('umaId')
            if uma_id in db_dict:
                p['characterUrl'] = db_dict[uma_id]

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed characterUrl for Cup 6 participants.")
