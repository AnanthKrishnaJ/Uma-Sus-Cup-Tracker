lines = open('index.html', encoding='utf-8').readlines()
matches = [f'{i+1}: {l.strip()}' for i, l in enumerate(lines) if 'gif' in l.lower() or 'png' in l.lower() or 'jpg' in l.lower() or 'webp' in l.lower() or 'jpeg' in l.lower()]
with open('matches.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(matches))
