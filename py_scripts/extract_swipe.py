with open('script_0.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('// Swipe and Gallery logic')
# find end of script tag
end = text.find('</script>', start)

with open('full_swipe_logic.txt', 'w', encoding='utf-8') as out:
    out.write(text[start:end])
