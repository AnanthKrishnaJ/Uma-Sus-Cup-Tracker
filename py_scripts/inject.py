import os

html_path = 'c:/Users/anant/OneDrive/Desktop/guess/Uma race tracker/.vscode/suscup1.html'
inject_path = 'c:/Users/anant/OneDrive/Desktop/guess/Uma race tracker/inject.js'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open(inject_path, 'r', encoding='utf-8') as f:
    inject_js = f.read()

target = "document.addEventListener('DOMContentLoaded', () => { App.init(); });"
if target in html:
    new_html = html.replace(target, inject_js + '\n\n        ' + target)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Injected successfully!")
else:
    print("Target not found!")
