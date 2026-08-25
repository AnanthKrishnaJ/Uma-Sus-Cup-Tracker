import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace for oishii-parfait
text = re.sub(
    r'("oishii-parfait"\s*:\s*\{.*?image\s*:\s*)"[^"]*"(\s*\})',
    r'\1null\2',
    text
)

# Replace for coronet-rhythm
text = re.sub(
    r'("coronet-rhythm"\s*:\s*\{.*?image\s*:\s*)"[^"]*"(\s*\})',
    r'\1null\2',
    text
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Removed Special Week images from oishii-parfait and coronet-rhythm!")
