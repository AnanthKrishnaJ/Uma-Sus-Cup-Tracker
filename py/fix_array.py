content = open('suscup1.html', 'r', encoding='utf-8').read()
content = content.replace('"races":\n        {', '"races": [\n        {')
with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed array bracket.")
