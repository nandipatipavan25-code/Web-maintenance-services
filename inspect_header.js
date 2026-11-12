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
  const header = homeHtml.match(/<header[\s\S]*?<\/header>/i)?.[0] || '';
  console.log('=== HEADER HTML (first 3000 chars) ===');
  console.log(header.slice(0, 3000));

  console.log('\n=== HOMEPAGE HERO / FIRST SECTIONS ===');
  const main = homeHtml.match(/<body[\s\S]*?<\/body>/i)?.[0] || '';
  console.log(main.slice(0, 4000));
})();
