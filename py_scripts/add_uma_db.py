import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const UMA_DATABASE = ')
end = text.find('};', start)
data_str = text[start + 21:end + 1]

missing_umas = {
    "100602": {"name": "Oguri Cap", "version": "Ashen Miracle"},
    "102602": {"name": "Mihono Bourbon", "version": "CODE: ICING"},
    "101702": {"name": "Symboli Rudolf", "version": "Alternate"},
    "100302": {"name": "Tokai Teio", "version": "Alternate"},
    "102002": {"name": "Seiun Sky", "version": "Soirée des Chatons"},
    "104502": {"name": "Super Creek", "version": "Chiffon-Wrapped Mummy"},
    "103002": {"name": "Rice Shower", "version": "Vampire Makeover!"},
    "100102": {"name": "Special Week", "version": "Hopp'n♪Happy Heart"},
    "101402": {"name": "El Condor Pasa", "version": "Kukulkan Warrior"},
    "101802": {"name": "Air Groove", "version": "Quercus Civilis"},
    "102302": {"name": "Biwa Hayahide", "version": "Rouge Caroler"},
    "100402": {"name": "Maruzensky", "version": "Alternate"},
    "101302": {"name": "Mejiro McQueen", "version": "Alternate"},
    "105602": {"name": "Matikanefukukitaru", "version": "Lucky Tidings"}
}

# we'll build a string of new JS object properties
new_props = []
for umaId, info in missing_umas.items():
    # Only add if it's not already in UMA_DATABASE string
    if f'"{umaId}":' not in data_str and f"'{umaId}':" not in data_str:
        prop = f'"{umaId}": {{ id: "{umaId}", name: "{info["name"]}", type: "Uma Musume", version: "{info["version"]}", url: "https://gametora.com/umamusume/characters/{umaId}-{info["name"].lower().replace(" ", "-")}", image: "https://gametora.com/images/umamusume/characters/chara_stand_{umaId}_1060.png" }}'
        new_props.append(prop)

if new_props:
    # Insert new_props right after the opening brace of UMA_DATABASE
    open_brace_idx = text.find('{', start)
    insert_str = '\n    ' + ',\n    '.join(new_props) + ','
    
    new_text = text[:open_brace_idx + 1] + insert_str + text[open_brace_idx + 1:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
        
    print(f"Added {len(new_props)} missing Umas to UMA_DATABASE.")
else:
    print("All Umas are already in UMA_DATABASE.")

