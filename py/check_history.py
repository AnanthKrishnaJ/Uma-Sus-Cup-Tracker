import json

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    cup_starts = []
    
    for i, line in enumerate(lines):
        if '"id":' in line and 'cupNumber' in lines[i+1]:
            try:
                cup_id = int(line.split(':')[1].strip().strip(','))
                cup_name = lines[i+2].split(':')[1].strip().strip('",')
                print(f"Found Cup: id={cup_id}, name={cup_name}")
            except Exception as e:
                pass

if __name__ == '__main__':
    main()
