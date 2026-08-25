const fs = require('fs');

const content = fs.readFileSync('suscup1.html', 'utf8');

// 1. Rewrite UMA_PROFILES
const start = content.indexOf('const UMA_PROFILES = {');
const end = content.indexOf('const NPC_PROFILES = {');
let profilesText = content.substring(start, end);

profilesText = profilesText.split('\n').map(line => {
    const match = line.match(/"([^"]+)":\s*\{[^}]*id:\s*(\d+)/);
    if (match) {
        const name = match[1];
        const id = match[2];
        const imageUrl = 'https://gametora.com/images/umamusume/characters/chara_stand_' + id.substring(0,4) + '_' + id + '.png';
        const urlMatch = line.match(/url:\s*"([^"]+)"/);
        let url = urlMatch ? urlMatch[1] : '';
        // Fix URLs to be just slugs if they have IDs
        url = url.replace(/\/(\d+)-/, '/');
        const versionMatch = line.match(/version:\s*"([^"]+)"/);
        const version = versionMatch ? versionMatch[1] : '';
        
        return `            "${name}": { version: "${version}", url: "${url}", imageUrl: "${imageUrl}" },`;
    }
    return line;
}).join('\n');

let newContent = content.substring(0, start) + profilesText + content.substring(end);

// 2. Rewrite getUmaImage
const imgStart = newContent.indexOf('getUmaImage(name, large = false) {');
const imgEnd = newContent.indexOf('getRankHtml(diff) {');
const newImgLogic = `getUmaImage(name, large = false) {
                const profile = CHARACTER_PROFILES[name];
                if (profile?.imageUrl) {
                    const cls = \`\${large ? 'uma-image-large' : 'uma-image'}\${NPC_PROFILES[name] ? ' npc-face' : ''}\`;
                    return \`<img class="\${cls}" src="\${profile.imageUrl}" alt="\${name}" loading="lazy">\`;
                }
                return \`<div class="avatar-circle">\${this.getInitials(name)}</div>\`;
            },

            `;
newContent = newContent.substring(0, imgStart) + newImgLogic + newContent.substring(imgEnd);

// 3. Fix initial data for Nice Nature and Super Creek and King Halo to be slug URLs
newContent = newContent.replace(/103801-nice-nature/g, 'nice-nature');
newContent = newContent.replace(/101601-super-creek/g, 'super-creek');
newContent = newContent.replace(/104401-king-halo/g, 'king-halo');

fs.writeFileSync('suscup1.html', newContent);
console.log('updated suscup1.html');
