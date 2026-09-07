import json

with open('index.html', encoding='utf-8') as f:
    text = f.read()

start = text.find('"races": [')
end = text.find('const UMA_DATABASE', start)
j = '{' + text[start:end-1].strip()[:-1] + '}'
d = json.loads(j)

for r in d['races']:
    if r.get('cupNumber') == 16:
        print(json.dumps(r, indent=2))
        break
