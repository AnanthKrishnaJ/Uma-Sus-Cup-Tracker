const fs = require('fs');
const vm = require('vm');
const content = fs.readFileSync('suscup1.html', 'utf8');

// Extract the script tag content
const scriptMatch = content.match(/<script>([\s\S]*?)<\/script>/);
if (scriptMatch) {
    const scriptContent = scriptMatch[1];
    try {
        const script = new vm.Script(scriptContent);
        console.log("No syntax errors in JS!");
    } catch (e) {
        console.error("Syntax Error found:", e);
    }
} else {
    console.log("No script tag found.");
}
