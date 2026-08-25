import json
import re

content = open('../.vscode/suscup1.html', encoding='utf-8').read()
start = content.find('const INITIAL_DATA = ') + 21
end = content.find('};', start) + 1
db = json.loads(content[start:end])

for r in db['races'][-5:]:
    print(f"--- {r['cupNumber']} ---")
    print(f"URL: {r.get('url')}")
    if r['participants']:
        print(f"First participant: {r['participants'][0]['uma']}")
    else:
        print("No participants.")
