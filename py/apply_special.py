import json
import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        start_str = '"winners": ['
        start_idx = content.find(start_str)
        if start_idx == -1:
            print("Could not find start")
            return
            
        # Find the matching closing bracket for the array
        # It's a large array, we can find the next top-level key like '"cups": ['
        end_idx = content.find('"cups": [')
        
        # We need to find the ] right before "cups"
        array_end = content.rfind(']', start_idx, end_idx)
        
        winners_str = content[start_idx + len('"winners": '):array_end + 1].strip()
        print("Found string ending with:", winners_str[-50:])
        
        winners = json.loads(winners_str)
        print("Parsed successfully. Count:", len(winners))
        
        # Filter
        new_winners = []
        for w in winners:
            if w.get('cup') in ['Sus Cup 17', 'Sus Cup 18', 'Sus Cup 19', 'Sus Cup 20'] and 'rankLabel' in w:
                continue
            new_winners.append(w)
            
        new_entries = [
            # Cup 17
            {"cup": "Sus Cup 17", "trainer": "Agnes", "uma": "T.M. Opera O", "umaId": "t-m-opera-o", "rankLabel": "Single Guts Winner", "version": "Original / Default"},
            {"cup": "Sus Cup 17", "trainer": "Cruzi", "uma": "Agnes Digital", "umaId": "agnes-digital", "rankLabel": "Double Guts Winner", "version": "Original / Default"},
            {"cup": "Sus Cup 17", "trainer": "Agnes", "uma": "Symboli Rudolf", "umaId": "symboli-rudolf", "rankLabel": "Triple Guts Winner", "version": "Original / Default"},
            # Cup 18
            {"cup": "Sus Cup 18", "trainer": "GohanXGAMER", "uma": "Nice Nature", "umaId": "nice-nature", "rankLabel": "Triple SSR Winner", "version": "Original / Default"},
            {"cup": "Sus Cup 18", "trainer": "Ananth", "uma": "Nice Nature", "umaId": "nice-nature", "rankLabel": "Double SSR Winner", "version": "Original / Default"},
            {"cup": "Sus Cup 18", "trainer": "Agnes", "uma": "Biwa Hayahide", "umaId": "biwa-hayahide", "rankLabel": "Single SSR Winner", "version": "Original / Default"},
            # Cup 19
            {"cup": "Sus Cup 19", "trainer": "Cruzi", "uma": "Mayano Top Gun", "umaId": "mayano-top-gun", "rankLabel": "0 Gold Skill Winner", "version": "Original / Default"},
            {"cup": "Sus Cup 19", "trainer": "Ananth", "uma": "Gold City", "umaId": "gold-city", "rankLabel": "1-2 Gold Skill Winner", "version": "Original / Default"},
            {"cup": "Sus Cup 19", "trainer": "Jiinxye", "uma": "T.M. Opera O", "umaId": "t-m-opera-o", "rankLabel": "Gold Skill Only Winner", "version": "Original / Default"},
            # Cup 20
            {"cup": "Sus Cup 20", "trainer": "Ananth", "uma": "Mihono Bourbon", "umaId": "mihono-bourbon", "rankLabel": "Front Winner", "version": "Original / Default"},
            {"cup": "Sus Cup 20", "trainer": "Cyciesta", "uma": "Mejiro McQueen", "umaId": "mejiro-mcqueen", "rankLabel": "Pace Winner", "version": "Original / Default"},
            {"cup": "Sus Cup 20", "trainer": "Yves", "uma": "Eishin Flash", "umaId": "eishin-flash", "rankLabel": "Late Winner", "version": "Original / Default"},
            {"cup": "Sus Cup 20", "trainer": "Yves", "uma": "Mayano Top Gun", "umaId": "mayano-top-gun", "rankLabel": "End Winner", "version": "Original / Default"}
        ]
        
        new_winners.extend(new_entries)
        new_winners_str = json.dumps(new_winners, indent=4)
        
        new_content = content[:start_idx + len('"winners": ')] + new_winners_str + content[array_end + 1:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print("Updated correctly!")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
