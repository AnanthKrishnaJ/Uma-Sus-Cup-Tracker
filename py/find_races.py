content = open('suscup1.html', 'r', encoding='utf-8').read()
idx = content.find('races\": [')
print(content[idx:idx+500])
