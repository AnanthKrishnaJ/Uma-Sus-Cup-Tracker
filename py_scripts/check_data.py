import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

for p in data['races'][0]['participants']:
    print(f"Pos: {p.get('pos')} - Gap: {p.get('gap')} - Time: {p.get('time')} - Num: {p.get('number')} - Pop: {p.get('pop')}")
