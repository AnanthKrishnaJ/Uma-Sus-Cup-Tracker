import re
content = open('suscup1.html', 'r', encoding='utf-8').read()
content = re.sub(
    r'"uma": "(Encore One More|Sidecar|Chalemie Rhythm|Mechanical Vapor|Aeneas|Leaf Leaf)",',
    lambda m: m.group(0) + f'\n                    "umaId": "{m.group(1).lower().replace(" ", "-")}",',
    content
)
with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated NPCs to include umaId")
