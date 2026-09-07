import json

def find_lines():
    with open('index.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if '"cupName": "Sus Cup 21' in line:
            print(f"Cup 21 at line {i}")
        if '"cupName": "Sus Cup 22' in line:
            print(f"Cup 22 at line {i}")
        if '"cupName": "Sus Cup 23' in line:
            print(f"Cup 23 at line {i}")
        if '"cupName": "Sus Cup 24' in line:
            print(f"Cup 24 at line {i}")

if __name__ == '__main__':
    find_lines()
