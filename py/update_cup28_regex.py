import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find Cup 28 block
cup28_idx = text.rfind('"cupNumber": 28')
end_idx = text.find('const UMA_DATABASE', cup28_idx)

cup28_text = text[cup28_idx:end_idx]

# Replace Seiun Sky
cup28_text = re.sub(
    r'"uma": "Seiun Sky"(.*?)"umaId": "[^"]+"(.*?)"version": "[^"]+"',
    r'"uma": "Seiun Sky"\1"umaId": "seiun-sky"\2"version": "Standard / Original"',
    cup28_text, flags=re.DOTALL
)

# Replace Meisho Doto
cup28_text = re.sub(
    r'"uma": "Meisho Doto"(.*?)"umaId": "[^"]+"',
    r'"uma": "Meisho Doto"\1"umaId": "105802-meisho-doto",\n          "version": "Dot-o\'-Lantern"',
    cup28_text, flags=re.DOTALL
)

# Replace Maruzensky
cup28_text = re.sub(
    r'"uma": "Maruzensky"(.*?)"umaId": "[^"]+"',
    r'"uma": "Maruzensky"\1"umaId": "maruzensky",\n          "version": "Standard / Original"',
    cup28_text, flags=re.DOTALL
)

# Replace Special Week
cup28_text = re.sub(
    r'"uma": "Special Week"(.*?)"umaId": "[^"]+"',
    r'"uma": "Special Week"\1"umaId": "special-week",\n          "version": "Standard / Original"',
    cup28_text, flags=re.DOTALL
)

# Replace Fuji Kiseki
cup28_text = re.sub(
    r'"uma": "Fuji Kiseki"(.*?)"umaId": "[^"]+"',
    r'"uma": "Fuji Kiseki"\1"umaId": "100502-fuji-kiseki",\n          "version": "Succès Étoilé"',
    cup28_text, flags=re.DOTALL
)

# Put it back
new_text = text[:cup28_idx] + cup28_text + text[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated Cup 28 IDs using regex.")
