import json

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find Sus Cup 21
    idx = content.find('"cupName": "Sus Cup 21')
    idx2 = content.find('"cupName": "Sus Cup 22', idx)
    
    cup_str = content[idx:idx2]
    
    for line in cup_str.split('\n'):
        if '"player":' in line or '"uma":' in line or '"position":' in line:
            print(line.strip())

if __name__ == '__main__':
    main()
