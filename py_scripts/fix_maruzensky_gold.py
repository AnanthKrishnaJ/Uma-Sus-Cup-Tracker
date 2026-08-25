import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

updated_maru = False
updated_gold = 0

for race in data.get('races', []):
    if race.get('cupNumber') == 'SUS CUP 21':
        for p in race.get('participants', []):
            if 'Maruzensky' in p.get('uma', '') and str(p.get('pos')) == '8':
                p['umaId'] = '100402'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/100402-maruzensky'
                updated_maru = True
    
    for p in race.get('participants', []):
        if 'Gold City' in p.get('uma', '') and not p.get('characterUrl'):
            p['umaId'] = '104001'
            p['characterUrl'] = 'https://gametora.com/umamusume/characters/104001-gold-city'
            updated_gold += 1

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'Updated Maruzensky pos 8: {updated_maru}')
print(f'Updated {updated_gold} missing Gold City images')
