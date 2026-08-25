import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

updates = 0
for race in data['races']:
    for p in race['participants']:
        player = p.get('player', '')
        if player == 'Jinxye':
            p['player'] = 'Jiinxye'
            updates += 1
        elif player == 'Cyclobly':
            p['player'] = 'Cyciesta'
            updates += 1
        elif player == 'agnes':
            p['player'] = 'Agnes'
            updates += 1

if updates > 0:
    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Normalized {updates} player names.")
else:
    print("No updates needed.")
