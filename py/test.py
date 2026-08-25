import re
with open('../.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

ids = re.findall(r"id:\s*['\"]([^'\"]+)['\"]", content)
print('Found IDs in INITIAL_DATA:')
print(ids)
