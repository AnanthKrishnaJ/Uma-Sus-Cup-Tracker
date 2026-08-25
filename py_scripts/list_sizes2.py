import re
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\initial_data.json', 'r', encoding='utf-8') as f:
    text = f.read()

matches = list(re.finditer(r'\"?cupNumber\"?:\s*\"?(\d+)\"?', text))
for i in range(len(matches)):
    start = matches[i].start()
    end = matches[i+1].start() if i+1 < len(matches) else len(text)
    print(f'Cup {matches[i].group(1)} length: {end - start}')
