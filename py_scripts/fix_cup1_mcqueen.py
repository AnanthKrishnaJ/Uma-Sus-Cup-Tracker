import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

for r in data['races']:
    if str(r.get('cupNumber')) == '1':
        for p in r.get('participants', []):
            if 'Mejiro McQueen' in p.get('uma', ''):
                p['umaId'] = '101302'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/101302-mejiro-mcqueen'

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated Cup 1 Mejiro McQueen')
