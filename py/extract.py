import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
match = re.search(r'showRaceDetail\(\w+\)\s*{.*?(?=^\s*\w+\(\)\s*{|renderPlayers\(\)\s*{)', html, re.MULTILINE | re.DOTALL)
if match:
    with open('showRaceDetail.js', 'w', encoding='utf-8') as f:
        f.write(match.group(0))
else:
    print("Not found")
