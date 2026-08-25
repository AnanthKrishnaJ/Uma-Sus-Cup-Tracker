import re
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\initial_data.json', 'r', encoding='utf-8') as f:
    text = f.read()

m = text.find('\"winners\": [')
if m != -1:
    winners_str = text[m:m+5000]
    for w in re.finditer(r'\"cup\": \"Sus Cup 1[6789]\",.*?\}', text, re.DOTALL):
        print(w.group(0))
    for w in re.finditer(r'\"cup\": \"Sus Cup 20\",.*?\}', text, re.DOTALL):
        print(w.group(0))
