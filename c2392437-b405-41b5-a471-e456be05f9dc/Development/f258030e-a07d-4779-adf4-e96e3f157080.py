"""
Milestone Achievement Tracking
Document key revenue and customer milestones for investor reporting
"""
import pandas as pd
import numpy as np

# Define major milestones
milestones_list = []

# ARR Milestones
arr_milestones = [1_000_000, 5_000_000, 10_000_000, 25_000_000, 50_000_000, 100_000_000, 
                  250_000_000, 500_000_000, 750_000_000, 1_000_000_000]

for _milestone in arr_milestones:
    _reached = arr_growth_metrics[arr_growth_metrics['arr'] >= _milestone]
    if len(_reached) > 0:
        _first = _reached.iloc[0]
        milestones_list.append({
            'milestone_type': 'ARR',
            'milestone_value': _milestone,
            'milestone_label': f'£{_milestone:,.0f} ARR',
            'month_achieved': int(_first['month']),
            'date_achieved': _first['date'],
            'year_achieved': int(_first['year']),
            'quarter_achieved': int(_first['quarter'])
        })

# Customer Count Milestones
customer_milestones = [100, 500, 1_000, 5_000, 10_000, 25_000, 50_000]

for _milestone in customer_milestones:
    _reached = tier_movement_df[tier_movement_df['total_active'] >= _milestone]
    if len(_reached) > 0:
        _first = _reached.iloc[0]
        _timeline_row = timeline_df[timeline_df['month'] == _first['month']].iloc[0]
        milestones_list.append({
            'milestone_type': 'Customers',
            'milestone_value': _milestone,
            'milestone_label': f'{_milestone:,} Total Customers',
            'month_achieved': int(_first['month']),
            'date_achieved': _timeline_row['date'],
            'year_achieved': int(_timeline_row['year']),
            'quarter_achieved': int(_timeline_row['quarter'])
        })

# GRR/NRR Milestones (reaching certain retention levels)
_grr_70_reached = retention_by_period[retention_by_period['grr_12m'] >= 0.70]
if len(_grr_70_reached) > 0:
    _first = _grr_70_reached.iloc[0]
    milestones_list.append({
        'milestone_type': 'Retention',
        'milestone_value': 0.70,
        'milestone_label': '70% GRR (12M)',
        'month_achieved': int(_first['month']),
        'date_achieved': _first['date'],
        'year_achieved': int(_first['year']) if not pd.isna(_first['year']) else 0,
        'quarter_achieved': int(_first['quarter']) if not pd.isna(_first['quarter']) else 0
    })

_nrr_70_reached = retention_by_period[retention_by_period['nrr_12m'] >= 0.70]
if len(_nrr_70_reached) > 0:
    _first = _nrr_70_reached.iloc[0]
    milestones_list.append({
        'milestone_type': 'Retention',
        'milestone_value': 0.70,
        'milestone_label': '70% NRR (12M)',
        'month_achieved': int(_first['month']),
        'date_achieved': _first['date'],
        'year_achieved': int(_first['year']) if not pd.isna(_first['year']) else 0,
        'quarter_achieved': int(_first['quarter']) if not pd.isna(_first['quarter']) else 0
    })

# LTV:CAC Ratio Milestones
_ltv_cac_3x_reached = cac_ltv_metrics[cac_ltv_metrics['ltv_cac_ratio'] >= 3.0]
if len(_ltv_cac_3x_reached) > 0:
    _first = _ltv_cac_3x_reached.iloc[0]
    _timeline_row = timeline_df[timeline_df['month'] == _first['month']].iloc[0]
    milestones_list.append({
        'milestone_type': 'Unit Economics',
        'milestone_value': 3.0,
        'milestone_label': '3:1 LTV:CAC Ratio',
        'month_achieved': int(_first['month']),
        'date_achieved': _timeline_row['date'],
        'year_achieved': int(_timeline_row['year']),
        'quarter_achieved': int(_timeline_row['quarter'])
    })

milestones_df = pd.DataFrame(milestones_list)
if len(milestones_df) > 0:
    milestones_df = milestones_df.sort_values('month_achieved')

print("✓ Milestone Achievement Tracking")
print(f"  Total milestones achieved: {len(milestones_df)}")
if len(milestones_df) > 0:
    print(f"  ARR milestones: {len(milestones_df[milestones_df['milestone_type']=='ARR'])}")
    print(f"  Customer milestones: {len(milestones_df[milestones_df['milestone_type']=='Customers'])}")
    print(f"  First major milestone: {milestones_df.iloc[0]['milestone_label']} (Month {milestones_df.iloc[0]['month_achieved']})")