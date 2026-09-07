import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace literal JSON escapes of the mojibake em-dash
text = text.replace(r'\u00e2\u20ac\u201d', '—')

# The user wants the trophy icon to be gold. Let's find all instances of fa-trophy and ensure they have a proper gold color.
# Actually, the user might mean the main sidebar icon, or the ones in headings.
# Let's replace the sidebar icon explicitly:
text = text.replace('<i class="fa-solid fa-trophy"></i> <span>Sus Cups</span>', '<i class="fa-solid fa-trophy" style="color: #f1c40f;"></i> <span>Sus Cups</span>')
text = text.replace('<i class="fa-solid fa-trophy" style="color: var(--gold);"></i> <span>Sus Cups</span>', '<i class="fa-solid fa-trophy" style="color: #f1c40f;"></i> <span>Sus Cups</span>')

# Also for the one in Player Rankings heading:
text = text.replace('<i class="fa-solid fa-trophy" style="color:var(--primary)"></i> Player Rankings', '<i class="fa-solid fa-trophy" style="color:#f1c40f"></i> Player Rankings')

# Replace var(--gold) trophy with the stronger #f1c40f gold for better visibility
text = text.replace('<i class="fa-solid fa-trophy" style="color:var(--gold); margin-right:6px;"></i>', '<i class="fa-solid fa-trophy" style="color:#f1c40f; margin-right:6px;"></i>')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied replacements")
