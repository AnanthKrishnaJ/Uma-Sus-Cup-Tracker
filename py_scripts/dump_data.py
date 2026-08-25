import re

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = {')
end = text.find('const UMA_DATABASE = {')

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\initial_data.json', 'w', encoding='utf-8') as fw:
    fw.write(text[start:end])
