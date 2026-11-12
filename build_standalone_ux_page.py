import re

with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    raw_main = f.read()

# Split raw_main by <h2
h2_pattern = re.compile(r'(<h2[^>]*>.*?</h2>)', re.DOTALL | re.IGNORECASE)
parts = h2_pattern.split(raw_main)

# Parse FAQs from Part 58
faq_content = parts[58]
faq_intro_match = re.match(r'(\s*<p>[\s\S]*?</p>)', faq_content)
faq_intro = faq_intro_match.group(1) if faq_intro_match else ""
faq_pairs = re.findall(r'<button class="accordionc">([\s\S]*?)</button>\s*<div class="panelc">([\s\S]*?)</div>', faq_content)

# Parse Plans from Part 54
plans_full = parts[54]
row_start = plans_full.find('<div class="row"')
row_end = plans_full.find('</div>\n</div>\n</div>', row_start) + len('</div>\n</div>\n</div>')
plans_intro = plans_full[:row_start]
plans_closing = plans_full[row_end:]

# Deliverable tasks 1 to 10
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

# Build the complete standalone HTML
standalone_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Website Maintenance Services in India | GA Digital Solutions</title>
  <meta name="description" content="Professional website maintenance services in India. 24/7 uptime monitoring, security scanning, daily backups, speed optimization & WordPress updates.">
  <link rel="canonical" href="https://gadigitalsolutions.com/services/website-maintenance">
  <link rel="icon" href="https://www.gadigitalsolutions.com/images/logo.png" type="image/png">
  
  <!-- Modern Clean Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --primary: #126db2;
      --primary-dark: #0c4d7e;
      --primary-light: #e0f2fe;
      --accent: #0284c7;
      --dark: #0f172a;
      --slate: #334155;
      --muted: #64748b;
      --border: #e2e8f0;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
      --shadow-md: 0 6px 18px rgba(0,0,0,0.07);
      --shadow-lg: 0 12px 30px rgba(0,0,0,0.09);
      --radius: 12px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--dark);
      background-color: var(--bg-page);
      line-height: 1.7;
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
    }}

    a {{
      color: var(--primary);
      text-decoration: none;
      transition: color 0.2s;
    }}
    a:hover {{
      color: var(--primary-dark);
      text-decoration: underline;
    }}

    img {{
      max-width: 100%;
      height: auto;
      display: block;
    }}

    .container {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* Global Header */
    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 14px 0;
      position: relative;
      z-index: 50;
    }}
    .header-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }}
    .header-logo img {{
      height: 52px;
      width: auto;
    }}
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 15px;
    }}
    .header-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 14px;
      font-weight: 600;
      color: var(--slate);
      text-decoration: none !important;
    }}
    .header-link:hover {{
      color: var(--primary);
    }}
    .header-cta-btn {{
      background: var(--primary);
      color: #ffffff !important;
      font-size: 14px;
      font-weight: 700;
      padding: 9px 18px;
      border-radius: 6px;
      text-decoration: none !important;
      transition: background 0.2s;
    }}
    .header-cta-btn:hover {{
      background: var(--primary-dark);
    }}

    /* Sticky Sub-Nav */
    .sticky-nav {{
      position: sticky;
      top: 0;
      z-index: 40;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border);
      padding: 10px 0;
      margin-bottom: 30px;
    }}
    .nav-scroller {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      list-style: none;
      white-space: nowrap;
      scrollbar-width: none;
    }}
    .nav-scroller::-webkit-scrollbar {{
      display: none;
    }}
    .nav-scroller li a {{
      display: inline-block;
      padding: 6px 14px;
      font-size: 13px;
      font-weight: 600;
      color: var(--slate);
      background: #f1f5f9;
      border: 1px solid var(--border);
      border-radius: 20px;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .nav-scroller li a:hover {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }}
    .nav-scroller li a.cta-pill {{
      background: #e0f2fe;
      color: var(--primary);
      border-color: #bae6fd;
      font-weight: 700;
    }}

    /* Typography & Section Styles */
    h1 {{
      font-size: 32px;
      font-weight: 800;
      line-height: 1.3;
      color: var(--dark);
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }}
    @media (min-width: 768px) {{
      h1 {{ font-size: 38px; }}
    }}

    h2 {{
      font-size: 24px;
      font-weight: 700;
      line-height: 1.35;
      color: var(--dark);
      margin: 0 0 14px;
      letter-spacing: -0.015em;
    }}

    h3 {{
      font-size: 19px;
      font-weight: 700;
      color: var(--dark);
      margin: 0 0 10px;
    }}

    p {{
      color: var(--slate);
      font-size: 16px;
      margin-bottom: 16px;
      line-height: 1.75;
    }}

    strong {{
      color: var(--dark);
    }}

    ul {{
      margin: 0 0 18px 20px;
      color: var(--slate);
    }}
    li {{
      margin-bottom: 8px;
    }}

    /* Card Containers */
    .card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 30px;
      margin-bottom: 30px;
      box-shadow: var(--shadow-sm);
    }}
    .card-accent {{
      border-left: 5px solid var(--primary);
      background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
    }}
    .card-warning {{
      border-left: 5px solid #f59e0b;
      background: #fffbeb;
    }}

    /* Hero Section */
    .hero-layout {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 35px;
      margin-bottom: 40px;
      align-items: start;
    }}
    @media (min-width: 992px) {{
      .hero-layout {{
        grid-template-columns: 1.15fr 0.85fr;
      }}
    }}
    .hero-media {{
      border-radius: var(--radius);
      overflow: hidden;
      margin-bottom: 22px;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--border);
    }}

    .trust-strip {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 10px;
      margin: 20px 0 25px;
    }}
    .trust-item {{
      background: #f1f5f9;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 8px 12px;
      font-size: 12px;
      font-weight: 700;
      color: var(--slate);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* Hero Lead Form Card */
    .lead-card {{
      background: #ffffff;
      border: 1.5px solid #bae6fd;
      border-radius: var(--radius);
      padding: 26px 22px;
      box-shadow: var(--shadow-lg);
    }}
    .lead-badge {{
      display: inline-block;
      background: #e0f2fe;
      color: var(--primary);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 4px;
      margin-bottom: 10px;
    }}
    .lead-card h3 {{
      font-size: 20px;
      margin-bottom: 6px;
    }}
    .lead-card p.lead-desc {{
      font-size: 13px;
      color: var(--muted);
      margin-bottom: 16px;
    }}
    .form-group {{
      margin-bottom: 12px;
    }}
    .form-group label {{
      display: block;
      font-size: 12px;
      font-weight: 700;
      color: var(--slate);
      margin-bottom: 4px;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }}
    .form-group input {{
      width: 100%;
      padding: 10px 12px;
      font-size: 14px;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: #f8fafc;
      font-family: inherit;
    }}
    .form-group input:focus {{
      outline: none;
      border-color: var(--primary);
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(18, 109, 178, 0.15);
    }}
    .btn-submit {{
      width: 100%;
      background: var(--primary);
      color: #ffffff;
      font-size: 15px;
      font-weight: 700;
      padding: 12px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.2s;
    }}
    .btn-submit:hover {{
      background: var(--primary-dark);
    }}
    .btn-wa-direct {{
      width: 100%;
      background: #25d366;
      color: #ffffff !important;
      font-size: 14px;
      font-weight: 700;
      padding: 10px;
      border-radius: 6px;
      text-align: center;
      display: block;
      margin-top: 8px;
      text-decoration: none !important;
    }}
    .btn-wa-direct:hover {{
      background: #1eb956;
    }}

    /* Deliverables Grid (10 Tasks) */
    .deliverables-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
      gap: 20px;
      margin-top: 25px;
    }}
    .deliv-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow-sm);
      border-top: 4px solid var(--primary);
    }}
    .deliv-card .badge-task {{
      display: inline-block;
      background: #f1f5f9;
      color: var(--dark);
      font-size: 11px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
      margin-bottom: 10px;
    }}
    .deliv-card h2 {{
      font-size: 18px;
      margin-bottom: 10px;
      color: var(--dark);
    }}

    /* 4-Pillar Impact Grid */
    .impact-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-top: 20px;
    }}
    .impact-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
    }}
    .impact-card h2 {{
      font-size: 17px;
      margin-bottom: 8px;
    }}

    /* Plans Section */
    .plans-container {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 35px 25px;
      margin-bottom: 35px;
    }}
    .plans-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
      gap: 22px;
      margin: 25px 0;
      align-items: stretch;
    }}
    .plan-card {{
      background: #ffffff;
      border: 1.5px solid var(--border);
      border-radius: var(--radius);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }}
    .plan-card-header {{
      background: #1e529b;
      color: #ffffff;
      padding: 16px 20px;
      text-align: center;
    }}
    .plan-card-header h3 {{
      color: #ffffff !important;
      margin: 0;
      font-size: 20px;
    }}
    .plan-card-body {{
      padding: 22px 20px;
      flex: 1;
      display: flex;
      flex-direction: column;
    }}
    .plan-card-body p {{
      margin-bottom: 12px;
    }}
    .plan-cta {{
      margin-top: auto;
      padding-top: 15px;
    }}

    /* Accordion FAQs */
    .faq-accordion {{
      border: 1px solid var(--border);
      border-radius: 8px;
      margin-bottom: 12px;
      background: #ffffff;
      overflow: hidden;
    }}
    .faq-summary {{
      padding: 16px 20px;
      font-size: 16px;
      font-weight: 700;
      color: var(--dark);
      cursor: pointer;
      list-style: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #f8fafc;
    }}
    .faq-summary::-webkit-details-marker {{
      display: none;
    }}
    .faq-summary::after {{
      content: '+';
      font-size: 20px;
      color: var(--primary);
    }}
    .faq-accordion[open] .faq-summary::after {{
      content: '−';
    }}
    .faq-body {{
      padding: 18px 20px;
      border-top: 1px solid var(--border);
      background: #ffffff;
    }}

    /* Audit Lead Section */
    .audit-section {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: #ffffff;
      border-radius: var(--radius);
      padding: 40px 30px;
      margin-bottom: 40px;
      box-shadow: var(--shadow-lg);
    }}
    .audit-section h2 {{
      color: #38bdf8 !important;
      font-size: 28px;
      margin-bottom: 12px;
    }}
    .audit-section p {{
      color: #cbd5e1;
    }}
    .audit-section strong {{
      color: #ffffff;
    }}
    .audit-section ul li {{
      color: #f1f5f9;
      padding: 3px 0;
    }}
    .audit-form-box {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 8px;
      padding: 24px;
      margin-top: 25px;
    }}
    .audit-form-box input {{
      background: #0f172a;
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      padding: 12px;
      border-radius: 6px;
      width: 100%;
    }}

    /* Related Articles Grid */
    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }}
    .related-col {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 18px;
    }}
    .related-col h2 {{
      font-size: 16px;
      color: var(--primary);
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
      margin-bottom: 10px;
    }}

    /* Global Footer */
    .site-footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 40px 0;
      margin-top: 50px;
      font-size: 14px;
      border-top: 1px solid #1e293b;
    }}
    .footer-row {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
    }}

    /* Mobile Sticky Bar */
    .mobile-bar {{
      display: none;
    }}
    @media (max-width: 767px) {{
      .mobile-bar {{
        display: flex;
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #ffffff;
        border-top: 1px solid #cbd5e1;
        padding: 8px 12px;
        z-index: 9999;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        gap: 10px;
      }}
      .mobile-bar a {{
        flex: 1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-weight: 700;
        border-radius: 6px;
        text-decoration: none !important;
      }}
      .bar-call {{
        background: #f1f5f9;
        color: var(--dark) !important;
        border: 1px solid #cbd5e1;
      }}
      .bar-wa {{
        background: #25d366;
        color: #ffffff !important;
      }}
      body {{
        padding-bottom: 60px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Site Header -->
  <header class="site-header">
    <div class="container header-row">
      <div class="header-logo">
        <a href="https://www.gadigitalsolutions.com/">
          <img src="https://www.gadigitalsolutions.com/images/GADS%20LOGO-01.svg" alt="GA Digital Solutions Logo" height="52">
        </a>
      </div>
      <div class="header-actions">
        <a href="tel:9849574618" class="header-link">📞 +91 98495 74618</a>
        <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="header-cta-btn" target="_blank" rel="noopener noreferrer">
          💬 WhatsApp Support
        </a>
      </div>
    </div>
  </header>

  <!-- Sticky Quick-Nav -->
  <nav class="sticky-nav">
    <div class="container">
      <ul class="nav-scroller">
        <li><a href="#overview">Overview</a></li>
        <li><a href="#deliverables">10 Tasks Included</a></li>
        <li><a href="#why-matters">Why It Matters</a></li>
        <li><a href="#cost-neglect">Cost of Neglect</a></li>
        <li><a href="#schedule">Maintenance Schedule</a></li>
        <li><a href="#diy-vs-pro">DIY vs Pro</a></li>
        <li><a href="#plans" class="cta-pill">Maintenance Plans</a></li>
        <li><a href="#faqs">FAQs</a></li>
        <li><a href="#free-audit" class="cta-pill">Free 20-Point Audit</a></li>
      </ul>
    </div>
  </nav>

  <!-- Main Content Area -->
  <main class="container">

    <!-- HERO SECTION -->
    <section class="hero-layout" id="hero">
      <div>
        <div class="hero-media">
          <img src="https://www.gadigitalsolutions.com/images/Website_Maintenance.jpg" width="820" height="460" alt="Website Maintenance Services in India - GA Digital Solutions" fetchpriority="high">
        </div>
        {parts[0]}
        
        <div class="trust-strip">
          <div class="trust-item">🛡️ 24/7 Monitoring</div>
          <div class="trust-item">⚡ Staging Tested</div>
          <div class="trust-item">💾 Daily Cloud Backups</div>
          <div class="trust-item">⏱️ 30-Min SLA</div>
        </div>

        {parts[1]}
        {parts[2]}
      </div>

      <div>
        <div class="lead-card">
          <span class="lead-badge">Free Diagnostic</span>
          <h3>Get Your Free 20-Point Website Health Audit</h3>
          <p class="lead-desc">Find security vulnerabilities, outdated plugins, and mobile page speed issues.</p>
          
          <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20a%20free%20website%20health%20audit%20for:%20' + encodeURIComponent(this.website.value);">
            <div class="form-group">
              <label for="f-site">Website URL *</label>
              <input type="url" id="f-site" name="website" placeholder="https://yourcompany.com" required>
            </div>
            <div class="form-group">
              <label for="f-name">Your Name *</label>
              <input type="text" id="f-name" name="name" placeholder="John Doe" required>
            </div>
            <div class="form-group">
              <label for="f-phone">WhatsApp / Phone *</label>
              <input type="tel" id="f-phone" name="phone" placeholder="+91 98765 43210" required>
            </div>
            <button type="submit" class="btn-submit">
              Get Free Health Audit &rarr;
            </button>
            <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="btn-wa-direct" target="_blank" rel="noopener noreferrer">
              💬 Chat Directly on WhatsApp
            </a>
          </form>
          <p style="font-size: 11px; text-align: center; color: var(--muted); margin: 10px 0 0;">
            🔒 100% Free &amp; Confidential. No spam.
          </p>
        </div>
      </div>
    </section>

    <!-- OVERVIEW -->
    <section class="card card-accent" id="overview">
      {parts[3]}
      {parts[4]}
    </section>

    <!-- 10 DELIVERABLES -->
    <section id="deliverables" style="margin-bottom: 35px;">
      <div class="card" style="margin-bottom: 20px;">
        {parts[5]}
        {parts[6]}
      </div>
      <div class="deliverables-grid">
"""

# Append 10 deliverables
deliv_cards = []
for h_idx, b_idx, num in deliv_indices:
    clean_h2 = re.sub(r'<h2[^>]*>', '<h2>', parts[h_idx])
    deliv_cards.append(f"""
        <div class="deliv-card">
          <span class="badge-task">TASK #{num}</span>
          {clean_h2}
          {parts[b_idx]}
        </div>
    """)

standalone_html += "".join(deliv_cards)

standalone_html += f"""
      </div>
    </section>

    <!-- WHY IT MATTERS -->
    <section class="card" id="why-matters">
      {parts[27]}
      {parts[28]}
      <div class="impact-grid">
        <div class="impact-card" style="border-top: 3px solid #10b981;">{parts[29]}{parts[30]}</div>
        <div class="impact-card" style="border-top: 3px solid #ef4444;">{parts[31]}{parts[32]}</div>
        <div class="impact-card" style="border-top: 3px solid #f59e0b;">{parts[33]}{parts[34]}</div>
        <div class="impact-card" style="border-top: 3px solid #126db2;">{parts[35]}{parts[36]}</div>
      </div>
    </section>

    <!-- COST OF NEGLECT -->
    <section class="card card-warning" id="cost-neglect">
      {parts[37]}
      {parts[38]}
    </section>

    <!-- SCHEDULE -->
    <section class="card" id="schedule">
      {parts[39]}
      {parts[40]}
    </section>

    <!-- DIY VS PRO -->
    <section class="card" id="diy-vs-pro">
      {parts[41]}
      {parts[42]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">
        <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 20px;">{parts[43]}{parts[44]}</div>
        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 20px;">{parts[45]}{parts[46]}</div>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">
        <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 20px;">{parts[47]}{parts[48]}</div>
        <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 20px;">{parts[49]}{parts[50]}</div>
      </div>
      <div style="margin-top: 25px; border-top: 1px solid var(--border); padding-top: 20px;">
        {parts[51]}
        {parts[52]}
      </div>
    </section>

    <!-- PLANS SECTION -->
    <section class="plans-container" id="plans">
      {parts[53]}
      {plans_intro}

      <div class="plans-grid">
        <!-- Essential Plan -->
        <div class="plan-card">
          <div class="plan-card-header">
            <h3>Essential</h3>
          </div>
          <div class="plan-card-body">
            <p><strong>For brochure websites and small business sites</strong></p>
            <p>Ideal for: standard websites with stable content and moderate visitor traffic</p>
            <div class="plan-cta">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Essential%20Website%20Maintenance%20Plan" class="header-cta-btn" style="display:block; text-align:center;" target="_blank" rel="noopener noreferrer">
                Enquire on WhatsApp &rarr;
              </a>
            </div>
          </div>
        </div>

        <!-- Growth Plan -->
        <div class="plan-card" style="border: 2px solid var(--primary);">
          <div class="plan-card-header" style="background: var(--primary);">
            <h3>Growth</h3>
          </div>
          <div class="plan-card-body">
            <p><strong>For websites actively generating leads</strong></p>
            <p>Ideal for: businesses relying on their website for consistent lead generation</p>
            <div class="plan-cta">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Growth%20Website%20Maintenance%20Plan" class="header-cta-btn" style="display:block; text-align:center;" target="_blank" rel="noopener noreferrer">
                Enquire on WhatsApp &rarr;
              </a>
            </div>
          </div>
        </div>

        <!-- Business Plan -->
        <div class="plan-card">
          <div class="plan-card-header">
            <h3>Business</h3>
          </div>
          <div class="plan-card-body">
            <p><strong>For e-commerce, booking platforms, and high-traffic sites</strong></p>
            <p>Ideal for: e-commerce stores and businesses with significant revenue dependence on their website</p>
            <div class="plan-cta">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Business%20Website%20Maintenance%20Plan" class="header-cta-btn" style="display:block; text-align:center;" target="_blank" rel="noopener noreferrer">
                Enquire on WhatsApp &rarr;
              </a>
            </div>
          </div>
        </div>
      </div>

      {plans_closing}
    </section>

    <!-- INDUSTRIES -->
    <section class="card" id="industries">
      {parts[55]}
      {parts[56]}
    </section>

    <!-- FAQS -->
    <section id="faqs" style="margin-bottom: 35px;">
      <div class="card" style="margin-bottom: 20px;">
        {parts[57]}
        {faq_intro}
      </div>
"""

faq_elements = []
for q_text, a_text in faq_pairs:
    faq_elements.append(f"""
      <details class="faq-accordion">
        <summary class="faq-summary">{q_text.strip()}</summary>
        <div class="faq-body">{a_text.strip()}</div>
      </details>
    """)

standalone_html += "".join(faq_elements)

standalone_html += f"""
    </section>

    <!-- FREE AUDIT -->
    <section class="audit-section" id="free-audit">
      {parts[59]}
      {parts[60]}

      <div class="audit-form-box">
        <h3 style="margin-top: 0; color: #38bdf8; font-size: 20px; font-weight: 700;">
          ⚡ Enter Your Website to Start Your Free 20-Point Audit
        </h3>
        <p style="font-size: 14px; color: #cbd5e1; margin-bottom: 18px;">
          Submit your URL directly here and our team will begin your review with no obligation.
        </p>
        <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20requesting%20the%20Free%2020-Point%20Website%20Health%20Audit%20for:%20' + encodeURIComponent(this.audit_site.value) + '%20(Name:%20' + encodeURIComponent(this.audit_name.value) + ');'">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin-bottom: 15px;">
            <div>
              <label style="display:block; font-size: 12px; font-weight: 700; color: #94a3b8; margin-bottom: 5px;">WEBSITE URL *</label>
              <input type="url" name="audit_site" placeholder="https://yourwebsite.com" required>
            </div>
            <div>
              <label style="display:block; font-size: 12px; font-weight: 700; color: #94a3b8; margin-bottom: 5px;">YOUR NAME *</label>
              <input type="text" name="audit_name" placeholder="John Doe" required>
            </div>
            <div>
              <label style="display:block; font-size: 12px; font-weight: 700; color: #94a3b8; margin-bottom: 5px;">WHATSAPP / PHONE *</label>
              <input type="tel" name="audit_phone" placeholder="+91 98765 43210" required>
            </div>
          </div>
          <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 15px;">
            <button type="submit" class="btn-submit" style="flex: 2; min-width: 240px; padding: 14px;">
              Claim My Free Website Health Audit &rarr;
            </button>
            <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20to%20request%20the%20Free%20Website%20Health%20Audit%20directly" class="btn-wa-direct" style="flex: 1; min-width: 200px; padding: 14px; margin: 0;" target="_blank" rel="noopener noreferrer">
              💬 WhatsApp Fast Track
            </a>
          </div>
        </form>
      </div>
    </section>

    <!-- RELATED ARTICLES -->
    <section class="card" id="related-articles">
      {parts[61]}
      {parts[62]}
      <div class="related-grid">
        <div class="related-col">{parts[63]}{parts[64]}</div>
        <div class="related-col">{parts[65]}{parts[66]}</div>
        <div class="related-col">{parts[67]}{parts[68]}</div>
        <div class="related-col">{parts[69]}{parts[70]}</div>
      </div>
    </section>

  </main>

  <!-- Global Footer -->
  <footer class="site-footer">
    <div class="container footer-row">
      <div>
        <p style="color: #ffffff; font-weight: 700; margin-bottom: 4px;">GA Digital Solutions</p>
        <p style="color: #94a3b8; font-size: 13px; margin: 0;">A Business Unit of Gunnam Associates | Hyderabad, India</p>
      </div>
      <div>
        <p style="color: #94a3b8; font-size: 13px; margin: 0;">&copy; 2026 GA Digital Solutions. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <!-- Mobile Sticky Bar -->
  <div class="mobile-bar">
    <a href="tel:9849574618" class="bar-call">📞 Call Engineer</a>
    <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="bar-wa" target="_blank" rel="noopener noreferrer">💬 WhatsApp</a>
  </div>

</body>
</html>
"""

with open('website-maintenance-ux.html', 'w', encoding='utf-8') as f:
    f.write(standalone_html)

print("Successfully generated website-maintenance-ux.html! Size:", len(standalone_html))
