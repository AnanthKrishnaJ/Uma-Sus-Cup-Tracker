const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('../index.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on('jsdomError', (err) => {
  console.error('jsdomError:', err.stack, err.detail);
});

try {
  const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole });
  
  dom.window.console.error = function(...args) {
    console.log('BROWSER CONSOLE ERROR:', ...args);
  };
  
  dom.window.eval('try { App.init(); } catch(e) { console.error("INIT ERROR:", e.stack); }');
  dom.window.eval('try { App.navigate("players"); } catch(e) { console.error("NAV ERROR:", e.stack); }');
  
} catch (e) {
  console.error('Exception:', e.message);
}
