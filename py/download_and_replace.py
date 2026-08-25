import os
import urllib.request

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
local_img_dir = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscupimages21-30'
os.makedirs(local_img_dir, exist_ok=True)

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

umas_to_fetch = [
    '100702', # Gold Ship
    '104002', # Gold City
    '102602', # Mihono Bourbon
    '101902', # Agnes Digital
    '101002', # Taiki Shuttle
    '106002', # Nice Nature
    '101802', # Air Groove
]

for uid in umas_to_fetch:
    url = f"https://gametora.com/images/umamusume/characters/chara_stand_{uid[:4]}_{uid}.png"
    referer = f"https://gametora.com/umamusume/characters/{uid}-uma"

    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': referer
    })

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                local_filename = f"chara_stand_{uid}.png"
                local_path = os.path.join(local_img_dir, local_filename)
                with open(local_path, 'wb') as img_f:
                    img_f.write(response.read())
                print(f"Downloaded {uid}")
                
                # Replace in HTML
                old_img = f"https://gametora.com/images/umamusume/characters/chara_stand_{uid[:4]}_{uid}.png"
                new_img = f"suscupimages21-30/{local_filename}"
                html = html.replace(old_img, new_img)
            else:
                print(f"Failed {uid}: {response.status}")
    except Exception as e:
        print(f"Error {uid}: {e}")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated UMA_DATABASE images in suscup1.html")
