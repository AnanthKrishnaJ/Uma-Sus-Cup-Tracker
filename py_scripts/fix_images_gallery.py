import json, re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

# 1. Update UMA images for Cup 18, 19, 20
for r in data['races']:
    cup_num = str(r.get('cupNumber', ''))
    if '18' in cup_num:
        for p in r.get('participants', []):
            if 'Symboli Rudolf' in p.get('uma', ''):
                p['umaId'] = '101702'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/101702-symboli-rudolf'
    if '19' in cup_num:
        for p in r.get('participants', []):
            if 'Gold City' in p.get('uma', ''):
                p['umaId'] = '104002'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/104002-gold-city'
    if '20' in cup_num:
        for p in r.get('participants', []):
            if 'Gold City' in p.get('uma', ''):
                p['umaId'] = '104002'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/104002-gold-city'
            if 'Mayano Top Gun' in p.get('uma', ''):
                p['umaId'] = '102402'
                p['characterUrl'] = 'https://gametora.com/umamusume/characters/102402-mayano-top-gun'

# 2. Update the winners array with the correct images too
for w in data.get('winners', []):
    cup = str(w.get('cup', ''))
    uma = w.get('uma', '')
    if '18' in cup and 'Symboli Rudolf' in uma:
        w['umaId'] = '101702'
        w['url'] = 'https://gametora.com/umamusume/characters/101702-symboli-rudolf'
    if ('19' in cup or '20' in cup) and 'Gold City' in uma:
        w['umaId'] = '104002'
        w['url'] = 'https://gametora.com/umamusume/characters/104002-gold-city'
    if '20' in cup and 'Mayano Top Gun' in uma:
        w['umaId'] = '102402'
        w['url'] = 'https://gametora.com/umamusume/characters/102402-mayano-top-gun'

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

# 3. Fix openGalleryModal
text = text.replace(
    'onclick=\\\'openGalleryModal(${JSON.stringify(race.images)}, ${index})\\\'',
    'onclick="openGallery(\\\'${race.images.join(\',\')}\\\', ${index})"'
)
# Also just in case:
text = text.replace(
    'onclick=\'openGalleryModal(${JSON.stringify(race.images)}, ${index})\'',
    'onclick="openGallery(\'${race.images.join(\',\')}\', ${index})"'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated UMA images and gallery function')
