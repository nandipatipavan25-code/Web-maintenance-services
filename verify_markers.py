import re
import html

with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    raw = f.read()

print("Raw main length:", len(raw))

# Let's inspect where key sections begin
markers = [
    "<h1>Website Maintenance Services",
    "<h2>Is Your Website Working as Hard as You Are?</h2>",
    "<h2>What Is Website Maintenance?</h2>",
    "<h2>What Does Website Maintenance Include?</h2>",
    "<h2>1. Software, Plugin, and Theme Updates</h2>",
    "<h2>2. Website Backups</h2>",
    "<h2>3. Security Monitoring and Malware Scanning</h2>",
    "<h2>4. Uptime Monitoring</h2>",
    "<h2>5. Performance and Speed Optimisation</h2>",
    "<h2>6. Broken Link and Error Page Checks</h2>",
    "<h2>7. Content Updates and Freshness</h2>",
    "<h2>8. SSL Certificate Management</h2>",
    "<h2>9. Database Optimisation</h2>",
    "<h2>10. Analytics and Reporting</h2>",
    "<h2>Why Website Maintenance Matters for Your Business</h2>",
    "<h2>Your Google Rankings</h2>",
    "<h2>Your Security and Your Customers' Data</h2>",
    "<h2>Your Conversion Rate</h2>",
    "<h2>Your Brand Reputation</h2>",
    "<h2>The Real Cost of Neglecting Your Website</h2>",
    "<h2>How Often Should You Maintain Your Website?</h2>",
    "<h2>DIY vs. Professional Website Maintenance</h2>",
    "<h2>What You Can Handle Yourself</h2>",
    "<h2>What Requires Technical Expertise</h2>",
    "<h2>The Real Cost of DIY</h2>",
    "<h2>The Case for Professional Maintenance</h2>",
    "<h2>What to Look for in a Website Maintenance Partner</h2>",
    "<h2>Website Maintenance Plans from GA Digital Solutions</h2>",
    "<h2>Industries We Serve</h2>",
    "<h2>Frequently Asked Questions</h2>",
    "<h2>Get Your Free 20-Point Website Health Audit</h2>",
    "<h2>Related Articles</h2>"
]

for m in markers:
    idx = raw.find(m)
    print(f"Marker found at {idx}: {m[:45]}")
