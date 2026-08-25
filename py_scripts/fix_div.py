with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '        </div>\n        </div>\n        <ul class="nav-links">'
replacement = '        </div>\n        <ul class="nav-links">'

if target in text:
    text = text.replace(target, replacement)
    with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Fixed extra div in sidebar.')
else:
    print('Target not found!')
