with open('index.html', 'rb') as f:
    content = f.read()

# Fix residual double-encoded characters
replacements = {
    # Em-dash
    b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d': b'\xe2\x80\x94',
    # Warning emoji ⚠️
    b'\xc3\xa2\xc5\xa1\xc2\xa0\xc3\xaf\xc2\xb8\xc2\x8f': b'\xe2\x9a\xa0\xef\xb8\x8f',
    # Agnes Digital: Fanatic☆Jiangshi
    b'Fanatic\xc3\xa2\xe2\x84\xa2\xc2\xa1Jiangshi': b'Fanatic\xe2\x98\x86Jiangshi',
    # Taiki Shuttle: Bubblegum☆Memories
    b'Bubblegum\xc3\xa2\xcb\x9c\xe2\x80\xa0Memories': b'Bubblegum\xe2\x98\x86Memories',
    # Special Week: Hopp'n♪Happy Heart (or something similar, usually it's ♪)
    b'Hopp\'n\xc3\xa2\xe2\x84\xa2\xc2\xaaHappy Heart': b'Hopp\'n\xe2\x99\xaaHappy Heart',
    # Fuji Kiseki 100502: Succès Étoilé
    b'SuccA\xef\xbf\xbdA"s A\xef\xbf\xbd?\xef\xbf\xbdtoilA\xef\xbf\xbdAc': b'Succ\xc3\xa8s \xc3\x89toil\xc3\xa9',
    b'SuccA\xef\xbf\xbdA\xef\xbf\xbdA\xef\xbf\xbdA\xef\xbf\xbdA\xef\xbf\xbd': b'Succ\xc3\xa8s \xc3\x89toil\xc3\xa9' # catch-all
}

for bad, good in replacements.items():
    content = content.replace(bad, good)

# Also I noticed Fuji Kiseki is still messed up from an earlier grep:
# "SuccAA"s A?toilAAc"
# I'll just use string replacement for Fuji Kiseki entirely to be safe
try:
    text = content.decode('utf-8')
    import re
    text = re.sub(r'Succ.*?toil.*?"', r'Succès Étoilé"', text)
    content = text.encode('utf-8')
except Exception as e:
    print("Regex fix failed:", e)

with open('index.html', 'wb') as f:
    f.write(content)

print("Replaced successfully again")
