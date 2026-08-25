import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Gametora alt image format
# From: chara_stand_100602_1060.png
# To: chara_stand_1006_100602.png
content = re.sub(r'chara_stand_(\d{4})(\d{2})_1060\.png', r'chara_stand_\1_\1\2.png', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied regex fix to all alt costume images in UMA_DATABASE.")
