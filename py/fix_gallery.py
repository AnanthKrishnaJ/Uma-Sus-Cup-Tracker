import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace object-fit: cover with object-fit: contain for .race-gallery img
# We can do this with a precise regex
content = re.sub(
    r'(\.race-gallery img\s*\{.*?)(object-fit:\s*cover;)(.*?\})',
    r'\1object-fit: contain;\3',
    content,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
