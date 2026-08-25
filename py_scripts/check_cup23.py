import json

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

for race in data.get('races', []):
    if str(race.get('cupNumber')) == 'SUS CUP 23' or str(race.get('cupNumber')) == '23':
        for p in race.get('participants', []):
            if 'Oguri Cap' in p.get('uma', '') or 'Bourbon' in p.get('uma', ''):
                print(f"uma={p.get('uma')} pos={p.get('pos')} no={p.get('number')} currentUrl={p.get('characterUrl')}")
