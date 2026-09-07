import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the specific "â€”" character (often \u00e2\u20ac\u201d in Python due to how cp1252 to utf-8 conversion mangles it)
text = text.replace('â€”', '—')
text = text.replace('â€"', '—')
text = text.replace('â€“', '–')

# Just to be fully safe for the specific text found in the database:
text = text.replace('Sus Cup 27 â€” Multi CM Sussing', 'Sus Cup 27 — Multi CM Sussing')
text = text.replace('Sus Cup 28 â€” Triple Threat', 'Sus Cup 28 — Triple Threat')
# If it's literally \u00e2\u20ac\u201d:
text = text.replace('\u00e2\u20ac\u201d', '—')

# Fix the trophy icon to be gold
text = text.replace('<i class="fa-solid fa-trophy"></i> <span>Sus Cups</span>', '<i class="fa-solid fa-trophy" style="color: var(--gold);"></i> <span>Sus Cups</span>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied replacements")
