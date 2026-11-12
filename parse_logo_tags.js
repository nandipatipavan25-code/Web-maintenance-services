const fs = require('fs');
const svg = fs.readFileSync('gads_logo.svg', 'utf8');

// Print all elements
console.log('SVG structure:');
const matches = [...svg.matchAll(/<([a-z]+)[^>]*>/gi)].map(m => m[0]);
console.log('Total tags:', matches.length);
console.log('Unique tags:', [...new Set(matches.map(m => m.split(' ')[0].replace('<', '')))])
