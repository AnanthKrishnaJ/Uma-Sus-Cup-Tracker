const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('suscup1.html', 'utf8');

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("error", () => { console.error("Error:", ...arguments); });
virtualConsole.on("warn", () => { console.warn("Warn:", ...arguments); });
virtualConsole.on("info", () => { console.info("Info:", ...arguments); });
virtualConsole.on("dir", () => { console.dir("Dir:", ...arguments); });
virtualConsole.on("log", (msg) => { console.log(msg); });

const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole: virtualConsole });

setTimeout(() => {
    console.log("Runtime check complete.");
}, 500);
