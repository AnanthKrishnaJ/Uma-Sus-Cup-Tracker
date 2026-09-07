import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

data_match = re.search(r'const INITIAL_DATA = (\{.*?\});\n', content, re.DOTALL)
if data_match:
    data_json = data_match.group(1)
    print('Found INITIAL_DATA block')
    winners_match = re.search(r'\"winners\":\s*(\[\s*\{.*?\}\s*\])\s*,\s*\"races\"', data_json, re.DOTALL)
    if winners_match:
        winners = json.loads(winners_match.group(1))
        print('Number of winners:', len(winners))
        print('Sample winner:', winners[-1])
        print('Sample winner keys:', list(winners[-1].keys()))
    else:
        print('winners array not found')
        
    races_match = re.search(r'\"races\":\s*(\[\s*\{.*?\}\s*\])\s*\}', data_json, re.DOTALL)
    if races_match:
        races = json.loads(races_match.group(1))
        print('Number of races:', len(races))
        print('Sample race keys:', list(races[-1].keys()))
        print('Sample participant keys:', list(races[-1]['participants'][0].keys()))
        print('Sample participant:', races[-1]['participants'][0])
    else:
        print('races array not found')
else:
    print('const INITIAL_DATA not found')
