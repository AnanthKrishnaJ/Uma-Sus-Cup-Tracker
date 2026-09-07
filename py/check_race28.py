import json

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('"races": [')
end = text.find('const UMA_DATABASE', start)
j = '{' + text[start:end-1].strip()[:-1] + '}'
d = json.loads(j)

for race in d['races']:
    if race.get('cupNumber') == 28:
        for p in race['participants']:
            print(f"{p['uma']} - current ID: {p.get('umaId')}")
