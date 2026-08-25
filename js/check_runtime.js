const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('suscup1.html', 'utf8');
const dom = new JSDOM(html, { runScripts: "dangerously" });

// Wait for a short time to let scripts run
setTimeout(() => {
    console.log("Done");
}, 1000);
