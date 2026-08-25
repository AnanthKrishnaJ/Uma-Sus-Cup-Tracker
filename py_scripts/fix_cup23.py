import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

updated = 0

for race in data.get('races', []):
    if str(race.get('cupNumber')) == 'SUS CUP 23' or str(race.get('cupNumber')) == '23':
        for p in race.get('participants', []):
            if 'Oguri Cap' in p.get('uma', '') and str(p.get('pos')) == '13':
                p['umaId'] = '100602'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/100602-oguri-cap'
                updated += 1
            if 'Bourbon' in p.get('uma', ''):
                p['umaId'] = '102602'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/102602-mihono-bourbon'
                updated += 1

if updated > 0:
    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
print(f'Updated {updated} records in Sus Cup 23')
