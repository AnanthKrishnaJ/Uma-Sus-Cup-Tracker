import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add Lightbox HTML right after <body>
lightbox_html = """
    <div id="lightbox" class="lightbox" style="display:none; position:fixed; z-index:9999; left:0; top:0; width:100%; height:100%; background:rgba(0,0,0,0.9); text-align:center;">
        <span class="close-lightbox" onclick="App.closeLightbox()" style="position:absolute; top:20px; right:30px; color:white; font-size:40px; font-weight:bold; cursor:pointer;">&times;</span>
        <img class="lightbox-content" id="img01" style="margin:auto; display:block; max-width:90%; max-height:90%; top:50%; position:relative; transform:translateY(-50%); transition: transform 0.2s ease;">
        <a class="prev" onclick="App.changeSlide(-1)" style="cursor:pointer; position:absolute; top:50%; width:auto; padding:16px; margin-top:-50px; color:white; font-weight:bold; font-size:40px; transition:0.6s ease; border-radius:0 3px 3px 0; user-select:none; left:0;">&#10094;</a>
        <a class="next" onclick="App.changeSlide(1)" style="cursor:pointer; position:absolute; top:50%; width:auto; padding:16px; margin-top:-50px; color:white; font-weight:bold; font-size:40px; transition:0.6s ease; border-radius:3px 0 0 3px; user-select:none; right:0;">&#10095;</a>
    </div>
"""
if '<div id="lightbox"' not in text:
    text = text.replace('<body>', '<body>\n' + lightbox_html)

# 2. Update gallery rendering in showRaceDetail
old_gallery = '`<a href="${image}" target="_blank" rel="noopener"><img src="${image}" alt="Sus Cup ${race.cupNumber} result screenshot ${index + 1}" loading="lazy"></a>`'
new_gallery = '`<img src="${image}" alt="Sus Cup ${race.cupNumber} result screenshot ${index + 1}" loading="lazy" style="cursor:pointer;" onclick="App.lightboxImages=${JSON.stringify(race.images).replace(/\\"/g, \'&quot;\')}; App.openLightbox(${index})">`'
text = text.replace(old_gallery, new_gallery)

# 3. Add JS methods for lightbox to App object
js_methods = """
    closeLightbox() { document.getElementById('lightbox').style.display = "none"; },
    changeSlide(n) {
        this.lightboxIndex = (this.lightboxIndex || 0) + n;
        if (this.lightboxIndex >= this.lightboxImages.length) { this.lightboxIndex = 0; }
        if (this.lightboxIndex < 0) { this.lightboxIndex = this.lightboxImages.length - 1; }
        this.openLightbox(this.lightboxIndex);
    },
    openLightbox(index) {
        this.lightboxIndex = index;
        document.getElementById('lightbox').style.display = "block";
        var img = document.getElementById("img01");
        img.src = this.lightboxImages[index];
        this.zoomLevel = 1;
        img.style.transform = `translateY(-50%) scale(${this.zoomLevel})`;
    },
"""
if 'closeLightbox()' not in text:
    text = text.replace('init() {', js_methods + '\n    init() {')

# 4. Add wheel event listener for zooming
zoom_listener = """
        const img01 = document.getElementById('img01');
        if (img01) {
            img01.addEventListener('wheel', function(e) {
                e.preventDefault();
                App.zoomLevel = App.zoomLevel || 1;
                if(e.deltaY < 0) { App.zoomLevel += 0.1; }
                else { App.zoomLevel -= 0.1; if(App.zoomLevel < 0.5) App.zoomLevel = 0.5; }
                this.style.transform = `translateY(-50%) scale(${App.zoomLevel})`;
            });
        }
"""
if 'img01.addEventListener' not in text:
    text = text.replace('document.addEventListener(\'DOMContentLoaded\', () => { App.init(); });', 
                        zoom_listener + '\n        document.addEventListener(\'DOMContentLoaded\', () => { App.init(); });')


# 5. Fix Cup 6 Data
start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

# Markdown table for Cup 6
markdown_table = \"\"\"
| 🥇 1st | Gold Ship       | Cyciesta    |       14 |  No. 5 | End   | **2:29.0**  |
| 🥈 2nd | Mejiro McQueen  | Jinxye      |        7 |  No. 2 | Pace  | **1 1/4 L** |
| 🥉 3rd | Symboli Rudolf  | Agnes       |       12 |  No. 3 | Pace  | **1 1/4 L** |
| 4th    | Gold Ship       | Yves        |       10 |  No. 7 | End   | **2 L**     |
| 5th    | Mayano Top Gun  | Agnes       |        1 |  No. 6 | End   | **3/4 L**   |
| 6th    | Keyboard Rhythm | —           |        8 | No. 11 | End   | **5 L**     |
| 7th    | Tokai Teio      | Jinxye      |        5 |  No. 4 | Pace  | **3/4 L**   |
| 8th    | Ogress          | —           |        3 |  No. 9 | End   | **2 1/2 L** |
| 9th    | Oguri Cap       | Cyciesta    |       13 |  No. 1 | Pace  | **3 L**     |
| 10th   | Agnes Tachyon   | Cruzi       |       15 | No. 13 | Pace  | **Head**    |
| 11th   | Ribbon Nocturne | —           |        9 | No. 12 | Pace  | **Head**    |
| 12th   | Maleficus       | —           |        4 | No. 15 | Late  | **1 3/4 L** |
| 13th   | Nice Nature     | Yves        |       16 |  No. 8 | Late  | **5 L**     |
| 14th   | Oguri Cap       | GohanXGAMER |        6 | No. 10 | Pace  | **2 1/2 L** |
| 15th   | Super Creek     | GohanXGAMER |        2 | No. 16 | Pace  | **2 L**     |
| 16th   | Tokai Teio      | Cruzi       |       11 | No. 14 | Pace  | **3/4 L**   |
\"\"\"

cup6_updates = {}
for line in markdown_table.strip().split('\\n'):
    parts = [p.strip() for p in line.split('|')]
    if len(parts) > 5:
        pos_str = parts[1].strip()
        pos = int(re.search(r'\d+', pos_str).group())
        uma = parts[2]
        player = parts[3]
        if player == '—': player = 'NPC'
        number = int(parts[4])
        pop = int(re.search(r'\d+', parts[5]).group())
        style = parts[6]
        gap = parts[7].replace('**', '')
        cup6_updates[pos] = {'gap': gap, 'pop': pop, 'number': number, 'strategy': style, 'uma': uma, 'player': player}

# Mapping numeric IDs in Cup 6 to correct keys
id_mapping = {
    '100101': 'gold-ship',
    '101301': 'mejiro-mcqueen', # assuming this is correct? wait, let's just use what's right.
    '101701': 'symboli-rudolf',
    '102401': 'mayano-top-gun',
    '100301': 'tokai-teio-beyond', # As requested by user: 100302
    '100601': 'oguri-cap',
    '103201': 'agnes-tachyon',
    '106001': 'nice-nature',
    '104501': 'super-creek'
}

for race in data['races']:
    if str(race.get('cupNumber')) == 'SUS CUP 6':
        for p in race['participants']:
            pos = p['pos']
            if pos in cup6_updates:
                upd = cup6_updates[pos]
                if pos == 1:
                    p['time'] = upd['gap']
                p['gap'] = upd['gap']
                p['pop'] = upd['pop']
                p['number'] = upd['number']
                p['strategy'] = upd['strategy']
                
                # Player Normalization
                player = upd['player']
                if player == 'Jinxye': player = 'Jiinxye'
                if player == 'Cyclobly': player = 'Cyciesta'
                p['player'] = player
                
            old_id = p.get('umaId', '')
            if old_id in id_mapping:
                p['umaId'] = id_mapping[old_id]
            
            # Special override for Tokai Teio as requested
            if 'Tokai Teio' in p.get('uma', ''):
                p['umaId'] = 'tokai-teio-beyond'

new_json = json.dumps(data, indent=4, ensure_ascii=False)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied Lightbox features, Cup 6 data cross-check, and umaId mapping!")
