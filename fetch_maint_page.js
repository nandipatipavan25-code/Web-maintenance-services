const https = require('https');
const fs = require('fs');

https.get('https://www.gadigitalsolutions.com/services/website-maintenance', (res) => {
  let data = '';
  res.on('data', chunk => { data += chunk; });
  res.on('end', () => {
    fs.writeFileSync('original_maintenance_page.html', data, 'utf8');
    console.log('Saved original_maintenance_page.html, size:', data.length);
  });
}).on('error', (err) => console.error(err));
