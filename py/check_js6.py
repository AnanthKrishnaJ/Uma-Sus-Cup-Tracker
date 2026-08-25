content = open('suscup1.html', 'r', encoding='utf-8').read()
start = content.find('"id": 11,')
print(content[start+4000:start+6000])
