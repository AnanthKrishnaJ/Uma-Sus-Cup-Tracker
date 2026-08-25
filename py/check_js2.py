content = open('suscup1.html', 'r', encoding='utf-8').read()
start = content.find('"id": 6,')
print(content[start-50:start+1000])
