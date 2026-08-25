import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

for r in data['races']:
    if str(r.get('cupNumber')) in ['1', '5']:
        for p in r['participants']:
            if 'McQueen' in p.get('uma', ''):
                p['umaId'] = 'mejiro-mcqueen-end-of-the-skies'
                
new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed McQueen in Cup 1 and Cup 5")
