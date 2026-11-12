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
  const noScripts = homeHtml.replace(/<script[\s\S]*?<\/script>/gi, '').replace(/<style[\s\S]*?<\/style>/gi, '');
  const lines = noScripts.split('\n').map(l => l.trim()).filter(l => l.length > 0);
  
  // Print lines 120 to 300
  console.log(lines.slice(120, 280).join('\n'));
})();
