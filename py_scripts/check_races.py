with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\initial_data.json', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('races\": [')
if idx != -1:
    print(text[idx:idx+800])
else:
    print('Not found')
