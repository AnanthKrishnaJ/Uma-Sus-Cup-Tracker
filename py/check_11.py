import json
import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    idx = content.find('"winners": [')
    end_idx = content.find('],\n  "cups": [', idx)
    winners_str = content[idx:end_idx]
    
    count_11 = winners_str.count('"Sus Cup 11"')
    print(f'Sus Cup 11 appears {count_11} times in winners array')
    
    lines = winners_str.split('\n')
    for i, line in enumerate(lines):
        if '"Sus Cup 11"' in line:
            print(''.join(lines[max(0, i-1):i+10]))

if __name__ == '__main__':
    main()
