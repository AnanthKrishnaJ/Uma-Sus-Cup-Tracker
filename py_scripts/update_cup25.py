import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

alt_versions = {
    'Oguri Cap': ('100602', 'https://gametora.com/umamusume/characters/100602-oguri-cap'),
    'Mihono Bourbon': ('102602', 'https://gametora.com/umamusume/characters/102602-mihono-bourbon'),
    'Symboli Rudolf': ('101702', 'https://gametora.com/umamusume/characters/101702-symboli-rudolf'),
    'Gold City': ('104002', 'https://gametora.com/umamusume/characters/104002-gold-city'),
    'Tokai Teio': ('100302', 'https://gametora.com/umamusume/characters/100302-tokai-teio'),
    'Seiun Sky': ('102002', 'https://gametora.com/umamusume/characters/102002-seiun-sky'),
    'Super Creek': ('104502', 'https://gametora.com/umamusume/characters/104502-super-creek'),
    'Rice Shower': ('103002', 'https://gametora.com/umamusume/characters/103002-rice-shower'),
    'Special Week': ('100102', 'https://gametora.com/umamusume/characters/100102-special-week'),
    'El Condor Pasa': ('101402', 'https://gametora.com/umamusume/characters/101402-el-condor-pasa'),
    'Air Groove': ('101802', 'https://gametora.com/umamusume/characters/101802-air-groove'),
    'Biwa Hayahide': ('102302', 'https://gametora.com/umamusume/characters/102302-biwa-hayahide'),
    'Mayano Top Gun': ('102402', 'https://gametora.com/umamusume/characters/102402-mayano-top-gun')
}

updated = 0

for race in data.get('races', []):
    if str(race.get('cupNumber')) == 'SUS CUP 25' or str(race.get('cupNumber')) == '25':
        for p in race.get('participants', []):
            uma_name = p.get('uma', '')
            for alt_name, (alt_id, alt_url) in alt_versions.items():
                if alt_name in uma_name:
                    p['umaId'] = alt_id
                    p['characterUrl'] = alt_url
                    updated += 1
                    break

if updated > 0:
    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
print(f'Updated {updated} records in Sus Cup 25')
