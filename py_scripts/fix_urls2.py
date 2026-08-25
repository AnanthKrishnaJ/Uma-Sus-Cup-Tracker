import re, json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will replace specific gametora urls that are missing IDs
corrections = {
    'https://gametora.com/umamusume/characters/nishino-flower': 'https://gametora.com/umamusume/characters/105101-nishino-flower',
    'https://gametora.com/umamusume/characters/air-groove': 'https://gametora.com/umamusume/characters/101801-air-groove',
    'https://gametora.com/umamusume/characters/seeking-the-pearl': 'https://gametora.com/umamusume/characters/104201-seeking-the-pearl',
    'https://gametora.com/umamusume/characters/agnes-digital': 'https://gametora.com/umamusume/characters/101901-agnes-digital'
}

count = 0
for bad, good in corrections.items():
    text, n = re.subn(f'"{bad}"', f'"{good}"', text)
    count += n

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(f'Replaced {count} bad URLs.')
