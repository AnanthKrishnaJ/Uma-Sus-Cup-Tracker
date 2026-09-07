import re
text = open('index.html', encoding='utf-8').read()
cups = re.findall(r'"id"\s*:\s*(\d+)[\s\S]*?"cupName"\s*:\s*"([^"]+)"', text)
for c in cups:
    print(c[0], c[1])
