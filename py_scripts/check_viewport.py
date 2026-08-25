import re

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<meta name="viewport"[^>]*>', text)
if m:
    print('Viewport:', m.group(0))

m = re.search(r'function openGallery\b', text)
if m:
    print('openGallery found at:', m.start())
else:
    print('openGallery NOT FOUND in suscup1.html!')
