"""
Deal Pipeline Model by Customer Segment
Models deal pipeline with phased GTM approach and realistic sales funnel progression
"""

import pandas as pd
import numpy as np

# Define pipeline stages and conversion rates for enterprise sales
pipeline_stages = {
    'identified': {'stage_num': 1, 'conversion_to_next': 0.60},
    'qualified': {'stage_num': 2, 'conversion_to_next': 0.55},
    'demo_poc': {'stage_num': 3, 'conversion_to_next': 0.45},
    'proposal': {'stage_num': 4, 'conversion_to_next': 0.65},
    'negotiation': {'stage_num': 5, 'conversion_to_next': 0.70},
    'closed_won': {'stage_num': 6, 'conversion_to_next': 1.0}
}

# Pipeline targets by segment and year (identified prospects entering funnel)
# Based on GTM timing from customer segments
pipeline_targets = {
    'trade_credit_insurers': {
        'Y1': 15, 'Y2': 12, 'Y3': 8, 'Y4': 6,
        'win_rate': 0.30,
        'sales_cycle_months': 12
    },
    'mnc_supply_chain': {
        'Y1': 0, 'Y2': 20, 'Y3': 25, 'Y4': 18,
        'win_rate': 0.22,
        'sales_cycle_months': 9
    },
    'banks_payment_processors': {
        'Y1': 0, 'Y2': 0, 'Y3': 15, 'Y4': 22,
        'win_rate': 0.18,
        'sales_cycle_months': 18
    },
    'reinsurers_auditors': {
        'Y1': 0, 'Y2': 18, 'Y3': 20, 'Y4': 15,
        'win_rate': 0.25,
        'sales_cycle_months': 6
    }
}

# Calculate expected closed won deals by year for each segment
pipeline_summary_list = []
for segment, targets in pipeline_targets.items():
    for year in ['Y1', 'Y2', 'Y3', 'Y4']:
        identified_deals = targets[year]
        win_rate = targets['win_rate']
        expected_wins = identified_deals * win_rate
        
        pipeline_summary_list.append({
            'segment': segment,
            'year': year,
            'identified_prospects': identified_deals,
            'expected_closed_won': round(expected_wins, 1),
            'win_rate': win_rate,
            'sales_cycle_months': targets['sales_cycle_months']
        })

pipeline_summary_df = pd.DataFrame(pipeline_summary_list)

# Calculate cumulative pipeline value
# Using mid-point contract values from enterprise_segments
contract_midpoints = {
    'trade_credit_insurers': 325000,
    'mnc_supply_chain': 150000,
    'banks_payment_processors': 250000,
    'reinsurers_auditors': 137500
}

pipeline_summary_df['mid_contract_gbp'] = pipeline_summary_df['segment'].map(contract_midpoints)
pipeline_summary_df['expected_pipeline_value_gbp'] = (
    pipeline_summary_df['expected_closed_won'] * pipeline_summary_df['mid_contract_gbp']
)

# Aggregate by year
yearly_pipeline = pipeline_summary_df.groupby('year').agg({
    'identified_prospects': 'sum',
    'expected_closed_won': 'sum',
    'expected_pipeline_value_gbp': 'sum'
}).round(1)

print("=" * 80)
print("ENTERPRISE LICENSING - DEAL PIPELINE BY SEGMENT")
print("=" * 80)
print(f"\nTotal Identified Prospects (4 years): {pipeline_summary_df['identified_prospects'].sum():.0f}")
print(f"Total Expected Wins (4 years): {pipeline_summary_df['expected_closed_won'].sum():.1f}")
print(f"Total Expected Pipeline Value: £{pipeline_summary_df['expected_pipeline_value_gbp'].sum():,.0f}")
print(f"\nAverage Win Rate Across All Segments: {pipeline_summary_df['win_rate'].mean():.1%}")
print("\nYearly Pipeline Summary:")
print(yearly_pipeline)
print("=" * 80)