content = open('suscup1.html', 'r', encoding='utf-8').read()
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'document.createElement' in line and "'option'" in line:
        print('\n'.join(lines[max(0, i-5):i+15]))
        break
