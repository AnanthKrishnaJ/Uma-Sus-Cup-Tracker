import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add dates to evolutionData initialization
text = text.replace(
    "const evolutionData = { cups: [], 'Front': [], 'Pace': [], 'Late': [], 'End': [] };",
    "const evolutionData = { cups: [], dates: [], 'Front': [], 'Pace': [], 'Late': [], 'End': [] };"
)

# 2. Add pushing date when cup is added
text = text.replace(
    "evolutionData.cups.push(h.cup);",
    "evolutionData.cups.push(h.cup);\n                        evolutionData.dates.push(h.date || '');"
)

# 3. Update the labels mapping for the chart
text = text.replace(
    "labels: evolutionData.cups.map(c => 'Cup ' + String(c).replace(/\D/g, '')),",
    "labels: evolutionData.cups.map((c, i) => 'Cup ' + String(c).replace(/\D/g, '') + (evolutionData.dates[i] ? ' (' + App.formatDate(evolutionData.dates[i]) + ')' : '')),"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Evolution date fixed')
