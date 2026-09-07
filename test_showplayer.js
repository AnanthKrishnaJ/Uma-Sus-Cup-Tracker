const fs = require('fs');
const { JSDOM } = require('jsdom');

let html = fs.readFileSync('index.html', 'utf8');
// Expose App to window
html = html.replace('const App = {', 'window.App = {');

const dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost/" });

dom.window.addEventListener('error', (event) => {
    console.error('Browser Error:', event.error);
});

// Wait for DOM to load
setTimeout(() => {
    try {
        console.log('Calling App.showPlayer("Agnes")...');
        dom.window.App.init(); // ensure init happens if DOMContentLoaded didn't fire
        dom.window.App.showPlayer('Agnes');
        console.log('Finished App.showPlayer');
    } catch (e) {
        console.error('Exception in showPlayer:', e);
    }
}, 1000);
