content = open('suscup1.html', 'r', encoding='utf-8').read()
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'innerHTML' in line and '<option' in line:
        print('\n'.join(lines[max(0, i-2):i+10]))
        print('---')
