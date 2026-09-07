import re

cup_names = {
    1: "Sus Cup 1 — The Start",
    2: "Sus Cup 2 — Mile Front Runners",
    3: "Sus Cup 3 — Mile Dirt",
    4: "Sus Cup 4 — 1 Runner + 1 Debuffer",
    5: "Sus Cup 5 — Gemini Cup Open League Training",
    6: "Sus Cup 6 — Unique Epithets / Steamy Solidarity",
    7: "Sus Cup 7 — Pace Chaser Medium",
    8: "Sus Cup 8 — Father-Daughter duo",
    9: "Sus Cup 9 — GP Round 1/3",
    10: "Sus Cup 10 — GP Round 2/3",
    11: "Sus Cup 11 — GP Round 3/3",
    12: "Sus Cup 12 — Frontend Race",
    13: "Sus Cup 13 — Haru Leading",
    14: "Sus Cup 14 — Graded Open Leo CM",
    15: "Sus Cup 15 — Triple Front Runners",
    16: "Sus Cup 16 — Mixed Class Race",
    17: "Sus Cup 17 — Gutsy Race",
    18: "Sus Cup 18 — SSR Race",
    19: "Sus Cup 19 — Gold Skills",
    20: "Sus Cup 20 — All Style",
    21: "Sus Cup 21 — Spark Race",
    22: "Sus Cup 22 — Cross Career Race",
    23: "Sus Cup 23 — Mixed Rarity Race",
    24: "Sus Cup 24 — Solo Queue Race",
    25: "Sus Cup 25 — Fashion Statement Race",
    26: "Sus Cup 26 — Grand Live Sussery",
    27: "Sus Cup 27 — Multi CM Sussing",
    28: "Sus Cup 28 — Triple Threat"
}

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Locate the races array
start = text.find('"races": [')
end = text.find('const UMA_DATABASE', start)

if start == -1 or end == -1:
    print("Could not find races array")
    exit(1)

races_text = text[start:end]

# For each cup number, we want to normalize cupNumber to just the digit and add/replace cupName.
def replace_cup(match):
    full_match = match.group(0)
    cup_num_str = match.group(1) # The value of cupNumber
    
    # Extract digit
    m = re.search(r'\d+', cup_num_str)
    if not m:
        return full_match # Should not happen
    
    cup_idx = int(m.group(0))
    if cup_idx not in cup_names:
        return full_match
        
    official_name = cup_names[cup_idx]
    
    # Replace cupNumber with just the digit
    new_str = f'"cupNumber": {cup_idx},\n            "cupName": "{official_name}",'
    
    return new_str

# First, remove any existing "cupName": "...", lines in races_text to avoid duplicates
races_text = re.sub(r'\s*"cupName":\s*"[^"]*",\n', '\n', races_text)

# Now find and replace cupNumber
races_text = re.sub(r'"cupNumber":\s*([^,]+),', replace_cup, races_text)

new_text = text[:start] + races_text + text[end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated cup names.")
