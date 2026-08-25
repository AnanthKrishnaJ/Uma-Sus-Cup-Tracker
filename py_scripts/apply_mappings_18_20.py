import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
db_start = text.find('const UMA_DATABASE = ')
end = text.rfind('};', start, db_start)

data = json.loads(text[start + 21:end + 1])
races = data['races']

for race in races:
    if race['id'] == 18:
        for p in race['participants']:
            if p['uma'] == 'Symboli Rudolf':
                if p['pos'] == 12:
                    p['umaId'] = '101702'
                elif p['pos'] == 17:
                    p['umaId'] = 'symboli-rudolf'
    elif race['id'] == 19:
        for p in race['participants']:
            if p['uma'] == 'Gold City':
                p['umaId'] = '104002'
    elif race['id'] == 20:
        for p in race['participants']:
            if p['uma'] == 'Gold City':
                p['umaId'] = '104002'
            elif p['uma'] == 'Mayano Top Gun':
                p['umaId'] = '102402'
            elif p['uma'] == 'Mihono Bourbon':
                pass # user didn't mention CODE: ICING for 20, they mentioned it for 23

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_text = text[:start + 21] + new_json + text[end + 1:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Applied alt mappings for Cups 18-20.")
