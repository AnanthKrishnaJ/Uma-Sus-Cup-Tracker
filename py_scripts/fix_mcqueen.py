import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

updates = 0
for race in data.get('races', []):
    cup_num = race.get('cupNumber')
    # Use string comparison since it might be a string in JSON
    if str(cup_num) in ['1', '5']:
        for p in race.get('participants', []):
            # Change any Mejiro McQueen in Cup 1 or 5 to use the 101302 version
            if 'mcqueen' in p.get('uma', '').lower():
                p['uma'] = 'Mejiro McQueen [End of the Skies]'
                p['umaId'] = '101302-mejiro-mcqueen'
                updates += 1

if updates > 0:
    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Fixed {updates} Mejiro McQueen entries in Sus Cups 1 and 5.")
else:
    print("No updates needed.")
