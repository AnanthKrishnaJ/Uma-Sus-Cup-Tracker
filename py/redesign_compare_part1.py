import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update buildLeaderboards
# Find: `name: p.player, runs: 0, w: 0, secondPlaces: 0, thirdPlaces: 0,`
# Replace with: `name: p.player, runs: 0, w: 0, secondPlaces: 0, thirdPlaces: 0, fourthPlaces: 0, fifthPlaces: 0,`
# Also need to track umaStats per player for Best Uma calculation

leaderboards_old = """                                name: p.player, runs: 0, w: 0, secondPlaces: 0, thirdPlaces: 0,
                                podiums: 0, top5: 0, sumPos: 0, bestFinish: 99, worstFinish: 0,
                                firstCup: race.cupNumber, latestCup: race.cupNumber,
                                uniqueUmas: new Set(), history: []"""

leaderboards_new = """                                name: p.player, runs: 0, w: 0, secondPlaces: 0, thirdPlaces: 0, fourthPlaces: 0, fifthPlaces: 0,
                                podiums: 0, top4: 0, top5: 0, sumPos: 0, bestFinish: 99, worstFinish: 0,
                                firstCup: race.cupNumber, latestCup: race.cupNumber,
                                uniqueUmas: new Set(), history: [], umaStats: {}"""

if leaderboards_old in content:
    content = content.replace(leaderboards_old, leaderboards_new)
    print("Updated player object initialization.")
else:
    print("Could not find player object initialization.")

# Find:
#                          if (p.pos === 1) pl.w++;
#                          if (p.pos === 2) pl.secondPlaces++;
#                          if (p.pos === 3) pl.thirdPlaces++;
#                          if (p.pos <= 3) pl.podiums++;
#                          if (p.pos <= 5) pl.top5++;

stats_old = """                        if (p.pos === 1) pl.w++;
                        if (p.pos === 2) pl.secondPlaces++;
                        if (p.pos === 3) pl.thirdPlaces++;
                        if (p.pos <= 3) pl.podiums++;
                        if (p.pos <= 5) pl.top5++;
                        if (p.pos < pl.bestFinish) pl.bestFinish = p.pos;
                        if (p.pos > pl.worstFinish) pl.worstFinish = p.pos;
                        pl.latestCup = race.cupNumber;
                        pl.uniqueUmas.add(p.umaId);"""

stats_new = """                        if (p.pos === 1) pl.w++;
                        if (p.pos === 2) pl.secondPlaces++;
                        if (p.pos === 3) pl.thirdPlaces++;
                        if (p.pos === 4) pl.fourthPlaces++;
                        if (p.pos === 5) pl.fifthPlaces++;
                        if (p.pos <= 3) pl.podiums++;
                        if (p.pos <= 4) pl.top4++;
                        if (p.pos <= 5) pl.top5++;
                        if (p.pos < pl.bestFinish) pl.bestFinish = p.pos;
                        if (p.pos > pl.worstFinish) pl.worstFinish = p.pos;
                        pl.latestCup = race.cupNumber;
                        pl.uniqueUmas.add(p.umaId);
                        
                        if (!pl.umaStats[p.umaId]) {
                            pl.umaStats[p.umaId] = { runs: 0, wins: 0, podiums: 0, name: p.uma };
                        }
                        pl.umaStats[p.umaId].runs++;
                        if (p.pos === 1) pl.umaStats[p.umaId].wins++;
                        if (p.pos <= 3) pl.umaStats[p.umaId].podiums++;"""

if stats_old in content:
    content = content.replace(stats_old, stats_new)
    print("Updated player stats accumulation.")
else:
    print("Could not find player stats accumulation.")
    
# 2. Add html2canvas library above chart.js
html2canvas_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>'
chartjs_script = '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>'
if chartjs_script in content and html2canvas_script not in content:
    content = content.replace(chartjs_script, f"{html2canvas_script}\n    {chartjs_script}")
    print("Added html2canvas script.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved modifications.")
