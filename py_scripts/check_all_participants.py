import json
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data = json.loads(text[start + 21:end].strip().rstrip(';'))

print('Cup 18:')
for r in data['races']:
    if str(r.get('cupNumber')) == '18':
        for p in r['participants']:
            print(f"  Pos: {p.get('pos')}, Number: {p.get('number')}, Name: {p['uma']}, ID: {p.get('umaId')}")

print('Cup 19:')
for r in data['races']:
    if str(r.get('cupNumber')) == '19':
        for p in r['participants']:
            print(f"  Pos: {p.get('pos')}, Number: {p.get('number')}, Name: {p['uma']}, ID: {p.get('umaId')}")
