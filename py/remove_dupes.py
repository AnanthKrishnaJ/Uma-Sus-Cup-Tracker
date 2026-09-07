import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove duplicate 100602 (Ashen Miracle) and 100402 (Alternate)
c = re.sub(r'[ \t]*"100602": \{ id: "100602", name: "Oguri Cap", type: "Uma Musume", version: "Ashen Miracle"[^\n]*\n', '', c)
c = re.sub(r'[ \t]*"100402": \{ id: "100402", name: "Maruzensky", type: "Uma Musume", version: "Alternate"[^\n]*\n', '', c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Removed duplicates.")
