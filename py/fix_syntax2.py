import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix literal template interpolations
content = content.replace(r'\${', '${')

# Fix literal backticks
content = content.replace(r'\`', '`')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
