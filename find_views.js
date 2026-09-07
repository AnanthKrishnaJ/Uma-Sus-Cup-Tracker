const fs = require('fs');
const lines = fs.readFileSync('index.html', 'utf8').split('\n');
const start = lines.findIndex(l => l.includes('id="view-dashboard"'));
console.log(lines.slice(start, start + 100).join('\n'));
