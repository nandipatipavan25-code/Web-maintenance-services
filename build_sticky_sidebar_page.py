import re

from builder_core import (
    parts, faq_intro, faq_pairs, plans_intro, plans_closing, 
    deliv_data, clean_svg_logo
)

# Build deliverable cards
deliv_cards_html = "".join([f"""
  <div class="deliv-card">
    <div class="task-badge">TASK #{num}</div>
    {re.sub(r'<h2[^>]*>', '<h2>', parts[h])}
    {parts[b]}
  </div>
""" for h, b, num, title, cat in deliv_data])

# Build FAQ accordions
faq_accordions_html = "".join([f"""
  <details class="faq-item">
    <summary class="faq-summary">{q.strip()}</summary>
    <div class="faq-body">{a.strip()}</div>
  </details>
""" for q, a in faq_pairs])

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Website Maintenance Services in India | GA Digital Solutions</title>
  <meta name="description" content="Professional website maintenance services in India. 24/7 uptime monitoring, security scanning, daily backups, speed optimization & WordPress updates.">
  <link rel="canonical" href="https://gadigitalsolutions.com/services/website-maintenance">
  <link rel="icon" href="https://www.gadigitalsolutions.com/images/logo.png" type="image/png">

  <!-- Google Fonts: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@700&display=swap" rel="stylesheet">

  <style>
    :root {{
      --primary: #126db2;
      --primary-dark: #0d4e80;
      --primary-light: #e0f2fe;
      --accent-blue: #0284c7;
      --emerald: #10b981;
      --amber: #f59e0b;
      --red: #ef4444;
      --dark: #0f172a;
      --slate-800: #1e293b;
      --slate-600: #475569;
      --slate-400: #94a3b8;
      --slate-100: #f1f5f9;
      --border: #e2e8f0;
      --bg-page: #f8fafc;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
      --shadow-md: 0 6px 18px rgba(0,0,0,0.08);
      --shadow-lg: 0 12px 35px rgba(0,0,0,0.1);
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
      color: var(--dark);
      background-color: var(--bg-page);
      line-height: 1.7;
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
    }}

    a {{
      color: var(--primary);
      text-decoration: none;
      transition: all 0.2s;
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

    /* Top Utility Header */
    .top-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 12px 0;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(10px);
    }}
    .top-header-flex {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }}
    .top-logo img {{
      height: 44px;
      width: auto;
    }}
    .top-contact {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .top-phone {{
      font-size: 14px;
      font-weight: 700;
      color: var(--slate-800);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none !important;
    }}
    .top-phone:hover {{
      color: var(--primary);
    }}
    .top-wa-btn {{
      background: #25d366;
      color: #ffffff !important;
      font-size: 13px;
      font-weight: 700;
      padding: 8px 16px;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none !important;
      transition: background 0.2s;
    }}
    .top-wa-btn:hover {{
      background: #1eb956;
    }}

    /* Main 2-Column Layout */
    .layout-wrapper {{
      max-width: 1400px;
      margin: 25px auto 50px;
      padding: 0 24px;
    }}
    .page-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 40px;
      align-items: start;
    }}
    @media (min-width: 1024px) {{
      .page-grid {{
        grid-template-columns: 360px minmax(0, 1fr);
      }}
    }}

    /* =========================================================
       LEFT-SIDE STICKY SIDEBAR: OVERVIEW BAR + FORM + WHATSAPP
       ========================================================= */
    .sticky-sidebar {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    @media (min-width: 1024px) {{
      .sticky-sidebar {{
        position: sticky;
        top: 85px;
        max-height: calc(100vh - 105px);
        overflow-y: auto;
        padding-right: 6px;
        scrollbar-width: thin;
        scrollbar-color: #cbd5e1 transparent;
      }}
      .sticky-sidebar::-webkit-scrollbar {{
        width: 5px;
      }}
      .sticky-sidebar::-webkit-scrollbar-thumb {{
        background: #cbd5e1;
        border-radius: 4px;
      }}
    }}

    /* Sidebar Brand & Status Card */
    .side-brand-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}
    .side-pulse {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 700;
      color: var(--emerald);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .pulse-dot {{
      width: 7px;
      height: 7px;
      background: var(--emerald);
      border-radius: 50%;
      box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
      animation: pulse 1.8s infinite;
    }}
    @keyframes pulse {{
      0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }}
      70% {{ transform: scale(1); box-shadow: 0 0 0 7px rgba(16, 185, 129, 0); }}
      100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
    }}

    /* Sidebar Page Overview Bar (Table of Contents) */
    .side-overview-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 20px;
      box-shadow: var(--shadow-sm);
    }}
    .side-overview-title {{
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--slate-400);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .side-nav-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .side-nav-link {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 7px 12px;
      border-radius: 6px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--slate-600);
      text-decoration: none !important;
      transition: all 0.2s;
    }}
    .side-nav-link:hover {{
      background: var(--slate-100);
      color: var(--primary);
      transform: translateX(3px);
    }}
    .side-nav-link.active {{
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 700;
      border-left: 3px solid var(--primary);
    }}
    .side-nav-link .nav-num {{
      font-size: 11px;
      font-weight: 700;
      color: var(--slate-400);
      min-width: 18px;
    }}

    /* Sidebar Form Card */
    .side-form-card {{
      background: #ffffff;
      border: 2px solid var(--primary-light);
      border-radius: var(--radius-md);
      padding: 22px 20px;
      box-shadow: var(--shadow-md);
      position: relative;
    }}
    .side-form-badge {{
      background: var(--primary-light);
      color: var(--primary);
      font-size: 10.5px;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-block;
      margin-bottom: 8px;
    }}
    .side-form-card h3 {{
      font-size: 17px;
      color: var(--dark);
      margin-bottom: 4px;
      line-height: 1.35;
    }}
    .side-form-card p.form-sub {{
      font-size: 12px;
      color: var(--slate-600);
      margin-bottom: 14px;
    }}
    .side-form-group {{
      margin-bottom: 10px;
    }}
    .side-form-group label {{
      display: block;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--slate-600);
      margin-bottom: 3px;
    }}
    .side-form-group input {{
      width: 100%;
      padding: 9px 11px;
      font-size: 13.5px;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: var(--slate-100);
      font-family: inherit;
    }}
    .side-form-group input:focus {{
      outline: none;
      background: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(18, 109, 178, 0.12);
    }}
    .side-btn-submit {{
      width: 100%;
      background: var(--primary);
      color: #ffffff;
      font-size: 14px;
      font-weight: 700;
      padding: 11px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.2s;
    }}
    .side-btn-submit:hover {{
      background: var(--primary-dark);
    }}

    /* Dedicated Sticky WhatsApp Button */
    .side-wa-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 14px;
      box-shadow: var(--shadow-sm);
      text-align: center;
    }}
    .side-wa-action {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: #25d366;
      color: #ffffff !important;
      font-size: 14px;
      font-weight: 700;
      padding: 11px 16px;
      border-radius: 8px;
      text-decoration: none !important;
      box-shadow: 0 4px 12px rgba(37, 211, 102, 0.25);
      transition: background 0.2s;
    }}
    .side-wa-action:hover {{
      background: #1eb956;
    }}
    .side-wa-note {{
      font-size: 11px;
      color: var(--slate-400);
      margin-top: 6px;
    }}

    /* =========================================================
       RIGHT-SIDE MAIN CONTENT (100% TEXT PRESERVED)
       ========================================================= */
    .content-column {{
      min-width: 0; /* prevent flex/grid blowout */
    }}

    .hero-banner-img {{
      border-radius: var(--radius-md);
      overflow: hidden;
      margin-bottom: 24px;
      border: 1px solid var(--border);
      box-shadow: var(--shadow-md);
    }}

    h1 {{
      font-size: 32px;
      font-weight: 800;
      line-height: 1.25;
      color: var(--dark);
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }}
    @media (min-width: 768px) {{
      h1 {{ font-size: 38px; }}
    }}

    h2 {{
      font-size: 23px;
      font-weight: 700;
      color: var(--dark);
      margin: 0 0 14px;
      letter-spacing: -0.015em;
    }}

    h3 {{
      font-size: 18px;
      font-weight: 700;
      color: var(--dark);
      margin: 0 0 10px;
    }}

    p {{
      color: var(--slate-600);
      font-size: 16px;
      line-height: 1.75;
      margin-bottom: 16px;
    }}

    strong {{
      color: var(--dark);
    }}

    ul {{
      margin: 0 0 18px 22px;
      color: var(--slate-600);
    }}
    li {{
      margin-bottom: 8px;
    }}

    /* Section Cards */
    .content-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 30px 26px;
      margin-bottom: 30px;
      box-shadow: var(--shadow-sm);
    }}
    .content-card-accent {{
      border-left: 5px solid var(--primary);
      background: linear-gradient(180deg, #f0f9ff 0%, #ffffff 100%);
    }}
    .content-card-warning {{
      border-left: 5px solid var(--amber);
      background: #fffbeb;
    }}

    .trust-badge-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 18px 0 25px;
    }}
    .trust-pill {{
      background: var(--slate-100);
      border: 1px solid var(--border);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      color: var(--slate-800);
    }}

    /* 10 Deliverables Grid */
    .deliv-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }}
    .deliv-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 22px;
      box-shadow: var(--shadow-sm);
      border-top: 4px solid var(--primary);
      transition: transform 0.2s;
    }}
    .deliv-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }}
    .task-badge {{
      font-size: 11px;
      font-weight: 800;
      color: var(--primary);
      background: var(--primary-light);
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-block;
      margin-bottom: 10px;
    }}
    .deliv-card h2 {{
      font-size: 18px;
      margin-bottom: 10px;
    }}

    /* 4 Pillars Impact Grid */
    .impact-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 16px;
      margin-top: 18px;
    }}
    .impact-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 18px;
    }}
    .impact-box h2 {{
      font-size: 17px;
      margin-bottom: 8px;
    }}

    /* Plans Grid */
    .plans-box {{
      background: var(--slate-100);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 32px 24px;
      margin-bottom: 30px;
    }}
    .plans-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 20px;
      margin: 25px 0;
    }}
    .plan-tier {{
      background: #ffffff;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-sm);
    }}
    .plan-top {{
      background: #1e529b;
      color: #ffffff;
      padding: 16px;
      text-align: center;
    }}
    .plan-top h3 {{
      color: #ffffff !important;
      margin: 0;
      font-size: 20px;
    }}
    .plan-body {{
      padding: 20px;
      flex: 1;
      display: flex;
      flex-direction: column;
    }}
    .plan-cta {{
      margin-top: auto;
      padding-top: 15px;
    }}
    .plan-btn-wa {{
      display: block;
      text-align: center;
      background: var(--primary);
      color: #ffffff !important;
      font-size: 13.5px;
      font-weight: 700;
      padding: 10px;
      border-radius: 6px;
      text-decoration: none !important;
    }}
    .plan-btn-wa:hover {{
      background: var(--primary-dark);
    }}

    /* FAQ Accordion */
    .faq-item {{
      border: 1px solid var(--border);
      border-radius: 8px;
      margin-bottom: 10px;
      background: #ffffff;
      overflow: hidden;
    }}
    .faq-summary {{
      padding: 15px 18px;
      font-size: 15.5px;
      font-weight: 700;
      color: var(--dark);
      cursor: pointer;
      list-style: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #ffffff;
    }}
    .faq-summary::-webkit-details-marker {{ display: none; }}
    .faq-summary::after {{
      content: '+';
      font-size: 18px;
      color: var(--primary);
    }}
    .faq-item[open] .faq-summary::after {{
      content: '−';
    }}
    .faq-body {{
      padding: 16px 18px;
      border-top: 1px solid var(--border);
      background: #f8fafc;
    }}

    /* Bottom Free Audit Card */
    .audit-box {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: #ffffff;
      border-radius: var(--radius-md);
      padding: 35px 28px;
      margin-bottom: 30px;
      box-shadow: var(--shadow-lg);
    }}
    .audit-box h2 {{
      color: #38bdf8 !important;
      font-size: 26px;
      margin-bottom: 12px;
    }}
    .audit-box p {{
      color: #cbd5e1;
    }}
    .audit-box strong {{
      color: #ffffff;
    }}
    .audit-box ul li {{
      color: #f1f5f9;
      padding: 3px 0;
    }}
    .audit-form-inner {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 8px;
      padding: 22px;
      margin-top: 22px;
    }}
    .audit-form-inner input {{
      background: #0f172a;
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      padding: 11px;
      border-radius: 6px;
      width: 100%;
      font-family: inherit;
    }}

    /* Related Articles Grid */
    .articles-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 18px;
      margin-top: 18px;
    }}
    .article-col {{
      background: var(--slate-100);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
    }}
    .article-col h2 {{
      font-size: 15px;
      color: var(--primary);
      border-bottom: 1px solid var(--border);
      padding-bottom: 6px;
      margin-bottom: 8px;
    }}

    /* Global Footer */
    .global-footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 35px 0;
      margin-top: 60px;
      border-top: 1px solid #1e293b;
      font-size: 13.5px;
    }}
    .footer-flex {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 24px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
    }}

    /* Mobile Bottom Action Bar */
    .mobile-bottom-bar {{
      display: none;
    }}
    @media (max-width: 767px) {{
      .mobile-bottom-bar {{
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
      .mobile-bottom-bar a {{
        flex: 1;
        text-align: center;
        padding: 10px;
        font-size: 13.5px;
        font-weight: 700;
        border-radius: 6px;
        text-decoration: none !important;
      }}
      .m-call {{
        background: #f1f5f9;
        color: var(--dark) !important;
        border: 1px solid #cbd5e1;
      }}
      .m-wa {{
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

  <!-- Top Header -->
  <header class="top-header">
    <div class="top-header-flex">
      <div class="top-logo">
        <a href="https://www.gadigitalsolutions.com/">
          <img src="https://www.gadigitalsolutions.com/images/GADS%20LOGO-01.svg" alt="GA Digital Solutions Logo" height="44">
        </a>
      </div>
      <div class="top-contact">
        <a href="tel:9849574618" class="top-phone">📞 +91 98495 74618</a>
        <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="top-wa-btn" target="_blank" rel="noopener noreferrer">
          💬 WhatsApp
        </a>
      </div>
    </div>
  </header>

  <!-- 2-Column Main Layout -->
  <div class="layout-wrapper">
    <div class="page-grid">

      <!-- =========================================================
           LEFT-SIDE COLUMN: STICKY OVERVIEW BAR + FORM + WHATSAPP
           ========================================================= -->
      <aside class="sticky-sidebar">

        <!-- 1. Brand & 24/7 Status Box -->
        <div class="side-brand-box">
          <div style="display: flex; align-items: center; gap: 8px;">
            <img src="https://www.gadigitalsolutions.com/images/logo.png" alt="GA" height="26" style="border-radius: 4px;">
            <span style="font-weight: 700; font-size: 13.5px; color: var(--dark);">GA Digital Solutions</span>
          </div>
          <span class="side-pulse">
            <span class="pulse-dot"></span> 24/7 ACTIVE
          </span>
        </div>

        <!-- 2. Sticky Page Overview Navigation Bar (Table of Contents) -->
        <nav class="side-overview-card" aria-label="Page Sections Navigation">
          <div class="side-overview-title">
            <span>📑</span> Page Overview
          </div>
          <ul class="side-nav-list" id="sidebarNav">
            <li><a href="#overview" class="side-nav-link active"><span class="nav-num">01</span> Overview</a></li>
            <li><a href="#deliverables" class="side-nav-link"><span class="nav-num">02</span> 10 Tasks Included</a></li>
            <li><a href="#why-matters" class="side-nav-link"><span class="nav-num">03</span> Why It Matters</a></li>
            <li><a href="#cost-neglect" class="side-nav-link"><span class="nav-num">04</span> Cost of Neglect</a></li>
            <li><a href="#schedule" class="side-nav-link"><span class="nav-num">05</span> Schedule Cadence</a></li>
            <li><a href="#diy-vs-pro" class="side-nav-link"><span class="nav-num">06</span> DIY vs Professional</a></li>
            <li><a href="#plans" class="side-nav-link"><span class="nav-num">07</span> Maintenance Plans</a></li>
            <li><a href="#faqs" class="side-nav-link"><span class="nav-num">08</span> FAQs</a></li>
            <li><a href="#free-audit" class="side-nav-link"><span class="nav-num">09</span> Claim Free Audit</a></li>
            <li><a href="#related-articles" class="side-nav-link"><span class="nav-num">10</span> Related Articles</a></li>
          </ul>
        </nav>

        <!-- 3. Sticky Lead Capture Form -->
        <div class="side-form-card">
          <span class="side-form-badge">Fast Diagnostic</span>
          <h3>Get Your Free 20-Point Site Audit</h3>
          <p class="form-sub">Check security, outdated plugins &amp; page speed in 24 hours.</p>

          <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20a%20free%20website%20health%20audit%20for:%20' + encodeURIComponent(this.website.value);">
            <div class="side-form-group">
              <label for="side-site">Website URL *</label>
              <input type="url" id="side-site" name="website" placeholder="https://yourcompany.com" required>
            </div>
            <div class="side-form-group">
              <label for="side-name">Your Name *</label>
              <input type="text" id="side-name" name="name" placeholder="John Doe" required>
            </div>
            <div class="side-form-group">
              <label for="side-phone">WhatsApp / Phone *</label>
              <input type="tel" id="side-phone" name="phone" placeholder="+91 98765 43210" required>
            </div>
            <button type="submit" class="side-btn-submit">
              Get Free Health Audit &rarr;
            </button>
          </form>
        </div>

        <!-- 4. Dedicated Sticky WhatsApp Button Box -->
        <div class="side-wa-box">
          <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="side-wa-action" target="_blank" rel="noopener noreferrer">
            💬 Message on WhatsApp
          </a>
          <p class="side-wa-note">⚡ Immediate on-call engineer response</p>
        </div>

      </aside>

      <!-- =========================================================
           RIGHT-SIDE COLUMN: MAIN CONTENT (100% TEXT PRESERVED)
           ========================================================= -->
      <main class="content-column">

        <!-- HERO SECTION -->
        <div class="hero-banner-img">
          <img src="https://www.gadigitalsolutions.com/images/Website_Maintenance.jpg" width="820" height="460" alt="Website Maintenance Services in India - GA Digital Solutions" fetchpriority="high">
        </div>

        {parts[0]}

        <div class="trust-badge-row">
          <div class="trust-pill">🛡️ 24/7 Monitoring</div>
          <div class="trust-pill">⚡ Staging Tested</div>
          <div class="trust-pill">💾 Daily Cloud Backups</div>
          <div class="trust-pill">⏱️ 30-Min SLA</div>
        </div>

        {parts[1]}
        {parts[2]}

        <!-- OVERVIEW -->
        <div class="content-card content-card-accent" id="overview">
          {parts[3]}
          {parts[4]}
        </div>

        <!-- 10 DELIVERABLES -->
        <div id="deliverables" style="margin-bottom: 35px;">
          <div class="content-card" style="margin-bottom: 20px;">
            {parts[5]}
            {parts[6]}
          </div>
          <div class="deliv-grid">
            {deliv_cards_html}
          </div>
        </div>

        <!-- WHY IT MATTERS -->
        <div class="content-card" id="why-matters">
          {parts[27]}
          {parts[28]}
          <div class="impact-grid">
            <div class="impact-box" style="border-top: 3px solid #10b981;">{parts[29]}{parts[30]}</div>
            <div class="impact-box" style="border-top: 3px solid #ef4444;">{parts[31]}{parts[32]}</div>
            <div class="impact-box" style="border-top: 3px solid #f59e0b;">{parts[33]}{parts[34]}</div>
            <div class="impact-box" style="border-top: 3px solid #126db2;">{parts[35]}{parts[36]}</div>
          </div>
        </div>

        <!-- COST OF NEGLECT -->
        <div class="content-card content-card-warning" id="cost-neglect">
          {parts[37]}
          {parts[38]}
        </div>

        <!-- SCHEDULE -->
        <div class="content-card" id="schedule">
          {parts[39]}
          {parts[40]}
        </div>

        <!-- DIY VS PRO -->
        <div class="content-card" id="diy-vs-pro">
          {parts[41]}
          {parts[42]}
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 18px 0;">
            <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 18px;">{parts[43]}{parts[44]}</div>
            <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 18px;">{parts[45]}{parts[46]}</div>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 18px 0;">
            <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 18px;">{parts[47]}{parts[48]}</div>
            <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 18px;">{parts[49]}{parts[50]}</div>
          </div>
          <div style="margin-top: 25px; border-top: 1px solid var(--border); padding-top: 20px;">
            {parts[51]}
            {parts[52]}
          </div>
        </div>

        <!-- PLANS & PRICING -->
        <div class="plans-box" id="plans">
          {parts[53]}
          {plans_intro}
          <div class="plans-grid">
            <div class="plan-tier">
              <div class="plan-top"><h3>Essential</h3></div>
              <div class="plan-body">
                <p><strong>For brochure websites and small business sites</strong></p>
                <p>Ideal for: standard websites with stable content and moderate visitor traffic</p>
                <div class="plan-cta">
                  <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Essential%20Website%20Maintenance%20Plan" class="plan-btn-wa" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
                </div>
              </div>
            </div>
            <div class="plan-tier" style="border: 2px solid var(--primary);">
              <div class="plan-top" style="background: var(--primary);"><h3>Growth</h3></div>
              <div class="plan-body">
                <p><strong>For websites actively generating leads</strong></p>
                <p>Ideal for: businesses relying on their website for consistent lead generation</p>
                <div class="plan-cta">
                  <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Growth%20Website%20Maintenance%20Plan" class="plan-btn-wa" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
                </div>
              </div>
            </div>
            <div class="plan-tier">
              <div class="plan-top"><h3>Business</h3></div>
              <div class="plan-body">
                <p><strong>For e-commerce, booking platforms, and high-traffic sites</strong></p>
                <p>Ideal for: e-commerce stores and businesses with significant revenue dependence on their website</p>
                <div class="plan-cta">
                  <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Business%20Website%20Maintenance%20Plan" class="plan-btn-wa" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
                </div>
              </div>
            </div>
          </div>
          {plans_closing}
        </div>

        <!-- INDUSTRIES -->
        <div class="content-card" id="industries">
          {parts[55]}
          {parts[56]}
        </div>

        <!-- FAQS -->
        <div id="faqs" style="margin-bottom: 35px;">
          <div class="content-card" style="margin-bottom: 15px;">
            {parts[57]}
            {faq_intro}
          </div>
          {faq_accordions_html}
        </div>

        <!-- AUDIT SECTION -->
        <div class="audit-box" id="free-audit">
          {parts[59]}
          {parts[60]}

          <div class="audit-form-inner">
            <h3 style="color: #38bdf8; margin-top: 0; font-size: 19px;">⚡ Enter Your Website for Your Free 20-Point Audit</h3>
            <p style="color: #cbd5e1; font-size: 13.5px; margin-bottom: 15px;">Direct engineer review with zero obligation.</p>
            <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Free%20Audit%20Request:%20' + encodeURIComponent(this.audit_site.value);">
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 12px; margin-bottom: 12px;">
                <input type="url" name="audit_site" placeholder="https://yourwebsite.com" required>
                <input type="text" name="audit_name" placeholder="Your Name" required>
                <input type="tel" name="audit_phone" placeholder="WhatsApp / Phone" required>
              </div>
              <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px;">
                <button type="submit" style="flex: 2; min-width: 220px; background: #0284c7; color: #fff; font-weight: 700; padding: 12px; border: none; border-radius: 6px; cursor: pointer;">
                  Submit Free Audit Request &rarr;
                </button>
                <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20to%20request%20the%20Free%20Website%20Health%20Audit%20directly" style="flex: 1; min-width: 180px; background: #25d366; color: #fff !important; font-weight: 700; padding: 12px; border-radius: 6px; text-align: center; text-decoration: none;" target="_blank" rel="noopener noreferrer">
                  💬 WhatsApp Fast Track
                </a>
              </div>
            </form>
          </div>
        </div>

        <!-- RELATED ARTICLES -->
        <div class="content-card" id="related-articles">
          {parts[61]}
          {parts[62]}
          <div class="articles-grid">
            <div class="article-col">{parts[63]}{parts[64]}</div>
            <div class="article-col">{parts[65]}{parts[66]}</div>
            <div class="article-col">{parts[67]}{parts[68]}</div>
            <div class="article-col">{parts[69]}{parts[70]}</div>
          </div>
        </div>

      </main>

    </div>
  </div>

  <!-- Global Footer -->
  <footer class="global-footer">
    <div class="footer-flex">
      <div style="display: flex; align-items: center; gap: 12px;">
        <img src="https://www.gadigitalsolutions.com/images/logo.png" alt="GA" height="30" style="border-radius: 4px;">
        <div>
          <p style="color: #ffffff; font-weight: 700; margin: 0; font-size: 14px;">GA Digital Solutions</p>
          <p style="color: #64748b; font-size: 12px; margin: 0;">A Business Unit of Gunnam Associates | Hyderabad, India</p>
        </div>
      </div>
      <div>
        <p style="color: #64748b; font-size: 12px; margin: 0;">&copy; 2026 GA Digital Solutions. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <!-- Mobile Sticky Bar -->
  <div class="mobile-bottom-bar">
    <a href="tel:9849574618" class="m-call">📞 Call Engineer</a>
    <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="m-wa" target="_blank" rel="noopener noreferrer">💬 WhatsApp</a>
  </div>

  <!-- Scroll-Spy JavaScript for Left-Side Overview Navigation -->
  <script>
    const sections = document.querySelectorAll('.content-column > div[id], .content-column > section[id]');
    const navLinks = document.querySelectorAll('.side-nav-link');

    window.addEventListener('scroll', () => {{
      let current = '';
      sections.forEach(section => {{
        const sectionTop = section.offsetTop - 120;
        if (window.pageYOffset >= sectionTop) {{
          current = section.getAttribute('id');
        }}
      }});

      navLinks.forEach(link => {{
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {{
          link.classList.add('active');
        }}
      }});
    }});
  </script>

</body>
</html>
"""

with open('website-maintenance-sidebar-layout.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully created website-maintenance-sidebar-layout.html! Size:", len(html_content))
