import json

text = open('index.html', encoding='utf-8').read()
data = json.loads(text[text.find('const INITIAL_DATA = {')+21:text.find('};', text.find('const INITIAL_DATA = {'))+1])
for r in data.get('races', []):
    if r.get('cupNumber') == 26:
        for p in r.get('participants', []):
            print(f"{p.get('uma')} | Pos: {p.get('position')} | number: {p.get('number')} | pop: {p.get('pop')}")
