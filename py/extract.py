import json

with open('../.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = {')
if start == -1:
    print('Not found')
    exit()

brace_count = 0
in_string = False
escape = False
end = -1
for i in range(start + 21, len(text)):
    char = text[i]
    if escape:
        escape = False
        continue
    if char == '\\':
        escape = True
        continue
    if char == '"':
        in_string = not in_string
    if not in_string:
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end = i + 1
                break

json_str = text[start+21:end]
with open('extracted.json', 'w', encoding='utf-8') as f:
    f.write(json_str)
print('Extracted json of length', len(json_str))
