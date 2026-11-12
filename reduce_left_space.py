import re

for fname in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update .top-header-flex
    old_thf = """.top-header-flex {
      max-width: 1380px;
      margin: 0 auto;
      padding: 0 24px;"""
    new_thf = """.top-header-flex {
      max-width: 1650px;
      width: 96%;
      margin: 0 auto;
      padding: 0 16px;"""
    if old_thf in content:
        content = content.replace(old_thf, new_thf, 1)

    # 2. Update .layout-wrapper
    old_lw = """.layout-wrapper {
      max-width: 1380px;
      margin: 28px auto 60px;
      padding: 0 24px;
    }"""
    new_lw = """.layout-wrapper {
      max-width: 1650px;
      width: 96%;
      margin: 20px auto 60px;
      padding: 0 16px;
    }"""
    if old_lw in content:
        content = content.replace(old_lw, new_lw, 1)

    # 3. Update .footer-flex
    old_ff = """.footer-flex {
      max-width: 1380px;
      margin: 0 auto;
      padding: 0 24px;"""
    new_ff = """.footer-flex {
      max-width: 1650px;
      width: 96%;
      margin: 0 auto;
      padding: 0 16px;"""
    if old_ff in content:
        content = content.replace(old_ff, new_ff, 1)

    # 4. Update .page-grid columns and gap on desktop
    old_pg = """@media (min-width: 1024px) {
      .page-grid {
        grid-template-columns: 350px minmax(0, 1fr);
      }"""
    new_pg = """@media (min-width: 1024px) {
      .page-grid {
        grid-template-columns: 320px minmax(0, 1fr);
        gap: 28px;
      }"""
    if old_pg in content:
        content = content.replace(old_pg, new_pg, 1)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {fname} successfully!")
