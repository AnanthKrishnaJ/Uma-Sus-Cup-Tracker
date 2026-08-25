import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the image URLs in UMA_DATABASE
content = content.replace('chara_stand_104002_1060.png', 'chara_stand_1040_104002.png')
content = content.replace('chara_stand_102402_1060.png', 'chara_stand_1024_102402.png')

# 2. Fix the active App.showRaceDetail
last_show_race_idx = content.rfind('App.showRaceDetail = function(id) {')

if last_show_race_idx != -1:
    old_time = "race.date && `${race.date}${race.time ? ` / ${race.time}` : ''}`"
    new_time = "race.date && `${race.date.split(',')[0]}`"
    
    old_title = '<span><i class="fa-solid fa-horse-head"></i> ${p.uma}</span>'
    new_title = """<span><i class="fa-solid fa-horse-head"></i> ${p.characterUrl || (UMA_DATABASE[p.umaId] && UMA_DATABASE[p.umaId].url) ? `<a href="${p.characterUrl || UMA_DATABASE[p.umaId].url}" target="_blank" style="color:inherit; text-decoration:none;" onmouseover="this.style.textDecoration='underline'" onmouseout="this.style.textDecoration='none'">${p.uma} <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:0.7em; opacity:0.7;"></i></a>` : p.uma}</span>"""
    
    prefix = content[:last_show_race_idx]
    suffix = content[last_show_race_idx:]
    
    suffix = suffix.replace(old_time, new_time)
    suffix = suffix.replace(old_title, new_title)
    
    content = prefix + suffix

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied fixes to the active showRaceDetail and UMA_DATABASE.")
