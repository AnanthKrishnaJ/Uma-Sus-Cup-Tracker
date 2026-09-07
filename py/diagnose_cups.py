import json

def check_cups():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    for cup_num in [11, 21, 22, 23, 24]:
        idx = content.find(f'"cupName": "Sus Cup {cup_num}')
        if idx == -1:
            print(f"Cup {cup_num} not found!")
            continue
            
        end_idx = content.find('"id":', idx)
        if end_idx == -1:
            end_idx = content.find(']', idx) # just roughly find end of object
            
        cup_str = content[idx:end_idx]
        
        pos1_idx = cup_str.find('"position": 1\n')
        if pos1_idx == -1:
            pos1_idx = cup_str.find('"position": 1\r')
            if pos1_idx == -1:
                pos1_idx = cup_str.find('"position": 1')
        
        if pos1_idx != -1:
            # find player around pos1
            start_pos = max(0, pos1_idx - 150)
            chunk = cup_str[start_pos:pos1_idx+20]
            player = ""
            uma = ""
            for line in chunk.split('\n'):
                if '"player":' in line:
                    player = line.strip()
                if '"uma":' in line:
                    uma = line.strip()
            print(f"Cup {cup_num} 1st place: {player}, {uma}")
        else:
            print(f"Cup {cup_num}: No position 1 found!")

if __name__ == '__main__':
    check_cups()
