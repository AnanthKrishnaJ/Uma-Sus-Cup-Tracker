import json

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    cups_idx = content.find('"cups": [')

    for cup_id in [21, 22, 23, 24]:
        idx = content.find(f'"id": {cup_id},', cups_idx)
        if idx == -1: continue
        
        part_idx = content.find('"participants": [', idx)
        if part_idx == -1: continue
        
        chunk = content[part_idx:part_idx+300]
        print(f'\\n--- Cup {cup_id} ---')
        print('\\n'.join(chunk.split('\\n')[:15]))

if __name__ == '__main__':
    main()
