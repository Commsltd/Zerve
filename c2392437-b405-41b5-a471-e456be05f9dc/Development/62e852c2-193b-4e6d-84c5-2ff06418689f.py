"""
Token Consumption Patterns by Segment
Calculates monthly token consumption based on customer density and activity patterns
"""
import pandas as pd

# Customer density model - avg customers per account by segment
segment_density = {
    'micro': 25,
    'small': 35,
    'medium': 210,
    'large': 1325,
    'mnc': 23000
}

# Calculate monthly monitors per segment based on account density
# Assumptions: 
# - Monitor ratio: ~120% of customer count (monitoring some customers plus prospects)
# - Search ratio: ~30-35% of monitor count (searches done per month)
monitor_ratio = 1.20
search_ratio = 0.32

consumption_by_segment = {}

for _seg, _density in segment_density.items():
    _monthly_monitors = int(_density * monitor_ratio)
    _monthly_searches = int(_monthly_monitors * search_ratio)
    
    consumption_by_segment[_seg] = {
        'customers_per_account': _density,
        'monthly_monitors': _monthly_monitors,
        'monthly_searches': _monthly_searches,
        'tokens_monitoring': _monthly_monitors * 1,  # 1 token per monitor
        'tokens_search': _monthly_searches * 1,  # 1 token per search
        'tokens_base': _monthly_monitors + _monthly_searches
    }

# Add AI report generation (varies by segment)
report_frequency = {
    'micro': 0.5,  # 0.5 reports per month on average
    'small': 0.8,
    'medium': 3,
    'large': 8,
    'mnc': 20
}

for _seg in consumption_by_segment:
    _reports = report_frequency[_seg]
    consumption_by_segment[_seg]['monthly_reports'] = _reports
    consumption_by_segment[_seg]['tokens_reports'] = _reports * 10  # 10 tokens per report
    consumption_by_segment[_seg]['total_monthly_tokens'] = (
        consumption_by_segment[_seg]['tokens_base'] + 
        consumption_by_segment[_seg]['tokens_reports']
    )

# Convert to DataFrame for easier analysis
consumption_df = pd.DataFrame.from_dict(consumption_by_segment, orient='index')

print("Token Consumption Patterns by Segment")
print("="*60)
for _seg_name in consumption_df.index:
    _row = consumption_df.loc[_seg_name]
    print(f"\n{_seg_name.upper()}:")
    print(f"  Monitors: {_row['monthly_monitors']:.0f}/month = {_row['tokens_monitoring']:.0f} tokens")
    print(f"  Searches: {_row['monthly_searches']:.0f}/month = {_row['tokens_search']:.0f} tokens")
    print(f"  Reports: {_row['monthly_reports']:.1f}/month = {_row['tokens_reports']:.0f} tokens")
    print(f"  TOTAL: {_row['total_monthly_tokens']:.0f} tokens/month")