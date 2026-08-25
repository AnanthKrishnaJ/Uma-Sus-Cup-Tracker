import re

html_path = '../.vscode/suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_code = '<div class="item-title">${p.uma}</div>'
new_code = '''<div class="item-title">
                                        ${p.characterUrl || (UMA_DATABASE[p.umaId] && UMA_DATABASE[p.umaId].url) ? 
                                            `<a href="${p.characterUrl || UMA_DATABASE[p.umaId].url}" target="_blank" style="color:inherit; text-decoration:none;" onmouseover="this.style.textDecoration='underline'" onmouseout="this.style.textDecoration='none'">${p.uma} <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:0.7em; opacity:0.7;"></i></a>` 
                                            : p.uma}
                                    </div>'''

content = content.replace(old_code, new_code)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Character URL added!")
