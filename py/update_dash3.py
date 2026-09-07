import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix encoding artifacts
        content = content.replace('', '&mdash;')
        
        # Remove background: var(--bg-alt) if the user wanted it completely flush, but let's just keep flex: 1.
        # Actually, if I look at the screenshot, the user is likely complaining about the empty white space at the bottom of the card.
        # My flex: 1 fix should have addressed that, but let's make sure the resultsHtml div looks good.
        # Let's completely remove the grey background and padding to make it flush.
        
        content = content.replace(
            'resultsHtml = `<div style="margin-top:20px; flex: 1; overflow-y: auto; background: var(--bg-alt); padding: 10px; border-radius: 8px; min-height: 300px;">',
            'resultsHtml = `<div style="margin-top:20px; flex: 1; overflow-y: auto; min-height: 300px; padding-right: 5px;">'
        )

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Fixed encoding and removed grey background from resultsHtml.")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
