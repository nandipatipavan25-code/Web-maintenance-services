import pandas as pd

excel_gsc = 'GSC Performance-on-Search - sep 1,2026 to nov 2,2026.xlsx'
df_q = pd.read_excel(excel_gsc, sheet_name='Queries')
df_p = pd.read_excel(excel_gsc, sheet_name='Pages')
df_c = pd.read_excel(excel_gsc, sheet_name='Countries')
df_d = pd.read_excel(excel_gsc, sheet_name='Devices')

print('=== GSC OVERVIEW ===')
print(f"Total Queries: {len(df_q)}, Total Clicks in Queries: {df_q['Clicks'].sum()}, Total Impressions: {df_q['Impressions'].sum()}")
print(f"Total Pages: {len(df_p)}, Total Clicks in Pages: {df_p['Clicks'].sum()}, Total Impressions: {df_p['Impressions'].sum()}")

print('\n=== GSC TOP 25 QUERIES BY CLICKS ===')
print(df_q.sort_values(by=['Clicks', 'Impressions'], ascending=False).head(25).to_string())

print('\n=== GSC TOP 25 QUERIES BY IMPRESSIONS ===')
print(df_q.sort_values(by='Impressions', ascending=False).head(25).to_string())

print('\n=== GSC STRIKING DISTANCE QUERIES (Pos 11-25, Impressions >= 30) ===')
striking = df_q[(df_q['Position'] >= 11) & (df_q['Position'] <= 25) & (df_q['Impressions'] >= 30)].sort_values(by='Impressions', ascending=False)
print(striking.head(30).to_string())

print('\n=== GSC TOP 25 PAGES BY CLICKS ===')
print(df_p.sort_values(by=['Clicks', 'Impressions'], ascending=False).head(25).to_string())

print('\n=== GSC TOP 25 PAGES BY IMPRESSIONS ===')
print(df_p.sort_values(by='Impressions', ascending=False).head(25).to_string())
