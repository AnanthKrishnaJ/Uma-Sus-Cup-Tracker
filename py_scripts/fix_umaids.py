import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const INITIAL_DATA = ')
end = html.find('};\n', start) + 1
if start != -1:
    data_str = html[start + len('const INITIAL_DATA = '):end]
    data = json.loads(data_str)
    
    for i, race in enumerate(data.get('races', [])):
        for j, p in enumerate(race.get('participants', [])):
            if p.get('uma') in ('Nishino Flower', 'Air Groove'):
                print(f"Race {race.get('id')} - {p.get('uma')} - umaId: {p.get('umaId')}")
                if p.get('uma') == 'Nishino Flower':
                    data['races'][i]['participants'][j]['umaId'] = '105101'
                if p.get('uma') == 'Air Groove':
                    data['races'][i]['participants'][j]['umaId'] = '101801'

    # write back data
    new_data_str = json.dumps(data, indent=8)
    # Fix indentation roughly
    
    new_html = html[:start + len('const INITIAL_DATA = ')] + new_data_str + html[end:]
    
    with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated INITIAL_DATA with proper umaIds!")
