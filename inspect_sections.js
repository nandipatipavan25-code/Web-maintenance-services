const fs = require('fs');

const content = fs.readFileSync('main_content_extracted.html', 'utf8');

// Split by <h2>
const sections = content.split(/<h2[^>]*>/i);

console.log('Total sections separated by H2:', sections.length);
sections.forEach((sec, idx) => {
  const headingMatch = sec.match(/^([\s\S]*?)<\/h2>/i);
  if (headingMatch) {
    console.log(`[Section ${idx}] H2: ${headingMatch[1].replace(/<[^>]+>/g, '').trim()} | Length: ${sec.length}`);
  } else {
    console.log(`[Section ${idx}] Pre-H2 chunk | Length: ${sec.length}`);
  }
});
