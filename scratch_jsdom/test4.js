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
  
  dom.window.eval('try { App.init(); } catch(e) { console.error("INIT ERROR:", e.stack); }');
  dom.window.eval('try { App.navigate("players"); } catch(e) { console.error("NAV ERROR:", e.stack); }');
  
} catch (e) {
  console.error('Exception:', e.message);
}
