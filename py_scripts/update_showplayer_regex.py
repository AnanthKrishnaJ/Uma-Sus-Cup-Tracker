import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace championships line
old_champ = r"const championships\s*=\s*\(this\.data\.winners\s*\|\|\s*\[\]\)\.filter\(w\s*=>\s*w\.trainer\s*===\s*name\s*&&\s*!NPC_PROFILES\[w\.uma\]\s*&&\s*w\.type\s*!==\s*'NPC Uma'\)\.length;"
new_champ = """const allTrainerWins = (this.data.winners || []).filter(w => w.trainer === name && !NPC_PROFILES[w.uma] && w.type !== 'NPC Uma');
                const championships = allTrainerWins.filter(w => !w.rankLabel).length;
                const criteriaWins = allTrainerWins.filter(w => w.rankLabel);"""

text = re.sub(old_champ, new_champ, text, count=1)

# Replace achievements line
old_ach = r"if\s*\(championships\s*>\s*0\)\s*achievements\.push\(\{.*?'Sus Cup Champion'.*?\}\);"
new_ach = """if (championships > 0) achievements.push({ icon: '🏆', title: 'Sus Cup Champion', desc: `Won ${championships} Championship${championships > 1 ? 's' : ''}` });
                criteriaWins.forEach(cw => {
                    achievements.push({ icon: '🏅', title: 'Criteria Winner', desc: `${cw.rankLabel} in ${cw.cup}` });
                });"""

text = re.sub(old_ach, new_ach, text, count=1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated showPlayer')
