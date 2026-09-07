import re

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        # Step 1: Update the resultsHtml div
        # We need to change the max-height to flex: 1
        old_div = """resultsHtml = `<div style="margin-top:20px; max-height: 300px; overflow-y: auto; background: var(--bg-alt); padding: 10px; border-radius: 8px;">"""
        new_div = """resultsHtml = `<div style="margin-top:20px; flex: 1; overflow-y: auto; background: var(--bg-alt); padding: 10px; border-radius: 8px; min-height: 300px;">"""
        
        if old_div in content:
            content = content.replace(old_div, new_div)
        else:
            print("Could not find the old_div string!")

        # Step 2: Make the innerHTML wrapper flex
        old_inner = """document.getElementById('latest-cup-summary').innerHTML = `
                    <span class="eyebrow">${this.dashboardRaceIndex === 0 ? 'Latest champion' : 'Champion'}</span>
                    <h3 style="font-size:1.7rem; margin:15px 0 8px;">${latestRace ? `${latestRace.cupName || `Sus Cup ${latestRace.cupNumber || latestRace.id}`} / ${latestRace.name || ''}` : 'No races recorded'}</h3>
                    <p style="font-weight:800; margin-bottom:8px;">${latestWinner?.player || 'Not recorded'} — ${latestWinner?.uma || 'Not recorded'}</p>
                    <p style="color:var(--text-muted); font-size:.85rem; margin-bottom:15px;">${latestRace ? `${latestRace.date || ''} — ${latestRace.course || ''} ${latestRace.distance || ''} ${latestRace.surface || ''}` : ''}</p>
                    ${resultsHtml}
                `;"""
                
        new_inner = """const summaryCard = document.getElementById('latest-cup-summary');
                summaryCard.style.display = 'flex';
                summaryCard.style.flexDirection = 'column';
                summaryCard.innerHTML = `
                    <div style="flex-shrink: 0;">
                        <span class="eyebrow">${this.dashboardRaceIndex === 0 ? 'Latest champion' : 'Champion'}</span>
                        <h3 style="font-size:1.7rem; margin:15px 0 8px;">${latestRace ? `${latestRace.cupName || `Sus Cup ${latestRace.cupNumber || latestRace.id}`} / ${latestRace.name || ''}` : 'No races recorded'}</h3>
                        <p style="font-weight:800; margin-bottom:8px;">${latestWinner?.player || 'Not recorded'} — ${latestWinner?.uma || 'Not recorded'}</p>
                        <p style="color:var(--text-muted); font-size:.85rem; margin-bottom:15px;">${latestRace ? `${latestRace.date || ''} — ${latestRace.course || ''} ${latestRace.distance || ''} ${latestRace.surface || ''}` : ''}</p>
                    </div>
                    ${resultsHtml}
                `;"""

        # Replace might fail if backticks or spaces are different.
        # Let's do a more robust regex replace.
        content = re.sub(
            r"document\.getElementById\('latest-cup-summary'\)\.innerHTML = `[\s\S]*?\$\{resultsHtml\}\s*`;",
            new_inner.replace("`Sus Cup ${latestRace.cupNumber || latestRace.id}`", "\\`Sus Cup ${latestRace.cupNumber || latestRace.id}\\`"),
            content
        )

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
            
        print("Updated dashboard flex styles successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
