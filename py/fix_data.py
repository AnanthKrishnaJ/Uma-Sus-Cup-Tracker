import json
import re

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove trailing junk after </html>
end_idx = content.find('</html>')
if end_idx != -1:
    content = content[:end_idx + 7] + '\n'

# 2. Extract INITIAL_DATA
start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')

json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

# Add cupName
for race in data['races']:
    if race.get('id') == 11:
        race['cupName'] = "Sus Cup 11"
    elif race.get('id') == 6:
        race['cupName'] = "Sus Cup 6"

# Inject it back
new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated INITIAL_DATA and removed trailing junk.")
