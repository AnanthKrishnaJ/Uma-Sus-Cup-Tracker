with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('\"winners\":')
if idx != -1:
    print(text[idx-50:idx+2500])
else:
    print('Not found')
