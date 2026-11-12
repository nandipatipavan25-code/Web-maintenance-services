with open('website-maintenance.html', 'r', encoding='utf-8') as f:
    html = f.read()

overview_pos = html.find('id="overview"')
related_pos = html.find('id="related-articles"')
clients_pos = html.find('id="clients"')
speed_pos = html.find('id="speed-odometer"')
main_pos = html.find('</main>')

print('Overview pos:        ', overview_pos)
print('Related Articles pos:', related_pos)
print('Clients pos:         ', clients_pos)
print('Speed Odometer pos:  ', speed_pos)
print('Main end pos:        ', main_pos)
print('Is clients at the bottom (after related-articles)?', clients_pos > related_pos)
print('Is clients NOT at the start (after overview)?', clients_pos > overview_pos)
print('Is speed odometer the final section before </main>?', clients_pos < speed_pos < main_pos)
