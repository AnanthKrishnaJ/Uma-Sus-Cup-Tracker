const fs = require('fs');
let content = fs.readFileSync('suscup1.html', 'utf8');

const fix = `            loadData() {
                const local = localStorage.getItem('sus_cup_db');
                if (local) this.data = JSON.parse(local);
                else { this.data = JSON.parse(JSON.stringify(INITIAL_DATA)); this.saveData(); }
                this.migrateHistoricalRecord();
                this.calculateStats();
            },

            migrateHistoricalRecord() {`;

content = content.replace('            migrateHistoricalRecord() {', fix);

const fix2 = `            saveData() {
                localStorage.setItem('sus_cup_db', JSON.stringify(this.data));
                this.calculateStats();
            },

            resetData() {`;

content = content.replace('            resetData() {', fix2);

fs.writeFileSync('suscup1.html', content);
console.log('fixed');
