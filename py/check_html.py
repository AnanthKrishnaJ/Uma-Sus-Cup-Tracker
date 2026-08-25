with open(r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html', 'r', encoding='utf-8') as f:
    html = f.read()
idx = html.find('id="latest-cup-summary"')
start = max(0, idx-500)
end = min(len(html), idx+2000)
print(html[start:end])
