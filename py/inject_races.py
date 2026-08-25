import json
import add_suscup6
import add_suscup11

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

def inject_race(content, race_obj):
    # Formats the race object nicely and injects it at the top of INITIAL_DATA.races
    race_json = json.dumps(race_obj, indent=4)
    # Add 4 spaces to each line to make it 8 spaces total
    formatted_lines = []
    for line in race_json.split('\n'):
        if line == '{' or line == '}':
            formatted_lines.append('        ' + line)
        else:
            formatted_lines.append('        ' + line)
    
    formatted_str = '\n'.join(formatted_lines) + ',\n'
    
    races_idx = content.find('"races": [\n        {')
    if races_idx == -1:
        print("Could not find 'races: [' pattern")
        return content
    
    # We want to insert right after '"races": ['
    insert_pos = content.find('[', races_idx) + 1
    content = content[:insert_pos] + '\n' + formatted_str + content[insert_pos:]
    return content

def inject_winner(content, winner_obj):
    winner_json = json.dumps(winner_obj, indent=4)
    formatted_lines = []
    for line in winner_json.split('\n'):
        if line == '{' or line == '}':
            formatted_lines.append('        ' + line)
        else:
            formatted_lines.append('        ' + line)
            
    formatted_str = '\n'.join(formatted_lines) + ',\n'
    
    winners_idx = content.find('winners: [')
    if winners_idx == -1:
        winners_idx = content.find('"winners": [')
        
    insert_pos = content.find('[', winners_idx) + 1
    content = content[:insert_pos] + '\n' + formatted_str + content[insert_pos:]
    return content

print("Injecting Sus Cup 11...")
content = inject_race(content, add_suscup11.suscup11_race)
content = inject_winner(content, add_suscup11.suscup11_winner)

print("Injecting Sus Cup 6...")
content = inject_race(content, add_suscup6.suscup6_race)
content = inject_winner(content, add_suscup6.suscup6_winner)

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected successfully!")
