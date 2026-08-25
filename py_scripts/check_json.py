import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = {')
end = text.find('const UMA_DATABASE = {')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

for r in data['races']:
    print(f"Cup {r.get('id')}: {len(r.get('participants', []))} participants")
