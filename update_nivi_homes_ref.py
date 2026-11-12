for filename in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html', 'test_logos.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace nivi-homes.webp with nivi-homes.png for maximum crispness
    content = content.replace('images/clients/nivi-homes.webp', 'images/clients/nivi-homes.png')
    content = content.replace('nivi-homes.webp', 'nivi-homes.png')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename} successfully!")
