import re
import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The empty race 6 might be looking like:
# { "id": 6, "cupNumber": "SUS CUP 6", ... "participants": [] }
# We want to replace it with the data from add_suscup6.py

match = re.search(r'\{\s*"id":\s*6,\s*"cupNumber":\s*"SUS CUP 6"[\s\S]*?"participants":\s*\[\]\s*\}', html)
if match:
    print('FOUND EMPTY CUP 6')
    print(match.group(0))
else:
    print('COULD NOT FIND EMPTY CUP 6')
