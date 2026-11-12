const https = require('https');

https.get('https://www.gadigitalsolutions.com/images/GADS%20LOGO-01.svg', (res) => {
  let data = '';
  res.on('data', chunk => { data += chunk; });
  res.on('end', () => {
    // Find linearGradient or class="c" or main symbol
    const matches = data.match(/<path[^>]*class=["']c["'][^>]*d=["']([^"']*)["']/i);
    if (matches) {
      console.log('Main emblem path (class c):', matches[1].slice(0, 300));
    }
    // Print all styles and elements
    console.log('Defs & styles:', data.match(/<defs[\s\S]*?<\/defs>/i)?.[0]);
    // Look for G / A shape
    const paths = [...data.matchAll(/<path[^>]*>/gi)].map(m => m[0]);
    console.log('Total paths:', paths.length);
  });
});
