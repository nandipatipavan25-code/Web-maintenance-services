const https = require('https');

https.get('https://www.gadigitalsolutions.com/images/GADS%20LOGO-01.svg', (res) => {
  let data = '';
  res.on('data', chunk => { data += chunk; });
  res.on('end', () => {
    console.log('SVG length:', data.length);
    console.log('First 1500 chars of SVG:');
    console.log(data.slice(0, 1500));
  });
}).on('error', err => console.error(err));
