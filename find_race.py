import json
text = open('index.html', encoding='utf-8').read()
data = json.loads(text[text.find('const INITIAL_DATA = {')+21:text.find('};', text.find('const INITIAL_DATA = {'))+1])
for r in data.get('races', []):
    umas = [p.get('uma') for p in r.get('participants', [])]
    if 'Symboli Rudolf' in umas and 'Biwa Hayahide' in umas and 'Super Creek' in umas:
        print(f"Found race with these umas! Cup: {r.get('cupNumber')} | Name: {r.get('name')}")
