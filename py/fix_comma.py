content = open('suscup1.html', 'r', encoding='utf-8').read()
content = content.replace('"stenz": {"id":"stenz","name":"Stenz","type":"NPC","url":null,"image":null}\n        "encore-one-more"', '"stenz": {"id":"stenz","name":"Stenz","type":"NPC","url":null,"image":null},\n        "encore-one-more"')
with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Comma fixed.")
