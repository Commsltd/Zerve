import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create 60-month timeframe (5 years)
start_date = datetime(2025, 1, 1)
_months_count = 60

# Generate month-by-month timeline
timeline_data = []
for _month_idx in range(_months_count):
    current_date = start_date + timedelta(days=30 * _month_idx)
    _yr = (_month_idx // 12) + 1
    _qtr = ((_month_idx % 12) // 3) + 1
    
    timeline_data.append({
        'month': _month_idx + 1,
        'date': current_date,
        'year': _yr,
        'quarter': _qtr,
        'month_of_year': (_month_idx % 12) + 1
    })

timeline_df = pd.DataFrame(timeline_data)

# Define GTM phase mapping
def get_gtm_phase(month):
    if month <= 6:
        return 'stealth'
    elif month <= 18:
        return 'beta'
    else:
        return 'launch'

timeline_df['gtm_phase'] = timeline_df['month'].apply(get_gtm_phase)

# Define geographic expansion
def get_active_regions(month):
    regions = ['uk']
    if month >= 13:  # Year 2
        regions.append('eu')
    if month >= 25:  # Year 3
        regions.append('us')
    if month >= 37:  # Year 4
        regions.append('apac')
    return regions

timeline_df['active_regions'] = timeline_df['month'].apply(get_active_regions)

print(f"Timeline created: {_months_count} months ({len(timeline_df)} rows)")
print(f"\nPhase Distribution:")
print(timeline_df.groupby('gtm_phase').size())