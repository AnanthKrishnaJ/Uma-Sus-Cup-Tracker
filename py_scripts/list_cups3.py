import re
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'\"?cupNumber\"?:\s*\"?(\d+)\"?', text)
s = set()
for m in matches:
    s.add(int(m.group(1)))
print(sorted(list(s)))
