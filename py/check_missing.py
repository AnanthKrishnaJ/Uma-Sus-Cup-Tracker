import re
import json
import ast

js = open('index.html', encoding='utf-8').read()
db_match = re.search(r'const UMA_DATABASE = (\{.*?\});', js, re.DOTALL)
if db_match:
    # UMA_DATABASE might not be valid strict JSON, use ast.literal_eval if possible
    # but JS objects have unquoted keys often. Let's do a simple extraction of just the umas present.
    db_text = db_match.group(1)
    # Extract keys like: "special-week": { or special-week: {
    uma_keys = re.findall(r'"([^"]+)":\s*\{', db_text)
    print("Found", len(uma_keys), "UMA keys in DB")
else:
    print("UMA DB not found")

data_match = re.search(r'const INITIAL_DATA = (\{.*?\});', js, re.DOTALL)
if data_match:
    try:
        init_data = json.loads(data_match.group(1))
        missing = set()
        for race in init_data['races']:
            for p in race['participants']:
                uid = p.get('umaId') or p.get('uma')
                if uid not in uma_keys:
                    missing.add(uid)
        print("Missing UMAs:", missing)
    except Exception as e:
        print("Failed to parse data:", e)
