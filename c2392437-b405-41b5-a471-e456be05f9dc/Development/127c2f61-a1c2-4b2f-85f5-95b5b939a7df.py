"""
Export 4: Geographic Breakdown by Region
Monthly revenue allocated to active regions
"""
import pandas as pd
import ast

# Build geographic breakdown table
export_geographic = pd.DataFrame({
    'month': timeline_df['month'],
    'date': timeline_df['date'].dt.strftime('%Y-%m-%d'),
    'year': timeline_df['year'],
    'quarter': timeline_df['quarter'],
    'active_regions': timeline_df['active_regions'].astype(str),
    'num_regions': [len(ast.literal_eval(str(r))) if isinstance(r, str) else len(r) for r in timeline_df['active_regions']],
    'uk_active': [('uk' in str(r).lower()) for r in timeline_df['active_regions']],
    'eu_active': [('eu' in str(r).lower()) for r in timeline_df['active_regions']],
    'us_active': [('us' in str(r).lower()) for r in timeline_df['active_regions']],
    'apac_active': [('apac' in str(r).lower()) for r in timeline_df['active_regions']],
})

# Add total revenue per month
export_geographic['total_monthly_revenue'] = export_monthly_revenue['total_monthly_revenue']

print(f"✓ Geographic breakdown table prepared: {len(export_geographic)} months")
print(f"  Regions expanded from 1 (UK) to {export_geographic.iloc[-1]['num_regions']} by month 60")
