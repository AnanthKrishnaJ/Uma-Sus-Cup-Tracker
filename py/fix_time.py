import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix: Remove time display in showRaceDetail
old_time_code = "race.date && `${race.date.split(',')[0]}${race.time ? ` / ${race.time}` : ''}`,"
new_time_code = "race.date && `${race.date.split(',')[0]}`,"
content = content.replace(old_time_code, new_time_code)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Time removed!")
