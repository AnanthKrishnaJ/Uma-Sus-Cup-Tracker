import re
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\initial_data.json', 'r', encoding='utf-8') as f:
    text = f.read()
for i in range(16, 22):
    m = re.search(r'cupNumber:\s*' + str(i) + r'.*?participants:\s*\[(.*?)\]', text, re.DOTALL)
    if m:
        participants = m.group(1)
        print(f'Cup {i} has {participants.count("player:")} participants')
    else:
        print(f'Cup {i} not found')
