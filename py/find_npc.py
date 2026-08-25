import re
content = open('suscup1.html', 'r', encoding='utf-8').read()
db_start = content.find('const UMA_DATABASE = {')
db_end = content.find('};', db_start)
db_content = content[db_start:db_end]
for match in re.findall(r'\"[^\"]+\"\s*:\s*\{[^\}]+NPC[^\}]+\}', db_content):
    print(match)
