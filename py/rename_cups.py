import json
import re

def main():
    names_map = {
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
        24: "Sus Cup 24 — Solo Queue Race"
    }

    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    for num, new_name in names_map.items():
        # Let's find "cupNumber": num, \n "cupName": "..." and replace the cupName.
        # This will update the races array in INITIAL_DATA.
        pattern = rf'("cupNumber":\s*{num},\s*"cupName":\s*")([^"]+)(")'
        def replacer(m):
            return f'{m.group(1)}{new_name}{m.group(3)}'
        content = re.sub(pattern, replacer, content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Cup names updated.")

if __name__ == '__main__':
    main()
