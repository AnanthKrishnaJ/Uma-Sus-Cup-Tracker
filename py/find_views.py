with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="view-players"' in line or 'id="view-player-profile"' in line:
        for j in range(max(0, i-2), i+15):
            print(f'{j+1}: {lines[j].rstrip()}')
        break
