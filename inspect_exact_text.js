const fs = require('fs');

const content = fs.readFileSync('main_content_extracted.html', 'utf8');

// Check the exact audit and plans text
const planIdx = content.indexOf('Website Maintenance Plans from GA Digital Solutions');
const indIdx = content.indexOf('Industries We Serve');
const faqIdx = content.indexOf('Frequently Asked Questions');
const auditIdx = content.indexOf('Get Your Free 20-Point Website Health Audit');
const relIdx = content.indexOf('Related Articles');

console.log('--- PLANS CHUNK ---');
console.log(content.substring(planIdx, indIdx));

console.log('\n--- AUDIT CHUNK ---');
console.log(content.substring(auditIdx, relIdx));
