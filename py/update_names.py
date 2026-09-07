import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace in renderHistory
old_history = '<span class="badge" style="background:var(--accent-dark);">SUS CUP ${race.cupNumber}</span>'
new_history = '<span class="badge" style="background:var(--accent-dark);">${(race.cupName || `SUS CUP ${race.cupNumber}`).toUpperCase()}</span>'
text = text.replace(old_history, new_history)

# Replace in renderSearch
old_search = '<span class="badge" style="background:var(--accent-dark);">SUS CUP ${race.cupNumber}</span>'
new_search = '<span class="badge" style="background:var(--accent-dark);">${(race.cupName || `SUS CUP ${race.cupNumber}`).toUpperCase()}</span>'
text = text.replace(old_search, new_search)

# Replace in showRaceDetail
old_detail = "document.getElementById('race-detail-title').innerText = `Sus Cup ${race.cupNumber || race.id}`;"
new_detail = "document.getElementById('race-detail-title').innerText = race.cupName || `Sus Cup ${race.cupNumber || race.id}`;"
text = text.replace(old_detail, new_detail)

# Replace in renderDashboard latest-cup-summary
old_dash = '<h3 style="font-size:1.7rem; margin:15px 0 8px;">${latestRace ? `Sus Cup ${latestRace.cupNumber || latestRace.id} / ${latestRace.name || \'\'}` : \'No races recorded\'}</h3>'
new_dash = '<h3 style="font-size:1.7rem; margin:15px 0 8px;">${latestRace ? `${latestRace.cupName || `Sus Cup ${latestRace.cupNumber || latestRace.id}`} / ${latestRace.name || \'\'}` : \'No races recorded\'}</h3>'
text = text.replace(old_dash, new_dash)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated cup names in UI successfully")
