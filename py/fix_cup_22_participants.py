import json
import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix scenarioWinners URA Finale player
        content = content.replace(
            '"URA Finale": {\n          "player": "ARN",\n          "uma": "Gold Ship",\n          "pos": 4\n        }',
            '"URA Finale": {\n          "player": "guest club member",\n          "uma": "Gold Ship",\n          "pos": 4\n        }'
        )

        # We need to replace the specific participants in Sus Cup 22.
        # Find Sus Cup 22 boundaries
        idx = content.find('"cupName": "Sus Cup 22')
        end_idx = content.find('"cupName": "Sus Cup 23', idx)
        
        cup_str = content[idx:end_idx]
        
        # Replace pos 1
        cup_str = re.sub(
            r'"uma": "Mejiro Dober",(\s*)"player": "jayeative",([\s\S]*?)"umaId": "mejiro-dober",(\s*)"position": 1',
            r'"uma": "Agnes Tachyon",\1"player": "Cyciesta",\2"umaId": "agnes-tachyon",\3"position": 1',
            cup_str
        )
        
        # Replace pos 3
        cup_str = re.sub(
            r'"uma": "Maruzensky",(\s*)"player": "Vilthaar",([\s\S]*?)"umaId": "maruzensky",(\s*)"position": 3',
            r'"uma": "Oguri Cap",\1"player": "Cyciesta",\2"umaId": "oguri-cap",\3"position": 3',
            cup_str
        )
        
        # Replace pos 4
        cup_str = re.sub(
            r'"uma": "Admire Vega",(\s*)"player": "GohanXGAMER",([\s\S]*?)"umaId": "admire-vega",(\s*)"position": 4',
            r'"uma": "Gold Ship",\1"player": "guest club member",\2"umaId": "gold-ship",\3"position": 4',
            cup_str
        )
        
        content = content[:idx] + cup_str + content[end_idx:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Sus Cup 22 data fixed!")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
