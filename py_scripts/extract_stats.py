with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('updateStats: function() {')
if idx == -1:
    idx = text.find('updateStats() {')
if idx != -1:
    with open('stats.py', 'w', encoding='utf-8') as fw:
        fw.write(text[idx:idx+2500])
