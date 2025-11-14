"""
Cohort Retention Curves Export
Track customer retention by cohort month for investor reporting
"""
import pandas as pd
import numpy as np

# Calculate cohort retention curves
cohort_retention = cohort_df.copy()

# Pivot to get retention by cohort
_cohort_pivot = cohort_df.groupby(['cohort_month', 'months_since_acquisition']).agg({
    'starter_count': 'sum',
    'growth_count': 'sum',
    'scale_count': 'sum',
    'enterprise_count': 'sum'
}).reset_index()

_cohort_pivot['total_customers'] = (
    _cohort_pivot['starter_count'] +
    _cohort_pivot['growth_count'] +
    _cohort_pivot['scale_count'] +
    _cohort_pivot['enterprise_count']
)

# Calculate retention percentages for each cohort
cohort_retention_pcts = []

for _cohort_month in range(1, 61):
    _cohort_data = _cohort_pivot[_cohort_pivot['cohort_month'] == _cohort_month].sort_values('months_since_acquisition')
    
    if len(_cohort_data) > 0:
        _month_0 = _cohort_data[_cohort_data['months_since_acquisition'] == 0]['total_customers'].values
        
        if len(_month_0) > 0 and _month_0[0] > 0:
            _baseline = _month_0[0]
            
            for _, _row in _cohort_data.iterrows():
                cohort_retention_pcts.append({
                    'cohort_month': _cohort_month,
                    'months_since_acquisition': _row['months_since_acquisition'],
                    'customers_retained': _row['total_customers'],
                    'retention_pct': _row['total_customers'] / _baseline,
                    'cohort_baseline': _baseline
                })

cohort_retention_curves_df = pd.DataFrame(cohort_retention_pcts)

print("✓ Cohort Retention Curves Calculated")
print(f"  Total cohorts tracked: {cohort_retention_curves_df['cohort_month'].nunique()}")
print(f"  Max retention period: {cohort_retention_curves_df['months_since_acquisition'].max()} months")
print(f"  Average 12M retention: {cohort_retention_curves_df[cohort_retention_curves_df['months_since_acquisition']==12]['retention_pct'].mean():.1%}")