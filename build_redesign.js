const fs = require('fs');

const origHtml = fs.readFileSync('original_maintenance_page.html', 'utf8');

// We will build the redesigned HTML with 100% exact text preserved.
// Let's create build_redesign.js to construct the entire clean HTML.
