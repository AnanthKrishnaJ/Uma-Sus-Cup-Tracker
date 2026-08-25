import json
import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update JSON data
start = text.find('const INITIAL_DATA = ')
end = text.find('const UMA_DATABASE =')
json_str = text[start + 21:end].strip().rstrip(';')
data = json.loads(json_str)

for race in data.get('races', []):
    if race.get('id') == 27.1:
        race['images'] = [
            "suscupimages21-30/mile27.1.png",
            "suscupimages21-30/mile27.2.png",
            "suscupimages21-30/mile27.3.png",
            "suscupimages21-30/mile27.4.png"
        ]
    elif race.get('id') == 27.2:
        race['images'] = [
            "suscupimages21-30/medium27.1.png",
            "suscupimages21-30/medium27.2.png",
            "suscupimages21-30/medium27.3.png",
            "suscupimages21-30/medium27.4.png"
        ]

new_json = json.dumps(data, indent=4)
text = text[:start + 21] + new_json + ';\n\n        ' + text[end:]

# 2. Add CSS keyframes
css_to_add = """
        @keyframes slideInFade {
            0% { opacity: 0; transform: translateX(-20px); }
            100% { opacity: 1; transform: translateX(0); }
        }
        @keyframes dotPulse {
            0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(var(--rgb-val), 0.4); }
            70% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(var(--rgb-val), 0); }
            100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(var(--rgb-val), 0); }
        }
    </style>
"""
if '@keyframes slideInFade' not in text:
    text = text.replace('</style>', css_to_add, 1)

# 3. Update evolutionHtml generation
# Find the forEach block
old_block = """    p.styleEvolution.forEach((e) => {
        const bg = styleColors[e.style] || styleColors['Unknown'];
        evolutionHtml += `
            <div style="position:relative; margin-bottom:15px;">
                <div style="position:absolute; left:-28.5px; top:4px; width:14px; height:14px; background:${bg}; border-radius:50%; border:3px solid #fff; box-shadow:0 0 0 1px #eee;"></div>
                <div style="font-weight:800; color:var(--text-muted); font-size:0.8rem; text-transform:uppercase;">Sus Cup ${e.cup}</div>
                <div style="font-weight:bold; font-size:1.05rem; color:${bg};">${e.style}</div>
            </div>
        `;
    });"""

new_block = """    p.styleEvolution.forEach((e, idx) => {
        const bg = styleColors[e.style] || styleColors['Unknown'];
        let rgb_val = '0,0,0';
        if(bg === '#e17055') rgb_val = '225, 112, 85';
        else if(bg === '#e67e22') rgb_val = '230, 126, 34';
        else if(bg === '#00b894') rgb_val = '0, 184, 148';
        else if(bg === '#0984e3') rgb_val = '9, 132, 227';
        else if(bg === '#b2bec3') rgb_val = '178, 190, 195';

        evolutionHtml += `
            <div style="position:relative; margin-bottom:15px; opacity:0; animation: slideInFade 0.4s ease forwards; animation-delay: ${idx * 0.15}s; --rgb-val: ${rgb_val};">
                <div style="position:absolute; left:-28.5px; top:4px; width:14px; height:14px; background:${bg}; border-radius:50%; border:3px solid #fff; animation: dotPulse 2s infinite; animation-delay: ${idx * 0.15}s;"></div>
                <div style="font-weight:800; color:var(--text-muted); font-size:0.8rem; text-transform:uppercase;">Sus Cup ${e.cup}</div>
                <div style="font-weight:bold; font-size:1.05rem; color:${bg};">${e.style}</div>
            </div>
        `;
    });"""

if old_block in text:
    text = text.replace(old_block, new_block)
else:
    print("Warning: old_block not found for replacement")


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updates applied successfully.")
