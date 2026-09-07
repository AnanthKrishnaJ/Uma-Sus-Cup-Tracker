import json

with open('index_modified.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = 'const INITIAL_DATA ='
start = html.find(start_marker) + len(start_marker)
while html[start] != '{': start += 1

end = html.rfind('};') + 1
# wait, actually the end of INITIAL_DATA can be found properly using the stack approach.
# let's just use the stack approach from earlier
stack = []
end = -1
for i in range(start, len(html)):
    if html[i] == '{': stack.append('{')
    elif html[i] == '}':
        stack.pop()
        if not stack:
            end = i + 1
            break

json_str = html[start:end]
import re
json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)
data = json.loads(json_str)

for r in data['races']:
    cupNum = r.get('cupNumber', -1)
    if not cupNum and 'cupName' in r and 'Sus Cup' in r['cupName']:
        try: cupNum = int(r['cupName'].replace('Sus Cup', '').strip().split()[0])
        except: pass
    
    if cupNum in [17, 18, 19, 20]:
        print(f'\n--- Cup {cupNum} ---')
        for p in sorted(r['participants'], key=lambda x: x.get('pos', x.get('position', 99)))[:3]:
            print(f"{p.get('pos')}: {p.get('uma')} ({p.get('player')})")
        if 'scenarioWinners' in r:
            print("scenarioWinners:", r['scenarioWinners'])
