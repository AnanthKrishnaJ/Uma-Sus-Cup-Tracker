import re

def modify_file():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix Cup 22 Gold Ship
        content = content.replace(
            '"uma": "Gold Ship",\n      "rankLabel": "URA Finale scenario winner"',
            '"uma": "Gold Ship",\n      "umaId": "gold-ship",\n      "rankLabel": "URA Finale scenario winner"'
        )
        
        # Fix Cup 22 Oguri Cap
        content = content.replace(
            '"uma": "Oguri Cap",\n      "rankLabel": "Unity Cup scenario winner"',
            '"uma": "Oguri Cap",\n      "umaId": "oguri-cap",\n      "rankLabel": "Unity Cup scenario winner"'
        )
        
        # Fix Cup 22 Agnes Tachyon
        content = content.replace(
            '"uma": "Agnes Tachyon",\n      "rankLabel": "Trackblazer scenario winner"',
            '"uma": "Agnes Tachyon",\n      "umaId": "agnes-tachyon",\n      "rankLabel": "Trackblazer scenario winner"'
        )
        
        # Fix Cup 23 Narita Taishin
        content = content.replace(
            '"uma": "Narita Taishin",\n      "rankLabel": "3* winner"',
            '"uma": "Narita Taishin",\n      "umaId": "narita-taishin",\n      "rankLabel": "3* winner"'
        )
        
        # Fix Cup 23 Air Groove
        content = content.replace(
            '"uma": "Air Groove",\n      "rankLabel": "2* winner"',
            '"uma": "Air Groove",\n      "umaId": "air-groove",\n      "rankLabel": "2* winner"'
        )
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Data fixed for Cup 22 and 23!")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    modify_file()
