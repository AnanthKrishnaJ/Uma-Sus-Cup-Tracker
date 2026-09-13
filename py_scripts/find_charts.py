import re

text = open('index.html', encoding='utf-8').read()
for match in re.finditer(r'new Chart', text):
    start = max(0, match.start() - 100)
    end = min(len(text), match.end() + 200)
    print("MATCH AT LINE", text[:match.start()].count('\n'))
    print(text[start:end])
    print("-" * 50)
