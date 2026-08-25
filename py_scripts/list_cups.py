import re
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\initial_data.json', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'\"?cupNumber\"?:\s*(\d+)', text)
for m in matches:
    print(m.group(1))
