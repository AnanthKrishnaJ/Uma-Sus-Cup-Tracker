const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('../index.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on('jsdomError', (err) => {
  console.error('jsdomError:', err.message, err.stack);
});
virtualConsole.on('error', (err) => {
  // console.error('Virtual Console Error:', err);
});

try {
  const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole, url: "http://localhost/" });
  
  dom.window.console.error = function(...args) {
    console.log('BROWSER CONSOLE ERROR:', ...args);
  };
  
  // App.init() normally runs on DOMContentLoaded. We force it just in case.
  dom.window.eval('try { App.init(); } catch(e) { console.error("INIT ERROR:", e.stack); }');
  dom.window.eval('try { App.navigate("players"); } catch(e) { console.error("NAV ERROR:", e.stack); }');
  dom.window.eval('try { App.navigate("compare"); } catch(e) { console.error("NAV ERROR:", e.stack); }');
  
} catch (e) {
  console.error('Exception:', e.message);
}
