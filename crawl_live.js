const https = require('https');

const pages = [
  '/',
  '/careers',
  '/services/',
  '/services/website-maintenance',
  '/services/websiteservices/website-maintenance-services',
  '/services/website-development',
  '/contact',
  '/enquiry',
  '/portfolio',
  '/about',
  '/resumes/',
  '/blogs/website-maintenance-services-hyderabad'
];

async function checkPage(path) {
  return new Promise((resolve) => {
    const url = `https://www.gadigitalsolutions.com${path}`;
    const req = https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => { if (data.length < 50000) data += chunk; });
      res.on('end', () => {
        const title = data.match(/<title>(.*?)<\/title>/i)?.[1]?.trim();
        const metaDesc = data.match(/<meta[^>]*name=["']description["'][^>]*content=["']([^"']*)["']/i)?.[1]?.trim();
        const canonical = data.match(/<link[^>]*rel=["']canonical["'][^>]*href=["']([^"']*)["']/i)?.[1]?.trim();
        const h1s = [...data.matchAll(/<h1[^>]*>(.*?)<\/h1>/gis)].map(m => m[1].replace(/<[^>]+>/g, '').trim());
        resolve({
          path,
          statusCode: res.statusCode,
          title,
          metaDesc,
          canonical,
          h1s,
          contentLength: data.length
        });
      });
    });
    req.on('error', (err) => {
      resolve({ path, error: err.message });
    });
    req.setTimeout(8000, () => {
      req.destroy();
      resolve({ path, error: 'Timeout' });
    });
  });
}

(async () => {
  console.log('Fetching live pages...');
  for (const p of pages) {
    const res = await checkPage(p);
    console.log(JSON.stringify(res, null, 2));
  }
})();
