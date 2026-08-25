import re

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

for key in ('seeking-the-pearl', 'agnes-digital'):
    match = re.search(r'\"' + key + r'\"\s*:.*?\},', html)
    if match: print(match.group(0))
