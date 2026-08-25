import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data = json.loads(text[start + 21:end].strip().rstrip(';'))

for r in data['races']:
    for p in r['participants']:
        if 'Tokai Teio' in p.get('uma', ''):
            p['umaId'] = 'tokai-teio-beyond'

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Tokai Teio everywhere.")
