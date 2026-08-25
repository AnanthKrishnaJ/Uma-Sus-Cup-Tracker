import sys

with open('suscup1.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('const NPC_PROFILES = {')
end = content.find('calculateStats() {')

correctCode = """const NPC_PROFILES = {
            "Revival Lyric": { name: "Revival Lyric", japaneseName: "リバイバルリリック", type: "NPC Uma", characterUrl: "https://mobumamusume.net/%E3%83%AA%E3%83%90%E3%82%A4%E3%83%90%E3%83%AB%E3%83%AA%E3%83%AA%E3%83%83%E3%82%AF/", alternativeSourceUrl: "https://z.wikiwiki.jp/rnf0njoslv454htx/topic/370", imageUrl: "https://mobumamusume.net/wp-content/uploads/2021/05/%E3%83%AA%E3%83%90%E3%82%A4%E3%83%90%E3%83%AB%E3%83%AA%E3%83%AA%E3%83%83%E3%82%AF2.png", imageSource: "Revival Lyric face image from the dedicated Mobu Musume character page" },
            "Marine Seagull": { name: "Marine Seagull", type: "NPC Uma", characterUrl: "https://mobumamusume.net/%E3%83%9E%E3%83%AA%E3%83%B3%E3%82%B7%E3%83%BC%E3%82%AC%E3%83%AB/", imageUrl: "https://mobumamusume.net/wp-content/uploads/2021/09/%E3%83%9E%E3%83%AA%E3%83%B3%E3%82%B7%E3%83%BC%E3%82%AC%E3%83%AB-164x300.jpg", imageSource: "Marine Seagull image from the dedicated Mobu Musume character page" },
            "Reverent": { name: "Reverent", type: "NPC Uma", characterUrl: "https://mobumamusume.net/name_list/", imageUrl: "", imageSource: "No verified dedicated character image available yet" },
            "Cithara Rhythm": { name: "Cithara Rhythm", type: "NPC Uma", characterUrl: "https://mobumamusume.net/name_list/", imageUrl: "", imageSource: "No verified dedicated character image available yet" },
            "Bravo Deux": { name: "Bravo Deux", type: "NPC Uma", characterUrl: "https://mobumamusume.net/name_list/", imageUrl: "", imageSource: "No verified dedicated character image available yet" }
            ,"Venabulum": { name: "Venabulum", type: "NPC Uma", characterUrl: null, imageUrl: null }
            ,"Jewel Onyx": { name: "Jewel Onyx", type: "NPC Uma", characterUrl: null, imageUrl: null }
            ,"Basal Shoot": { name: "Basal Shoot", type: "NPC Uma", characterUrl: null, imageUrl: null }
            ,"Keyboard Rhythm": { name: "Keyboard Rhythm", type: "NPC Uma", characterUrl: null, imageUrl: null }
            ,"Hearty Letter": { name: "Hearty Letter", type: "NPC Uma", characterUrl: null, imageUrl: null }
            ,"Krasnaya": { name: "Krasnaya", type: "NPC Uma", characterUrl: null, imageUrl: null }
            ,"Dunna": { name: "Dunna", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: "", imageSource: "Name verified against the Umamusume Wiki mob-racer directory" }
            ,"Gold Chouchou": { name: "Gold Chouchou", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: "", imageSource: "Name verified against the Umamusume Wiki mob-racer directory" }
            ,"Chalemie Rhythm": { name: "Chalemie Rhythm", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: "", imageSource: "Name verified against the Umamusume Wiki mob-racer directory" }
            ,"Aqua Spring": { name: "Aqua Spring", type: "NPC Uma", characterUrl: "https://mobumamusume.net/%E3%82%A2%E3%82%AF%E3%82%A2%E3%82%B9%E3%83%97%E3%83%AA%E3%83%B3%E3%82%B0/", imageUrl: "https://mobumamusume.net/wp-content/uploads/2021/07/%E3%82%A2%E3%82%AF%E3%82%A2%E3%82%B9%E3%83%97%E3%83%AA%E3%83%B3%E3%82%B0%EF%BC%92.png", imageSource: "Aqua Spring close-up from the dedicated Mobu Musume character page" }
            ,"Bridge Comp": { name: "Bridge Comp", type: "NPC Uma", characterUrl: "https://mobumamusume.net/%E3%83%96%E3%83%AA%E3%83%83%E3%82%B8%E3%82%B3%E3%83%B3%E3%83%97/", imageUrl: "https://mobumamusume.net/wp-content/uploads/2021/08/%E3%83%96%E3%83%AA%E3%83%83%E3%82%B8%E3%82%B3%E3%83%B3%E3%83%97_le2.jpg" }
            ,"Navigate Light": { name: "Navigate Light", type: "NPC Uma", characterUrl: "https://mobumamusume.net/%E3%83%8A%E3%83%93%E3%82%B2%E3%83%BC%E3%83%88%E3%83%A9%E3%82%A4%E3%83%88/", imageUrl: "https://mobumamusume.net/wp-content/uploads/2021/09/%E3%83%8A%E3%83%93%E3%82%B2%E3%83%BC%E3%83%88%E3%83%A9%E3%82%A4%E3%83%88.jpg" }
            ,"Mini Lotus": { name: "Mini Lotus", type: "NPC Uma", characterUrl: "https://mobumamusume.net/%E3%83%9F%E3%83%8B%E3%83%AD%E3%83%BC%E3%82%BF%E3%82%B9/", imageUrl: "https://mobumamusume.net/wp-content/uploads/2021/09/%E3%83%9F%E3%83%8B%E3%83%AD%E3%83%BC%E3%82%BF%E3%82%B9.jpg" }
            ,"Summer Bonfire": { name: "Summer Bonfire", type: "NPC Uma", characterUrl: "https://mobumamusume.net/%E3%82%B5%E3%83%9E%E3%83%BC%E3%83%9C%E3%83%B3%E3%83%95%E3%82%A1%E3%82%A4%E3%82%A2/", imageUrl: "https://mobumamusume.net/wp-content/uploads/2021/10/%E3%82%B5%E3%83%9E%E3%83%BC%E3%83%9C%E3%83%B3%E3%83%95%E3%82%A1%E3%82%A4%E3%82%A2_2.jpg" }
            ,"Muruga": { name: "Muruga", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: null }
            ,"Mechanical Vapor": { name: "Mechanical Vapor", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: null }
            ,"Insight Catch": { name: "Insight Catch", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: null }
            ,"Ribbon Carol": { name: "Ribbon Carol", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: null }
            ,"Marsyas": { name: "Marsyas", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: null }
            ,"Black Tipped": { name: "Black Tipped", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: null }
            ,"Breeze Chopper": { name: "Breeze Chopper", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: null }
            ,"Speechless Hack": { name: "Speechless Hack", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: null }
            ,"Yggdra Valley": { name: "Yggdra Valley", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: null }
            ,"Flute Rhythm": { name: "Flute Rhythm", type: "NPC Uma", characterUrl: "https://umamusu.wiki/Game%3AMob_Umamusume", imageUrl: null }
        };

        const CHARACTER_PROFILES = { ...UMA_PROFILES, ...NPC_PROFILES };

        const App = {
            data: null, stats: null, runnerCount: 0,

            init() {
                this.loadData();
                this.setupNavigation();
                this.setupForm();
                this.navigate('dashboard');
            },

            loadData() {
                const local = localStorage.getItem('sus_cup_db');
                if (local) this.data = JSON.parse(local);
                else { this.data = JSON.parse(JSON.stringify(INITIAL_DATA)); this.saveData(); }
                this.migrateHistoricalRecord();
                this.calculateStats();
            },

            migrateHistoricalRecord() {
                // Ensure all participants in all races have up-to-date image/profile mappings
                this.data.races.forEach(race => {
                    if (race.participants) {
                        race.participants = race.participants.map(participant => ({
                            ...participant,
                            version: CHARACTER_PROFILES[participant.uma]?.version || participant.version,
                            characterUrl: CHARACTER_PROFILES[participant.uma]?.characterUrl || CHARACTER_PROFILES[participant.uma]?.url || participant.characterUrl,
                            imageUrl: CHARACTER_PROFILES[participant.uma]?.imageUrl || "",
                            participantType: CHARACTER_PROFILES[participant.uma]?.type || "Uma Musume"
                        }));
                    }
                });

                const sourceRace = INITIAL_DATA.races[0];
                let race = this.data.races.find(item => item.id === sourceRace.id);
                if (!race) {
                    race = JSON.parse(JSON.stringify(sourceRace));
                    this.data.races.unshift(race);
                } else {
                    Object.assign(race, {
                        cupNumber: sourceRace.cupNumber, name: sourceRace.name, date: sourceRace.date,
                        images: [...sourceRace.images],
                        time: sourceRace.time, roomId: sourceRace.roomId, course: sourceRace.course,
                        surface: sourceRace.surface, distance: sourceRace.distance, distanceType: sourceRace.distanceType,
                        direction: sourceRace.direction, weather: sourceRace.weather, ground: sourceRace.ground,
                        condition: sourceRace.condition, mood: sourceRace.mood, season: sourceRace.season,
                        restriction: sourceRace.restriction
                    });
                }
                
                INITIAL_DATA.races.slice(1).forEach(sourceRace => {
                    const existingRace = this.data.races.find(item => item.id === sourceRace.id);
                    if (!existingRace) this.data.races.push(JSON.parse(JSON.stringify(sourceRace)));
                    else if (sourceRace.id >= 3) Object.assign(existingRace, JSON.parse(JSON.stringify(sourceRace)));
                    else if (sourceRace.images) existingRace.images = [...sourceRace.images];
                });
                
                // Re-run the update after Object.assign to make sure newly merged races get updated URLs too
                this.data.races.forEach(race => {
                    if (race.participants) {
                        race.participants = race.participants.map(participant => ({
                            ...participant,
                            version: CHARACTER_PROFILES[participant.uma]?.version || participant.version,
                            characterUrl: CHARACTER_PROFILES[participant.uma]?.characterUrl || CHARACTER_PROFILES[participant.uma]?.url || participant.characterUrl,
                            imageUrl: CHARACTER_PROFILES[participant.uma]?.imageUrl || "",
                            participantType: CHARACTER_PROFILES[participant.uma]?.type || "Uma Musume"
                        }));
                    }
                });

                const seededCups = new Set(INITIAL_DATA.winners.map(winner => winner.cup));
                const customWinners = (this.data.winners || []).filter(winner => !seededCups.has(winner.cup));
                this.data.winners = [...INITIAL_DATA.winners.map(winner => JSON.parse(JSON.stringify(winner))), ...customWinners];
                this.data.championships = this.data.winners.reduce((championships, winner) => {
                    if (!NPC_PROFILES[winner.uma] && winner.type !== 'NPC Uma') {
                        championships[winner.uma] = (championships[winner.uma] || 0) + 1;
                    }
                    return championships;
                }, {});
                this.data.npcs = Object.values(NPC_PROFILES).map(npc => ({ ...npc }));
                this.data.winners = this.data.winners.map(winner => ({
                    ...winner,
                    version: CHARACTER_PROFILES[winner.uma]?.version || winner.version,
                    url: CHARACTER_PROFILES[winner.uma]?.characterUrl || CHARACTER_PROFILES[winner.uma]?.url || winner.url,
                    race: winner.race || (this.data.races.find(r => r.cupName === winner.cup)?.name || ""),
                    result: winner.result || (this.data.races.find(r => r.cupName === winner.cup)?.participants.find(p => p.pos === 1)?.gap || "")
                }));
                localStorage.setItem('sus_cup_db', JSON.stringify(this.data));
            },

            saveData() {
                localStorage.setItem('sus_cup_db', JSON.stringify(this.data));
                this.calculateStats();
            },

            resetData() {
                if(confirm("Reset all data back to the demo SUS CUP 1 database?")) {
                    localStorage.removeItem('sus_cup_db');
                    this.loadData(); this.navigate('dashboard');
                }
            },

            exportData() {
                const str = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(this.data));
                const a = document.createElement('a');
                a.href = str; a.download = "sus_cup_backup.json"; a.click();
            },

            importData(e) {
                const file = e.target.files[0];
                if (!file) return;
                const reader = new FileReader();
                reader.onload = (ev) => {
                    try {
                        const parsed = JSON.parse(ev.target.result);
                        if(parsed.races) { this.data = parsed; this.saveData(); this.navigate('dashboard'); }
                    } catch(err) { alert("Invalid JSON file."); }
                    e.target.value = '';
                };
                reader.readAsText(file);
            },

            // --- STATISTICS ENGINE ---
            """

new_content = content[:start] + correctCode + content[end:]

with open('suscup1.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Fixed!")
