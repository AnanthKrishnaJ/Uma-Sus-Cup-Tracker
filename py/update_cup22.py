import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_participants = '''      "participants": [
        {
          "number": 17,
          "uma": "Agnes Tachyon",
          "player": "Cyclobly",
          "strategy": "Pace",
          "time": "3:13.4",
          "gap": "3:13.4",
          "pop": 1,
          "rank": "?",
          "title": "Leading the Charge",
          "umaId": "agnes-tachyon",
          "position": 1,
          "pos": 1
        },
        {
          "number": 11,
          "uma": "Oguri Cap",
          "player": "Yes",
          "strategy": "Pace",
          "time": "1 3/4 L",
          "gap": "1 3/4 L",
          "pop": 3,
          "rank": "?",
          "title": "Leading the Charge",
          "umaId": "oguri-cap",
          "position": 2,
          "pos": 2
        },
        {
          "number": 10,
          "uma": "Oguri Cap",
          "player": "Cyclobly",
          "strategy": "Pace",
          "time": "3 1/2 L",
          "gap": "3 1/2 L",
          "pop": 6,
          "rank": "?",
          "title": "Witness to Legend",
          "umaId": "oguri-cap",
          "position": 3,
          "pos": 3
        },
        {
          "number": 14,
          "uma": "Gold Ship",
          "player": "Arn",
          "strategy": "End",
          "time": "1 1/2 L",
          "gap": "1 1/2 L",
          "pop": 17,
          "rank": "?",
          "title": "The GOAT",
          "umaId": "gold-ship",
          "position": 4,
          "pos": 4
        },
        {
          "number": 2,
          "uma": "Gold Ship",
          "player": "agnes",
          "strategy": "End",
          "time": "1/2 L",
          "gap": "1/2 L",
          "pop": 7,
          "rank": "?",
          "title": "Unpredictable",
          "umaId": "gold-ship",
          "position": 5,
          "pos": 5
        },
        {
          "number": 3,
          "uma": "Admire Vega",
          "player": "GohanXGAMER",
          "strategy": "End",
          "time": "1 1/4 L",
          "gap": "1 1/4 L",
          "pop": 2,
          "rank": "?",
          "title": "Leading the Charge",
          "umaId": "admire-vega",
          "position": 6,
          "pos": 6
        },
        {
          "number": 13,
          "uma": "Oguri Cap",
          "player": "GohanXGAMER",
          "strategy": "Pace",
          "time": "4 L",
          "gap": "4 L",
          "pop": 15,
          "rank": "?",
          "title": "G1 Hunter",
          "umaId": "oguri-cap",
          "position": 7,
          "pos": 7
        },
        {
          "number": 4,
          "uma": "Narita Taishin",
          "player": "Yes",
          "strategy": "End",
          "time": "5 L",
          "gap": "5 L",
          "pop": 8,
          "rank": "?",
          "title": "Witness to Legend",
          "umaId": "narita-taishin",
          "position": 8,
          "pos": 8
        },
        {
          "number": 9,
          "uma": "Tamamo Cross",
          "player": "GohanXGAMER",
          "strategy": "End",
          "time": "2 1/2 L",
          "gap": "2 1/2 L",
          "pop": 5,
          "rank": "?",
          "title": "Now That's White Lightning!",
          "umaId": "tamamo-cross",
          "position": 9,
          "pos": 9
        },
        {
          "number": 6,
          "uma": "Mayano Top Gun",
          "player": "Yes",
          "strategy": "Front",
          "time": "2 L",
          "gap": "2 L",
          "pop": 16,
          "rank": "?",
          "title": "Finals Champion",
          "umaId": "mayano-top-gun",
          "position": 10,
          "pos": 10
        },
        {
          "number": 8,
          "uma": "Tokai Teio",
          "player": "Jinxye",
          "strategy": "Pace",
          "time": "Head",
          "gap": "Head",
          "pop": 4,
          "rank": "?",
          "title": "Monarch",
          "umaId": "tokai-teio",
          "position": 11,
          "pos": 11
        },
        {
          "number": 15,
          "uma": "T.M. Opera O",
          "player": "agnes",
          "strategy": "Pace",
          "time": "3 1/2 L",
          "gap": "3 1/2 L",
          "pop": 9,
          "rank": "?",
          "title": "Centurial Overlord",
          "umaId": "tm-opera-o",
          "position": 12,
          "pos": 12
        },
        {
          "number": 16,
          "uma": "Mejiro McQueen",
          "player": "Arn",
          "strategy": "Pace",
          "time": "3 1/2 L",
          "gap": "3 1/2 L",
          "pop": 11,
          "rank": "?",
          "title": "Product Power",
          "umaId": "mejiro-mcqueen",
          "position": 13,
          "pos": 13
        },
        {
          "number": 18,
          "uma": "Matikanefukukitaru",
          "player": "Jinxye",
          "strategy": "Late",
          "time": "5 L",
          "gap": "5 L",
          "pop": 10,
          "rank": "?",
          "title": "Team Player Star Slayer",
          "umaId": "matikanefukukitaru",
          "position": 14,
          "pos": 14
        },
        {
          "number": 12,
          "uma": "Grass Wonder",
          "player": "agnes",
          "strategy": "Late",
          "time": "Distance",
          "gap": "Distance",
          "pop": 14,
          "rank": "?",
          "title": "Finals Champion",
          "umaId": "grass-wonder",
          "position": 15,
          "pos": 15
        },
        {
          "number": 5,
          "uma": "Meisho Doto",
          "player": "Cyclobly",
          "strategy": "Pace",
          "time": "1/2 L",
          "gap": "1/2 L",
          "pop": 12,
          "rank": "?",
          "title": "Legendary Diva",
          "umaId": "meisho-doto",
          "position": 16,
          "pos": 16
        },
        {
          "number": 1,
          "uma": "Seiun Sky",
          "player": "Arn",
          "strategy": "Front",
          "time": "5 L",
          "gap": "5 L",
          "pop": 13,
          "rank": "?",
          "title": "Witness to Legend",
          "umaId": "seiun-sky",
          "position": 17,
          "pos": 17
        },
        {
          "number": 7,
          "uma": "Nice Nature",
          "player": "Jinxye",
          "strategy": "Late",
          "time": "6 L",
          "gap": "6 L",
          "pop": 18,
          "rank": "?",
          "title": "Next-Gen Grandmaster",
          "umaId": "nice-nature",
          "position": 18,
          "pos": 18
        }
      ]'''

# Find the Sus Cup 22 block
# We know it starts around id: 22
pattern_cup22 = re.compile(r'(\{\s*"id": 22,\s*"cupNumber": 22,.*?)"participants": \[(?:[^\]]|\](?!\s*,\s*"details"))*\]', re.DOTALL)
match = pattern_cup22.search(content)

if match:
    # Update race properties
    cup22_header = match.group(1)
    
    # We only change the fields requested
    cup22_header = re.sub(r'"name": ".*?"', '"name": "G1 Tenno Sho (Spring)"', cup22_header)
    cup22_header = re.sub(r'"race": ".*?"', '"race": "Tenno Sho (Spring)"', cup22_header)
    cup22_header = re.sub(r'"course": ".*?"', '"course": "Kyoto Turf Outer"', cup22_header)
    cup22_header = re.sub(r'"distance": ".*?"', '"distance": "3200m"', cup22_header)
    
    new_block = cup22_header + new_participants
    new_content = content[:match.start()] + new_block + content[match.end():]
    
    # Also update details
    # The details string for Cup 22 is right after participants
    # Find the details string in the new block context
    def details_replacer(m):
        return '"details": "Kyoto Turf Outer 3200m (Long) Right | Heavy\\nCondition: Low Stamina"'
    
    # We want to replace the FIRST "details" string after match.start() in new_content
    # Let's do it with a more specific regex:
    # Look for `"details": "..."` that is after the `participants` block we just injected
    pattern_details = re.compile(r'"details": ".*?"')
    
    # Actually just replace the one that corresponds to Sus Cup 22 
    # Let's search from where we put new_participants and replace next "details"
    start_search = match.start() + len(new_block)
    details_match = pattern_details.search(new_content, start_search)
    if details_match:
        new_content = new_content[:details_match.start()] + '"details": "Kyoto Turf Outer 3200m (Long) Right | Heavy\\nCondition: Low Stamina"' + new_content[details_match.end():]
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated Sus Cup 22.")
else:
    print("Could not find Sus Cup 22 pattern.")
