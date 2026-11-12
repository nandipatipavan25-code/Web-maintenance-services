const https = require('https');
const fs = require('fs');

https.get('https://www.gadigitalsolutions.com/images/GADS%20LOGO-01.svg', (res) => {
  let data = '';
  res.on('data', chunk => { data += chunk; });
  res.on('end', () => {
    fs.writeFileSync('gads_logo.svg', data, 'utf8');
    console.log('Saved gads_logo.svg, length:', data.length);
  });
});
