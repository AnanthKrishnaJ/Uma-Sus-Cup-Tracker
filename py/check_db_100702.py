import json
with open(r'c:/Users/anant/OneDrive/Desktop/guess/Uma race tracker/.vscode/suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('"100702": {')
if idx != -1:
    print(repr(html[idx:idx+250]))
else:
    print("Not found")
