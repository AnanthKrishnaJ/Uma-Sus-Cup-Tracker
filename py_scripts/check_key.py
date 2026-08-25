import re

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const UMA_DATABASE =')
end = text.find('const SKILLS_DATABASE =')
db_str = text[start + 20:end].strip().rstrip(';')

for m in re.finditer(r'[\'\"a-zA-Z0-9_-]+:\s*\{[^}]+\}', db_str):
    if '100101' in m.group(0):
        print('KEY:', m.group(0).split(':')[0].strip(), '=>', m.group(0)[:100])
