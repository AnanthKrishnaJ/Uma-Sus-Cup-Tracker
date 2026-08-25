import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Change p.number to p.number || '-'
content = content.replace(
    '<div class="avatar-circle" style="width:45px;height:45px;font-size:1rem;background:#eee;color:#333;">${p.number}</div>',
    '<div class="avatar-circle" style="width:45px;height:45px;font-size:1rem;background:#eee;color:#333;">${p.number || \'-\'}</div>'
)

# Fix 2: Limit images to 4 in gallery overview
# We look for race.images.map and change to race.images.slice(0, 4).map
content = content.replace(
    'race.images.map((image, index)',
    'race.images.slice(0, 4).map((image, index)'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("UI fixes applied!")
