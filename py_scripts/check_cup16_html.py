import re
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\{\s*\"?id\"?:\s*16,.*?(?=\s*\{\s*\"?id\"?:)', text, re.DOTALL)
if m:
    print(m.group(0)[:500])
else:
    print('Cup 16 not found')
