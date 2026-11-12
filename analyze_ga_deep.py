import pandas as pd

excel_gsc = 'GSC Performance-on-Search - sep 1,2026 to nov 2,2026.xlsx'
excel_ga = 'Google analytics - spe 1,2026 to nov 2 ,2026.xlsx'

df_p = pd.read_excel(excel_gsc, sheet_name='Pages')
df_q = pd.read_excel(excel_gsc, sheet_name='Queries')

print("--- Pages with clicks >= 1 ---")
print(df_p[df_p['Clicks'] >= 1][['Top pages', 'Clicks', 'Impressions', 'CTR', 'Position']].to_string())

# GA Pages analysis
df_ga_pages = pd.read_excel(excel_ga, sheet_name='Pages_and_screens_Page_path_and', skiprows=1)
df_ga_pages.columns = ['Page', 'Views', 'Active users', 'Views_per_user', 'Avg_engagement_sec', 'Event_count', 'Sessions']
print("\n--- GA Top 30 Pages by Views ---")
print(df_ga_pages.sort_values(by='Views', ascending=False).head(30)[['Page', 'Views', 'Active users', 'Avg_engagement_sec', 'Sessions']].to_string())

# GA Organic landing pages
df_ga_landing = pd.read_excel(excel_ga, sheet_name='Landing_page organic search', skiprows=2)
df_ga_landing.columns = ['Landing_page', 'Sessions', 'Engaged_sessions', 'New_users', 'Avg_engagement_sec']
print("\n--- GA Organic Landing Pages ---")
print(df_ga_landing.sort_values(by='Sessions', ascending=False).head(25).to_string())

# GA Traffic Acquisition
df_ga_traffic = pd.read_excel(excel_ga, sheet_name='Traffic_acquisition_Session_pri', skiprows=2)
df_ga_traffic.columns = ['Channel', 'Sessions', 'Engaged_sessions', 'Engagement_rate', 'Avg_engagement_sec', 'Events_per_session', 'Event_count']
print("\n--- GA Traffic Acquisition ---")
print(df_ga_traffic.to_string())
