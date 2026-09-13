import json
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const INITIAL_DATA = ')
end = text.find('const NPC_PROFILES = {};')
data_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(data_str)

race_29 = next(r for r in data['races'] if r['id'] == '29')
race_29['cupName'] = 'Sus Cup 29 - RGB Race' # Fix emdash if any

for p in race_29['participants']:
    if p['uma'] == 'Nice Nature' and p['player'] == 'Cruzi':
        p['umaId'] = '106001'
        p['version'] = 'Standard / Original'
    elif p['uma'] == 'Eishin Flash' and p['player'] == 'Ananth':
        p['umaId'] = '103701'
        p['version'] = 'Standard / Original'
    elif p['uma'] == 'Mejiro McQueen' and p['player'] == 'agnes':
        p['umaId'] = '101301'
        p['version'] = 'Standard / Original'
    elif p['uma'] == 'Maruzensky' and p['player'] == 'Ananth':
        p['umaId'] = '100401'
        p['version'] = 'Standard / Original'

new_json = json.dumps(data, indent=4, ensure_ascii=False)
new_text = text[:start + 21] + new_json + '\n        ' + text[end:]

# Now remove the upcoming race HTML
# We look for a <div class="..."> that contains "Upcoming Race Schedule"
# Since it might be multiple lines, let's use regex
# We want to remove the block from <div class="content-block hero-block" (or similar)
# to the end of that block.
match = re.search(r'\<div class=\"content-block hero-block\"[^\>]*\>[\s\r\n]*\<div class=\"record-heading\"\>[\s\r\n]*\<span class=\"eyebrow\"\>Upcoming Race Schedule(.*?)\</div\>[\s\r\n]*\</div\>[\s\r\n]*\</div\>', new_text, re.DOTALL | re.IGNORECASE)

if match:
    new_text = new_text[:match.start()] + new_text[match.end():]
    print("Upcoming race block removed.")
else:
    # Try a broader search if the class is different
    match2 = re.search(r'\<div [^\>]*\>[\s\r\n]*\<div class=\"record-heading\"\>[\s\r\n]*\<span class=\"eyebrow\"\>Upcoming Race Schedule.*?\</div\>[\s\r\n]*\</div\>[\s\r\n]*\</div\>[\s\r\n]*\</div\>', new_text, re.DOTALL | re.IGNORECASE)
    if match2:
        new_text = new_text[:match2.start()] + new_text[match2.end():]
        print("Upcoming race block removed using broader search.")
    else:
        # Fallback to remove based on known string
        idx = new_text.find('<span class="eyebrow">Upcoming Race Schedule</span>')
        if idx != -1:
            start_div = new_text.rfind('<div', 0, idx)
            end_div = new_text.find('</div>', idx)
            end_div = new_text.find('</div>', end_div + 1)
            end_div = new_text.find('</div>', end_div + 1)
            
            # Walk backwards from start_div until we hit the parent container
            # This is a bit risky but we know the structure usually has a container
            parent_start = new_text.rfind('<div class="content-block', 0, idx)
            if parent_start != -1:
                # find the closing div of parent_start
                # just counting divs
                count = 1
                pos = parent_start + 4
                while count > 0 and pos < len(new_text):
                    next_open = new_text.find('<div', pos)
                    next_close = new_text.find('</div', pos)
                    if next_close == -1:
                        break
                    if next_open != -1 and next_open < next_close:
                        count += 1
                        pos = next_open + 4
                    else:
                        count -= 1
                        pos = next_close + 5
                
                new_text = new_text[:parent_start] + new_text[pos:]
                print("Upcoming race block removed using div counting.")
        else:
            print("Could not find Upcoming Race Schedule")


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Fixes applied successfully!")
