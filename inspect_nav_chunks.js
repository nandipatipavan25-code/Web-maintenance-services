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
  const homeHtml = await fetchPage('https://www.gadigitalsolutions.com/');
  
  // Look for desktop navigation
  const desktopIdx = homeHtml.indexOf('content-desktop');
  const mobileIdx = homeHtml.indexOf('content-mobile');
  
  console.log('=== DESKTOP NAV CHUNK ===');
  console.log(homeHtml.substring(desktopIdx, desktopIdx + 2500));

  console.log('\n=== MOBILE NAV CHUNK ===');
  console.log(homeHtml.substring(mobileIdx, mobileIdx + 2500));
})();
