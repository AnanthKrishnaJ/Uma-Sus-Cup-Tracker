import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const INITIAL_DATA = {')
end = html.find('};', start) + 1
data_str = html[start+21:end]

def get_race_by_id(cup_id):
    search_str = f'"id": {cup_id},'
    idx = data_str.find(search_str)
    if idx == -1:
        search_str = f'"cupNumber": {cup_id},'
        idx = data_str.find(search_str)
    if idx == -1:
        return f"Not found {cup_id}"
        
    start_brace = data_str.rfind('{', 0, idx)
    end_brace = data_str.find('    },', start_brace)
    
    return data_str[start_brace:end_brace+6]

with open('cup22_24.txt', 'w', encoding='utf-8') as f:
    f.write('--- Sus Cup 22 ---\n')
    f.write(get_race_by_id(22))
    f.write('\n--- Sus Cup 23 ---\n')
    f.write(get_race_by_id(23))
    f.write('\n--- Sus Cup 24 ---\n')
    f.write(get_race_by_id(24))
