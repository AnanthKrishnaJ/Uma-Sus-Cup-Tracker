import re
html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

db_start = text.find('const UMA_DATABASE = ')
db_end = text.rfind('};', db_start)
db_str = text[db_start + 21:db_end + 1]

# find all keys that have 1001_100101
matches = re.findall(r"['\"]?([\w-]+)['\"]?\s*:\s*\{[^}]*1001_100101[^}]*\}", db_str)
print("NPCs using Special Week image:")
for m in matches:
    print(m)
