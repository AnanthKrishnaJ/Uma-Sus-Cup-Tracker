import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Fav: ${p.pop} with Fav: ${p.pop || '-'}
content = content.replace("Fav: ${p.pop}", "Fav: ${p.pop || '-'}")

# Replace the weird time prefix with "Time: "
content = re.sub(r'&bull; [^\x00-\x7F]+ \$\{h\.time', '&bull; Time: ${h.time', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed Fav display and Time mojibake.")
