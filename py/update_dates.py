import json

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')
json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

for race in data['races']:
    if race['id'] == 14:
        race['date'] = "02 November 2025, 18:00" # approximate time or just "02 November 2025"
    elif race['id'] == 15:
        race['date'] = "06 November 2025, 18:00"

new_json = json.dumps(data, indent=4)
content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Dates updated successfully!")
