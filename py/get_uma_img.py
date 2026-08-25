import re

with open('../.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'getUmaImage[^{]*\{.*?\}', content, flags=re.DOTALL)
if match:
    print(match.group(0))
else:
    print("Not found")
