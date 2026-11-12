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
  
  // Clean up styles and scripts to see actual DOM content
  const noScripts = homeHtml.replace(/<script[\s\S]*?<\/script>/gi, '').replace(/<style[\s\S]*?<\/style>/gi, '');
  
  // Let's print out lines with text and tags
  const lines = noScripts.split('\n').map(l => l.trim()).filter(l => l.length > 0);
  console.log('Total non-empty lines without script/style:', lines.length);
  
  // Print first 120 lines
  console.log(lines.slice(0, 120).join('\n'));
})();
