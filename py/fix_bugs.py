import re

content = open('suscup1.html', 'r', encoding='utf-8').read()

# Fix the missing view-add-race tag
content = content.replace(
    '        </div>\n\n            <div class="card">\n                <form id="form-add-race">',
    '        </div>\n\n        <!-- ADD RACE VIEW -->\n        <div id="view-add-race" class="view-section">\n            <div class="card">\n                <form id="form-add-race">'
)

# Fix renderCompare code
def fix_compare(match):
    s = match.group(0)
    s = s.replace('.winRate.toFixed(1)', '.winRate')
    s = s.replace('.podiumRate', '.top3Rate')
    s = s.replace('.consistency.toFixed(1)', '.consistencyScore')
    s = s.replace('.consistency', '.consistencyScore')
    s = s.replace('.experience', '.experienceScore')
    s = s.replace('.races', '.runs')
    s = s.replace('.wins', '.w')
    s = s.replace('.avgPos', '.avgFinish')
    return s

# Find renderCompare block
start_idx = content.find('renderCompare() {')
end_idx = content.find('            // --- UI LOGIC ---', start_idx)

if start_idx != -1 and end_idx != -1:
    compare_block = content[start_idx:end_idx]
    fixed_block = fix_compare(re.match(r'(?s).*', compare_block))
    content = content[:start_idx] + fixed_block + content[end_idx:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixes applied.")
