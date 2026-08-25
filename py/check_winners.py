import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const INITIAL_DATA = ') + 21
end = html.find('};\n', start) + 1
data = json.loads(html[start:end])
for r in data['races']:
    winners = [p for p in r.get('participants', []) if p.get('position') == 1 or p.get('position') == '1']
    if len(winners) > 1:
        print(f"Cup {r.get('id')} has {len(winners)} winners.")
