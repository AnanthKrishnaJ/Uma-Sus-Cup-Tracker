import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove my injected lightbox HTML
start_lightbox = text.find('<div id="lightbox"')
if start_lightbox != -1:
    end_lightbox = text.find('</div>', start_lightbox) + 6
    text = text[:start_lightbox] + text[end_lightbox:]

# 2. Remove my injected App methods (changeSlide, openLightbox, closeLightbox)
js_methods = r"closeLightbox\(\) \{.*?\},\s*changeSlide\(n\) \{.*?\},\s*openLightbox\(index\) \{.*?\},"
text = re.sub(js_methods, '', text, flags=re.DOTALL)

# 3. Remove my injected wheel listener
wheel_listener = r"const img01 = document.getElementById\('img01'\);.*?img01\.addEventListener\('wheel'.*?\n        \}"
text = re.sub(wheel_listener, '', text, flags=re.DOTALL)

# 4. Remove my touch event listeners if any
touch_listener = r"const lightbox = document.getElementById\('lightbox'\);.*?\}\);\n        \}"
text = re.sub(touch_listener, '', text, flags=re.DOTALL)

# 5. Fix gallery template to use original openGalleryModal
old_gallery = '`<img src="${image}" alt="Sus Cup ${race.cupNumber} result screenshot ${index + 1}" loading="lazy" style="cursor:pointer;" onclick="App.lightboxImages=${JSON.stringify(race.images).replace(/\\"/g, \'&quot;\')}; App.openLightbox(${index})">`'

# we will encode it simply
new_gallery = r'`<img src="${image}" alt="Sus Cup ${race.cupNumber} result screenshot ${index + 1}" loading="lazy" style="cursor:pointer;" onclick=\'openGalleryModal(${JSON.stringify(race.images)}, ${index})\'>`'

if old_gallery in text:
    text = text.replace(old_gallery, new_gallery)
else:
    print("WARNING: Could not find old gallery code to replace!")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Restored original gallery and cleaned up injected lightbox code.")
