import json

suscup12 = {
    "id": 12,
    "cupNumber": "SUS CUP 12 - Frontend Race",
    "cupName": "Sus Cup 12",
    "name": "Tenno Sho (Autumn)",
    "date": "2025-09-24",
    "time": "18:45",
    "roomId": "7604 2408",
    "race": "Tenno Sho (Autumn)",
    "course": "Tokyo Turf",
    "surface": "Turf",
    "distance": "2000m",
    "distanceType": "Medium",
    "direction": "Left",
    "weather": "Random",
    "ground": "Random",
    "mood": "Random",
    "rankLimit": "As configured for this race",
    "specialRule": "All players must use Front Runner and End Closer characters only.",
    "images": [
        "suscup12-20/12.1.png",
        "suscup12-20/12.2.png",
        "suscup12-20/12.3.png",
        "suscup12-20/12.4.png"
    ],
    "participants": [
        {
          "pos": 1,
          "uma": "Narita Taishin",
          "umaId": "narita-taishin",
          "player": "Cyciesta",
          "number": 1,
          "rank": "A",
          "title": "The GOAT",
          "strategy": "End",
          "time": "1:56.1",
          "pop": 1,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/narita-taishin"
        },
        {
          "pos": 2,
          "uma": "Hishi Amazon",
          "umaId": "hishi-amazon",
          "player": "Jiinxye",
          "number": 8,
          "rank": "A",
          "title": "Record Holder",
          "strategy": "End",
          "gap": "1 3/4 L",
          "pop": 2,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/hishi-amazon"
        },
        {
          "pos": 3,
          "uma": "Gold Ship",
          "umaId": "gold-ship",
          "player": "Cruzi",
          "number": 7,
          "rank": "A",
          "title": "Finals Champion",
          "strategy": "End",
          "gap": "3/4 L",
          "pop": 3,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/gold-ship"
        },
        {
          "pos": 4,
          "uma": "Silence Suzuka",
          "umaId": "silence-suzuka",
          "player": "agnes",
          "number": 2,
          "rank": "A",
          "title": "Legendary Diva",
          "strategy": "Front",
          "gap": "Nose",
          "pop": 4,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/silence-suzuka"
        },
        {
          "pos": 5,
          "uma": "Gold Ship",
          "umaId": "gold-ship",
          "player": "GohanXGAMER",
          "number": 11,
          "rank": "B+",
          "title": "Finals Champion",
          "strategy": "End",
          "gap": "2 L",
          "pop": 5,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/gold-ship"
        },
        {
          "pos": 6,
          "uma": "Silence Suzuka",
          "umaId": "silence-suzuka",
          "player": "GohanXGAMER",
          "number": 16,
          "rank": "B+",
          "title": "The GOAT",
          "strategy": "Front",
          "gap": "3/4 L",
          "pop": 6,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/silence-suzuka"
        },
        {
          "pos": 7,
          "uma": "Seiun Sky",
          "umaId": "seiun-sky",
          "player": "Cruzi",
          "number": 5,
          "rank": "A",
          "title": "The GOAT",
          "strategy": "Front",
          "gap": "3/4 L",
          "pop": 7,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/seiun-sky"
        },
        {
          "pos": 8,
          "uma": "Bella Prateria",
          "player": "NPC",
          "number": 6,
          "rank": "B",
          "strategy": "Pace",
          "gap": "1 3/4 L",
          "pop": 8,
          "version": "NPC",
          "participantType": "NPC Uma"
        },
        {
          "pos": 9,
          "uma": "Mayano Top Gun",
          "umaId": "mayano-top-gun",
          "player": "Ananth",
          "number": 4,
          "rank": "B+",
          "title": "Finals Champion",
          "strategy": "Front",
          "gap": "1 1/2 L",
          "pop": 9,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/mayano-top-gun"
        },
        {
          "pos": 10,
          "uma": "Arcade Champ",
          "player": "NPC",
          "number": 12,
          "rank": "C+",
          "strategy": "End",
          "gap": "1/2 L",
          "pop": 10,
          "version": "NPC",
          "participantType": "NPC Uma"
        },
        {
          "pos": 11,
          "uma": "Gold Ship",
          "umaId": "gold-ship",
          "player": "agnes",
          "number": 17,
          "rank": "A",
          "title": "Unpredictable",
          "strategy": "End",
          "gap": "Nose",
          "pop": 11,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/gold-ship"
        },
        {
          "pos": 12,
          "uma": "Oishii Parfait",
          "player": "NPC",
          "number": 10,
          "rank": "C+",
          "strategy": "Front",
          "gap": "Head",
          "pop": 12,
          "version": "NPC",
          "participantType": "NPC Uma"
        },
        {
          "pos": 13,
          "uma": "Ogress",
          "player": "NPC",
          "number": 9,
          "rank": "C+",
          "strategy": "Front",
          "gap": "3/4 L",
          "pop": 13,
          "version": "NPC",
          "participantType": "NPC Uma"
        },
        {
          "pos": 14,
          "uma": "Silence Suzuka",
          "umaId": "silence-suzuka",
          "player": "Jiinxye",
          "number": 18,
          "rank": "A",
          "title": "Finals Champion",
          "strategy": "Front",
          "gap": "Nose",
          "pop": 14,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/silence-suzuka"
        },
        {
          "pos": 15,
          "uma": "Ribbon Etude",
          "player": "NPC",
          "number": 15,
          "rank": "C+",
          "strategy": "End",
          "gap": "3/4 L",
          "pop": 15,
          "version": "NPC",
          "participantType": "NPC Uma"
        },
        {
          "pos": 16,
          "uma": "Mihono Bourbon",
          "umaId": "mihono-bourbon",
          "player": "Cyciesta",
          "number": 14,
          "rank": "A",
          "title": "Finals Champion",
          "strategy": "Front",
          "gap": "1 3/4 L",
          "pop": 16,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/mihono-bourbon"
        },
        {
          "pos": 17,
          "uma": "Gray Chouchou",
          "player": "NPC",
          "number": 13,
          "rank": "C+",
          "strategy": "Late",
          "gap": "3/4 L",
          "pop": 17,
          "version": "NPC",
          "participantType": "NPC Uma"
        },
        {
          "pos": 18,
          "uma": "Oguri Cap",
          "umaId": "oguri-cap",
          "player": "Ananth",
          "number": 3,
          "rank": "B+",
          "title": "Finals Champion",
          "strategy": "Late",
          "gap": "Distance",
          "pop": 18,
          "version": "Original / Default",
          "participantType": "Playable Uma",
          "characterUrl": "https://gametora.com/umamusume/characters/oguri-cap"
        }
    ]
}

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate INITIAL_DATA
start = content.find('const INITIAL_DATA = ')
end = content.find('const UMA_DATABASE =')

json_str = content[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

# Insert the new race at the beginning of the races array (or check if it exists)
if not any(r.get('id') == 12 for r in data['races']):
    data['races'].insert(0, suscup12)
    
new_json = json.dumps(data, indent=4)
new_content = content[:start + 21] + new_json + ';\n\n        ' + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("SUS CUP 12 has been injected successfully!")
