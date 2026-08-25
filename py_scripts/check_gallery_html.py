import re

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<div id=\"galleryModal\".*?(?=</script>)', text, re.DOTALL)
if m:
    with open('gallery_logic.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0)[:3000])
