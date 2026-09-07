import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_winners = """        {
            "cup": "Sus Cup 17",
            "trainer": "agnes",
            "uma": "TM Opera O",
            "umaId": "t-m-opera-o",
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
            "umaId": "t-m-opera-o",
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
        },
"""

    if '"Double Guts Winner"' not in html:
        # insert right after "winners": [
        html = html.replace('"winners": [\n', '"winners": [\n' + new_winners)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("index.html successfully updated with winners")
    else:
        print("Winners already added")

if __name__ == '__main__':
    update_html()
