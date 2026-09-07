import json

def check_22():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_str = '"cupName": "Sus Cup 22'
    idx = content.find(start_str)
    
    if idx != -1:
        start_line = content[:idx].count('\n')
        lines = content.split('\n')
        
        # print 150 lines starting slightly before
        for i in range(max(0, start_line - 5), min(len(lines), start_line + 150)):
            print(f"{i}: {lines[i]}")

if __name__ == '__main__':
    check_22()
