with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.rfind('"cupNumber": 28')
print(text[idx:idx+3500])
