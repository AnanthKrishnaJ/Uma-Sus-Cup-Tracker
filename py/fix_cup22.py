import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix scenarioWinners missing umaIds
# We know they are inside Sus Cup 22 block, so we target the scenarioWinners string.
scenario_winners_orig = '''      "scenarioWinners": {
        "URA Finale": {
          "player": "guest club member",
          "uma": "Gold Ship",
          "pos": 4
        },
        "Unity Cup": {
          "player": "Cyciesta",
          "uma": "Oguri Cap",
          "pos": 3
        },
        "Trackblazer": {
          "player": "Cyciesta",
          "uma": "Agnes Tachyon",
          "pos": 1
        }
      }'''

scenario_winners_fixed = '''      "scenarioWinners": {
        "URA Finale": {
          "player": "guest club member",
          "uma": "Gold Ship",
          "pos": 4,
          "umaId": "gold-ship"
        },
        "Unity Cup": {
          "player": "Cyciesta",
          "uma": "Oguri Cap",
          "pos": 3,
          "umaId": "100602-oguri-cap"
        },
        "Trackblazer": {
          "player": "Cyciesta",
          "uma": "Agnes Tachyon",
          "pos": 1,
          "umaId": "agnes-tachyon"
        }
      }'''

content = content.replace(scenario_winners_orig, scenario_winners_fixed)

# Now fix the participants IDs
# 2nd Place Oguri Cap
content = re.sub(
    r'("player": "Yes",\s*"strategy": "Pace",\s*"time": "1 3/4 L",.*?)"umaId": "oguri-cap"',
    r'\1"umaId": "100602-oguri-cap"',
    content, count=1, flags=re.DOTALL
)

# 3rd Place Oguri Cap
content = re.sub(
    r'("player": "Cyclobly",\s*"strategy": "Pace",\s*"time": "3 1/2 L",.*?)"umaId": "oguri-cap"',
    r'\1"umaId": "100602-oguri-cap"',
    content, count=1, flags=re.DOTALL
)

# 11th Place Tokai Teio (player Jinxye)
content = re.sub(
    r'("player": "Jinxye",\s*"strategy": "Pace",\s*"time": "Head",.*?)"umaId": "tokai-teio"',
    r'\1"umaId": "100302-tokai-teio"',
    content, count=1, flags=re.DOTALL
)

# 13th Place Mejiro McQueen (player Arn)
content = re.sub(
    r'("player": "Arn",\s*"strategy": "Pace",\s*"time": "3 1/2 L",.*?)"umaId": "mejiro-mcqueen"',
    r'\1"umaId": "101302-mejiro-mcqueen"',
    content, count=1, flags=re.DOTALL
)

# 14th Place Matikanefukukitaru (player Jinxye)
content = re.sub(
    r'("player": "Jinxye",\s*"strategy": "Late",\s*"time": "5 L",.*?)"umaId": "matikanefukukitaru"',
    r'\1"umaId": "105602-matikanefukukitaru"',
    content, count=1, flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed IDs and scenarioWinners.")
