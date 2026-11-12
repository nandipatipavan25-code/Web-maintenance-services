const fs = require('fs');
const html = fs.readFileSync('original_maintenance_page.html', 'utf8');

const h1Index = html.indexOf('<h1');
const footerIndex = html.indexOf('<footer');
const mainContent = html.substring(h1Index, footerIndex);

// Let's print out the sections in slices or check structure
fs.writeFileSync('main_content_extracted.html', mainContent, 'utf8');
console.log('Saved main_content_extracted.html, length:', mainContent.length);
