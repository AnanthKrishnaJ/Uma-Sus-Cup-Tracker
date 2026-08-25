import json
with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')

json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

for race in data['races']:
    print(race.get('cupName') or race.get('name'), race.get('id'), race.get('cupNumber'))
