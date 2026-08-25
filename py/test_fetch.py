import os
import urllib.request

local_img_dir = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscupimages21-30'
uid = '100702'
url = 'https://gametora.com/images/umamusume/characters/chara_stand_1007_100702.png'
referer = 'https://gametora.com/umamusume/characters/100702-gold-ship'

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
            print(f"Success! {local_path} downloaded.")
        else:
            print(response.status)
except Exception as e:
    print(f"Error: {e}")
