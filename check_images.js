const https = require('https');

const urls = [
  'https://www.gadigitalsolutions.com/images/GADS%20LOGO-01.svg',
  'https://www.gadigitalsolutions.com/images/logo.png',
  'https://www.gadigitalsolutions.com/images/Website_Maintenance.jpg'
];

urls.forEach(u => {
  https.get(u, res => {
    console.log(u, 'Status:', res.statusCode);
  }).on('error', err => console.log(u, 'Error:', err.message));
});
