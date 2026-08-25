import json
with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const UMA_DATABASE = ')
end = text.find('};', start)
data_str = text[start + 21:end + 1]
data = json.loads(data_str)
for key, value in data.items():
    if 'Gold City' in key:
        print(f"{key}: {value}")
