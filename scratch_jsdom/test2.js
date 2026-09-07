const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('../index.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on('error', (err) => {
  console.error('JSDOM Error:', err.message, err.stack);
});

try {
  const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole });
  const document = dom.window.document;
  
  // Simulate App.init() (usually triggered by DOMContentLoaded, but jsdom should trigger it if it's there)
  // Let's explicitly trigger App.navigate('players')
  dom.window.App.navigate('players');
  console.log('Navigated to players successfully');
  
  dom.window.App.navigate('compare');
  console.log('Navigated to compare successfully');
  
} catch (e) {
  console.error('Exception during navigation:', e);
}
