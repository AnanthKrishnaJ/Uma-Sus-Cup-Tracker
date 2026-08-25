import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
db_start = text.find('const UMA_DATABASE = ')
end = text.rfind('};', start, db_start)

data = json.loads(text[start + 21:end + 1])
races = data['races']

mappings = {
    22: {'Oguri Cap': '100602'},
    23: {'Oguri Cap': '100602'},
    24: {'Oguri Cap': '100602', 'Maruzensky': '100402'},
    25: {
        'Oguri Cap': '100602',
        'Mihono Bourbon': '102602',
        'Symboli Rudolf': '101702',
        'Gold City': '104002',
        'Tokai Teio': '100302',
        'Seiun Sky': '102002',
        'Super Creek': '104502',
        'Rice Shower': '103002',
        'Special Week': '100102',
        'El Condor Pasa': '101402',
        'Air Groove': '101802',
        'Biwa Hayahide': '102302',
        'Mayano Top Gun': '102402'
    }
}

for cup in races:
    cup_id = cup['id']
    if cup_id in mappings:
        for p in cup['participants']:
            if p['uma'] in mappings[cup_id]:
                p['umaId'] = mappings[cup_id][p['uma']]

# write back
new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_text = text[:start + 21] + new_json + text[end + 1:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Applied alt umaId mappings successfully.")
