import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

format_date_fn = '''            formatDate(dateStr) {
                if (!dateStr) return '';
                try {
                    const d = new Date(dateStr.split(',')[0].trim());
                    if (isNaN(d.getTime())) return dateStr.split(',')[0].trim();
                    const y = d.getFullYear();
                    const m = String(d.getMonth() + 1).padStart(2, '0');
                    const day = String(d.getDate()).padStart(2, '0');
                    return `${y}-${m}-${day}`;
                } catch(e) {
                    return dateStr.split(',')[0].trim();
                }
            },

            getInitials(name) {'''

html = html.replace('            getInitials(name) {', format_date_fn)

# Dashboard latest champion date
html = html.replace('${latestRace.date || \'\'}', '${App.formatDate(latestRace.date)}')
html = html.replace('${latestRace.date || ""}', '${App.formatDate(latestRace.date)}')

# History view date
html = html.replace('${race.date}  ${race.course}', '${App.formatDate(race.date)}  ${race.course}')
html = html.replace('${race.date} ${race.course}', '${App.formatDate(race.date)} ${race.course}')

# Championship history date
old_champ = '''                    const rawDate = winner.date || (race ? race.date : '');
                    const dateStr = rawDate ? rawDate.split(",")[0].trim() : '';'''
new_champ = '''                    const rawDate = winner.date || (race ? race.date : '');
                    const dateStr = App.formatDate(rawDate);'''
html = html.replace(old_champ, new_champ)

old_champ_2 = '''                    const rawDate = winner.date || (race ? race.date : '');
                    const dateStr = rawDate ? rawDate.split(',')[0].trim() : '';'''
html = html.replace(old_champ_2, new_champ)

# Compare view / Player profiles uses date inside map for recent races
html = html.replace("${race.date.split(',')[0]}", "${App.formatDate(race.date)}")
html = html.replace("race.date && `${race.date.split(',')[0]}`", "race.date && `${App.formatDate(race.date)}`")
html = html.replace("${firstUse.date || ''}", "${App.formatDate(firstUse.date)}")
html = html.replace("${winner.date}", "${App.formatDate(winner.date)}")
html = html.replace("${race.date}", "${App.formatDate(race.date)}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
