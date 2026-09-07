const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('../index.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on('jsdomError', (err) => {
  console.error('jsdomError:', err.message);
});
virtualConsole.on('error', (err) => {
  console.error('Virtual Console Error:', err);
});

try {
  const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole, url: "http://localhost/" });
  
  // Try to fire DOMContentLoaded
  dom.window.document.dispatchEvent(new dom.window.Event('DOMContentLoaded'));
  
} catch (e) {
  console.error('Exception:', e.message);
}
