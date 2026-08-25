import json

with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const UMA_DATABASE =')
end = text.find('const SKILLS_DATABASE =')
if end == -1: end = text.find('</script>')
json_str = text[start + 20:end].strip().rstrip(';')
data = json.loads(json_str)

for id, name in data.items():
    if 'mcqueen' in id.lower() or 'mcqueen' in name.lower():
        print(f"{id}: {name}")
