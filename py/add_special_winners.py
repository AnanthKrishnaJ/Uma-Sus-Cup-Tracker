import json
import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Find where "winners": [ starts and where "cups": [ starts
        start_idx = content.find('"winners": [')
        end_idx = content.find('"cups": [')
        
        if start_idx == -1 or end_idx == -1:
            print("Could not find winners or cups array boundaries.")
            return
            
        # Extract the winners JSON substring (remove the trailing comma before "cups":)
        winners_str = content[start_idx + 11:end_idx].strip()
        if winners_str.endswith(','):
            winners_str = winners_str[:-1]

        # Parse JSON
        winners = json.loads(winners_str)
        
        # Filter out existing rankLabel winners for Cups 17-20
        new_winners = []
        for w in winners:
            if w.get('cup') in ['Sus Cup 17', 'Sus Cup 18', 'Sus Cup 19', 'Sus Cup 20'] and 'rankLabel' in w:
                continue
            new_winners.append(w)
            
        # Add the new ones
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
        
        # Serialize back
        new_winners_str = json.dumps(new_winners, indent=4)
        
        # Replace in content
        new_content = content[:start_idx] + '"winners": ' + new_winners_str + ",\n  " + content[end_idx:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Successfully updated special category winners! Old count: {len(winners)}, New count: {len(new_winners)}")
        
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
