with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const UMA_DATABASE = ')
end = text.find('};', start)
data_str = text[start + 21:end + 1]

missing = []
for umaId in ['100602', '102602', '101702', '104002', '100302', '102002', '104502', '103002', '100102', '101402', '101802', '102302', '102402', '100402', '101302', '105602']:
    if f'"{umaId}":' not in data_str and f"'{umaId}':" not in data_str:
        missing.append(umaId)

print('Missing in UMA_DATABASE:', missing)
