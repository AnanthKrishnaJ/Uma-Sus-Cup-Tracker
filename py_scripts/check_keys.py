import json
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const NPC_PROFILES = {};')
if start == -1 or end == -1:
    print("Could not find INITIAL_DATA bounds")
else:
    data_str = text[start + 21:end].strip().rstrip(';')
    data = json.loads(data_str)
    
    print("Winner keys:")
    print(list(data['winners'][-1].keys()))
    
    print("\nRace keys:")
    print(list(data['races'][-1].keys()))
    
    print("\nParticipant keys:")
    print(list(data['races'][-1]['participants'][0].keys()))
    print(data['races'][-1]['participants'][0])
