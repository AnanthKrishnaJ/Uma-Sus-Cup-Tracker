content = open('suscup1.html', 'r', encoding='utf-8').read()
start = content.find('<script>')
end = content.find('</script>')
while start != -1:
    with open('extracted.js', 'a', encoding='utf-8') as f:
        f.write(content[start+8:end])
        f.write('\n')
    start = content.find('<script>', end)
    end = content.find('</script>', start)
print("Extracted JS.")
