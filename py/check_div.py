import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'resultsHtml = `<div style="margin-top:20px;[^>]+>', content)
if match:
    print(match.group(0))
