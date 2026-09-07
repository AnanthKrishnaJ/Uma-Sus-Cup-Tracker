import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = {
    '"100602-oguri-cap"': '"100602"',
    '"100302-tokai-teio"': '"100302"',
    '"101302-mejiro-mcqueen"': '"101302"',
    '"105602-matikanefukukitaru"': '"105602"'
}

for k, v in changes.items():
    content = content.replace(k, v)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated umaIds')
