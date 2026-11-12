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
  console.log('Total length:', html.length);
  
  // Clean scripts and styles
  const clean = html.replace(/<script[\s\S]*?<\/script>/gi, '').replace(/<style[\s\S]*?<\/style>/gi, '');
  
  // Extract all headings (h1, h2, h3, h4)
  const headings = [...clean.matchAll(/<(h[1-4])[^>]*>([\s\S]*?)<\/\1>/gi)].map(m => ({
    tag: m[1].toLowerCase(),
    text: m[2].replace(/<[^>]+>/g, '').trim()
  }));
  console.log('Headings:', JSON.stringify(headings, null, 2));

  // Extract forms and CTAs
  const forms = [...clean.matchAll(/<form[\s\S]*?<\/form>/gi)];
  console.log('Forms count:', forms.length);
  forms.forEach((f, i) => console.log(`Form ${i+1}:`, f[0].slice(0, 500)));

  // Sample lines
  const lines = clean.split('\n').map(l => l.trim()).filter(l => l.length > 0);
  console.log('\nFirst 80 lines of clean content:');
  console.log(lines.slice(0, 80).join('\n'));
})();
