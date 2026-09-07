import re

with open('index.html', 'r', encoding='utf8') as f:
    html = f.read()

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

# Let's find exactly where grid-2 starts
# Searching for: <div class="grid-2" style="margin-bottom:30px;">
# And ending at the </div> that closes it.
import textwrap

match = re.search(r'<div class="grid-2" style="margin-bottom:30px;">\s*<div class="card" id="latest-cup-summary"></div>\s*<div class="card">.*?</div>\s*</div>', html, re.DOTALL)
if match:
    html = html.replace(match.group(0), new_grid2)
    print("Replaced grid-2 successfully")
else:
    print("Regex failed to find grid-2 block")
    
with open('index.html', 'w', encoding='utf8') as f:
    f.write(html)
