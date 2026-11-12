old_css = """    /* 4 Pillars Impact Grid */
    .impact-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-top: 18px;
      align-items: stretch;
    }"""

new_css = """    /* 4 Pillars Impact Grid: 2 Columns x 2 Rows */
    .impact-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      margin-top: 22px;
      align-items: stretch;
    }
    @media (max-width: 768px) {
      .impact-grid {
        grid-template-columns: 1fr;
        gap: 16px;
      }
    }"""

for filename in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_css in content:
        content = content.replace(old_css, new_css, 1)
        print(f"Updated .impact-grid CSS in {filename}!")
    else:
        print(f"Warning: Could not find exact old_css in {filename}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Saved {filename}!")
