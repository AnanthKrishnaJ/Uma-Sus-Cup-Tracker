import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = "const INITIAL_DATA ="
start_idx = html.find(start_marker)
start_idx += len(start_marker)
while html[start_idx] != '{': start_idx += 1

stack = []
end_idx = -1
for i in range(start_idx, len(html)):
    if html[i] == '{': stack.append('{')
    elif html[i] == '}':
        stack.pop()
        if not stack:
            end_idx = i + 1
            break

json_str = html[start_idx:end_idx]
json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)
data = json.loads(json_str)

cup16_ranks = {1: ("Vodka", "A+"), 2: ("Oguri Cap", "A+"), 3: ("Silence Suzuka", "A"), 4: ("Oguri Cap", "B+"), 5: ("Hishi Amazon", "A"), 6: ("El Condor Pasa", "B+"), 7: ("Silence Suzuka", "A+"), 8: ("Sakura Bakushin O", "B+"), 9: ("Narita Brian", "A+"), 10: ("Silence Suzuka", "B+"), 11: ("Book of Sugar", "B"), 12: ("El Condor Pasa", "A"), 13: ("Grass Wonder", "B+"), 14: ("Smart Falcon", "A+"), 15: ("Pan Pacific", "B"), 16: ("Grass Wonder", "A"), 17: ("Maruzensky", "A"), 18: ("Mihono Bourbon", "B+")}
cup17_ranks = {1: ("Symboli Rudolf", "A"), 2: ("Agnes Digital", "A+"), 3: ("Grass Wonder", "A+"), 4: ("T.M. Opera O", "A+"), 5: ("Oguri Cap", "A+"), 6: ("Narita Brian", "A"), 7: ("Nice Nature", "A"), 8: ("Oguri Cap", "A+"), 9: ("Silence Suzuka", "A+"), 10: ("Seiun Sky", "A+"), 11: ("Tokai Teio", "A"), 12: ("Agnes Digital", "A+"), 13: ("Grass Wonder", "A+"), 14: ("Shadow Stalker", "B"), 15: ("Gold Chouchou", "B"), 16: ("Nice Nature", "A"), 17: ("Mayano Top Gun", "A"), 18: ("Frozen Sky", "B")}
cup18_ranks = {1: ("Nice Nature", "A"), 2: ("Nice Nature", "A"), 3: ("Nice Nature", "A"), 4: ("Gold Ship", "A+"), 5: ("Winning Ticket", "A"), 6: ("T.M. Opera O", "A+"), 7: ("Matikane Fukukitaru", "A+"), 8: ("Mayano Top Gun", "A+"), 9: ("Mayano Top Gun", "A"), 10: ("Biwa Hayahide", "A"), 11: ("Agnes Tachyon", "A+"), 12: ("Symboli Rudolf", "A"), 13: ("Torch and Book", "B"), 14: ("Set Your Record", "B"), 15: ("Grass Wonder", "A"), 16: ("Breeze Glider", "B"), 17: ("Symboli Rudolf", "A"), 18: ("Out of Black", "B")}
cup19_ranks = {1: ("Gold City", "A+"), 2: ("T.M. Opera O", "A+"), 3: ("Agnes Tachyon", "A+"), 4: ("Gold Ship", "A+"), 5: ("Gold Ship", "A"), 6: ("Gold Ship", "A+"), 7: ("Mayano Top Gun", "A+"), 8: ("Oguri Cap", "A+"), 9: ("Daiwa Scarlet", "A+"), 10: ("Seiun Sky", "A+"), 11: ("Winning Ticket", "A"), 12: ("Mejiro McQueen", "A"), 13: ("Gray Chouchou", "C+"), 14: ("Jagdplaute", "C+"), 15: ("Mini Narcissus", "C+"), 16: ("Turcke", "C+"), 17: ("Gran Shamal", "C+"), 18: ("Circuit Breaker", "C+")}
cup20_ranks = {1: ("Mejiro McQueen", "A+"), 2: ("Eishin Flash", "A+"), 3: ("Mayano Top Gun", "A+"), 4: ("Agnes Digital", "A+"), 5: ("Narita Taishin", "S"), 6: ("Gold City", "A+"), 7: ("Symboli Rudolf", "S"), 8: ("Agnes Tachyon", "A+"), 9: ("Mejiro Ryan", "A+"), 10: ("Gold Ship", "A+"), 11: ("Mihono Bourbon", "A+"), 12: ("Meisho Doto", "A+"), 13: ("King Halo", "A+"), 14: ("Silence Suzuka", "A+"), 15: ("Seiun Sky", "A+"), 16: ("Neptunus", "B"), 17: ("Maleficus", "B"), 18: ("Ribbon Virelai", "B")}

def update_race(race, ranks_dict):
    p_dict = {}
    for p in race['participants']:
        pos = p.get('pos', p.get('position', None))
        if pos is not None:
            if pos not in p_dict: p_dict[pos] = []
            p_dict[pos].append(p)
            
    new_participants = []
    
    for pos in range(1, 19):
        if pos in ranks_dict:
            target_uma, target_rank = ranks_dict[pos]
            found_p = None
            if pos in p_dict:
                for p in p_dict[pos]:
                    if p['uma'].strip() == target_uma.strip():
                        found_p = p
                        break
                if not found_p and len(p_dict[pos]) > 0:
                    found_p = p_dict[pos].pop(0) # take the first one available
            
            if found_p:
                found_p['uma'] = target_uma
                found_p['rank'] = target_rank
                if 'NPC' in found_p.get('player', '') or found_p.get('participantType') == 'NPC Uma':
                    found_p['umaId'] = target_uma.lower().replace(' ', '-')
                new_participants.append(found_p)
            else:
                new_p = {
                    "pos": pos,
                    "uma": target_uma,
                    "umaId": target_uma.lower().replace(' ', '-'),
                    "player": "NPC" if "Chouchou" in target_uma or target_uma in ["Jagdplaute", "Mini Narcissus", "Turcke", "Gran Shamal", "Circuit Breaker", "Neptunus", "Maleficus", "Ribbon Virelai", "Torch and Book", "Set Your Record", "Breeze Glider", "Out of Black", "Shadow Stalker", "Gold Chouchou", "Frozen Sky", "Book of Sugar", "Pan Pacific"] else "Unknown",
                    "number": pos,
                    "rank": target_rank,
                    "title": "-",
                    "strategy": "Unknown",
                    "gap": "",
                    "pop": 18
                }
                new_participants.append(new_p)
    
    race['participants'] = new_participants

    # Build 3 winners if requested (Cup 17 to 20)
    cup_num = race.get('cupNumber', -1)
    if not cup_num and 'cupName' in race and 'Sus Cup' in race['cupName']:
        try: cup_num = int(race['cupName'].replace('Sus Cup', '').strip().split()[0])
        except: pass
        
    if cup_num in [17, 18, 19, 20]:
        winners = {}
        sorted_p = sorted(new_participants, key=lambda x: x.get('pos', x.get('position', 99)))
        for i, place in enumerate(["1st Place", "2nd Place", "3rd Place"]):
            if i < len(sorted_p):
                p = sorted_p[i]
                winners[place] = {
                    "player": p.get('player'),
                    "uma": p.get('uma'),
                    "pos": p.get('pos', p.get('position'))
                }
        race['scenarioWinners'] = winners

for race in data['races']:
    cup_num = race.get('cupNumber', -1)
    if not cup_num and 'cupName' in race and 'Sus Cup' in race['cupName']:
        try: cup_num = int(race['cupName'].replace('Sus Cup', '').strip().split()[0])
        except: pass
            
    if cup_num == 16: update_race(race, cup16_ranks)
    elif cup_num == 17: update_race(race, cup17_ranks)
    elif cup_num == 18: update_race(race, cup18_ranks)
    elif cup_num == 19: update_race(race, cup19_ranks)
    elif cup_num == 20: update_race(race, cup20_ranks)

new_json_str = json.dumps(data, indent=2)
new_html = html[:start_idx] + new_json_str + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Saved directly to index.html")
