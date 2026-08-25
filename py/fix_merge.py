import re

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add cupName to the explicitly merged properties for INITIAL_DATA.races[0]
content = content.replace(
    'cupNumber: sourceRace.cupNumber, name: sourceRace.name, date: sourceRace.date,',
    'cupNumber: sourceRace.cupNumber, cupName: sourceRace.cupName, name: sourceRace.name, date: sourceRace.date,'
)

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)
