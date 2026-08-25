import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data = json.loads(text[start + 21:end].strip().rstrip(';'))

for r in data['races']:
    if '16' in str(r.get('cupNumber')):
        print(f"Race: {r['name']}, Date: {r['date']}")
        for p in r['participants']:
            if p['pos'] in [1, 3, 4]:
                print(p)
