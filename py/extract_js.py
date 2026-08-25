from bs4 import BeautifulSoup

with open('suscup1.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

scripts = soup.find_all('script')
with open('extracted.js', 'w', encoding='utf-8') as f:
    for s in scripts:
        if s.string:
            f.write(s.string)
            f.write('\n')

print("Extracted JS.")
