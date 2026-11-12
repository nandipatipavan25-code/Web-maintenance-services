new_audit_css = """    /* ============================================================
       AUDIT SECTION: REALISTIC CORPORATE LIGHT THEME
       ============================================================ */
    .audit-box {
      background: #ffffff;
      color: #0f172a;
      border: 1.5px solid #e2e8f0;
      border-top: 4px solid #126db2;
      border-radius: 16px;
      padding: 38px 34px;
      margin-bottom: 35px;
      box-shadow: 0 10px 30px -5px rgba(15, 23, 42, 0.08), 0 4px 10px -2px rgba(15, 23, 42, 0.04);
      position: relative;
    }
    .audit-badge-strip {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      margin-bottom: 16px;
    }
    .audit-pill-tag {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #0284c7;
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 5px 14px;
      border-radius: 999px;
    }
    .audit-pill-meta {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      color: #64748b;
      font-size: 11.5px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 999px;
    }
    .audit-main-heading {
      color: #0f172a !important;
      font-size: 26px;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.25;
      margin: 0 0 12px 0;
    }
    .audit-lead-text {
      color: #475569;
      font-size: 15px;
      line-height: 1.65;
      max-width: 820px;
      margin: 0 0 18px 0;
    }
    .audit-section-subhead {
      color: #0f172a;
      font-size: 13.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin: 22px 0 14px 0;
    }
    .audit-inspection-matrix {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
      margin-bottom: 24px;
    }
    @media (max-width: 640px) {
      .audit-inspection-matrix {
        grid-template-columns: 1fr;
        gap: 10px;
      }
    }
    .audit-matrix-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 14px 16px;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      transition: all 0.2s ease;
    }
    .audit-matrix-card:hover {
      background: #ffffff;
      border-color: #cbd5e1;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.06);
      transform: translateY(-1px);
    }
    .matrix-icon-box {
      width: 38px;
      height: 38px;
      border-radius: 8px;
      background: #eff6ff;
      border: 1px solid #dbeafe;
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
      color: #0f172a;
      font-size: 13.5px;
      font-weight: 700;
      line-height: 1.35;
      margin-bottom: 3px;
    }
    .matrix-badge {
      color: #64748b;
      font-size: 11.5px;
      font-weight: 500;
    }
    .audit-guarantee-card {
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: 12px;
      padding: 18px 20px;
      margin-bottom: 24px;
    }
    .audit-guarantee-header {
      display: flex;
      align-items: center;
      gap: 8px;
      color: #15803d;
      font-size: 14px;
      font-weight: 700;
      margin-bottom: 8px;
    }
    .audit-guarantee-card p {
      color: #1e3a2b;
      font-size: 13.5px;
      line-height: 1.55;
      margin: 0 0 8px 0;
    }
    .audit-form-inner {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 24px;
    }
    .audit-form-inner h3 {
      color: #0f172a !important;
    }
    .audit-form-inner input {
      background: #ffffff !important;
      border: 1px solid #cbd5e1 !important;
      color: #0f172a !important;
      padding: 12px 14px !important;
      border-radius: 8px !important;
      font-size: 13.5px !important;
      width: 100%;
      box-sizing: border-box;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .audit-form-inner input:focus {
      outline: none;
      border-color: #126db2 !important;
      box-shadow: 0 0 0 3px rgba(18, 109, 178, 0.15) !important;
    }
    .audit-form-inner input::placeholder {
      color: #94a3b8 !important;
    }"""

import re

# Old CSS block to replace
old_css_pattern = r'/\* =+[\s\n]*AUDIT SECTION:[\s\S]*?(?=\.audit-form-inner\s*\{[^}]+\}\s*\n)'

for fname in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the audit css region
    start_str = '.audit-box {'
    # Let's inspect where .audit-box is in content
    idx = content.find(start_str)
    print(f"{fname}: first audit-box at {idx}")
