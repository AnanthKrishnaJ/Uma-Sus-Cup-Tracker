import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const INITIAL_DATA = {')
end = html.find('};', start) + 1
data_str = html[start+21:end]

# Extract the races array string
races_start = data_str.find('races: [')
# Let's just find the start of each and the end of the object.
def get_race_by_id(cup_id):
    search_str = f'"id": {cup_id},'
    idx = data_str.find(search_str)
    if idx == -1:
        # try cupNumber
        search_str = f'"cupNumber": {cup_id},'
        idx = data_str.find(search_str)
    if idx == -1:
        return f"Not found {cup_id}"
        
    start_brace = data_str.rfind('{', 0, idx)
    # find the matching closing brace, or just take next 2000 chars
    end_brace = data_str.find('    },', start_brace)
    
    return data_str[start_brace:end_brace+6]

print('--- Sus Cup 22 ---')
print(get_race_by_id(22))
print('--- Sus Cup 23 ---')
print(get_race_by_id(23))
print('--- Sus Cup 24 ---')
print(get_race_by_id(24))

