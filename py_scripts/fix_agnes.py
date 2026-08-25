import re
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix "agnes" to "Agnes"
html = re.sub(r'player:\s*"agnes"', 'player: "Agnes"', html)

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Fixed agnes -> Agnes.")
