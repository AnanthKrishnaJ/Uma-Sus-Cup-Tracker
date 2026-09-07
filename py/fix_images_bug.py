import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I want to remove the injected "images": [], "participants": [ where it is preceded by a real images array.
# But honestly, it's safer to just remove ALL instances of "images": [], "participants": [ and "images": [],\n        "participants": [ and replace them with "participants": [ 
# Wait, some races might NOT have an images array at all! Which ones didn't have one before?
# Wait, if we just remove "images": [], "participants": [ we'd lose the images array for races that didn't have one, BUT migrateHistoricalRecord handles undefined images gracefully now!

content = content.replace('"images": [], "participants": [', '"participants": [')
content = content.replace('"images": [],\n        "participants": [', '"participants": [')
content = content.replace('"images": [],\n    "participants": [', '"participants": [')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
