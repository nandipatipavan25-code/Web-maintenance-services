const fs = require('fs');

const html = fs.readFileSync('original_maintenance_page.html', 'utf8');

// Find all main content parts
// What's in header, main content container, and footer?
console.log('HTML length:', html.length);

const bodyMatch = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
if (bodyMatch) {
  const body = bodyMatch[1];
  console.log('Body length:', body.length);
}

// Let's see main tags and structure
const h2s = [...html.matchAll(/<h2[^>]*>([\s\S]*?)<\/h2>/gi)].map(m => m[1].replace(/<[^>]+>/g, '').trim());
console.log('H2 headings count:', h2s.length);
console.log('H2s:', h2s);
