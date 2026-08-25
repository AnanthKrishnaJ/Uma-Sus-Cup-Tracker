content = open('suscup1.html', 'r', encoding='utf-8').read()
content = content.replace('"suscupimages1-10/suscup6.4.png"\n            ,', '"suscupimages1-10/suscup6.4.png"\n            ],')
with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Bracket fixed.")
