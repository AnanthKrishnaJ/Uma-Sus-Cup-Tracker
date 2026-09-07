import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = "const INITIAL_DATA = "
start_idx = html.find(start_marker)

if start_idx == -1:
    print("Could not find INITIAL_DATA")
    exit(1)

start_idx += len(start_marker)
end_idx = -1
brace_count = 0
in_string = False
string_char = ''

for i in range(start_idx, len(html)):
    char = html[i]
    if in_string:
        if char == string_char and html[i-1] != '\\':
            in_string = False
        continue
    
    if char in ('"', "'", '`'):
        in_string = True
        string_char = char
        continue
        
    if char == '{':
        brace_count += 1
    elif char == '}':
        brace_count -= 1
        if brace_count == 0:
            end_idx = i
            break

data_str = html[start_idx:end_idx+1]
try:
    # It should be valid JSON except it might have unquoted keys or trailing commas if it's raw JS,
    # but the previous data was valid JSON. Let's try parsing it as JSON first.
    # Actually, in JS it's just an object literal. We can use a regex to fix keys or use a JS runner.
    pass
except Exception as e:
    print("Error parsing json in python", e)

# Since Python's json.loads might fail on JS object literals, we will write a JS script instead that is rock solid.
