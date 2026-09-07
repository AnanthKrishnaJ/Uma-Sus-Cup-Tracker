import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the umaIds that might have -<name> suffix when umasMap only expects numbers for the alternate versions
content = content.replace('"100602-oguri-cap"', '"100602"')
content = content.replace('"100302-tokai-teio"', '"100302"')
content = content.replace('"101302-mejiro-mcqueen"', '"101302"')
content = content.replace('"105602-matikanefukukitaru"', '"105602"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
