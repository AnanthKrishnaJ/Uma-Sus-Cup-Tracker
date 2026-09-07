import json

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    cups_idx = content.find('"cups": [')
    
    # We will use regex to find all cups and write their participants out
    import re
    # Match the whole cup object roughly
    matches = re.finditer(r'{\s*"id": (\d+),[\s\S]*?(?=\n    {\s*"id": \d+|$)', content[cups_idx:])
    
    for match in matches:
        cup_id = int(match.group(1))
        if cup_id in [21, 22, 23, 24]:
            cup_str = match.group(0)
            part_idx = cup_str.find('"participants": [')
            if part_idx != -1:
                # Find end of participants array
                end_part = cup_str.find('    }', part_idx)
                participants_str = cup_str[part_idx:end_part]
                with open(f'cup_{cup_id}_participants.txt', 'w', encoding='utf-8') as out:
                    out.write(participants_str)

if __name__ == '__main__':
    main()
