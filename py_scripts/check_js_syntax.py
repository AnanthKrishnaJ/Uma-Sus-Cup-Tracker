import re
import sys
import subprocess

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

script_match = re.search(r'<script>([\s\S]*?)</script>', text)
if script_match:
    js_code = script_match.group(1)
    with open('temp_test.js', 'w', encoding='utf-8') as f:
        f.write(js_code)
    
    result = subprocess.run(['node', '-c', 'temp_test.js'], capture_output=True, text=True)
    if result.returncode == 0:
        print("Valid JS syntax!")
    else:
        print("Syntax error in JS!")
        print(result.stderr)
else:
    print("Could not find script block")
