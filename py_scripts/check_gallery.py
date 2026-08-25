import re
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

if 'id="galleryModal"' in text:
    print('galleryModal found')
else:
    print('galleryModal not found')
