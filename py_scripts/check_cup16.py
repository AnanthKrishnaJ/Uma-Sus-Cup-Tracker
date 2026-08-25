import re
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\initial_data.json', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'\"?cupNumber\"?:\s*16\b', text):
    print(text[m.start()-50:m.end()+300])
