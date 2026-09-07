import json

js = open('index.html', encoding='utf-8').read()
data_start = js.find('const INITIAL_DATA = ')
data_end = js.find(';\n\n        const UMA_DATABASE')
init_data = json.loads(js[data_start+21:data_end])

for race in init_data['races']:
    for p in race['participants']:
        if not p.get('umaId'):
            uma = p.get('uma', '')
            if uma:
                # generate umaId
                uma_id = uma.lower().replace(" ", "-").replace("(", "").replace(")", "").replace(".", "").replace("'", "")
                p['umaId'] = uma_id

new_json = json.dumps(init_data, indent=2)
new_text = js[:data_start+21] + new_json + js[data_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Added missing umaIds to all participants.")
