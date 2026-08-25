import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

last_show_race_idx = content.rfind('App.showRaceDetail = function(id) {')

if last_show_race_idx != -1:
    prefix = content[:last_show_race_idx]
    suffix = content[last_show_race_idx:]
    
    suffix = suffix.replace('this.stylesMap[p.strategy] || p.strategy', 'this.stylesMap[p.strategy || p.style] || (p.strategy || p.style)')
    suffix = suffix.replace("p.gap || '-'", "p.gap || p.time || p.finish || '-'")
    suffix = suffix.replace('p.number ?', '(p.number || p.no) ?')
    suffix = suffix.replace("'#' + p.number", "'#' + (p.number || p.no)")
    
    content = prefix + suffix

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied data fallbacks to the active showRaceDetail.")
