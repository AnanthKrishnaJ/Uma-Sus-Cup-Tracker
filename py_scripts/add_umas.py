import re

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()

entries = """
            "105101": { id: "105101", name: "Nishino Flower", type: "Uma Musume", version: "Original / Default", url: "https://gametora.com/umamusume/characters/105101-nishino-flower", image: "https://gametora.com/images/umamusume/characters/chara_stand_1051_105101.png" },
            "101801": { id: "101801", name: "Air Groove", type: "Uma Musume", version: "Original / Default", url: "https://gametora.com/umamusume/characters/101801-air-groove", image: "https://gametora.com/images/umamusume/characters/chara_stand_1018_101801.png" },
"""

# Insert these directly into UMA_DATABASE at the beginning
pattern = r'(const UMA_DATABASE = \{\s*)'
new_html = re.sub(pattern, r'\1' + entries.lstrip('\n'), html, count=1)

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Added Nishino Flower and Air Groove to UMA_DATABASE.")
