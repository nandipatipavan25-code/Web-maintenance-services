import re

# Read files
with open('original_maintenance_page.html', 'r', encoding='utf-8') as f:
    full_html = f.read()

with open('luxury_theme.css', 'r', encoding='utf-8') as f:
    luxury_css = f.read()

with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    raw_main = f.read()

# Split raw_main by <h2
h2_pattern = re.compile(r'(<h2[^>]*>.*?</h2>)', re.DOTALL | re.IGNORECASE)
parts = h2_pattern.split(raw_main)

# SVG Icons
svg_shield = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
svg_zap = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
svg_cloud = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/></svg>'
svg_clock = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
svg_check = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
svg_wa = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'

# Quick Navigation Bar
quick_nav = """
<div class="gads-sticky-subnav">
  <ul class="gads-nav-scroller">
    <li><a href="#overview">Overview</a></li>
    <li><a href="#deliverables">10 Maintenance Tasks</a></li>
    <li><a href="#why-matters">Why It Matters</a></li>
    <li><a href="#cost-neglect">Cost of Neglect</a></li>
    <li><a href="#how-often">Schedule Cadence</a></li>
    <li><a href="#diy-vs-pro">DIY vs Professional</a></li>
    <li><a href="#plans" class="pill-cta">Plans &amp; Pricing</a></li>
    <li><a href="#faqs">FAQs</a></li>
    <li><a href="#free-audit" class="pill-cta">Free 20-Point Audit</a></li>
  </ul>
</div>
"""

# Hero Lead Capture Card
hero_card = f"""
<div class="gads-hero-card">
  <span class="gads-eyebrow">
    <span class="pulse-indicator"></span> 24/7 Security &amp; Speed Diagnostic
  </span>
  <h3>Claim Your Free 20-Point Website Health Audit</h3>
  <p class="card-sub">Identify hidden malware, outdated plugins, and mobile speed bottlenecks in 24 hours.</p>
  
  <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20a%20free%20website%20health%20audit%20for:%20' + encodeURIComponent(this.website.value);">
    <div class="gads-input-group">
      <label for="lead-url">Website URL *</label>
      <input type="url" id="lead-url" name="website" placeholder="https://yourcompany.com" required>
    </div>
    <div class="gads-input-group">
      <label for="lead-name">Your Name *</label>
      <input type="text" id="lead-name" name="name" placeholder="John Doe" required>
    </div>
    <div class="gads-input-group">
      <label for="lead-phone">WhatsApp / Phone Number *</label>
      <input type="tel" id="lead-phone" name="phone" placeholder="+91 98765 43210" required>
    </div>
    <button type="submit" class="gads-btn-primary" style="margin-top: 6px;">
      Get Free Health Audit &amp; Recommendations &rarr;
    </button>
    <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="gads-btn-wa" target="_blank" rel="noopener noreferrer">
      {svg_wa} Chat with an Engineer on WhatsApp
    </a>
  </form>
  <div style="display: flex; align-items: center; justify-content: center; gap: 6px; margin-top: 14px; font-size: 12px; color: #64748b;">
    <span>🔒 100% Free &amp; Confidential</span>
    <span>•</span>
    <span>No credit card required</span>
  </div>
</div>
"""

# Trust Metric Strip
metric_strip = f"""
<div class="gads-metric-strip">
  <div class="gads-metric-badge">{svg_shield} <span>24/7 Uptime Ping</span></div>
  <div class="gads-metric-badge">{svg_zap} <span>Staging Testing</span></div>
  <div class="gads-metric-badge">{svg_cloud} <span>Daily Cloud Backups</span></div>
  <div class="gads-metric-badge">{svg_clock} <span>30-Min Emergency SLA</span></div>
</div>
"""

out = []
out.append('<div class="gads-pro-page">')
out.append(quick_nav)

# HERO SECTION
out.append('<section id="hero" class="gads-hero-container">')
out.append('  <div class="gads-hero-main">')
out.append('    <div class="gads-hero-media">')
out.append('      <img src="/images/Website_Maintenance.jpg" width="820" height="460" alt="Website Maintenance Services in India - GA Digital Solutions" fetchpriority="high">')
out.append('    </div>')
out.append('    ' + parts[0])  # H1
out.append(metric_strip)
out.append('    ' + parts[1])  # H2: Is Your Website Working as Hard as You Are?
out.append('    ' + parts[2])  # 5 Opening paragraphs
out.append('  </div>')
out.append('  <div class="gads-hero-sidebar">')
out.append(hero_card)
out.append('  </div>')
out.append('</section>')

# OVERVIEW SECTION
out.append('<section id="overview" class="gads-section-card accent-card">')
out.append('  ' + parts[3])  # H2: What Is Website Maintenance?
out.append('  ' + parts[4])  # text & bullet points
out.append('</section>')

# 10 DELIVERABLES BENTO GRID
out.append('<section id="deliverables" style="margin: 45px 0;">')
out.append('  <div class="gads-section-card" style="margin-bottom: 25px;">')
out.append('    ' + parts[5])  # H2: What Does Website Maintenance Include?
out.append('    ' + parts[6])  # intro text
out.append('  </div>')
out.append('  <div class="gads-bento-grid">')

deliv_pairs = [
    (7, 8, "01 // UPDATES"),
    (9, 10, "02 // BACKUPS"),
    (11, 12, "03 // SECURITY"),
    (13, 14, "04 // UPTIME"),
    (15, 16, "05 // PERFORMANCE"),
    (17, 18, "06 // INTEGRITY"),
    (19, 20, "07 // CONTENT"),
    (21, 22, "08 // SSL"),
    (23, 24, "09 // DATABASE"),
    (25, 26, "10 // ANALYTICS")
]

for h_idx, b_idx, tag in deliv_pairs:
    clean_h2 = re.sub(r'<h2[^>]*>', '<h2>', parts[h_idx])
    out.append('    <div class="gads-bento-item">')
    out.append(f'      <span class="gads-bento-tag">{tag}</span>')
    out.append('      ' + clean_h2)
    out.append('      ' + parts[b_idx])
    out.append('    </div>')

out.append('  </div>')
out.append('</section>')

# WHY IT MATTERS IMPACT GRID
out.append('<section id="why-matters" class="gads-section-card" style="margin: 40px 0;">')
out.append('  ' + parts[27])  # H2: Why Website Maintenance Matters for Your Business
out.append('  ' + parts[28])  # intro
out.append('  <div class="gads-impact-grid">')
out.append('    <div class="gads-impact-box" style="border-top: 4px solid #10b981;">' + parts[29] + parts[30] + '</div>')
out.append('    <div class="gads-impact-box" style="border-top: 4px solid #ef4444;">' + parts[31] + parts[32] + '</div>')
out.append('    <div class="gads-impact-box" style="border-top: 4px solid #f59e0b;">' + parts[33] + parts[34] + '</div>')
out.append('    <div class="gads-impact-box" style="border-top: 4px solid #0284c7;">' + parts[35] + parts[36] + '</div>')
out.append('  </div>')
out.append('</section>')

# COST OF NEGLECT & HOW OFTEN
out.append('<section id="cost-neglect" class="gads-section-card warning-card">')
out.append('  ' + parts[37] + parts[38])  # The Real Cost of Neglecting Your Website
out.append('</section>')

out.append('<section id="how-often" class="gads-section-card">')
out.append('  ' + parts[39] + parts[40])  # How Often Should You Maintain Your Website?
out.append('</section>')

# DIY VS PRO
out.append('<section id="diy-vs-pro" class="gads-section-card" style="margin: 40px 0;">')
out.append('  ' + parts[41] + parts[42])  # DIY vs. Professional Website Maintenance
out.append('  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 25px 0;">')
out.append('    <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: var(--g-radius-md); padding: 22px;">' + parts[43] + parts[44] + '</div>')
out.append('    <div style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: var(--g-radius-md); padding: 22px;">' + parts[45] + parts[46] + '</div>')
out.append('  </div>')
out.append('  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">')
out.append('    <div style="background: #fef2f2; border: 1.5px solid #fecaca; border-radius: var(--g-radius-md); padding: 22px;">' + parts[47] + parts[48] + '</div>')
out.append('    <div style="background: #eff6ff; border: 1.5px solid #bfdbfe; border-radius: var(--g-radius-md); padding: 22px;">' + parts[49] + parts[50] + '</div>')
out.append('  </div>')
out.append('  <div style="margin-top: 35px; border-top: 1px solid #e2e8f0; padding-top: 25px;">')
out.append('    ' + parts[51] + parts[52])  # What to Look for in a Website Maintenance Partner
out.append('  </div>')
out.append('</section>')

# ELEVATED 3-TIER PRICING BLOCK
out.append('<section id="plans" class="gads-pricing-block">')
out.append('  ' + parts[53])  # H2: Website Maintenance Plans from GA Digital Solutions

plans_full = parts[54]
row_start = plans_full.find('<div class="row"')
row_end = plans_full.find('</div>\n</div>\n</div>', row_start) + len('</div>\n</div>\n</div>')

plans_intro = plans_full[:row_start]
plans_closing = plans_full[row_end:]

out.append('  ' + plans_intro)

out.append(f"""
  <div class="gads-pricing-row">
    <!-- Essential Plan -->
    <div class="gads-price-card">
      <h3 class="gads-plan-name">Essential</h3>
      <div class="gads-plan-desc">
        <p><strong>For brochure websites and small business sites</strong></p>
        <p>Ideal for: standard websites with stable content and moderate visitor traffic</p>
      </div>
      <div style="margin-top: 25px; padding-top: 18px; border-top: 1px solid #f1f5f9;">
        <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Essential%20Website%20Maintenance%20Plan" class="gads-btn-primary" target="_blank" rel="noopener noreferrer">
          Choose Essential Plan &rarr;
        </a>
      </div>
    </div>

    <!-- Growth Plan (Featured) -->
    <div class="gads-price-card featured">
      <div class="gads-featured-ribbon">⭐ Most Popular for Business</div>
      <h3 class="gads-plan-name" style="color: #0284c7;">Growth</h3>
      <div class="gads-plan-desc">
        <p><strong>For websites actively generating leads</strong></p>
        <p>Ideal for: businesses relying on their website for consistent lead generation</p>
      </div>
      <div style="margin-top: 25px; padding-top: 18px; border-top: 1px solid #f1f5f9;">
        <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Growth%20Website%20Maintenance%20Plan" class="gads-btn-primary" style="background: linear-gradient(135deg, #0284c7, #0369a1);" target="_blank" rel="noopener noreferrer">
          Choose Growth Plan &rarr;
        </a>
      </div>
    </div>

    <!-- Business Plan -->
    <div class="gads-price-card">
      <h3 class="gads-plan-name">Business</h3>
      <div class="gads-plan-desc">
        <p><strong>For e-commerce, booking platforms, and high-traffic sites</strong></p>
        <p>Ideal for: e-commerce stores and businesses with significant revenue dependence on their website</p>
      </div>
      <div style="margin-top: 25px; padding-top: 18px; border-top: 1px solid #f1f5f9;">
        <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Business%20Website%20Maintenance%20Plan" class="gads-btn-primary" target="_blank" rel="noopener noreferrer">
          Choose Business Plan &rarr;
        </a>
      </div>
    </div>
  </div>
""")

out.append('  ' + plans_closing)
out.append('</section>')

# INDUSTRIES WE SERVE
out.append('<section id="industries" class="gads-section-card">')
out.append('  ' + parts[55] + parts[56])
out.append('</section>')

# FREQUENTLY ASKED QUESTIONS
out.append('<section id="faqs" style="margin: 45px 0;">')
out.append('  <div class="gads-section-card" style="margin-bottom: 25px;">')
out.append('    ' + parts[57])  # H2: Frequently Asked Questions

faq_content = parts[58]
faq_intro_match = re.match(r'(\s*<p>[\s\S]*?</p>)', faq_content)
if faq_intro_match:
    out.append('    ' + faq_intro_match.group(1))

out.append('  </div>')

faq_pairs = re.findall(r'<button class="accordionc">([\s\S]*?)</button>\s*<div class="panelc">([\s\S]*?)</div>', faq_content)

for q_text, a_text in faq_pairs:
    out.append('  <details class="gads-faq-item">')
    out.append(f'    <summary class="gads-faq-toggle">{q_text.strip()}</summary>')
    out.append(f'    <div class="gads-faq-answer">{a_text.strip()}</div>')
    out.append('  </details>')

out.append('</section>')

# FREE 20-POINT AUDIT SECTION (LUXURY DARK LAB CONTAINER)
out.append('<section id="free-audit" class="gads-lab-audit">')
out.append('  ' + parts[59])  # H2: Get Your Free 20-Point Website Health Audit
out.append('  ' + parts[60])  # Audit text & deliverables

audit_lab_form = f"""
<div class="gads-lab-form-box">
  <h3 style="margin-top: 0; color: #38bdf8; font-size: 20px; font-weight: 700;">
    ⚡ Enter Your Website to Start Your Free 20-Point Audit
  </h3>
  <p style="font-size: 14px; color: #cbd5e1; margin-bottom: 20px;">
    No need to navigate away. Submit your URL right here and our technical engineering team will begin your review.
  </p>
  <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20requesting%20the%20Free%2020-Point%20Website%20Health%20Audit%20for:%20' + encodeURIComponent(this.audit_site.value) + '%20(Name:%20' + encodeURIComponent(this.audit_name.value) + ');'">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin-bottom: 15px;">
      <div>
        <label style="display:block; font-size: 12px; font-weight: 700; color: #94a3b8; margin-bottom: 6px; letter-spacing: 0.5px;">WEBSITE URL *</label>
        <input type="url" name="audit_site" placeholder="https://yourwebsite.com" required style="width: 100%; padding: 12px 14px; border-radius: var(--g-radius-sm); font-size: 15px; box-sizing: border-box;">
      </div>
      <div>
        <label style="display:block; font-size: 12px; font-weight: 700; color: #94a3b8; margin-bottom: 6px; letter-spacing: 0.5px;">YOUR NAME *</label>
        <input type="text" name="audit_name" placeholder="John Doe" required style="width: 100%; padding: 12px 14px; border-radius: var(--g-radius-sm); font-size: 15px; box-sizing: border-box;">
      </div>
      <div>
        <label style="display:block; font-size: 12px; font-weight: 700; color: #94a3b8; margin-bottom: 6px; letter-spacing: 0.5px;">WHATSAPP / PHONE NUMBER *</label>
        <input type="tel" name="audit_phone" placeholder="+91 98765 43210" required style="width: 100%; padding: 12px 14px; border-radius: var(--g-radius-sm); font-size: 15px; box-sizing: border-box;">
      </div>
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 15px;">
      <button type="submit" class="gads-btn-primary" style="flex: 2; min-width: 240px; padding: 14px;">
        Claim My Free Website Health Audit &rarr;
      </button>
      <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20to%20request%20the%20Free%20Website%20Health%20Audit%20directly" class="gads-btn-wa" style="flex: 1; min-width: 200px; padding: 14px; margin: 0;" target="_blank" rel="noopener noreferrer">
        {svg_wa} WhatsApp Fast Track
      </a>
    </div>
  </form>
</div>
"""
out.append(audit_lab_form)
out.append('</section>')

# RELATED ARTICLES
out.append('<section id="related-articles" class="gads-section-card" style="margin-top: 45px;">')
out.append('  ' + parts[61] + parts[62])
out.append('  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-top: 25px;">')
out.append('    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: var(--g-radius-md); padding: 20px;">' + parts[63] + parts[64] + '</div>')
out.append('    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: var(--g-radius-md); padding: 20px;">' + parts[65] + parts[66] + '</div>')
out.append('    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: var(--g-radius-md); padding: 20px;">' + parts[67] + parts[68] + '</div>')
out.append('    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: var(--g-radius-md); padding: 20px;">' + parts[69] + parts[70] + '</div>')
out.append('  </div>')
out.append('</section>')

# MOBILE STICKY DOCK
mobile_dock = f"""
<div class="gads-mobile-dock">
  <a href="tel:9849574618" class="gads-dock-call">
    <span class="fa fa-phone"></span> Call Engineer
  </a>
  <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="gads-dock-wa" target="_blank" rel="noopener noreferrer">
    {svg_wa} WhatsApp
  </a>
</div>
"""
out.append(mobile_dock)
out.append('</div>')  # close .gads-pro-page

redesigned_main_html = "\n".join(out)

# Inject into full HTML
start_marker = '<div class="main-content-col" style="text-align:left;">'
end_marker = '<footer id="gad-footer"'

start_idx = full_html.find(start_marker)
end_idx = full_html.find(end_marker)

head_close_idx = full_html.find('</head>')
final_html = (
    full_html[:head_close_idx] +
    "\n<style>\n" + luxury_css + "\n</style>\n" +
    full_html[head_close_idx:start_idx + len(start_marker)] +
    "\n" + redesigned_main_html + "\n" +
    full_html[end_idx:]
)

with open('redesigned_website_maintenance.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully built luxury redesigned page! Total length:", len(final_html))
