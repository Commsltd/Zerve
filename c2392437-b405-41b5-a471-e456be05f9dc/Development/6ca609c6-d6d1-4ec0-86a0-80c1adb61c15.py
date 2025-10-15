"""
Logo Acquisition Timeline
Tracks cumulative customer logo acquisition by segment over 48 months
"""

import pandas as pd
import numpy as np

# Reconstruct logo tracking month-by-month
months_total = 48
logo_timeline_records = []

# Segment-specific parameters
seg_params = {
    'trade_credit_insurers': {
        'wins_by_year': {1: 4.5, 2: 3.6, 3: 2.4, 4: 1.8},
        'gtm_start': 1
    },
    'mnc_supply_chain': {
        'wins_by_year': {1: 0, 2: 4.4, 3: 5.5, 4: 4.0},
        'gtm_start': 13
    },
    'banks_payment_processors': {
        'wins_by_year': {1: 0, 2: 0, 3: 2.7, 4: 4.0},
        'gtm_start': 25
    },
    'reinsurers_auditors': {
        'wins_by_year': {1: 0, 2: 4.5, 3: 5.0, 4: 3.75},
        'gtm_start': 13
    }
}

# Monthly churn rate (converting from 92% annual retention)
monthly_retention = 0.92 ** (1/12)
monthly_logo_churn = 1 - monthly_retention

# Track cumulative logos by segment
cumulative_logos = {_seg: 0 for _seg in seg_params.keys()}

for _month_num in range(1, months_total + 1):
    _year_num = ((_month_num - 1) // 12) + 1
    
    month_record = {
        'month': _month_num,
        'year': _year_num
    }
    
    for _seg, _params in seg_params.items():
        # Add new logos if GTM active
        if _month_num >= _params['gtm_start'] and _year_num in _params['wins_by_year']:
            _monthly_new = _params['wins_by_year'][_year_num] / 12
            cumulative_logos[_seg] += _monthly_new
        
        # Apply churn
        cumulative_logos[_seg] *= (1 - monthly_logo_churn)
        
        month_record[f'{_seg}_logos'] = cumulative_logos[_seg]
    
    # Total across all segments
    month_record['total_logos'] = sum(cumulative_logos.values())
    logo_timeline_records.append(month_record)

logo_timeline_df = pd.DataFrame(logo_timeline_records)

# Add strategic partners (4 partners active from month 1)
logo_timeline_df['strategic_partner_logos'] = 4
logo_timeline_df['total_with_partners'] = logo_timeline_df['total_logos'] + 4

# Summary by year end
yearly_logo_summary = logo_timeline_df[logo_timeline_df['month'].isin([12, 24, 36, 48])][
    ['month', 'year', 'total_logos', 'strategic_partner_logos', 'total_with_partners']
]

print("=" * 80)
print("LOGO ACQUISITION TIMELINE")
print("=" * 80)
print(f"\nTotal Institutional Logos by Year End:")
for _i, _summary_row in yearly_logo_summary.iterrows():
    print(f"  Year {int(_summary_row['year'])}: {_summary_row['total_with_partners']:.1f} logos "
          f"({_summary_row['total_logos']:.1f} institutional + {_summary_row['strategic_partner_logos']:.0f} strategic partners)")
print(f"\nFinal Logo Count (Month 48): {logo_timeline_df.iloc[-1]['total_with_partners']:.1f}")
print(f"  - Institutional Customers: {logo_timeline_df.iloc[-1]['total_logos']:.1f}")
print(f"  - Strategic Partners: 4")
print("=" * 80)