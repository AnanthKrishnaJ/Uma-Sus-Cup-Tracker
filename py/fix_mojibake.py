with open('index.html', 'rb') as f:
    content = f.read()

# Byte sequence replacements
replacements = {
    # 🥇 (1st place medal)
    b'\xc3\xb0\xc5\xb8\xc2\xa5\xe2\x80\xa1': b'\xf0\x9f\xa5\x87',
    # 🥈 (2nd place medal)
    b'\xc3\xb0\xc5\xb8\xc2\xa5\xcb\x86': b'\xf0\x9f\xa5\x88',
    # 🥉 (3rd place medal)
    b'\xc3\xb0\xc5\xb8\xc2\xa5\xe2\x80\xb0': b'\xf0\x9f\xa5\x89',
    # 🏆 (Trophy)
    b'\xc3\xb0\xc5\xb8\xc2\x8f\xe2\x80\xa0': b'\xf0\x9f\x8f\x86',
    # 🏅 (Sports medal)
    b'\xc3\xb0\xc5\xb8\xc2\x8f\xe2\x80\xa6': b'\xf0\x9f\x8f\x85',
    # 🌟 (Glowing star)
    b'\xc3\xb0\xc5\xb8\xc5\x92\xc5\xb8': b'\xf0\x9f\x8c\x9f',
    # • (Bullet) - typical double encode: â€¢
    b'\xc3\xa2\xe2\x82\xac\xc2\xa2': b'\xe2\x80\xa2',
    # · (Middle dot) - typical double encode: Â·
    b'\xc3\x82\xc2\xb7': b'\xc2\xb7',
    # — (Em dash) - typical double encode: â€”
    b'\xc3\xa2\xe2\x80\x94\xef\xbf\xbd': b'\xe2\x80\x94',
    # – (En dash) - typical double encode: â€“
    b'\xc3\xa2\xe2\x80\x9c\xef\xbf\xbd': b'\xe2\x80\x93',
    # é (e acute) - typical double encode: Ã©
    b'\xc3\x83\xc2\xa9': b'\xc3\xa9',
    # Weird character for '-' (e.g. from '?"')
    b'\xef\xbf\xbd?"': b'-',
    # "A,A" which seems to be corrupted bullet
    b'A\xef\xbf\xbd,\xef\xbf\xbdA\xef\xbf\xbd': b'\xe2\x80\xa2',
    b'A\xef\xbf\xbd\xc2\x80\xef\xbf\xbdA\xef\xbf\xbd': b'\xe2\x80\xa2',
    # Warning sign corrupted
    b'A\xef\xbf\xbdAA_A,\xef\xbf\xbdA?': b'\xe2\x9a\xa0\xef\xb8\x8f'
}

for bad, good in replacements.items():
    content = content.replace(bad, good)

# Also fix the weird "dY" stuff if they exist
content = content.replace(b'dY\xef\xbf\xbd 1', b'\xf0\x9f\xa5\x87 1')
content = content.replace(b'dY\xef\xbf\xbd^ 2', b'\xf0\x9f\xa5\x88 2')
content = content.replace(b'dY\xef\xbf\xbd% 3', b'\xf0\x9f\xa5\x89 3')
content = content.replace(b'dY\x8f 1', b'\xf0\x9f\xa5\x87 1')
content = content.replace(b'dY\x8f^ 2', b'\xf0\x9f\xa5\x88 2')
content = content.replace(b'dY\x8f% 3', b'\xf0\x9f\xa5\x89 3')

with open('index.html', 'wb') as f:
    f.write(content)

print("Replaced successfully")
