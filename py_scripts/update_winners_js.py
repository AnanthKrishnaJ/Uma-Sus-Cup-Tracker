import re

html_path = r'c:\Users\anant\OneDrive\Desktop\guess\Uma race tracker\.vscode\suscup1.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. renderHistory
history_pattern = re.compile(
    r'const winner = winners\.find\(item => item\.cup === `Sus Cup \$\{race\.cupNumber\}`\) \|\| race\.participants\.find\(p => p\.pos === 1\);.*?<p style="margin-top:12px; font-weight:800;">Winner: \$\{winner\?\.trainer \|\| winner\?\.player \|\| \'Not recorded\'\}.*?\$\{winner\?\.uma \|\| \'Not recorded\'\}</p>',
    re.DOTALL
)

history_replacement = '''const cupWinners = winners.filter(item => item.cup === `Sus Cup ${race.cupNumber}`);
                    let winnersHtml = '';
                    if (cupWinners.length > 0) {
                        winnersHtml = cupWinners.map(w => `<p style="margin-top:4px; font-weight:800; font-size: 0.95rem;">${w.rankLabel || 'Winner'}: ${w.trainer} <span style="opacity:0.7">&mdash;</span> ${w.uma}</p>`).join('');
                    } else {
                        const winner = race.participants.find(p => p.pos === 1);
                        winnersHtml = `<p style="margin-top:12px; font-weight:800;">Winner: ${winner?.player || 'Not recorded'} <span style="opacity:0.7">&mdash;</span> ${winner?.uma || 'Not recorded'}</p>`;
                    }'''

# Replace the block up to the Winner <p> tag. Wait, I also need to replace the original <p> tag with the new ${winnersHtml}.
def history_repl(m):
    return history_replacement + f'\n                        <div style="margin-top:12px;">${{winnersHtml}}</div>'

text = history_pattern.sub(history_repl, text)

# 2. renderDashboard - Championship Trainer
dashboard_pattern = re.compile(
    r'<div><strong>\$\{winner\.trainer\}</strong><span>Champion Trainer</span></div>'
)
dashboard_replacement = r'<div><strong>${winner.trainer}</strong><span>${winner.rankLabel || \'Champion Trainer\'}</span></div>'
text = dashboard_pattern.sub(dashboard_replacement, text)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("JS modifications applied successfully!")
