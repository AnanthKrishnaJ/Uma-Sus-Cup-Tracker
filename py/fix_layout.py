import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

correct = '''            <div class="grid-2" style="margin-bottom:30px; align-items: stretch;">
                <div class="card" id="latest-cup-summary" style="height: 100%; box-sizing: border-box; display: flex; flex-direction: column; margin-bottom: 0;"></div>
                <div class="card" style="height: 100%; box-sizing: border-box; display: flex; flex-direction: column; margin-bottom: 0;">
                    <span class="eyebrow">Complete tournament archive</span>
                    <h3 style="font-size:1.7rem; margin:15px 0 10px;">Every race, every finish</h3>
                    <p class="intro-copy" style="flex-grow: 1;">Browse the full Sus Cup history, including race conditions, all runner
                        entries, NPC/Mob Umas, champions, and final positions.</p>
                    <button class="btn btn-outline" style="margin-top:18px;" onclick="App.navigate('archive')">Open Race
                        Archive <i class="fa-solid fa-arrow-right"></i></button>
                </div>
            </div>

            <div class="grid-4" style="margin-bottom: 40px;" id="dash-stats"></div>
            <div class="card" id="championship-record"></div>

            <div class="grid-2">
                <div>
                    <h3 style="margin-bottom: 20px; display:flex; align-items:center; gap:10px;"><i
                            class="fa-solid fa-trophy" style="color:var(--primary)"></i> Player Rankings</h3>'''

html = re.sub(r'<h3 style="margin-bottom: 20px; display:flex; align-items:center; gap:10px;"><i\s*class="fa-solid fa-trophy" style="color:var\(--primary\)"></i> Player Rankings</h3>', correct, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
