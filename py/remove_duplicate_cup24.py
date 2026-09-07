with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '"id": 24,' in line and '"cup": "24",' in lines[i+1]:
        start_idx = i - 1
        for j in range(start_idx, len(lines)):
            if lines[j].strip() == '},' and '"id": 23,' in lines[j+2]:
                end_idx = j
                break
        break

if start_idx != -1 and end_idx != -1:
    print(f"Removing lines {start_idx} to {end_idx}")
    del lines[start_idx:end_idx+1]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
else:
    print("Could not find the exact block.")
