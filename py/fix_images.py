import json
import os

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

# The image folder is suscupimages11-20
# I will check which files exist and build the images array for each race from 11 to 19
folder = 'suscupimages11-20'
for race in data['races']:
    rid = race.get('id')
    if rid and 11 <= rid <= 20:
        race['images'] = []
        for i in range(1, 5):
            filename = f"{rid}.{i}.png"
            if os.path.exists(os.path.join(folder, filename)):
                race['images'].append(f"{folder}/{filename}")

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Images paths fixed!")
