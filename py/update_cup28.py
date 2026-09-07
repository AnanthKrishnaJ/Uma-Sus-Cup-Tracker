import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('"races": [')
end = text.find('const UMA_DATABASE', start)
j = '{' + text[start:end-1].strip()[:-1] + '}'
d = json.loads(j)

for r in d['races']:
    if r.get('cupNumber') == 28:
        for p in r['participants']:
            uma = p.get('uma')
            if uma == 'Seiun Sky':
                p['umaId'] = 'seiun-sky'
                p['version'] = 'Standard / Original'
            elif uma == 'Meisho Doto':
                p['umaId'] = '105802-meisho-doto'
                p['version'] = "Dot-o'-Lantern"
            elif uma == 'Maruzensky':
                p['umaId'] = 'maruzensky'
                p['version'] = 'Standard / Original'
            elif uma == 'Special Week':
                p['umaId'] = 'special-week'
                p['version'] = 'Standard / Original'
            elif uma == 'Fuji Kiseki':
                p['umaId'] = '100502-fuji-kiseki'
                p['version'] = 'Succès Étoilé'

new_races_json = json.dumps(d['races'], indent=4)
# JSON dumps uses 4 spaces. Let's try to format it to match exactly or just replace it.
# The original file has 2 spaces indent.
new_races_json = json.dumps(d['races'], indent=2)
# We need to add the 4 spaces offset that the original races array has
lines = new_races_json.split('\n')
indented_lines = [lines[0]] + ['    ' + line for line in lines[1:]]
final_races_json = '\n'.join(indented_lines)

# Replace the races array
new_text = text[:start] + '"races": ' + final_races_json + ',\n  ' + text[end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated Cup 28")
