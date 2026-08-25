import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Modify championships filter to only include actual 1st place winners or ones without rankLabel
# Actually, wait, some 1st place winners have rankLabel (e.g. A+ Winner, Triple Guts Winner).
# It's better to just separate regular wins from criteria wins.
old_champ = r"const championships = (this.data.winners || \[\]).filter(w => w.trainer === name && !NPC_PROFILES\[w.uma\] && w.type !== 'NPC Uma').length;"
new_champ = """const allTrainerWins = (this.data.winners || []).filter(w => w.trainer === name && !NPC_PROFILES[w.uma] && w.type !== 'NPC Uma');
                const championships = allTrainerWins.filter(w => !w.rankLabel).length;
                const criteriaWins = allTrainerWins.filter(w => w.rankLabel);"""

text = text.replace("const championships = (this.data.winners || []).filter(w => w.trainer === name && !NPC_PROFILES[w.uma] && w.type !== 'NPC Uma').length;", new_champ)

old_ach = r"if (championships > 0) achievements.push({ icon: 'dY?\+', title: 'Sus Cup Champion', desc: `Won \${championships} Championship\${championships > 1 \? 's' : ''}` });"
new_ach = """if (championships > 0) achievements.push({ icon: '🏆', title: 'Sus Cup Champion', desc: `Won ${championships} Championship${championships > 1 ? 's' : ''}` });
                criteriaWins.forEach(cw => {
                    achievements.push({ icon: '🏅', title: 'Criteria Winner', desc: `${cw.rankLabel} in ${cw.cup}` });
                });"""
# NOTE: The original icon was 'dY?+' because of encoding issues (emoji).
# I'll use raw emoji characters '🏆' and '🏅'.
text = text.replace("if (championships > 0) achievements.push({ icon: 'dY?+', title: 'Sus Cup Champion', desc: `Won ${championships} Championship${championships > 1 ? 's' : ''}` });", new_ach)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated showPlayer')
