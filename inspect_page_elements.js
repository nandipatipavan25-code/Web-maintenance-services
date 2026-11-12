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
  
  // Extract nav links
  const navMatches = [...homeHtml.matchAll(/<nav[\s\S]*?<\/nav>/gi)];
  console.log('Nav found:', navMatches.length);
  if (navMatches[0]) {
    const links = [...navMatches[0][0].matchAll(/<a[^>]*href=["']([^"']*)["'][^>]*>(.*?)<\/a>/gi)].map(m => ({
      href: m[1],
      text: m[2].replace(/<[^>]+>/g, '').trim()
    }));
    console.log('Nav links:', links);
  }

  // Extract form actions / inputs on homepage
  const forms = [...homeHtml.matchAll(/<form[\s\S]*?<\/form>/gi)];
  console.log('Forms on homepage:', forms.length);
  forms.forEach((f, i) => {
    console.log(`Form ${i+1} inputs:`, [...f[0].matchAll(/<(input|select|textarea|button)[^>]*name=["']?([^"'\s>]*)["']?[^>]*>/gi)].map(m => m[0]));
  });

  // Extract phone numbers, whatsapp, CTAs
  const ctas = [...homeHtml.matchAll(/(tel:[^"']+|mailto:[^"']+|wa\.me[^"']+|whatsapp[^"']+)/gi)].map(m => m[0]);
  console.log('Direct CTAs (tel/mailto/wa):', [...new Set(ctas)]);

  // Check footer links
  const footers = [...homeHtml.matchAll(/<footer[\s\S]*?<\/footer>/gi)];
  if (footers[0]) {
    const fLinks = [...footers[0][0].matchAll(/<a[^>]*href=["']([^"']*)["'][^>]*>(.*?)<\/a>/gi)].map(m => ({
      href: m[1],
      text: m[2].replace(/<[^>]+>/g, '').trim()
    }));
    console.log('Footer links count:', fLinks.length);
    console.log('Footer links sample:', fLinks.slice(0, 15));
  }
})();
