import re
html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

for key in ['oishii-parfait', 'coronet-rhythm', 'tropical-sky']:
    match = re.search(r"['\"]" + key + r"['\"]\s*:\s*\{[^}]*\}", text)
    if match:
        print(match.group(0))
    else:
        print(key, 'not found with regex')
