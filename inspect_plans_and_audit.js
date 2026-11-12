const https = require('https');

function fetchPage(url) {
  return new Promise((resolve) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => { data += chunk; });
      res.on('end', () => resolve(data));
    }).on('error', () => resolve(''));
  });
}

(async () => {
  const html = await fetchPage('https://www.gadigitalsolutions.com/services/website-maintenance');
  
  // Find where plans start
  const planIdx = html.indexOf('Website Maintenance Plans from GA Digital Solutions');
  console.log('=== PLANS SECTION ===');
  console.log(html.substring(planIdx, planIdx + 3000));

  // Find where Audit section is
  const auditIdx = html.indexOf('Get Your Free 20-Point Website Health Audit');
  console.log('\n=== AUDIT SECTION ===');
  console.log(html.substring(auditIdx, auditIdx + 2000));
})();
