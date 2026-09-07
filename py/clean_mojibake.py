with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "${mostUsedUma.runs} Races ? ${mostUsedUma.podiums} Podiums ? Avg ${mostUsedUma.avgFinish}": "${mostUsedUma.runs} Races &bull; ${mostUsedUma.podiums} Podiums &bull; Avg ${mostUsedUma.avgFinish}",
    "Fanatic~+Jiangshi": "Fanatic☆Jiangshi",
    "Bubblegum~+Memories": "Bubblegum☆Memories",
    "SuccA\"s A%toilAc": "Succès Étoilé",
    "SuccA\"s A%toilAe": "Succès Étoilé",
    "SuccA.s A.toilA.": "Succès Étoilé"
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Cleaned up mojibake using str.replace!")
