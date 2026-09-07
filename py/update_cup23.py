import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the Sus Cup 23 object and replace its participants array.
cup_23_index = content.find('"cupName": "Sus Cup 23')

if cup_23_index == -1:
    print("Could not find Sus Cup 23 block.")
    exit(1)

# Now we need to find the end of the participants array.
bracket_match = re.search(r'"participants":\s*\[', content[cup_23_index:])
if not bracket_match:
    print("Could not find participants array start.")
    exit(1)

arr_start = cup_23_index + bracket_match.end() - 1

# find matching closing bracket
bracket_count = 1
arr_end = -1
for i, char in enumerate(content[arr_start+1:], start=arr_start+1):
    if char == '[':
        bracket_count += 1
    elif char == ']':
        bracket_count -= 1
        if bracket_count == 0:
            arr_end = i
            break

if arr_end == -1:
    print("Could not find end of participants array.")
    exit(1)


new_participants = [
        {
          "number": 16,
          "uma": "Narita Taishin",
          "player": "Jiinxye",
          "strategy": "End",
          "time": "1:56.1",
          "gap": "1:56.1",
          "pop": 17,
          "rank": "SS",
          "title": "Phenomenal",
          "umaId": "narita-taishin",
          "pos": 1
        },
        {
          "number": 18,
          "uma": "Agnes Tachyon",
          "player": "Shadow Amber",
          "strategy": "Pace",
          "time": "1 L",
          "gap": "1 L",
          "pop": 8,
          "rank": "S",
          "title": "Leading the Charge",
          "umaId": "agnes-tachyon",
          "pos": 2
        },
        {
          "number": 5,
          "uma": "Mihono Bourbon",
          "player": "Cruzi",
          "strategy": "Front",
          "time": "Head",
          "gap": "Head",
          "pop": 11,
          "rank": "SS",
          "title": "Leading the Charge",
          "umaId": "mihono-bourbon",
          "pos": 3
        },
        {
          "number": 1,
          "uma": "King Halo",
          "player": "agnes",
          "strategy": "Late",
          "time": "Head",
          "gap": "Head",
          "pop": 7,
          "rank": "S+",
          "title": "Goddess",
          "umaId": "king-halo",
          "pos": 4
        },
        {
          "number": 9,
          "uma": "Nice Nature",
          "player": "Cyclobly",
          "strategy": "Late",
          "time": "1 1/2 L",
          "gap": "1 1/2 L",
          "pop": 3,
          "rank": "SS",
          "title": "Leading the Charge",
          "umaId": "nice-nature",
          "pos": 5
        },
        {
          "number": 6,
          "uma": "Agnes Tachyon",
          "player": "Cruzi",
          "strategy": "Pace",
          "time": "Head",
          "gap": "Head",
          "pop": 5,
          "rank": "S+",
          "title": "Leading the Charge",
          "umaId": "agnes-tachyon",
          "pos": 6
        },
        {
          "number": 10,
          "uma": "T.M. Opera O",
          "player": "agnes",
          "strategy": "Pace",
          "time": "Nose",
          "gap": "Nose",
          "pop": 1,
          "rank": "S+",
          "title": "Centurial Overlord",
          "umaId": "tm-opera-o",
          "pos": 7
        },
        {
          "number": 13,
          "uma": "Oguri Cap",
          "player": "Shadow Amber",
          "strategy": "Pace",
          "time": "Nose",
          "gap": "Nose",
          "pop": 6,
          "rank": "S",
          "title": "Ideal Idol",
          "umaId": "oguri-cap",
          "pos": 8
        },
        {
          "number": 12,
          "uma": "Air Groove",
          "player": "agnes",
          "strategy": "Late",
          "time": "Head",
          "gap": "Head",
          "pop": 16,
          "rank": "S",
          "title": "Empress",
          "umaId": "air-groove",
          "pos": 9
        },
        {
          "number": 4,
          "uma": "Eishin Flash",
          "player": "Ananth",
          "strategy": "Pace",
          "time": "1 L",
          "gap": "1 L",
          "pop": 13,
          "rank": "SS",
          "title": "Leading the Charge",
          "umaId": "eishin-flash",
          "pos": 10
        },
        {
          "number": 11,
          "uma": "Gold Ship",
          "player": "Cruzi",
          "strategy": "End",
          "time": "3/4 L",
          "gap": "3/4 L",
          "pop": 9,
          "rank": "S",
          "title": "Unpredictable",
          "umaId": "gold-ship",
          "pos": 11
        },
        {
          "number": 14,
          "uma": "Vodka",
          "player": "Jiinxye",
          "strategy": "Late",
          "time": "Neck",
          "gap": "Neck",
          "pop": 10,
          "rank": "S",
          "title": "Goddess",
          "umaId": "vodka",
          "pos": 12
        },
        {
          "number": 7,
          "uma": "Oguri Cap",
          "player": "Cyclobly",
          "strategy": "Pace",
          "time": "1/2 L",
          "gap": "1/2 L",
          "pop": 4,
          "rank": "SS",
          "title": "Leading the Charge",
          "umaId": "oguri-cap",
          "pos": 13
        },
        {
          "number": 15,
          "uma": "Grass Wonder",
          "player": "Cyclobly",
          "strategy": "Late",
          "time": "Nose",
          "gap": "Nose",
          "pop": 2,
          "rank": "SS",
          "title": "Leading the Charge",
          "umaId": "grass-wonder",
          "pos": 14
        },
        {
          "number": 8,
          "uma": "Mejiro Ryan",
          "player": "Haji",
          "strategy": "Late",
          "time": "1/2 L",
          "gap": "1/2 L",
          "pop": 12,
          "rank": "A+",
          "title": "Mesmerizing Muscle",
          "umaId": "mejiro-ryan",
          "pos": 15
        },
        {
          "number": 17,
          "uma": "Winning Ticket",
          "player": "Jiinxye",
          "strategy": "Late",
          "time": "3/4 L",
          "gap": "3/4 L",
          "pop": 14,
          "rank": "S",
          "title": "Herald of a New Age",
          "umaId": "winning-ticket",
          "pos": 16
        },
        {
          "number": 3,
          "uma": "Special Week",
          "player": "Haji",
          "strategy": "Pace",
          "time": "1 3/4 L",
          "gap": "1 3/4 L",
          "pop": 15,
          "rank": "S",
          "title": "Leading the Charge",
          "umaId": "special-week",
          "pos": 17
        },
        {
          "number": 2,
          "uma": "Super Creek",
          "player": "Haji",
          "strategy": "Pace",
          "time": "1 1/4 L",
          "gap": "1 1/4 L",
          "pop": 18,
          "rank": "A+",
          "title": "Legendary Diva",
          "umaId": "super-creek",
          "pos": 18
        }
]

new_participants_json = "[\n"
for i, p in enumerate(new_participants):
    p_str = json.dumps(p, indent=10)
    p_str = p_str.replace("{\n", "{\n")
    lines = p_str.split('\n')
    formatted = "        {\n"
    for line in lines[1:-1]:
        formatted += "  " + line + "\n"
    formatted += "        }"
    
    new_participants_json += formatted
    if i < len(new_participants) - 1:
        new_participants_json += ",\n"
    else:
        new_participants_json += "\n"
new_participants_json += "      ]"

new_content = content[:arr_start] + new_participants_json + content[arr_end+1:]

new_content = new_content.replace('"course": "Nakayama Turf",', '"course": "Nakayama Turf Inner",')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated Sus Cup 23 participants")
