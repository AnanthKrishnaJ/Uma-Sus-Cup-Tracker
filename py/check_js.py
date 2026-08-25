content = open('suscup1.html', 'r', encoding='utf-8').read()
start = content.find('"suscupimages1-10/suscup6.4.png"')
print(content[start-50:start+300])
