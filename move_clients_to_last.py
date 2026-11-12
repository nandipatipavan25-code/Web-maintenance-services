import re

for filename in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Extract the clients section
    clients_pattern = r'<!-- OUR CLIENTS -->\s*<section class="clients-section-card" id="clients">.*?</section>'
    match = re.search(clients_pattern, content, re.DOTALL)
    if not match:
        print(f"Error: Could not find clients section in {filename}!")
        continue

    clients_block = match.group(0)

    # 2. Remove clients section from the start (where it was before #overview)
    content = content[:match.start()] + content[match.end():]

    # 3. Clean up the sidebar navigation link: remove from near top
    content = re.sub(r'\s*<li><a href="#clients"[^>]*>.*?</a></li>', '', content)

    # 4. Insert clients section right before the Speed Odometer section
    odo_marker = '<!-- =========================================================\n             LAST ELEMENT ON THE WEBSITE:\n             INTERACTIVE WEBSITE SPEED ODOMETER'
    if odo_marker in content:
        content = content.replace(odo_marker, clients_block + '\n\n        ' + odo_marker, 1)
        print(f"Inserted clients block before speed-odometer in {filename}!")
    else:
        # Fallback to <section class="speed-odometer-box" id="speed-odometer"
        odo_fallback = '<section class="speed-odometer-box" id="speed-odometer"'
        if odo_fallback in content:
            content = content.replace(odo_fallback, clients_block + '\n\n        ' + odo_fallback, 1)
            print(f"Inserted clients block before speed-odometer (fallback) in {filename}!")
        else:
            print(f"Error: Could not find speed-odometer in {filename}!")

    # 5. Add clients link in sidebar nav before speed-odometer link
    nav_clients = '            <li><a href="#clients" class="side-nav-link"><span class="nav-num">11</span> Our Clients</a></li>\n'
    nav_odo_marker = '<li><a href="#speed-odometer" class="side-nav-link">'
    if nav_odo_marker in content:
        # Update speed-odometer nav number to 12
        content = content.replace(nav_odo_marker, nav_clients + '            ' + nav_odo_marker.replace('nav-num">⚡', 'nav-num">12'))
        print(f"Updated sidebar navigation in {filename}!")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully updated {filename}!")
