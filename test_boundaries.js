const fs = require('fs');

const origHtml = fs.readFileSync('original_maintenance_page.html', 'utf8');

// Find boundaries
const headEndIdx = origHtml.indexOf('</head>');
const footerIdx = origHtml.indexOf('<footer id="gad-footer"');

console.log('Head end:', headEndIdx, 'Footer start:', footerIdx);
