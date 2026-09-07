import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Remove duplicate Cup 11 from winners array
        w_start = content.find('"winners": [')
        w_end = content.find('],\n  "cups": [', w_start)
        if w_end == -1:
             w_end = content.find(']\n  "cups": [', w_start)
        
        winners_str = content[w_start:w_end]
        
        # There are 2 identical blocks of Cyciesta / Narita Taishin
        block_regex = r'(\{\s*"cup": "Sus Cup 11",\s*"trainer": "Cyciesta",\s*"uma": "Narita Taishin",[\s\S]*?"result": "2:21\.4"\s*\})'
        
        matches = list(re.finditer(block_regex, winners_str))
        if len(matches) >= 2:
            # We want to remove the second match, including its preceding comma if possible
            # Actually, let's just find the exact string of the block and replace two with one
            block_str = matches[0].group(1)
            double_block = block_str + ",\n    " + block_str
            if double_block in winners_str:
                winners_str = winners_str.replace(double_block, block_str)
            else:
                double_block2 = block_str + ",\r\n    " + block_str
                winners_str = winners_str.replace(double_block2, block_str)
                
            content = content[:w_start] + winners_str + content[w_end:]
            print("Fixed duplicate Cup 11 winner.")
        else:
            print(f"Could not find duplicate blocks for Cup 11. Matches found: {len(matches)}")
            
        # 2. Fix cupNumber for Cup 21
        content = content.replace(
            '"id": 21,\n      "cupNumber": 22,',
            '"id": 21,\n      "cupNumber": 21,'
        )
        content = content.replace(
            '"id": 21,\r\n      "cupNumber": 22,',
            '"id": 21,\r\n      "cupNumber": 21,'
        )

        # 3. Fix cupNumber for Cup 23
        content = content.replace(
            '"id": 23,\n      "cupNumber": 24,',
            '"id": 23,\n      "cupNumber": 23,'
        )
        content = content.replace(
            '"id": 23,\r\n      "cupNumber": 24,',
            '"id": 23,\r\n      "cupNumber": 23,'
        )
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Data fixed successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
