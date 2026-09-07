with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('"player": "agnes"', '"player": "Agnes"')
text = text.replace('"trainer": "agnes"', '"trainer": "Agnes"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
