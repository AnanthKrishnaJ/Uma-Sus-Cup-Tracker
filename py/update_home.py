import re

with open('index.html', 'r', encoding='utf8') as f:
    html = f.read()

# 1. Update the "What is Sus Cup?" section
new_about = """            <section class="card">
                <div class="record-heading"><span class="eyebrow">The archive / about the series</span><span
                        class="record-count">CREATED BY ANANTH</span></div>
                <h3 style="font-size:2rem; margin-bottom:15px;">What is Sus Cup?</h3>
                <div class="intro-copy">
                    <p><strong>Sus Cup is a community-organized Uma Musume racing tournament series conducted by Agnes, where every race becomes part of a growing history.</strong></p>
                    <p>Each Sus Cup brings players and their chosen Umas to the starting gate, with its own track, race conditions, distance, challengers, and unpredictable moments. From dominant performances to surprise victories and close finishes, every tournament creates a new chapter in the competition.</p>
                    <p>Conducted by <strong>Agnes</strong>, the Sus Cup series is built around competition, rivalry, and the stories created on race day. Every participant leaves their mark, whether they claim the championship or fight their way through the field.</p>
                    <p>The Sus Cup Tracker exists to preserve that history &mdash; recording the races, players, Uma entries, conditions, finishing positions, champions, and the moments that define each tournament.</p>
                    <p><strong>Every Sus Cup. Every race. Every contender. Every finish. Every champion.</strong></p>
                    <p>Because once the race is over, its place in Sus Cup history remains.</p>
                </div>
            </section>"""

# Find the old section and replace it
about_start = html.find('<section class="card">', html.find('id="view-dashboard"'))
about_end = html.find('</section>', about_start) + 10
old_about = html[about_start:about_end]

# It has the creator credit inside it! Let's extract that or just put it at the very bottom of the page.
html = html.replace(old_about, new_about)

# 2. Update the Grid-2 with Aston Machan
new_grid2 = """            <div class="grid-2" style="margin-bottom:30px;">
                <div class="card" id="latest-cup-summary"></div>
                <div class="card" style="display: flex; flex-direction: column; justify-content: space-between;">
                    <div style="margin-bottom: 20px; text-align: center;">
                        <img src="aston_machan.gif" alt="Aston Machan" style="max-width: 100%; border-radius: 8px; max-height: 250px; object-fit: contain;">
                    </div>
                    <div>
                        <span class="eyebrow">Complete tournament archive</span>
                        <h3 style="font-size:1.7rem; margin:10px 0;">Every race, every finish</h3>
                        <p class="intro-copy" style="margin-bottom: 15px;">Browse the full Sus Cup history, including race conditions, all runner entries, NPC/Mob Umas, champions, and final positions.</p>
                        <button class="btn btn-outline" style="width:100%;" onclick="App.navigate('archive')">Open Race Archive <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>
            </div>"""

grid2_start = html.find('<div class="grid-2"', html.find('id="latest-cup-summary"') - 50)
grid2_end = html.find('</div>\n            </div>', grid2_start) + 25
old_grid2 = html[grid2_start:grid2_end]
if 'Open Race' in old_grid2:
    html = html.replace(old_grid2, new_grid2)
else:
    print("Could not find grid-2 properly")

# 3. Add links below history timeline
new_history = """        <div id="view-history" class="view-section">
            <div class="page-header">
                <div>
                    <h2>Sus Cup History</h2>
                    <p>Every tournament, preserved in chronological order</p>
                </div>
            </div>
            <div class="timeline" id="history-timeline"></div>
            <div class="grid-2" style="margin-top: 40px; gap: 20px;">
                <div class="card" style="text-align: center; cursor: pointer;" onclick="App.navigate('players')">
                    <h3 style="margin-bottom: 10px; font-size: 1.5rem;"><i class="fa-solid fa-trophy" style="color:var(--primary)"></i> Player Rankings</h3>
                    <p class="intro-copy">View all-time player stats and victories</p>
                </div>
                <div class="card" style="text-align: center; cursor: pointer;" onclick="App.navigate('umas')">
                    <h3 style="margin-bottom: 10px; font-size: 1.5rem;"><i class="fa-solid fa-star" style="color:var(--gold)"></i> Best Umas</h3>
                    <p class="intro-copy">View the top performing Umas in Sus Cup</p>
                </div>
            </div>
        </div>"""

history_start = html.find('<div id="view-history"')
history_end = html.find('</div>', html.find('id="history-timeline"')) + 15
old_history = html[history_start:history_end]
html = html.replace(old_history, new_history)

# 4. Add the universal footer for "Created and maintained by Ananth"
# We can put this right before </main>
footer = """
            <div style="text-align: center; padding: 40px 20px; color: var(--text-muted); font-size: 0.9rem; margin-top: 40px; border-top: 1px solid var(--border);">
                <strong>Sus Cup Tournament Tracker</strong><br>
                This website was created and maintained by Ananth
            </div>
        </main>"""
if 'This website was created and maintained by Ananth' not in html:
    html = html.replace('</main>', footer)

with open('index.html', 'w', encoding='utf8') as f:
    f.write(html)
print("Updated index.html")
