import re

# Read original files
with open('original_maintenance_page.html', 'r', encoding='utf-8') as f:
    full_html = f.read()

with open('modern_css.html', 'r', encoding='utf-8') as f:
    modern_css = f.read()

with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    raw_main = f.read()

# Split raw_main by <h2
h2_pattern = re.compile(r'(<h2[^>]*>.*?</h2>)', re.DOTALL | re.IGNORECASE)
parts = h2_pattern.split(raw_main)

# 1. Hero Lead Capture Form Card
hero_lead_form = """
<div class="gads-lead-card">
    <span class="gads-lead-badge">Free Diagnostic</span>
    <h3>Get Your Free 20-Point Website Health Audit</h3>
    <p class="lead-sub">Check security vulnerabilities, outdated plugins, and mobile page speed in 24 hours.</p>
    
    <form class="gads-lead-form" onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20a%20free%20website%20health%20audit%20for:%20' + encodeURIComponent(this.website.value);">
        <div class="form-group">
            <label for="hero-url">Website URL *</label>
            <input type="url" id="hero-url" name="website" placeholder="https://yourcompany.com" required>
        </div>
        <div class="form-group">
            <label for="hero-name">Your Name *</label>
            <input type="text" id="hero-name" name="name" placeholder="John Doe" required>
        </div>
        <div class="form-group">
            <label for="hero-phone">WhatsApp / Phone Number *</label>
            <input type="tel" id="hero-phone" name="phone" placeholder="+91 98765 43210" required>
        </div>
        <button type="submit" class="gads-lead-btn">
            Get Free Health Audit & Plan Recommendations &rarr;
        </button>
        <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="gads-wa-btn" target="_blank" rel="noopener noreferrer">
            <span class="fa fa-whatsapp"></span> Chat Directly on WhatsApp (+91 98495 74618)
        </a>
    </form>
    <p style="font-size: 11px; text-align: center; color: #94a3b8; margin: 10px 0 0;">
        🔒 100% Free &amp; Confidential. No sales pressure. No credit card required.
    </p>
</div>
"""

# 2. Quick Navigation Bar
quick_nav = """
<div class="gads-quick-nav">
    <ul class="gads-quick-nav-list">
        <li><a href="#overview">🔍 Overview</a></li>
        <li><a href="#deliverables">🛠️ What's Included (10 Tasks)</a></li>
        <li><a href="#why-matters">💡 Why It Matters</a></li>
        <li><a href="#cost-neglect">⚠️ Cost of Neglect</a></li>
        <li><a href="#how-often">📅 Maintenance Schedule</a></li>
        <li><a href="#diy-vs-pro">⚖️ DIY vs Pro</a></li>
        <li><a href="#plans" class="nav-highlight">📦 Plans &amp; Pricing</a></li>
        <li><a href="#faqs">❓ FAQs</a></li>
        <li><a href="#free-audit" class="nav-highlight">🎁 Claim Free Audit</a></li>
    </ul>
</div>
"""

# 3. Trust Pills
trust_pills = """
<div class="gads-trust-pills">
    <span class="gads-trust-pill">🛡️ 24/7 Security &amp; Uptime Monitoring</span>
    <span class="gads-trust-pill">⚡ Tested in Isolated Staging</span>
    <span class="gads-trust-pill">💾 Automated Daily Cloud Backups</span>
    <span class="gads-trust-pill">⏱️ 30-Min Emergency Response SLA</span>
</div>
"""

# Construct redesigned sections
out = []
out.append('<div class="gads-maint-wrapper">')
out.append(quick_nav)

# HERO SECTION
out.append('<section id="hero" class="gads-hero-row">')
out.append('  <div class="gads-hero-left">')
out.append('    <div class="gads-hero-img-wrap">')
out.append('      <img src="/images/Website_Maintenance.jpg" width="820" height="460" alt="Website Maintenance Services in India - GA Digital Solutions" fetchpriority="high">')
out.append('    </div>')
out.append('    ' + parts[0])  # H1
out.append(trust_pills)
out.append('    ' + parts[1])  # H2: Is Your Website Working as Hard as You Are?
out.append('    ' + parts[2])  # Opening paragraphs
out.append('  </div>')
out.append('  <div class="gads-hero-right">')
out.append(hero_lead_form)
out.append('  </div>')
out.append('</section>')

# OVERVIEW CARD
out.append('<section id="overview" class="gads-content-card highlight-card">')
out.append('  ' + parts[3])  # H2: What Is Website Maintenance?
out.append('  ' + parts[4])  # text
out.append('</section>')

# DELIVERABLES SECTION
out.append('<section id="deliverables" style="margin: 40px 0;">')
out.append('  <div class="gads-content-card" style="margin-bottom: 20px;">')
out.append('    ' + parts[5])  # H2: What Does Website Maintenance Include?
out.append('    ' + parts[6])  # intro text
out.append('  </div>')
out.append('  <div class="gads-deliverables-grid">')

deliv_indices = [
    (7, 8, "01"),
    (9, 10, "02"),
    (11, 12, "03"),
    (13, 14, "04"),
    (15, 16, "05"),
    (17, 18, "06"),
    (19, 20, "07"),
    (21, 22, "08"),
    (23, 24, "09"),
    (25, 26, "10"),
]

for h_idx, b_idx, num in deliv_indices:
    h2_text = parts[h_idx]
    clean_h2 = re.sub(r'<h2[^>]*>', '<h2>', h2_text)
    body_text = parts[b_idx]
    out.append('    <div class="gads-deliverable-card">')
    out.append(f'      <div style="margin-bottom: 8px;"><span class="gads-deliv-num">TASK #{num}</span></div>')
    out.append('      ' + clean_h2)
    out.append('      ' + body_text)
    out.append('    </div>')

out.append('  </div>')
out.append('</section>')

# WHY IT MATTERS & 4 PILLARS
out.append('<section id="why-matters" class="gads-content-card" style="margin: 35px 0;">')
out.append('  ' + parts[27])  # H2: Why Website Maintenance Matters for Your Business
out.append('  ' + parts[28])  # intro
out.append('  <div class="gads-impact-grid">')
out.append('    <div class="gads-impact-card" style="border-top: 3px solid #10b981;">' + parts[29] + parts[30] + '</div>')
out.append('    <div class="gads-impact-card" style="border-top: 3px solid #ef4444;">' + parts[31] + parts[32] + '</div>')
out.append('    <div class="gads-impact-card" style="border-top: 3px solid #f59e0b;">' + parts[33] + parts[34] + '</div>')
out.append('    <div class="gads-impact-card" style="border-top: 3px solid #126db2;">' + parts[35] + parts[36] + '</div>')
out.append('  </div>')
out.append('</section>')

# COST OF NEGLECT & HOW OFTEN
out.append('<section id="cost-neglect" class="gads-content-card warning-card">')
out.append('  ' + parts[37] + parts[38])  # The Real Cost of Neglecting Your Website
out.append('</section>')

out.append('<section id="how-often" class="gads-content-card">')
out.append('  ' + parts[39] + parts[40])  # How Often Should You Maintain Your Website?
out.append('</section>')

# DIY VS PROFESSIONAL
out.append('<section id="diy-vs-pro" class="gads-content-card" style="margin: 35px 0;">')
out.append('  ' + parts[41] + parts[42])  # DIY vs. Professional Website Maintenance
out.append('  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">')
out.append('    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">' + parts[43] + parts[44] + '</div>')
out.append('    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 20px;">' + parts[45] + parts[46] + '</div>')
out.append('  </div>')
out.append('  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">')
out.append('    <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 20px;">' + parts[47] + parts[48] + '</div>')
out.append('    <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 20px;">' + parts[49] + parts[50] + '</div>')
out.append('  </div>')
out.append('  <div style="margin-top: 30px; border-top: 1px solid #e2e8f0; padding-top: 25px;">')
out.append('    ' + parts[51] + parts[52])  # What to Look for in a Website Maintenance Partner
out.append('  </div>')
out.append('</section>')

# PLANS & PRICING
out.append('<section id="plans" class="gads-plans-container">')
out.append('  ' + parts[53])

plans_full = parts[54]
row_start = plans_full.find('<div class="row"')
row_end = plans_full.find('</div>\n</div>\n</div>', row_start) + len('</div>\n</div>\n</div>')

plans_intro = plans_full[:row_start]
plans_closing = plans_full[row_end:]

out.append('  ' + plans_intro)

out.append("""
  <div class="gads-plans-grid">
    <!-- Essential Plan -->
    <div class="gads-plan-box">
      <div class="gads-plan-header">
        <h3 style="color: white; margin: 0;">Essential</h3>
      </div>
      <div class="gads-plan-body">
        <p><strong>For brochure websites and small business sites</strong></p>
        <p>Ideal for: standard websites with stable content and moderate visitor traffic</p>
        <div class="gads-plan-actions">
          <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Essential%20Website%20Maintenance%20Plan" class="gads-lead-btn" target="_blank" rel="noopener noreferrer">
            Choose Essential Plan &rarr;
          </a>
        </div>
      </div>
    </div>

    <!-- Growth Plan (Recommended) -->
    <div class="gads-plan-box recommended">
      <div class="gads-plan-ribbon">⭐ Most Popular for Business</div>
      <div class="gads-plan-header" style="background: #126db2;">
        <h3 style="color: white; margin: 0;">Growth</h3>
      </div>
      <div class="gads-plan-body">
        <p><strong>For websites actively generating leads</strong></p>
        <p>Ideal for: businesses relying on their website for consistent lead generation</p>
        <div class="gads-plan-actions">
          <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Growth%20Website%20Maintenance%20Plan" class="gads-lead-btn" style="background: #0284c7;" target="_blank" rel="noopener noreferrer">
            Choose Growth Plan &rarr;
          </a>
        </div>
      </div>
    </div>

    <!-- Business Plan -->
    <div class="gads-plan-box">
      <div class="gads-plan-header">
        <h3 style="color: white; margin: 0;">Business</h3>
      </div>
      <div class="gads-plan-body">
        <p><strong>For e-commerce, booking platforms, and high-traffic sites</strong></p>
        <p>Ideal for: e-commerce stores and businesses with significant revenue dependence on their website</p>
        <div class="gads-plan-actions">
          <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Business%20Website%20Maintenance%20Plan" class="gads-lead-btn" target="_blank" rel="noopener noreferrer">
            Choose Business Plan &rarr;
          </a>
        </div>
      </div>
    </div>
  </div>
""")

out.append('  ' + plans_closing)
out.append('</section>')

# INDUSTRIES WE SERVE
out.append('<section id="industries" class="gads-content-card">')
out.append('  ' + parts[55] + parts[56])
out.append('</section>')

# FREQUENTLY ASKED QUESTIONS (INTERACTIVE ACCORDIONS)
out.append('<section id="faqs" style="margin: 35px 0;">')
out.append('  <div class="gads-content-card" style="margin-bottom: 20px;">')
out.append('    ' + parts[57])

faq_content = parts[58]
faq_intro_match = re.match(r'(\s*<p>[\s\S]*?</p>)', faq_content)
if faq_intro_match:
    out.append('    ' + faq_intro_match.group(1))

out.append('  </div>')

faq_pairs = re.findall(r'<button class="accordionc">([\s\S]*?)</button>\s*<div class="panelc">([\s\S]*?)</div>', faq_content)

for q_text, a_text in faq_pairs:
    out.append('  <details class="gads-faq-accordion">')
    out.append(f'    <summary class="gads-faq-summary">{q_text.strip()}</summary>')
    out.append(f'    <div class="gads-faq-content">{a_text.strip()}</div>')
    out.append('  </details>')

out.append('</section>')

# FREE AUDIT SECTION
out.append('<section id="free-audit" class="gads-audit-section">')
out.append('  ' + parts[59])
out.append('  ' + parts[60])

audit_embedded_form = """
<div class="gads-audit-form-inner">
    <h3 style="margin-top: 0; color: #0f172a; font-size: 20px; font-weight: 700;">
        ⚡ Enter Your Website to Start Your Free 20-Point Audit
    </h3>
    <p style="font-size: 14px; color: #475569; margin-bottom: 18px;">
        No need to navigate away. Submit your URL right here and our engineering team will begin your review.
    </p>
    <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20requesting%20the%20Free%2020-Point%20Website%20Health%20Audit%20for:%20' + encodeURIComponent(this.audit_site.value) + '%20(Name:%20' + encodeURIComponent(this.audit_name.value) + ');'">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin-bottom: 15px;">
            <div>
                <label style="display:block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 5px;">WEBSITE URL *</label>
                <input type="url" name="audit_site" placeholder="https://yourwebsite.com" required style="width: 100%; padding: 12px; border: 1px solid #cbd5e1; border-radius: 6px; box-sizing: border-box;">
            </div>
            <div>
                <label style="display:block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 5px;">YOUR NAME *</label>
                <input type="text" name="audit_name" placeholder="John Doe" required style="width: 100%; padding: 12px; border: 1px solid #cbd5e1; border-radius: 6px; box-sizing: border-box;">
            </div>
            <div>
                <label style="display:block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 5px;">WHATSAPP / PHONE NUMBER *</label>
                <input type="tel" name="audit_phone" placeholder="+91 98765 43210" required style="width: 100%; padding: 12px; border: 1px solid #cbd5e1; border-radius: 6px; box-sizing: border-box;">
            </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 15px;">
            <button type="submit" class="gads-lead-btn" style="flex: 2; min-width: 240px; margin: 0; padding: 14px;">
                Claim My Free Website Health Audit &rarr;
            </button>
            <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20to%20request%20the%20Free%20Website%20Health%20Audit%20directly" class="gads-wa-btn" style="flex: 1; min-width: 200px; margin: 0; padding: 14px;" target="_blank" rel="noopener noreferrer">
                <span class="fa fa-whatsapp"></span> WhatsApp Fast Track
            </a>
        </div>
    </form>
</div>
"""
out.append(audit_embedded_form)
out.append('</section>')

# RELATED ARTICLES
out.append('<section id="related-articles" class="gads-content-card" style="margin-top: 35px;">')
out.append('  ' + parts[61] + parts[62])
out.append('  <div class="gads-related-grid">')
out.append('    <div class="gads-related-col">' + parts[63] + parts[64] + '</div>')
out.append('    <div class="gads-related-col">' + parts[65] + parts[66] + '</div>')
out.append('    <div class="gads-related-col">' + parts[67] + parts[68] + '</div>')
out.append('    <div class="gads-related-col">' + parts[69] + parts[70] + '</div>')
out.append('  </div>')
out.append('</section>')

# MOBILE STICKY ACTION BAR
mobile_sticky = """
<div class="gads-mobile-sticky-bar">
    <a href="tel:9849574618" class="gads-mobile-call">
        <span class="fa fa-phone"></span> Call Engineer
    </a>
    <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="gads-mobile-wa" target="_blank" rel="noopener noreferrer">
        <span class="fa fa-whatsapp"></span> WhatsApp Support
    </a>
</div>
"""
out.append(mobile_sticky)

out.append('</div>')  # close .gads-maint-wrapper

redesigned_main_html = "\n".join(out)

# Assemble into full HTML
start_marker = '<div class="main-content-col" style="text-align:left;">'
end_marker = '<footer id="gad-footer"'

start_idx = full_html.find(start_marker)
end_idx = full_html.find(end_marker)

head_close_idx = full_html.find('</head>')
final_html = (
    full_html[:head_close_idx] +
    "\n" + modern_css + "\n" +
    full_html[head_close_idx:start_idx + len(start_marker)] +
    "\n" + redesigned_main_html + "\n" +
    full_html[end_idx:]
)

with open('redesigned_website_maintenance.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully generated redesigned_website_maintenance.html! Total bytes:", len(final_html))
