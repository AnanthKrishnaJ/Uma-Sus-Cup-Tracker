import json
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data = json.loads(text[start + 21:end].strip().rstrip(';'))

print('Cup 20:')
for r in data['races']:
    if '20' in str(r.get('cupNumber')):
        for p in r['participants']:
            if 'Gold City' in p['uma'] or 'Mayano Top Gun' in p['uma']:
                print(f"  Pos: {p.get('pos')}, Number: {p.get('number')}, Name: {p['uma']}, ID: {p.get('umaId')}")
