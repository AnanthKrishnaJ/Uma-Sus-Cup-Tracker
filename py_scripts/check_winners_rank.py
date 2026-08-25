import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\initial_data.json', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
data_str = text[start + 21:text.find('const UMA_DATABASE =')].strip().rstrip(';')
data = json.loads(data_str)

for w in data.get('winners', []):
    if w.get('cup') in ('Sus Cup 16', 'Sus Cup 17', 'Sus Cup 18', 'Sus Cup 19', 'Sus Cup 20'):
        print(f"{w.get('trainer')} in {w.get('cup')}: rankLabel={w.get('rankLabel')} uma={w.get('uma')}")
