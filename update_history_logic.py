import json

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_block = text.find('const championshipWinners = this.data.winners')
end_block = text.find('const maxCupNum =', start_block)

new_js = """                const cupData = new Map();

                this.data.winners.forEach(winner => {
                    if (NPC_PROFILES[winner.uma] || winner.type === 'NPC Uma') return;
                    
                    const cupNumMatch = String(winner.cup).match(/\d+/);
                    const cupNum = cupNumMatch ? parseInt(cupNumMatch[0]) : 0;
                    if (cupNum === 0) return;
                    
                    if (!cupData.has(cupNum)) {
                        cupData.set(cupNum, {
                            cup: 'Sus Cup ' + cupNum,
                            cupNum: cupNum,
                            dateStr: '',
                            rawDate: winner.date || '',
                            players: new Set()
                        });
                    }
                    
                    const pName = winner.trainer || winner.player;
                    if (pName) {
                        cupData.get(cupNum).players.add(pName);
                    }
                });

                this.data.races.forEach(race => {
                    const cupNumMatch = String(race.cupNumber || race.id).match(/\d+/);
                    const cupNum = cupNumMatch ? parseInt(cupNumMatch[0]) : 0;
                    if (cupNum === 0) return;

                    if (!cupData.has(cupNum)) {
                        cupData.set(cupNum, {
                            cup: 'Sus Cup ' + cupNum,
                            cupNum: cupNum,
                            dateStr: '',
                            rawDate: race.date || '',
                            players: new Set()
                        });
                    } else {
                        if (!cupData.get(cupNum).rawDate && race.date) {
                            cupData.get(cupNum).rawDate = race.date;
                        }
                    }

                    if (cupData.get(cupNum).players.size === 0 && race.participants) {
                        const firstPlace = race.participants.filter(p => parseInt(p.pos) === 1 || parseInt(p.position) === 1);
                        firstPlace.forEach(p => {
                            if (p.player && p.player !== 'NPC') {
                                cupData.get(cupNum).players.add(p.player);
                            }
                        });
                    }
                });

                const championshipWinners = Array.from(cupData.values())
                    .map(data => {
                        let finalDate = 'Not recorded';
                        if (data.rawDate) {
                            finalDate = App.formatDate(data.rawDate) || 'Not recorded';
                        }
                        
                        return {
                            cup: data.cup,
                            cupNum: data.cupNum,
                            dateStr: finalDate,
                            playerStr: Array.from(data.players).join(', ') || 'Not recorded'
                        };
                    })
                    .sort((a, b) => b.cupNum - a.cupNum);

                """

text = text[:start_block] + new_js + text[end_block:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html logic.")
