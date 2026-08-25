with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''        ,
        "104002": "https://gametora.com/umamusume/characters/104002-gold-city"};'''

replacement = '''        "104002": "https://gametora.com/umamusume/characters/104002-gold-city"
        };'''

if target in text:
    text = text.replace(target, replacement)
    with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Fixed UMA_DATABASE syntax error!')
else:
    print('Target not found!')
