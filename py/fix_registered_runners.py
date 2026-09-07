import re, json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the INITIAL_DATA object
match = re.search(r'const INITIAL_DATA = (\{[\s\S]*?\});\n', content)
if not match:
    print("Could not find INITIAL_DATA")
    exit(1)

db_str = match.group(1)
data = json.loads(db_str)

# Clean up registeredRunners for finished races
for race in data.get('races', []):
    if 'participants' in race:
        # Check if this race is fully finished (has pos for its participants)
        finished_count = sum(1 for p in race['participants'] if 'pos' in p)
        if finished_count > 0:
            # If the race has results, we shouldn't use registeredRunners anymore.
            # Especially for Sus Cup 24 where registeredRunners is masking the results!
            if 'registeredRunners' in race:
                print(f"Clearing registeredRunners for Cup {race.get('cupNumber')} because it is finished.")
                race['registeredRunners'] = []

# Write back the modified JSON
new_db_str = json.dumps(data, indent=2)
new_content = content[:match.start(1)] + new_db_str + content[match.end(1):]
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Database updated.")
