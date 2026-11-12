import pandas as pd
import numpy as np

excel_ga = 'Google analytics - spe 1,2026 to nov 2 ,2026.xlsx'

# 1. Pages and Screens
df_p = pd.read_excel(excel_ga, sheet_name='Pages_and_screens_Page_path_and')
# inspect raw rows
print("Raw df_p rows 0-3:")
print(df_p.iloc[0:4])

# Find the header row
header_idx = None
for i in range(len(df_p)):
    if 'Page path' in str(df_p.iloc[i, 0]):
        header_idx = i
        break

if header_idx is not None:
    df_pages = df_p.iloc[header_idx+1:].copy()
    df_pages.columns = [str(c).strip() for c in df_p.iloc[header_idx]]
    for col in ['Views', 'Active users', 'Event count', 'Sessions']:
        if col in df_pages.columns:
            df_pages[col] = pd.to_numeric(df_pages[col], errors='coerce').fillna(0)
    if 'Average engagement time per active user' in df_pages.columns:
        df_pages['Average engagement time per active user'] = pd.to_numeric(df_pages['Average engagement time per active user'], errors='coerce').fillna(0)
    
    print("\n=== TOP 25 PAGES BY VIEWS ===")
    print(df_pages.sort_values(by='Views', ascending=False).head(25)[['Page path and screen class', 'Views', 'Active users', 'Sessions', 'Average engagement time per active user', 'Event count']].to_string())

# 2. Traffic Acquisition
df_t = pd.read_excel(excel_ga, sheet_name='Traffic_acquisition_Session_pri')
header_idx_t = None
for i in range(len(df_t)):
    if 'Session primary channel group' in str(df_t.iloc[i, 0]):
        header_idx_t = i
        break

if header_idx_t is not None:
    df_traffic = df_t.iloc[header_idx_t+1:].copy()
    df_traffic.columns = [str(c).strip() for c in df_t.iloc[header_idx_t]]
    print("\n=== TRAFFIC ACQUISITION ===")
    print(df_traffic.to_string())

# 3. Landing page organic search
df_l = pd.read_excel(excel_ga, sheet_name='Landing_page organic search')
header_idx_l = None
for i in range(len(df_l)):
    if 'Landing page' in str(df_l.iloc[i, 0]):
        header_idx_l = i
        break

if header_idx_l is not None:
    df_landing = df_l.iloc[header_idx_l+1:].copy()
    df_landing.columns = [str(c).strip() for c in df_l.iloc[header_idx_l]]
    for col in df_landing.columns[1:]:
        df_landing[col] = pd.to_numeric(df_landing[col], errors='coerce').fillna(0)
    print("\n=== ORGANIC SEARCH LANDING PAGES ===")
    print(df_landing.sort_values(by=df_landing.columns[1], ascending=False).head(30).to_string())
