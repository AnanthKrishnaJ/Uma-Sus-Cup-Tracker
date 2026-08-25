import json
import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const INITIAL_DATA = ') + 21
end = content.find('};', start) + 1
db = json.loads(content[start:end])

urls_to_add = {
    'SUS CUP 24': 'https://discord.com/channels/885095339885989942/1389671658905800797/1490350135895523409',
    'SUS CUP 25': 'https://discord.com/channels/885095339885989942/1389671658905800797/1492919399370461327',
    'SUS CUP 26': 'https://discord.com/channels/885095339885989942/1389671658905800797/1531310675006197861',
    'SUS CUP 27 (MILE)': 'https://discord.com/channels/885095339885989942/1389671658905800797/1540696698857197599',
    'SUS CUP 27 (MEDIUM)': 'https://discord.com/channels/885095339885989942/1389671658905800797/1540696698857197599'
}

for r in db['races']:
    if r['cupNumber'] == 'SUS CUP 27':
        if r.get('distanceType') == 'Mile':
            r['url'] = urls_to_add['SUS CUP 27 (MILE)']
        else:
            r['url'] = urls_to_add['SUS CUP 27 (MEDIUM)']
    elif r['cupNumber'] in urls_to_add:
        r['url'] = urls_to_add[r['cupNumber']]

new_db_str = json.dumps(db, indent=2, ensure_ascii=False)
new_content = content[:start] + new_db_str + content[end:]
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added Discord URLs to races.")
