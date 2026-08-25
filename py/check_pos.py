import json
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()
start = html.find('const INITIAL_DATA = ') + 21
end = html.find('};\n', start) + 1
data = json.loads(html[start:end])
for r in data['races']:
    if str(r['id']) == '27.2':
        print(json.dumps(r, indent=2))
