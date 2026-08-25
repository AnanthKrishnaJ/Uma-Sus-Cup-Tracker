import json
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = {')
end = text.find('};', start) + 1
data_str = text[start+21:end]

try:
    data = json.loads(data_str)
    for r in data['races']:
        if r['cupNumber'] in [16, 17, 18, 19, 20]:
            print(f"Cup {r['cupNumber']}: {len(r.get('participants', []))} participants")
except Exception as e:
    print('Error:', e)
