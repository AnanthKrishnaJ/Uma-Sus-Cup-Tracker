with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<div id="galleryModal"')
if idx != -1:
    print(text[idx-50:idx+800])
else:
    print('Not found')
