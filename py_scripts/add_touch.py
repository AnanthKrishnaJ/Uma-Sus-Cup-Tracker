import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

touch_listener = """
        const lightbox = document.getElementById('lightbox');
        if (lightbox) {
            let touchstartX = 0;
            let touchendX = 0;
            lightbox.addEventListener('touchstart', e => {
                touchstartX = e.changedTouches[0].screenX;
            });
            lightbox.addEventListener('touchend', e => {
                touchendX = e.changedTouches[0].screenX;
                if (touchendX < touchstartX - 50) { App.changeSlide(1); }
                if (touchendX > touchstartX + 50) { App.changeSlide(-1); }
            });
        }
"""
if 'touchstart' not in text:
    text = text.replace("img01.addEventListener('wheel'", touch_listener + "\n            img01.addEventListener('wheel'")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added touch listeners for swiping")
else:
    print("Touch listeners already present")
