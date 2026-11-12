const fs = require('fs');

const html = fs.readFileSync('original_maintenance_page.html', 'utf8');

// Find where main content begins (after header) and ends (before footer)
const h1Index = html.indexOf('<h1');
const footerIndex = html.indexOf('<footer');

console.log('H1 index:', h1Index);
console.log('Footer index:', footerIndex);

const mainContent = html.substring(h1Index, footerIndex);
console.log('Main content length:', mainContent.length);

// Let's print out the first 2000 chars of mainContent
console.log('--- START OF MAIN CONTENT ---');
console.log(mainContent.substring(0, 2000));
