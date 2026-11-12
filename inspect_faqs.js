const fs = require('fs');

const content = fs.readFileSync('main_content_extracted.html', 'utf8');

// Let's inspect the exact FAQs in main_content_extracted.html
const faqIdx = content.indexOf('Frequently Asked Questions');
const auditIdx = content.indexOf('Get Your Free 20-Point Website Health Audit');
const faqSection = content.substring(faqIdx, auditIdx);

console.log('FAQ section length:', faqSection.length);
console.log('FAQ section sample:');
console.log(faqSection.substring(0, 1500));
