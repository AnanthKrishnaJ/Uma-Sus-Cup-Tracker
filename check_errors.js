const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  page.on('console', msg => {
    if (msg.type() === 'error') {
      console.log('CONSOLE ERROR:', msg.text());
    } else if (msg.type() === 'warning') {
      console.log('CONSOLE WARNING:', msg.text());
    } else {
      console.log('CONSOLE LOG:', msg.text());
    }
  });
  
  page.on('pageerror', error => {
    console.log('PAGE ERROR:', error.message);
  });
  
  const fileUrl = 'file:///' + path.resolve('.vscode/suscup1.html').replace(/\\/g, '/');
  console.log('Navigating to', fileUrl);
  
  try {
    await page.goto(fileUrl, { waitUntil: 'networkidle' });
    console.log('Page loaded successfully');
    
    // Check if the dashboard is rendered
    const dashboard = await page.locator('#dashboard').count();
    console.log('Dashboard count:', dashboard);
    
    // Check local storage
    const ls = await page.evaluate(() => localStorage.getItem('sus_cup_db'));
    console.log('Local Storage Size:', ls ? ls.length : 0);
  } catch (err) {
    console.error('Failed to load page:', err);
  }
  
  await browser.close();
})();
