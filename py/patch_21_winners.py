import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # --- Update INITIAL_DATA ---
    sus21_json = """    "Sus Cup 21": {
        "names": [
            "Taiki Shuttle", "Winning Ticket", "Symboli Rudolf", "Narita Brian",
            "Eishin Flash", "El Condor Pasa", "Ines Fujin", "Silence Suzuka",
            "Mejiro McQueen", "Tokai Teio", "Air Groove", "Silence Suzuka",
            "Oguri Cap", "Smart Falcon", "Daiwa Scarlet"
        ],
        "players": [
            "Ananth", "GohanXGAMER", "agnes", "GohanXGAMER",
            "Jiinxye", "Cruzi", "Ananth", "agnes",
            "Jiinxye", "Yves", "agnes", "Cruzi",
            "Yves", "Yves", "Cruzi"
        ],
        "positions": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 17, 18],
        "times": ["1:08.5", "1:08.5", "Head", "2 1/2 L", "Nose", "1/2 L", "2 L", "Nose", "3 L", "Neck", "1 3/4 L", "1 1/4 L", "Nose", "1 3/4 L", "5 L"],
        "ranks": ["S", "S+", "S", "S", "S", "S", "S", "A+", "A+", "A", "A+", "A+", "A+", "A", "S"],
        "race_numbers": [4, 7, 12, 1, 11, 15, 17, 16, 5, 13, 18, 8, 13, 6, 10],
        "favorites": [1, 2, 13, 6, 4, 11, 10, 5, 12, 14, 9, 8, 7, 18, 3]
    }"""
    
    # insert before the last closing brace of INITIAL_DATA
    # find const INITIAL_DATA = { ... };
    data_match = re.search(r'(const INITIAL_DATA = \{.*?)(\n\});\n\s*const', html, re.DOTALL)
    if data_match:
        if '"Sus Cup 21"' not in data_match.group(1):
            new_data_str = data_match.group(1) + ",\n" + sus21_json + data_match.group(2)
            html = html[:data_match.start(0)] + new_data_str + html[data_match.end(0):]
            print("Patched INITIAL_DATA")
        else:
            print("INITIAL_DATA already has Sus Cup 21")
    else:
        print("Could not find INITIAL_DATA")

    # --- Update INITIAL_HALL_OF_FAME ---
    new_winners = """        ,
        {
            "cup": "Sus Cup 17",
            "trainer": "agnes",
            "uma": "TM Opera O",
            "umaId": "tm-opera-o",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/101501-tm-opera-o",
            "race": "Gutsy Race",
            "date": "",
            "result": "4th",
            "rankLabel": "Single Guts Winner"
        },
        {
            "cup": "Sus Cup 17",
            "trainer": "Cruzi",
            "uma": "Agnes Digital",
            "umaId": "agnes-digital",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/104301-agnes-digital",
            "race": "Gutsy Race",
            "date": "",
            "result": "2nd",
            "rankLabel": "Double Guts Winner"
        },
        {
            "cup": "Sus Cup 17",
            "trainer": "agnes",
            "uma": "Symboli Rudolf",
            "umaId": "symboli-rudolf",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/101701-symboli-rudolf",
            "race": "Gutsy Race",
            "date": "",
            "result": "1st",
            "rankLabel": "Triple Guts Winner"
        },
        {
            "cup": "Sus Cup 18",
            "trainer": "GohanXGAMER",
            "uma": "Nice Nature",
            "umaId": "nice-nature",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/106001-nice-nature",
            "race": "SSR Race",
            "date": "",
            "result": "1st",
            "rankLabel": "Triple SSR Winner"
        },
        {
            "cup": "Sus Cup 18",
            "trainer": "Ananth",
            "uma": "Nice Nature",
            "umaId": "nice-nature",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/106001-nice-nature",
            "race": "SSR Race",
            "date": "",
            "result": "2nd",
            "rankLabel": "Double SSR Winner"
        },
        {
            "cup": "Sus Cup 18",
            "trainer": "agnes",
            "uma": "Biwa Hayahide",
            "umaId": "biwa-hayahide",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/102301-biwa-hayahide",
            "race": "SSR Race",
            "date": "",
            "result": "10th",
            "rankLabel": "Single SSR Winner"
        },
        {
            "cup": "Sus Cup 19",
            "trainer": "Cruzi",
            "uma": "Mayano Top Gun",
            "umaId": "mayano-top-gun",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/102401-mayano-top-gun",
            "race": "Gold Skills",
            "date": "",
            "result": "7th",
            "rankLabel": "0 Gold Skill Winner"
        },
        {
            "cup": "Sus Cup 19",
            "trainer": "Ananth",
            "uma": "Gold City",
            "umaId": "gold-city",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/104001-gold-city",
            "race": "Gold Skills",
            "date": "",
            "result": "1st",
            "rankLabel": "1-2 Gold Skill Winner"
        },
        {
            "cup": "Sus Cup 19",
            "trainer": "Jiinxye",
            "uma": "TM Opera O",
            "umaId": "tm-opera-o",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/101501-tm-opera-o",
            "race": "Gold Skills",
            "date": "",
            "result": "2nd",
            "rankLabel": "Gold Skill Only Winner"
        },
        {
            "cup": "Sus Cup 20",
            "trainer": "Ananth",
            "uma": "Mihono Bourbon",
            "umaId": "mihono-bourbon",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/102601-mihono-bourbon",
            "race": "All Style",
            "date": "",
            "result": "11th",
            "rankLabel": "Front Winner"
        },
        {
            "cup": "Sus Cup 20",
            "trainer": "Cyciesta",
            "uma": "Mejiro McQueen",
            "umaId": "mejiro-mcqueen",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/101301-mejiro-mcqueen",
            "race": "All Style",
            "date": "",
            "result": "1st",
            "rankLabel": "Pace Winner"
        },
        {
            "cup": "Sus Cup 20",
            "trainer": "Yves",
            "uma": "Eishin Flash",
            "umaId": "eishin-flash",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/103701-eishin-flash",
            "race": "All Style",
            "date": "",
            "result": "2nd",
            "rankLabel": "Late Winner"
        },
        {
            "cup": "Sus Cup 20",
            "trainer": "Yves",
            "uma": "Mayano Top Gun",
            "umaId": "mayano-top-gun",
            "version": "Original / Default",
            "url": "https://gametora.com/umamusume/characters/102401-mayano-top-gun",
            "race": "All Style",
            "date": "",
            "result": "3rd",
            "rankLabel": "End Winner"
        }"""

    hof_match = re.search(r'(const INITIAL_HALL_OF_FAME = \[.*?)(\n\s*\]);\n\s*(?:const|var|let|function)', html, re.DOTALL)
    if hof_match:
        if '"Double Guts Winner"' not in hof_match.group(1):
            new_hof_str = hof_match.group(1) + new_winners + hof_match.group(2)
            html = html[:hof_match.start(0)] + new_hof_str + html[hof_match.end(0):]
            print("Patched INITIAL_HALL_OF_FAME")
        else:
            print("INITIAL_HALL_OF_FAME already patched")
    else:
        print("Could not find INITIAL_HALL_OF_FAME array")
        return

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        print("index.html successfully updated")

if __name__ == '__main__':
    update_html()
