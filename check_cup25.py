import json
text = open('index.html', encoding='utf-8').read()
data = json.loads(text[text.find('const INITIAL_DATA = {')+21:text.find('};', text.find('const INITIAL_DATA = {'))+1])
for r in data.get('races', []):
    if r.get('cupNumber') == 25:
        print('Cup 25:')
        for p in sorted(r.get('participants', []), key=lambda x: x.get('pos', x.get('position', 99))):
            print(f"{p.get('pos', p.get('position', 99))} | {p.get('uma')} | number: {p.get('number')} | pop: {p.get('pop')}")
