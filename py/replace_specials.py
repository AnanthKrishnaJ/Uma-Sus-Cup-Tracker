import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # We will replace the entire block from Sus Cup 17 to Sus Cup 20
        # First, find where Sus Cup 17 rankLabel="Triple Guts Winner" starts
        
        # We can just manually construct the replacement string using regex
        
        # Let's replace the whole chunk of Cup 17, 18, 19, 20 winners with the new formatted ones
        # I'll find all the winners using regex, parse them, modify them, and dump back
        
        start_str = '"winners": ['
        start_idx = content.find(start_str)
        
        end_str = '],\n  "cups": ['
        end_idx = content.find(end_str)
        if end_idx == -1:
             end_str = ']\n  "cups": ['
             end_idx = content.find(end_str)
             if end_idx == -1:
                 # let's just find "cups": [ and step back
                 c_idx = content.find('"cups": [')
                 end_idx = content.rfind(']', start_idx, c_idx)
                 
        winners_str = content[start_idx + len('"winners": '):end_idx + 1].strip()
        
        # because the string may have trailing commas inside or something, let's use a dirty hack or just regex
        
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
