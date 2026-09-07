const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Normalize line endings for replacement
const normalizedHtml = html.replace(/\r\n/g, '\n');

// 1. Add running styles breakdown to player profile
const insertAfterStr = `<div style="font-size:0.9rem; color:var(--text-muted);">\${leastUsedStrategy.runs} Races</div>
                                </div>
                            </div>`;

const breakdownHtml = `
                            <div style="margin-top:20px; padding-top:15px; border-top:1px solid var(--border-color); display:flex; flex-wrap:wrap; gap:10px; justify-content:center; align-items:center;">
                                <div style="font-size:0.8rem; font-weight:800; color:var(--text-muted); width:100%; text-align:center; margin-bottom:5px;">ALL STYLES USED</div>
                                \${Object.entries(stratStats).filter(([name, data]) => data.runs > 0).map(([name, data]) => \`
                                    <span class="badge" style="background:\${stratColors[name] || '#999'}; font-size:0.9rem; padding:6px 14px; border-radius:20px;">\${name} &bull; \${data.runs} Races (\${data.wins} Wins)</span>
                                \`).join('')}
                            </div>
`;

if (normalizedHtml.includes(insertAfterStr) && !normalizedHtml.includes('ALL STYLES USED')) {
    html = normalizedHtml.replace(insertAfterStr, insertAfterStr + breakdownHtml);
    console.log('Successfully injected running style breakdown');
} else {
    console.log('Failed to inject running style breakdown');
}

fs.writeFileSync('index.html', html, 'utf8');
