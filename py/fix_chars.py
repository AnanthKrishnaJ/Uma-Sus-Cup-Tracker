import sys
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace the diamond question mark character.
    # The diamond question mark is U+FFFD
    print('U+FFFD count:', content.count('\uFFFD'))
    print('em dash count:', content.count('\u2014'))

    content = content.replace('\uFFFD', '&mdash;')
    
    # Let's also fix the styling issue for the race results container.
    # We want to remove background: var(--bg-alt); padding: 10px; border-radius: 8px;
    import re
    old_div = r'resultsHtml = `<div style="margin-top:20px; flex: 1; overflow-y: auto; background: var\(--bg-alt\); padding: 10px; border-radius: 8px; min-height: 300px;">'
    new_div = r'resultsHtml = `<div style="margin-top:20px; flex: 1; overflow-y: auto; min-height: 300px; padding-right: 5px;">'
    
    content = re.sub(old_div, new_div, content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print('Done.')
except Exception as e:
    print('Error:', e)
