import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

match = re.search(r"const INITIAL_DATA = (\{[\s\S]*?\});", html)
if match:
    s = match.group(1)
    print("Match length:", len(s))
    print("End of string:")
    print(s[-200:])
else:
    print("No match")
