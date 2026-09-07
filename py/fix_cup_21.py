import re

def modify_file():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix Cup 21 Curren Chan
        content = content.replace(
            '"uma": "Curren Chan",\n      "rankLabel": "3* spark winner"',
            '"uma": "Curren Chan",\n      "umaId": "curren-chan",\n      "rankLabel": "3* spark winner"'
        )
        
        # Fix Cup 21 Taiki Shuttle
        content = content.replace(
            '"uma": "Taiki Shuttle",\n      "rankLabel": "2* spark winner"',
            '"uma": "Taiki Shuttle",\n      "umaId": "taiki-shuttle",\n      "rankLabel": "2* spark winner"'
        )
        
        # Fix Cup 21 Sakura Bakushin O
        content = content.replace(
            '"uma": "Sakura Bakushin O",\n      "rankLabel": "1* spark winner"',
            '"uma": "Sakura Bakushin O",\n      "umaId": "sakura-bakushin-o",\n      "rankLabel": "1* spark winner"'
        )
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Data fixed for Cup 21!")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    modify_file()
