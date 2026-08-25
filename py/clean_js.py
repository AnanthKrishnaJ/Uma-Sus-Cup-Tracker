import re

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The corrupted part starts right after `races: [`
# It contains the beginning of suscup6, then suscup11, then the rest of suscup6.
# It ends right before `        {` of `suscup1`

# Let's find `races: [`
races_idx = content.find('"races": [')
if races_idx == -1:
    races_idx = content.find('races: [')

# Let's find the start of suscup1 (id: 1)
suscup1_idx = content.find('{\n            "id": 1,\n', races_idx)
if suscup1_idx == -1:
    suscup1_idx = content.find('{\n            "id": 1,\n', races_idx)

# Remove the corrupted block
clean_content = content[:races_idx+8] + '\n        ' + content[suscup1_idx:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(clean_content)

print("Removed corrupted block.")
