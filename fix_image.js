const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf-8');

const oldFunc = `getUmaImage(umaId, searchNameFallback = null, large = false) {
                let uma = UMA_DATABASE[umaId];
                if (!uma && (umaId || searchNameFallback)) {
                    const strToSearch = String(umaId || searchNameFallback).toLowerCase().replace(/-/g, ' ');
                    const matchedKey = Object.keys(UMA_DATABASE).find(k => k.toLowerCase().includes(String(umaId || searchNameFallback).toLowerCase().replace(/-/g, '')) || UMA_DATABASE[k].name.toLowerCase() === strToSearch);
                    if (matchedKey) uma = UMA_DATABASE[matchedKey];
                }

                if (uma && uma.image) {`;

const newFunc = `getUmaImage(umaId, searchNameFallback = null, large = false) {
                // If the second parameter is a boolean, it's actually 'large'
                if (typeof searchNameFallback === 'boolean') {
                    large = searchNameFallback;
                    searchNameFallback = null;
                }
                
                let uma = UMA_DATABASE[umaId];
                
                // Fallback 1: Search by Name
                if (!uma && searchNameFallback) {
                    const strToSearch = String(searchNameFallback).toLowerCase().replace(/-/g, ' ');
                    const matchedKey = Object.keys(UMA_DATABASE).find(k => UMA_DATABASE[k].name.toLowerCase() === strToSearch || UMA_DATABASE[k].name.toLowerCase().includes(strToSearch));
                    if (matchedKey) uma = UMA_DATABASE[matchedKey];
                }
                
                // Fallback 2: Search by ID string
                if (!uma && umaId) {
                    const strToSearch = String(umaId).toLowerCase().replace(/-/g, ' ');
                    const matchedKey = Object.keys(UMA_DATABASE).find(k => k.toLowerCase().includes(strToSearch) || UMA_DATABASE[k].name.toLowerCase() === strToSearch);
                    if (matchedKey) uma = UMA_DATABASE[matchedKey];
                }

                if (uma && uma.image) {`;

html = html.replace(oldFunc, newFunc);
fs.writeFileSync('index.html', html, 'utf-8');
console.log('Fixed getUmaImage fallback');
