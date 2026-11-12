const fs = require('fs');
const html = fs.readFileSync('original_maintenance_page.html', 'utf8');

const h1Index = html.indexOf('<h1');
const footerIndex = html.indexOf('<footer');

console.log('--- BEFORE H1 (last 500 chars) ---');
console.log(html.substring(h1Index - 500, h1Index));

console.log('--- AFTER FOOTER (first 500 chars) ---');
console.log(html.substring(footerIndex, footerIndex + 500));
