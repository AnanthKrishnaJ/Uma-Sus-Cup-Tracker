import re
content = open('suscup1.html', 'r', encoding='utf-8').read()

npcs = ["Encore One More", "Sidecar", "Chalemie Rhythm", "Mechanical Vapor", "Aeneas", "Leaf Leaf"]
db_start = content.find('const UMA_DATABASE = {')
db_end = content.find('};', db_start)

# Extract db block
db_block = content[db_start:db_end]

for npc in npcs:
    npc_id = npc.lower().replace(' ', '-')
    if f'"{npc_id}":' not in db_block:
        npc_str = f'\n        "{npc_id}": {{"id":"{npc_id}","name":"{npc}","type":"NPC","url":null,"image":null}},'
        db_block += npc_str

# Replace back
content = content[:db_start] + db_block + '\n    ' + content[db_end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("NPCs added safely.")
