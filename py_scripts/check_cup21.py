import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

for race in data.get('races', []):
    if str(race.get('cupNumber')) == '21':
        for p in race.get('participants', []):
            if 'Maruzensky' in p.get('uma', ''):
                print(f"Found Maruzensky: pos={p.get('pos')} no={p.get('number')} url={p.get('characterUrl')}")
            if 'Gold City' in p.get('uma', ''):
                print(f"Found Gold City: pos={p.get('pos')} no={p.get('number')} url={p.get('characterUrl')}")
