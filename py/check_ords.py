import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match1 = re.search(r'<p style="font-weight:800.*?Not recorded.*?</p>', content, re.DOTALL)
if match1:
    s = match1.group(0)
    for c in s:
        if ord(c) > 127:
            print(f'Char: {repr(c)}, ord: {ord(c)}')
