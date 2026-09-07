import re, json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the INITIAL_DATA object
match = re.search(r'const INITIAL_DATA = (\{[\s\S]*?\});\n', content)
if not match:
    print("Could not find INITIAL_DATA")
    exit(1)

db_str = match.group(1)
try:
    data = json.loads(db_str)
except Exception as e:
    print("JSON parse error:", e)
    # the JSON string might be slightly malformed if it has JS-specific stuff, but we'll see
    pass

if 'data' in locals():
    # 1. Standardize agnes to Agnes
    for race in data.get('races', []):
        if 'participants' in race:
            for p in race['participants']:
                if p.get('player') == 'agnes':
                    p['player'] = 'Agnes'
        if 'registeredRunners' in race:
            for p in race['registeredRunners']:
                if p.get('player') == 'agnes':
                    p['player'] = 'Agnes'

    for winner in data.get('winners', []):
        if winner.get('playerStr') == 'agnes':
            winner['playerStr'] = 'Agnes'

    # Let's inspect Sus Cup 24 participants
    sc24 = next((r for r in data.get('races', []) if str(r.get('cupNumber')) == '24'), None)
    if sc24:
        print("Sus Cup 24 found. First 2 participants:")
        for p in sc24['participants'][:2]:
            print(f"  {p.get('uma')} ({p.get('player')}): time={p.get('time')}, finish={p.get('finish')}, gap={p.get('gap')}")

    # Write back the modified JSON
    new_db_str = json.dumps(data, indent=2)
    # We might need to replace it safely
    new_content = content[:match.start(1)] + new_db_str + content[match.end(1):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Database updated.")
