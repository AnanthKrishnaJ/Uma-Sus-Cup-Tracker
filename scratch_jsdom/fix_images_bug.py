import re

with open('../index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the bug in the JavaScript logic
content = content.replace('images: [...sourceRace.images]', 'images: [...(sourceRace.images || [])]')

# Add "images": [] to any object missing it right before participants, although fixing the JS prevents the crash anyway
# But we can also add it for completeness.
content = content.replace('"participants": [', '"images": [], "participants": [')

with open('../index.html', 'w', encoding='utf-8') as f:
    f.write(content)
