const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf-8');

const s1 = '${bestUma1.name !== \\'None\\' ? `<img src="${this.getUmaImage(bestUma1.umaId, bestUma1.name)}" class="uma-icon" style="width: 50px; height: 50px; border-radius: 50%; margin: 5px auto; display: block; border: 2px solid var(--accent-color);" onerror="this.src=\\'archive_mascot.png\\'">` : \\'\\'}';
const r1 = '${bestUma1.name !== \\'None\\' ? `<div style="display:flex; justify-content:center; margin: 5px 0;">` + this.getUmaImage(bestUma1.umaId, bestUma1.name).replace(`class="uma-image"`, `class="uma-image" style="margin-right:0; width:50px; height:50px; border-radius:50%; border: 2px solid var(--accent-color);"`) + `</div>` : \\'\\'}';

const s2 = '${bestUma2.name !== \\'None\\' ? `<img src="${this.getUmaImage(bestUma2.umaId, bestUma2.name)}" class="uma-icon" style="width: 50px; height: 50px; border-radius: 50%; margin: 5px auto; display: block; border: 2px solid var(--accent-color);" onerror="this.src=\\'archive_mascot.png\\'">` : \\'\\'}';
const r2 = '${bestUma2.name !== \\'None\\' ? `<div style="display:flex; justify-content:center; margin: 5px 0;">` + this.getUmaImage(bestUma2.umaId, bestUma2.name).replace(`class="uma-image"`, `class="uma-image" style="margin-right:0; width:50px; height:50px; border-radius:50%; border: 2px solid var(--accent-color);"`) + `</div>` : \\'\\'}';

html = html.replace(s1, r1);
html = html.replace(s2, r2);

// Fix the margin-right for All Uma list in player profile
const s3 = '<div style="margin-bottom:10px;">${this.getUmaImage(um.umaId, um.name)}</div>';
const r3 = '<div style="margin-bottom:10px; display:flex; justify-content:center;">${this.getUmaImage(um.umaId, um.name).replace(`class="uma-image"`, `class="uma-image" style="margin-right:0;"`)}</div>';
html = html.replace(s3, r3);

fs.writeFileSync('index.html', html, 'utf-8');
console.log('Fixed best uma compare image');
