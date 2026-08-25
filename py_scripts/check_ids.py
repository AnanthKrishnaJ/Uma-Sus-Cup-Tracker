import re

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const UMA_DATABASE =')
end = text.find('const SKILLS_DATABASE =')
db_str = text[start + 20:end].strip().rstrip(';')

ids = ['100101', '101301', '101701', '102401', '100301', '100601', '103201', '106001', '104501']
for i in ids:
    found = False
    for m in re.finditer(r'([\'\"a-zA-Z0-9_-]+):\s*\{[^}]+\}', db_str):
        if i in m.group(0):
            print(f'{i} -> {m.group(1).strip("\'\\"")}')
            found = True
            break
    if not found:
        print(f'{i} -> NOT FOUND')
