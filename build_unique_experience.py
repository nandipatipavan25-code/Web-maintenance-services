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

# Deliverable tasks 1 to 10 with categories for interactive filtering
deliv_data = [
    (7, 8, "01", "security", "Software & Plugins"),
    (9, 10, "02", "security", "Cloud Backups"),
    (11, 12, "03", "security", "Malware Defense"),
    (13, 14, "04", "performance", "24/7 Uptime"),
    (15, 16, "05", "performance", "Speed & Core Vitals"),
    (17, 18, "06", "maintenance", "Link & Error Checks"),
    (19, 20, "07", "maintenance", "Content Updates"),
    (21, 22, "08", "security", "SSL Management"),
    (23, 24, "09", "performance", "Database Optimization"),
    (25, 26, "10", "maintenance", "Analytics & Reporting"),
]

# Read official SVG logo code to embed directly into the custom GA Guardian Element
with open('gads_logo.svg', 'r', encoding='utf-8') as f:
    raw_svg_logo = f.read()

# Clean SVG for inline use in the badge/guardian
clean_svg_logo = re.sub(r'<\?xml[\s\S]*?\?>', '', raw_svg_logo).strip()

page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Website Maintenance Services in India | GA Digital Solutions</title>
  <meta name="description" content="Professional website maintenance services in India. 24/7 uptime monitoring, security scanning, daily backups, speed optimization & WordPress updates.">
  <link rel="canonical" href="https://gadigitalsolutions.com/services/website-maintenance">
  <link rel="icon" href="https://www.gadigitalsolutions.com/images/logo.png" type="image/png">

  <!-- Google Fonts: Plus Jakarta Sans & Space Grotesk -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">

  <style>
    :root {{
      --ga-blue-100: #e0f2fe;
      --ga-blue-500: #2296d3;
      --ga-blue-700: #1a4895;
      --ga-blue-900: #0f2b5c;
      --ga-navy-950: #0a1120;
      --ga-emerald: #10b981;
      --ga-amber: #f59e0b;
      --ga-red: #ef4444;
      --ga-slate-50: #f8fafc;
      --ga-slate-100: #f1f5f9;
      --ga-slate-200: #e2e8f0;
      --ga-slate-400: #94a3b8;
      --ga-slate-600: #475569;
      --ga-slate-800: #1e293b;
      --ga-slate-900: #0f172a;
      
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;

      --shadow-sm: 0 1px 3px rgba(10, 17, 32, 0.05);
      --shadow-md: 0 8px 24px -4px rgba(10, 17, 32, 0.08);
      --shadow-lg: 0 20px 45px -10px rgba(10, 17, 32, 0.12);
      --shadow-glow: 0 0 35px -5px rgba(34, 150, 211, 0.35);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--ga-slate-900);
      background-color: #ffffff;
      line-height: 1.7;
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}

    a {{
      color: var(--ga-blue-500);
      text-decoration: none;
      transition: all 0.2s ease;
    }}
    a:hover {{
      color: var(--ga-blue-700);
      text-decoration: underline;
    }}

    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    /* Global Header */
    .ga-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--ga-slate-200);
      padding: 16px 0;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }}
    .ga-header-flex {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }}
    .ga-brand-logo img {{
      height: 48px;
      width: auto;
      display: block;
    }}
    .ga-header-meta {{
      display: flex;
      align-items: center;
      gap: 20px;
    }}
    .ga-tel-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 14px;
      font-weight: 700;
      color: var(--ga-slate-800);
      text-decoration: none !important;
    }}
    .ga-tel-link:hover {{
      color: var(--ga-blue-500);
    }}
    .ga-header-cta {{
      background: linear-gradient(135deg, var(--ga-blue-500), var(--ga-blue-700));
      color: #ffffff !important;
      font-size: 14px;
      font-weight: 700;
      padding: 9px 18px;
      border-radius: var(--radius-sm);
      box-shadow: 0 4px 14px rgba(34, 150, 211, 0.3);
      text-decoration: none !important;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }}
    .ga-header-cta:hover {{
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(34, 150, 211, 0.45);
    }}

    /* Wayfinding Sticky Nav */
    .ga-subnav {{
      background: var(--ga-slate-50);
      border-bottom: 1px solid var(--ga-slate-200);
      padding: 8px 0;
      margin-bottom: 35px;
    }}
    .ga-nav-pills {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      list-style: none;
      scrollbar-width: none;
      white-space: nowrap;
    }}
    .ga-nav-pills::-webkit-scrollbar {{ display: none; }}
    .ga-nav-pills li a {{
      display: inline-block;
      padding: 6px 14px;
      font-size: 13px;
      font-weight: 600;
      color: var(--ga-slate-600);
      border-radius: var(--radius-full);
      text-decoration: none;
      transition: all 0.2s;
    }}
    .ga-nav-pills li a:hover {{
      background: #ffffff;
      color: var(--ga-blue-700);
      box-shadow: var(--shadow-sm);
    }}
    .ga-nav-pills li a.active-pill {{
      background: var(--ga-blue-700);
      color: #ffffff;
    }}

    /* Typography */
    h1 {{
      font-size: 34px;
      font-weight: 800;
      line-height: 1.25;
      color: var(--ga-slate-900);
      letter-spacing: -0.025em;
      margin-bottom: 16px;
    }}
    @media (min-width: 768px) {{
      h1 {{ font-size: 40px; }}
    }}

    h2 {{
      font-size: 24px;
      font-weight: 700;
      color: var(--ga-slate-900);
      margin-bottom: 14px;
      letter-spacing: -0.02em;
    }}

    p {{
      color: var(--ga-slate-600);
      font-size: 16px;
      line-height: 1.75;
      margin-bottom: 16px;
    }}

    /* =========================================================
       SIGNATURE ELEMENT: THE "GA GUARDIAN RADAR HUB" (BESPOKE UI)
       ========================================================= */
    .ga-guardian-card {{
      background: linear-gradient(145deg, #ffffff 0%, #f0f9fb 100%);
      border: 2px solid #bae6fd;
      border-radius: var(--radius-lg);
      padding: 28px 24px;
      box-shadow: var(--shadow-lg), var(--shadow-glow);
      position: relative;
      overflow: hidden;
    }}
    .ga-guardian-card::after {{
      content: '';
      position: absolute;
      top: -60px;
      right: -60px;
      width: 180px;
      height: 180px;
      background: radial-gradient(circle, rgba(34, 150, 211, 0.15) 0%, rgba(34, 150, 211, 0) 70%);
      pointer-events: none;
    }}
    .ga-guardian-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--ga-slate-200);
    }}
    .ga-emblem-badge {{
      width: 44px;
      height: 44px;
      border-radius: 10px;
      background: #ffffff;
      padding: 4px;
      border: 1px solid #bae6fd;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 10px rgba(34, 150, 211, 0.2);
    }}
    .ga-emblem-badge svg {{
      width: 100%;
      height: 100%;
    }}
    .ga-guardian-title h3 {{
      font-size: 18px;
      font-weight: 800;
      color: var(--ga-blue-700);
      margin: 0;
    }}
    .ga-pulse-status {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 700;
      color: var(--ga-emerald);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .ga-pulse-dot {{
      width: 7px;
      height: 7px;
      background: var(--ga-emerald);
      border-radius: 50%;
      box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
      animation: ga-pulse 1.8s infinite;
    }}
    @keyframes ga-pulse {{
      0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }}
      70% {{ transform: scale(1); box-shadow: 0 0 0 7px rgba(16, 185, 129, 0); }}
      100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
    }}

    .ga-telemetry-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-bottom: 18px;
    }}
    .ga-telemetry-item {{
      background: #ffffff;
      border: 1px solid #e0f2fe;
      border-radius: var(--radius-sm);
      padding: 8px 10px;
      font-size: 11px;
      font-weight: 700;
      color: var(--ga-slate-800);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .ga-telemetry-item span.icon {{
      font-size: 14px;
    }}

    .ga-audit-form label {{
      display: block;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--ga-slate-600);
      margin-bottom: 4px;
    }}
    .ga-audit-form input {{
      width: 100%;
      padding: 10px 12px;
      border: 1.5px solid var(--ga-slate-200);
      border-radius: var(--radius-sm);
      font-size: 14px;
      margin-bottom: 10px;
      background: #ffffff;
      font-family: inherit;
    }}
    .ga-audit-form input:focus {{
      outline: none;
      border-color: var(--ga-blue-500);
      box-shadow: 0 0 0 3px rgba(34, 150, 211, 0.15);
    }}
    .ga-btn-submit {{
      width: 100%;
      background: linear-gradient(135deg, var(--ga-blue-500), var(--ga-blue-700));
      color: #ffffff;
      font-size: 15px;
      font-weight: 700;
      padding: 12px;
      border: none;
      border-radius: var(--radius-sm);
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(34, 150, 211, 0.35);
      transition: all 0.2s;
    }}
    .ga-btn-submit:hover {{
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(34, 150, 211, 0.45);
    }}
    .ga-btn-wa-hero {{
      width: 100%;
      background: #25d366;
      color: #ffffff !important;
      font-size: 13px;
      font-weight: 700;
      padding: 10px;
      border-radius: var(--radius-sm);
      text-align: center;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      margin-top: 8px;
      text-decoration: none !important;
    }}

    /* Hero Layout Grid */
    .ga-hero-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 35px;
      align-items: start;
      margin-bottom: 45px;
    }}
    @media (min-width: 992px) {{
      .ga-hero-grid {{
        grid-template-columns: 1.15fr 0.85fr;
      }}
    }}
    .ga-hero-visual {{
      border-radius: var(--radius-lg);
      overflow: hidden;
      margin-bottom: 24px;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--ga-slate-200);
    }}

    /* Card Containers */
    .ga-card {{
      background: #ffffff;
      border: 1px solid var(--ga-slate-200);
      border-radius: var(--radius-lg);
      padding: 32px 28px;
      margin-bottom: 35px;
      box-shadow: var(--shadow-sm);
    }}
    .ga-card-accent {{
      border-left: 6px solid var(--ga-blue-500);
      background: linear-gradient(180deg, #f0f9fb 0%, #ffffff 100%);
    }}
    .ga-card-warning {{
      border-left: 6px solid var(--ga-amber);
      background: #fffbeb;
    }}

    /* 10 Deliverables Interactive Bento Grid */
    .ga-filter-toolbar {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 18px 0 25px;
    }}
    .ga-filter-btn {{
      background: var(--ga-slate-100);
      border: 1px solid var(--ga-slate-200);
      border-radius: var(--radius-full);
      padding: 6px 14px;
      font-size: 13px;
      font-weight: 700;
      color: var(--ga-slate-600);
      cursor: pointer;
      transition: all 0.2s;
    }}
    .ga-filter-btn.active, .ga-filter-btn:hover {{
      background: var(--ga-blue-700);
      color: #ffffff;
      border-color: var(--ga-blue-700);
    }}

    .ga-deliverables-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
    }}
    .ga-deliv-box {{
      background: #ffffff;
      border: 1px solid var(--ga-slate-200);
      border-radius: var(--radius-md);
      padding: 24px;
      box-shadow: var(--shadow-sm);
      border-top: 4px solid var(--ga-blue-500);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .ga-deliv-box:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
    }}
    .ga-task-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .ga-task-tag {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 11px;
      font-weight: 700;
      color: var(--ga-blue-700);
      background: var(--ga-blue-100);
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .ga-deliv-box h2 {{
      font-size: 18px;
      margin-bottom: 10px;
    }}

    /* 4-Pillar Impact Grid */
    .ga-impact-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-top: 20px;
    }}
    .ga-impact-card {{
      background: #ffffff;
      border: 1px solid var(--ga-slate-200);
      border-radius: var(--radius-md);
      padding: 20px;
    }}
    .ga-impact-card h2 {{
      font-size: 17px;
      margin-bottom: 8px;
    }}

    /* Plans Section */
    .ga-plans-wrap {{
      background: var(--ga-slate-50);
      border: 1px solid var(--ga-slate-200);
      border-radius: var(--radius-lg);
      padding: 35px 28px;
      margin-bottom: 35px;
    }}
    .ga-plans-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
      gap: 22px;
      margin: 25px 0;
    }}
    .ga-plan-tier {{
      background: #ffffff;
      border: 1.5px solid var(--ga-slate-200);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-sm);
    }}
    .ga-plan-top {{
      background: linear-gradient(135deg, var(--ga-blue-700), var(--ga-blue-900));
      color: #ffffff;
      padding: 16px 20px;
      text-align: center;
    }}
    .ga-plan-top h3 {{
      color: #ffffff !important;
      margin: 0;
      font-size: 20px;
    }}
    .ga-plan-content {{
      padding: 22px 20px;
      flex: 1;
      display: flex;
      flex-direction: column;
    }}
    .ga-plan-content p {{
      margin-bottom: 12px;
    }}
    .ga-plan-btn {{
      margin-top: auto;
      padding-top: 15px;
    }}
    .ga-plan-btn a {{
      display: block;
      text-align: center;
      background: var(--ga-blue-700);
      color: #ffffff !important;
      font-size: 14px;
      font-weight: 700;
      padding: 11px;
      border-radius: var(--radius-sm);
      text-decoration: none !important;
    }}
    .ga-plan-btn a:hover {{
      background: var(--ga-blue-900);
    }}

    /* Accordion FAQs */
    .ga-faq {{
      border: 1px solid var(--ga-slate-200);
      border-radius: var(--radius-sm);
      margin-bottom: 10px;
      background: #ffffff;
    }}
    .ga-faq-summary {{
      padding: 16px 20px;
      font-size: 16px;
      font-weight: 700;
      color: var(--ga-slate-900);
      cursor: pointer;
      list-style: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--ga-slate-50);
    }}
    .ga-faq-summary::-webkit-details-marker {{ display: none; }}
    .ga-faq-summary::after {{
      content: '+';
      font-size: 20px;
      color: var(--ga-blue-500);
    }}
    .ga-faq[open] .ga-faq-summary::after {{
      content: '−';
    }}
    .ga-faq-body {{
      padding: 18px 20px;
      border-top: 1px solid var(--ga-slate-200);
    }}

    /* Signature High-Tech Health Audit Section */
    .ga-audit-hub {{
      background: linear-gradient(135deg, var(--ga-navy-950) 0%, var(--ga-slate-900) 100%);
      color: #ffffff;
      border-radius: var(--radius-lg);
      padding: 45px 35px;
      margin-bottom: 40px;
      box-shadow: var(--shadow-lg);
      position: relative;
      overflow: hidden;
    }}
    .ga-audit-hub h2 {{
      color: #38bdf8 !important;
      font-size: 28px;
      margin-bottom: 12px;
    }}
    .ga-audit-hub p {{
      color: var(--ga-slate-400);
    }}
    .ga-audit-hub strong {{
      color: #ffffff;
    }}
    .ga-audit-hub ul li {{
      color: #f1f5f9;
      padding: 3px 0;
    }}
    .ga-hub-form-box {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-md);
      padding: 24px;
      margin-top: 25px;
      backdrop-filter: blur(12px);
    }}
    .ga-hub-form-box input {{
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      padding: 12px;
      border-radius: var(--radius-sm);
      width: 100%;
      font-family: inherit;
    }}

    /* Related Articles */
    .ga-articles-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }}
    .ga-article-col {{
      background: var(--ga-slate-50);
      border: 1px solid var(--ga-slate-200);
      border-radius: var(--radius-md);
      padding: 18px;
    }}
    .ga-article-col h2 {{
      font-size: 16px;
      color: var(--ga-blue-700);
      border-bottom: 1px solid var(--ga-slate-200);
      padding-bottom: 8px;
      margin-bottom: 10px;
    }}

    /* Global Footer */
    .ga-footer {{
      background: var(--ga-slate-900);
      color: var(--ga-slate-400);
      padding: 40px 0;
      margin-top: 60px;
      border-top: 1px solid var(--ga-slate-800);
    }}
    .ga-footer-row {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
    }}

    /* Floating Emergency Hub Drawer */
    .ga-floating-hub {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999;
    }}
    .ga-hub-trigger {{
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--ga-blue-500), var(--ga-blue-700));
      box-shadow: 0 8px 25px rgba(34, 150, 211, 0.45);
      border: 2px solid #ffffff;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 10px;
      transition: transform 0.2s;
    }}
    .ga-hub-trigger:hover {{
      transform: scale(1.08);
    }}
    .ga-hub-menu {{
      display: none;
      position: absolute;
      bottom: 70px;
      right: 0;
      width: 290px;
      background: #ffffff;
      border: 1px solid var(--ga-slate-200);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-lg);
      padding: 16px;
      animation: ga-slide 0.2s ease;
    }}
    @keyframes ga-slide {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    .ga-hub-menu.open {{
      display: block;
    }}
    .ga-hub-action-item {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px;
      border-radius: var(--radius-sm);
      text-decoration: none !important;
      font-size: 13px;
      font-weight: 700;
      color: var(--ga-slate-800);
      transition: background 0.2s;
      margin-bottom: 6px;
    }}
    .ga-hub-action-item:hover {{
      background: var(--ga-slate-100);
      color: var(--ga-blue-700);
    }}
  </style>
</head>
<body>

  <!-- Global Header -->
  <header class="ga-header">
    <div class="container ga-header-flex">
      <div class="ga-brand-logo">
        <a href="https://www.gadigitalsolutions.com/">
          <img src="https://www.gadigitalsolutions.com/images/GADS%20LOGO-01.svg" alt="GA Digital Solutions Logo" height="48">
        </a>
      </div>
      <div class="ga-header-meta">
        <a href="tel:9849574618" class="ga-tel-link">📞 +91 98495 74618</a>
        <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="ga-header-cta" target="_blank" rel="noopener noreferrer">
          💬 WhatsApp Support
        </a>
      </div>
    </div>
  </header>

  <!-- Wayfinding Sub-Navigation -->
  <nav class="ga-subnav">
    <div class="container">
      <ul class="ga-nav-pills">
        <li><a href="#overview">Overview</a></li>
        <li><a href="#deliverables">10 Maintenance Tasks</a></li>
        <li><a href="#why-matters">Why It Matters</a></li>
        <li><a href="#cost-neglect">Cost of Neglect</a></li>
        <li><a href="#schedule">Schedule Cadence</a></li>
        <li><a href="#diy-vs-pro">DIY vs Pro</a></li>
        <li><a href="#plans">Maintenance Plans</a></li>
        <li><a href="#faqs">FAQs</a></li>
        <li><a href="#free-audit" class="active-pill">Claim Free Audit</a></li>
      </ul>
    </div>
  </nav>

  <!-- Main Content Layout -->
  <main class="container">

    <!-- HERO SECTION WITH SIGNATURE GUARDIAN HUB -->
    <section class="ga-hero-grid" id="hero">
      <div>
        <div class="ga-hero-visual">
          <img src="https://www.gadigitalsolutions.com/images/Website_Maintenance.jpg" width="820" height="460" alt="Website Maintenance Services in India - GA Digital Solutions" fetchpriority="high">
        </div>
        {parts[0]}
        {parts[1]}
        {parts[2]}
      </div>

      <!-- SIGNATURE GA GUARDIAN ELEMENT (BESPOKE UI INTEGRATING THE EMBLEM) -->
      <div>
        <div class="ga-guardian-card">
          <div class="ga-guardian-header">
            <div class="ga-emblem-badge">
              {clean_svg_logo}
            </div>
            <div class="ga-guardian-title">
              <h3>GA Sentinel Guardian Hub</h3>
              <div class="ga-pulse-status">
                <span class="ga-pulse-dot"></span> 24/7 Active Site Defense
              </div>
            </div>
          </div>

          <div class="ga-telemetry-grid">
            <div class="ga-telemetry-item"><span class="icon">🛡️</span> 24/7 Uptime Ping</div>
            <div class="ga-telemetry-item"><span class="icon">⚡</span> Staging Tested</div>
            <div class="ga-telemetry-item"><span class="icon">💾</span> Cloud Daily Sync</div>
            <div class="ga-telemetry-item"><span class="icon">⏱️</span> 30-Min SLA</div>
          </div>

          <p style="font-size: 13px; color: var(--ga-slate-600); margin-bottom: 14px;">
            Run a complimentary 20-point diagnostic on your website to uncover security vulnerabilities, plugin conflicts, and speed issues:
          </p>

          <form class="ga-audit-form" onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20a%20free%20website%20health%20audit%20for:%20' + encodeURIComponent(this.website.value);">
            <div>
              <label for="hub-url">Website URL *</label>
              <input type="url" id="hub-url" name="website" placeholder="https://yourcompany.com" required>
            </div>
            <div>
              <label for="hub-name">Your Name *</label>
              <input type="text" id="hub-name" name="name" placeholder="John Doe" required>
            </div>
            <div>
              <label for="hub-phone">WhatsApp / Phone *</label>
              <input type="tel" id="hub-phone" name="phone" placeholder="+91 98765 43210" required>
            </div>
            <button type="submit" class="ga-btn-submit">
              Run Free 20-Point Health Audit &rarr;
            </button>
            <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="ga-btn-wa-hero" target="_blank" rel="noopener noreferrer">
              💬 Instant WhatsApp Consultation
            </a>
          </form>
          <p style="font-size: 11px; text-align: center; color: var(--ga-slate-400); margin: 8px 0 0;">
            🔒 100% Free &amp; Confidential. Direct engineer review.
          </p>
        </div>
      </div>
    </section>

    <!-- OVERVIEW CARD -->
    <section class="ga-card ga-card-accent" id="overview">
      {parts[3]}
      {parts[4]}
    </section>

    <!-- 10 DELIVERABLES WITH INTERACTIVE FILTERING TOOLBAR -->
    <section id="deliverables" style="margin-bottom: 40px;">
      <div class="ga-card" style="margin-bottom: 20px;">
        {parts[5]}
        {parts[6]}

        <div class="ga-filter-toolbar">
          <button class="ga-filter-btn active" onclick="filterTasks('all', this)">All 10 Tasks</button>
          <button class="ga-filter-btn" onclick="filterTasks('security', this)">🛡️ Security &amp; Backups</button>
          <button class="ga-filter-btn" onclick="filterTasks('performance', this)">⚡ Speed &amp; Uptime</button>
          <button class="ga-filter-btn" onclick="filterTasks('maintenance', this)">🛠️ Content &amp; Health</button>
        </div>
      </div>

      <div class="ga-deliverables-grid">
"""

for h_idx, b_idx, num, cat, tag in deliv_data:
    clean_h2 = re.sub(r'<h2[^>]*>', '<h2>', parts[h_idx])
    page_html += f"""
        <div class="ga-deliv-box" data-cat="{cat}">
          <div class="ga-task-header">
            <span class="ga-task-tag">TASK #{num}</span>
            <span style="font-size: 11px; font-weight: 700; color: var(--ga-slate-400);">{tag}</span>
          </div>
          {clean_h2}
          {parts[b_idx]}
        </div>
    """

page_html += f"""
      </div>
    </section>

    <!-- WHY IT MATTERS IMPACT GRID -->
    <section class="ga-card" id="why-matters">
      {parts[27]}
      {parts[28]}
      <div class="ga-impact-grid">
        <div class="ga-impact-card" style="border-top: 3px solid #10b981;">{parts[29]}{parts[30]}</div>
        <div class="ga-impact-card" style="border-top: 3px solid #ef4444;">{parts[31]}{parts[32]}</div>
        <div class="ga-impact-card" style="border-top: 3px solid #f59e0b;">{parts[33]}{parts[34]}</div>
        <div class="ga-impact-card" style="border-top: 3px solid #2296d3;">{parts[35]}{parts[36]}</div>
      </div>
    </section>

    <!-- COST OF NEGLECT -->
    <section class="ga-card ga-card-warning" id="cost-neglect">
      {parts[37]}
      {parts[38]}
    </section>

    <!-- SCHEDULE -->
    <section class="ga-card" id="schedule">
      {parts[39]}
      {parts[40]}
    </section>

    <!-- DIY VS PRO -->
    <section class="ga-card" id="diy-vs-pro">
      {parts[41]}
      {parts[42]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">
        <div style="background: #f8fafc; border: 1px solid var(--ga-slate-200); border-radius: var(--radius-md); padding: 22px;">{parts[43]}{parts[44]}</div>
        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: var(--radius-md); padding: 22px;">{parts[45]}{parts[46]}</div>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 20px 0;">
        <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: var(--radius-md); padding: 22px;">{parts[47]}{parts[48]}</div>
        <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: var(--radius-md); padding: 22px;">{parts[49]}{parts[50]}</div>
      </div>
      <div style="margin-top: 25px; border-top: 1px solid var(--ga-slate-200); padding-top: 20px;">
        {parts[51]}
        {parts[52]}
      </div>
    </section>

    <!-- PLANS & PRICING -->
    <section class="ga-plans-wrap" id="plans">
      {parts[53]}
      {plans_intro}

      <div class="ga-plans-grid">
        <!-- Essential Plan -->
        <div class="ga-plan-tier">
          <div class="ga-plan-top">
            <h3>Essential</h3>
          </div>
          <div class="ga-plan-content">
            <p><strong>For brochure websites and small business sites</strong></p>
            <p>Ideal for: standard websites with stable content and moderate visitor traffic</p>
            <div class="ga-plan-btn">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Essential%20Website%20Maintenance%20Plan" target="_blank" rel="noopener noreferrer">
                Enquire on WhatsApp &rarr;
              </a>
            </div>
          </div>
        </div>

        <!-- Growth Plan -->
        <div class="ga-plan-tier" style="border: 2px solid var(--ga-blue-500); box-shadow: 0 8px 25px rgba(34, 150, 211, 0.15);">
          <div class="ga-plan-top" style="background: linear-gradient(135deg, var(--ga-blue-500), var(--ga-blue-700));">
            <h3>Growth</h3>
          </div>
          <div class="ga-plan-content">
            <p><strong>For websites actively generating leads</strong></p>
            <p>Ideal for: businesses relying on their website for consistent lead generation</p>
            <div class="ga-plan-btn">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Growth%20Website%20Maintenance%20Plan" style="background: var(--ga-blue-500);" target="_blank" rel="noopener noreferrer">
                Enquire on WhatsApp &rarr;
              </a>
            </div>
          </div>
        </div>

        <!-- Business Plan -->
        <div class="ga-plan-tier">
          <div class="ga-plan-top">
            <h3>Business</h3>
          </div>
          <div class="ga-plan-content">
            <p><strong>For e-commerce, booking platforms, and high-traffic sites</strong></p>
            <p>Ideal for: e-commerce stores and businesses with significant revenue dependence on their website</p>
            <div class="ga-plan-btn">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Business%20Website%20Maintenance%20Plan" target="_blank" rel="noopener noreferrer">
                Enquire on WhatsApp &rarr;
              </a>
            </div>
          </div>
        </div>
      </div>

      {plans_closing}
    </section>

    <!-- INDUSTRIES -->
    <section class="ga-card" id="industries">
      {parts[55]}
      {parts[56]}
    </section>

    <!-- FAQS (EXPANDABLE DETAILS) -->
    <section id="faqs" style="margin-bottom: 35px;">
      <div class="ga-card" style="margin-bottom: 20px;">
        {parts[57]}
        {faq_intro}
      </div>
"""

for q_text, a_text in faq_pairs:
    page_html += f"""
      <details class="ga-faq">
        <summary class="ga-faq-summary">{q_text.strip()}</summary>
        <div class="ga-faq-body">{a_text.strip()}</div>
      </details>
    """

page_html += f"""
    </section>

    <!-- SIGNATURE DARK AUDIT HUB -->
    <section class="ga-audit-hub" id="free-audit">
      {parts[59]}
      {parts[60]}

      <div class="ga-hub-form-box">
        <h3 style="margin-top: 0; color: #38bdf8; font-size: 20px; font-weight: 700;">
          ⚡ Enter Your Website to Start Your Free 20-Point Audit
        </h3>
        <p style="font-size: 14px; color: var(--ga-slate-400); margin-bottom: 18px;">
          Submit your URL directly here and our engineering team will initiate your review with zero obligation.
        </p>
        <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20requesting%20the%20Free%2020-Point%20Website%20Health%20Audit%20for:%20' + encodeURIComponent(this.audit_site.value) + '%20(Name:%20' + encodeURIComponent(this.audit_name.value) + ');'">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin-bottom: 15px;">
            <div>
              <label style="display:block; font-size: 12px; font-weight: 700; color: var(--ga-slate-400); margin-bottom: 5px;">WEBSITE URL *</label>
              <input type="url" name="audit_site" placeholder="https://yourwebsite.com" required>
            </div>
            <div>
              <label style="display:block; font-size: 12px; font-weight: 700; color: var(--ga-slate-400); margin-bottom: 5px;">YOUR NAME *</label>
              <input type="text" name="audit_name" placeholder="John Doe" required>
            </div>
            <div>
              <label style="display:block; font-size: 12px; font-weight: 700; color: var(--ga-slate-400); margin-bottom: 5px;">WHATSAPP / PHONE *</label>
              <input type="tel" name="audit_phone" placeholder="+91 98765 43210" required>
            </div>
          </div>
          <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 15px;">
            <button type="submit" class="ga-btn-submit" style="flex: 2; min-width: 240px; padding: 14px;">
              Claim My Free Website Health Audit &rarr;
            </button>
            <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20to%20request%20the%20Free%20Website%20Health%20Audit%20directly" class="ga-btn-wa-hero" style="flex: 1; min-width: 200px; padding: 14px; margin: 0;" target="_blank" rel="noopener noreferrer">
              💬 WhatsApp Fast Track
            </a>
          </div>
        </form>
      </div>
    </section>

    <!-- RELATED ARTICLES -->
    <section class="ga-card" id="related-articles">
      {parts[61]}
      {parts[62]}
      <div class="ga-articles-grid">
        <div class="ga-article-col">{parts[63]}{parts[64]}</div>
        <div class="ga-article-col">{parts[65]}{parts[66]}</div>
        <div class="ga-article-col">{parts[67]}{parts[68]}</div>
        <div class="ga-article-col">{parts[69]}{parts[70]}</div>
      </div>
    </section>

  </main>

  <!-- Global Footer -->
  <footer class="ga-footer">
    <div class="container ga-footer-row">
      <div style="display: flex; align-items: center; gap: 14px;">
        <img src="https://www.gadigitalsolutions.com/images/logo.png" alt="GA Logo" height="32" style="border-radius: 4px;">
        <div>
          <p style="color: #ffffff; font-weight: 700; margin: 0; font-size: 15px;">GA Digital Solutions</p>
          <p style="color: var(--ga-slate-400); font-size: 13px; margin: 0;">A Business Unit of Gunnam Associates | Hyderabad, India</p>
        </div>
      </div>
      <div>
        <p style="color: var(--ga-slate-400); font-size: 13px; margin: 0;">&copy; 2026 GA Digital Solutions. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <!-- FLOATING GA EMERGENCY HUB (EXPANDABLE DRAWER) -->
  <div class="ga-floating-hub">
    <div class="ga-hub-menu" id="hubMenu">
      <div style="font-size: 12px; font-weight: 800; color: var(--ga-blue-700); text-transform: uppercase; margin-bottom: 8px;">
        GA Support &amp; Response Hub
      </div>
      <a href="https://wa.me/919849574618?text=EMERGENCY:%20My%20website%20is%20down%20or%20hacked!" class="ga-hub-action-item" style="color: #ef4444;" target="_blank" rel="noopener noreferrer">
        🚨 Emergency: Site Down / Hacked
      </a>
      <a href="#free-audit" class="ga-hub-action-item">
        🎁 Claim Free 20-Point Audit
      </a>
      <a href="tel:9849574618" class="ga-hub-action-item">
        📞 Call On-Call Engineer
      </a>
    </div>
    <button class="ga-hub-trigger" onclick="toggleHubMenu()" aria-label="Open GA Support Hub">
      <img src="https://www.gadigitalsolutions.com/images/logo.png" alt="GA Support" style="width: 100%; height: auto; border-radius: 50%;">
    </button>
  </div>

  <script>
    function toggleHubMenu() {{
      const menu = document.getElementById('hubMenu');
      menu.classList.toggle('open');
    }}

    function filterTasks(cat, btn) {{
      document.querySelectorAll('.ga-filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const boxes = document.querySelectorAll('.ga-deliv-box');
      boxes.forEach(box => {{
        if (cat === 'all' || box.getAttribute('data-cat') === cat) {{
          box.style.display = 'block';
        }} else {{
          box.style.display = 'none';
        }}
      }});
    }}
  </script>

</body>
</html>
"""

with open('unique-website-maintenance.html', 'w', encoding='utf-8') as f:
    f.write(page_html)

print("Successfully generated unique-website-maintenance.html! Total length:", len(page_html))
