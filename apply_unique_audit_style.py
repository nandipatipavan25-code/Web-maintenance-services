import re

new_css = """
    /* =========================================================
       BESPOKE EXECUTIVE AUDIT DOSSIER STYLES (UNIQUE / NON-GENERIC)
       ========================================================= */
    .audit-box {
      background: radial-gradient(circle at 90% 10%, rgba(14, 165, 233, 0.14) 0%, transparent 45%),
                  radial-gradient(circle at 10% 90%, rgba(16, 185, 129, 0.08) 0%, transparent 40%),
                  linear-gradient(150deg, #090e17 0%, #0f172a 55%, #131d38 100%);
      color: #ffffff;
      border: 1.5px solid rgba(56, 189, 248, 0.22);
      border-radius: 18px;
      padding: 38px 32px;
      margin-bottom: 35px;
      box-shadow: 0 20px 45px -10px rgba(15, 23, 42, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.05);
      position: relative;
      overflow: hidden;
    }
    .audit-box::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, #0284c7, #38bdf8, #10b981);
    }
    .audit-badge-strip {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      margin-bottom: 16px;
    }
    .audit-pill-tag {
      background: rgba(14, 165, 233, 0.18);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38bdf8;
      font-size: 11.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 5px 14px;
      border-radius: 999px;
    }
    .audit-pill-meta {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #94a3b8;
      font-size: 11.5px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 999px;
    }
    .audit-main-heading {
      color: #ffffff !important;
      font-size: 27px;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.25;
      margin: 0 0 14px 0;
    }
    .audit-lead-text {
      color: #cbd5e1;
      font-size: 15.5px;
      line-height: 1.65;
      max-width: 820px;
      margin: 0 0 18px 0;
    }
    .audit-section-subhead {
      color: #38bdf8;
      font-size: 14.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin: 22px 0 14px 0;
    }
    .audit-inspection-matrix {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      margin-bottom: 24px;
    }
    @media (max-width: 680px) {
      .audit-inspection-matrix {
        grid-template-columns: 1fr;
        gap: 10px;
      }
    }
    .audit-matrix-card {
      background: rgba(255, 255, 255, 0.035);
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: 10px;
      padding: 14px 16px;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      transition: all 0.2s ease;
    }
    .audit-matrix-card:hover {
      background: rgba(255, 255, 255, 0.065);
      border-color: rgba(56, 189, 248, 0.35);
      transform: translateY(-2px);
    }
    .matrix-icon-box {
      width: 36px;
      height: 36px;
      border-radius: 8px;
      background: rgba(14, 165, 233, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 17px;
      flex-shrink: 0;
    }
    .matrix-content {
      flex: 1;
    }
    .matrix-title {
      color: #f1f5f9;
      font-size: 13.5px;
      font-weight: 700;
      line-height: 1.35;
      margin-bottom: 3px;
    }
    .matrix-badge {
      color: #94a3b8;
      font-size: 11px;
      font-weight: 500;
    }
    .audit-guarantee-card {
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: 12px;
      padding: 18px 20px;
      margin-bottom: 24px;
    }
    .audit-guarantee-header {
      display: flex;
      align-items: center;
      gap: 8px;
      color: #34d399;
      font-size: 14px;
      margin-bottom: 8px;
    }
    .audit-guarantee-card p {
      color: #cbd5e1;
      font-size: 14px;
      line-height: 1.55;
      margin-bottom: 10px;
    }
    .audit-form-inner {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 12px;
      padding: 24px;
    }
    .audit-form-inner input {
      background: #090e17;
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      padding: 12px 14px;
      border-radius: 8px;
      width: 100%;
      font-size: 14px;
      font-family: inherit;
    }
    .audit-form-inner input:focus {
      outline: none;
      border-color: #38bdf8;
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
    }
"""

new_audit_html = """        <!-- AUDIT SECTION: BESPOKE EXECUTIVE INSPECTION DOSSIER -->
        <section class="audit-box" id="free-audit">
          <!-- Top Badge Strip -->
          <div class="audit-badge-strip">
            <span class="audit-pill-tag">📋 20-Point Technical Inspection</span>
            <span class="audit-pill-meta">⏱️ 48-Hour Turnaround</span>
            <span class="audit-pill-meta">🤝 100% Free &bull; No Obligation</span>
          </div>

          <!-- Section Title & Intro -->
          <h2 class="audit-main-heading">Get Your Free 20-Point Website Health Audit</h2>
          
          <p class="audit-lead-text">Most business websites in India have at least three significant, fixable problems that their owners are unaware of. Our free website health audit identifies them &mdash; in plain language, with no obligation to proceed.</p>

          <p class="audit-section-subhead">The audit covers:</p>

          <!-- Bespoke 2-Column Inspection Matrix (Replaces plain bulleted checklist) -->
          <div class="audit-inspection-matrix">
            <div class="audit-matrix-card">
              <div class="matrix-icon-box">🛡️</div>
              <div class="matrix-content">
                <div class="matrix-title">Security vulnerabilities and outdated software</div>
                <div class="matrix-badge">Core Platform &bull; Plugins &bull; Malware</div>
              </div>
            </div>

            <div class="audit-matrix-card">
              <div class="matrix-icon-box">⚡</div>
              <div class="matrix-content">
                <div class="matrix-title">Page speed and Core Web Vitals scores</div>
                <div class="matrix-badge">LCP &bull; FID &bull; CLS Telemetry</div>
              </div>
            </div>

            <div class="audit-matrix-card">
              <div class="matrix-icon-box">📱</div>
              <div class="matrix-content">
                <div class="matrix-title">Mobile usability assessment</div>
                <div class="matrix-badge">Responsive Viewport &bull; Tap Targets</div>
              </div>
            </div>

            <div class="audit-matrix-card">
              <div class="matrix-icon-box">🔒</div>
              <div class="matrix-content">
                <div class="matrix-title">SSL certificate status</div>
                <div class="matrix-badge">HTTPS Handshake &bull; Mixed Content</div>
              </div>
            </div>

            <div class="audit-matrix-card">
              <div class="matrix-icon-box">🔗</div>
              <div class="matrix-content">
                <div class="matrix-title">Broken links and error pages</div>
                <div class="matrix-badge">404 Errors &bull; Redirect Chains</div>
              </div>
            </div>

            <div class="audit-matrix-card">
              <div class="matrix-icon-box">💾</div>
              <div class="matrix-content">
                <div class="matrix-title">Backup status assessment</div>
                <div class="matrix-badge">Cloud Frequency &bull; Recovery Tests</div>
              </div>
            </div>

            <div class="audit-matrix-card">
              <div class="matrix-icon-box">📈</div>
              <div class="matrix-content">
                <div class="matrix-title">SEO technical health &mdash; crawl errors, indexing issues</div>
                <div class="matrix-badge">Robots.txt &bull; Sitemap &bull; Meta Tags</div>
              </div>
            </div>

            <div class="audit-matrix-card">
              <div class="matrix-icon-box">🎯</div>
              <div class="matrix-content">
                <div class="matrix-title">Contact form and conversion point functionality</div>
                <div class="matrix-badge">Lead Routing &bull; WhatsApp Triggers</div>
              </div>
            </div>
          </div>

          <!-- Trust & Transparency Guarantee Callout -->
          <div class="audit-guarantee-card">
            <div class="audit-guarantee-header">
              <span class="guarantee-icon">🤝</span>
              <strong>No-Pitch Transparency Guarantee</strong>
            </div>
            <p>Fill in our contact form with your website URL and contact details. Our team will complete the audit within 2 business days and walk you through the findings on a call or via WhatsApp &mdash; whichever you prefer.</p>
            <p style="margin-bottom: 0;">There is no pitch at the end. If your website is in good health, we will tell you so. If there are issues worth addressing, we will explain them clearly and you can decide what to do next.</p>
          </div>

          <!-- Intake Form Card -->
          <div class="audit-form-inner">
            <h3 style="color: #38bdf8; margin-top: 0; font-size: 19px; display: flex; align-items: center; gap: 8px;">
              <span>⚡</span> Request Your Free 20-Point Website Health Audit
            </h3>
            <p style="color: #cbd5e1; font-size: 13.5px; margin-bottom: 16px;">Direct expert review with zero cost and zero obligation.</p>
            <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Free%20Audit%20Request:%20' + encodeURIComponent(this.audit_site.value);">
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 12px; margin-bottom: 14px;">
                <input type="url" name="audit_site" placeholder="https://yourwebsite.com" required>
                <input type="text" name="audit_name" placeholder="Your Name" required>
                <input type="tel" name="audit_phone" placeholder="WhatsApp / Phone" required>
              </div>
              <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 10px;">
                <button type="submit" class="btn btn-primary" style="flex: 2; min-width: 240px; background-color: #126db2; border: 1px solid #38bdf8; color: #ffffff !important; display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 13px 22px; border-radius: 8px; font-weight: 700; text-decoration: none; cursor: pointer; box-shadow: 0 4px 14px rgba(18, 109, 178, 0.35);">
                  &rarr; Get My Free Website Audit &mdash; No Cost, No Obligation
                </button>
                <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20to%20request%20the%20Free%20Website%20Health%20Audit%20directly" style="flex: 1; min-width: 190px; background: #25d366; color: #fff !important; font-weight: 700; padding: 13px 18px; border-radius: 8px; text-align: center; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 6px; box-shadow: 0 4px 14px rgba(37, 211, 102, 0.3);" target="_blank" rel="noopener noreferrer">
                  💬 WhatsApp Fast Track
                </a>
              </div>
            </form>
            <p style="font-size: 12.5px; color: #94a3b8; margin: 12px 0 0 0; text-align: center;">Or contact us directly via WhatsApp for a faster response.</p>
          </div>
        </section>"""

for filename in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the old audit HTML section
    old_audit_pattern = r'<!-- AUDIT SECTION -->\s*<div class="audit-box" id="free-audit">.*?</div>\s*</div>'
    match = re.search(old_audit_pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_audit_html + content[match.end():]
        print(f"Replaced audit HTML in {filename}!")
    else:
        print(f"Warning: Could not find old audit HTML in {filename}!")

    # 2. Append new CSS
    if 'BESPOKE EXECUTIVE AUDIT DOSSIER STYLES' not in content:
        content = content.replace('</style>', new_css + '\n</style>', 1)
        print(f"Added bespoke audit CSS to {filename}!")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Saved {filename}!")
