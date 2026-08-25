import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const INITIAL_DATA = ') + 21
end = html.find('};\n', start) + 1
data = json.loads(html[start:end])

db = data.get('UMA_DATABASE', {})

for uid, info in db.items():
    if 'image' in info and 'suscupimages' in info['image']:
        # It's currently pointing to local file that failed to download.
        # Restore it.
        # Wait, not all suscupimages are bad. Only the ones we broke!
        if uid in ['100702', '104002', '102602', '101902', '101002', '106002', '101802']:
            info['image'] = f"https://gametora.com/images/umamusume/characters/chara_stand_{uid[:4]}_{uid}.png"

new_json = json.dumps(data, indent=4)
new_html = html[:start] + new_json + html[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Restored Gametora URLs for broken umas")
