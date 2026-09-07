const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('../index.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on('error', (err) => {
  console.error('JSDOM Error:', err);
});
virtualConsole.on('log', (msg) => {
  console.log('JSDOM Log:', msg);
});

try {
  const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole });
  console.log('JSDOM Initialized Successfully');
} catch (e) {
  console.error('Exception during init:', e);
}
