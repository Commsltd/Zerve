"""
Enterprise Licensing - Monthly Revenue Calculation
Calculates monthly licensing revenue with renewals and expansion
"""

import pandas as pd
import numpy as np

# Constants
months_horizon = 48
monthly_revenue_records = []

# Contract economics
renewal_rate_annual = 0.92
upsell_expansion_annual = 0.15
monthly_churn = 1 - (renewal_rate_annual ** (1/12))

# Segment configurations for phased GTM
segment_configs = {
    'trade_credit_insurers': {'start_month': 1, 'monthly_new_logos': 0.42},  # Y1-Y2
    'mnc_supply_chain': {'start_month': 13, 'monthly_new_logos': 0.625},      # Y2-Y3
    'banks_payment_processors': {'start_month': 25, 'monthly_new_logos': 0.2083},  # Y3-Y4
    'reinsurers_auditors': {'start_month': 13, 'monthly_new_logos': 0.4583}   # Y2-Y3
}

# Track segment logos over time
segment_logo_tracking = {seg: [] for seg in segment_configs.keys()}

for _month_idx in range(1, months_horizon + 1):
    _year_num = ((_month_idx - 1) // 12) + 1
    
    total_new_logo_revenue = 0
    total_renewal_revenue = 0
    total_expansion_revenue = 0
    
    for seg, _seg_config in segment_configs.items():
        if _month_idx >= _seg_config['start_month']:
            monthly_new_logos = _seg_config['monthly_new_logos']
            new_logo_mrr = monthly_new_logos * segment_acv_df[segment_acv_df['segment']==seg]['weighted_acv_gbp'].iloc[0] / 12
            
            # Calculate existing ARR from previous month
            if len(segment_logo_tracking[seg]) > 0:
                cumulative_logos_prev = sum(segment_logo_tracking[seg])
                existing_arr = cumulative_logos_prev * segment_acv_df[segment_acv_df['segment']==seg]['weighted_acv_gbp'].iloc[0]
                existing_mrr = existing_arr / 12
                
                # Apply monthly churn
                churned_mrr = existing_mrr * monthly_churn
                renewal_mrr = existing_mrr - churned_mrr
                
                total_renewal_revenue += renewal_mrr
                
                # Expansion revenue (15% annual = 1.25% monthly applied to existing base)
                if _month_idx % 12 == 0:  # Annual expansion
                    expansion_arr = existing_arr * upsell_expansion_annual
                    total_expansion_revenue += expansion_arr / 12
            
            total_new_logo_revenue += new_logo_mrr
            segment_logo_tracking[seg].append(monthly_new_logos)
        else:
            segment_logo_tracking[seg].append(0)
    
    # Total month revenue
    total_month_revenue = total_new_logo_revenue + total_renewal_revenue + total_expansion_revenue
    
    # Add strategic partner revenue
    if _year_num <= 2:
        partner_mrr = 37500  # £450k ARR / 12 at 50% discount
    elif _year_num == 3:
        partner_mrr = 56250  # £675k ARR / 12 at 25% discount
    else:
        partner_mrr = 75000  # £900k ARR / 12 at standard pricing
    
    monthly_revenue_records.append({
        'month': _month_idx,
        'year': _year_num,
        'new_logo_revenue_gbp': total_new_logo_revenue,
        'renewal_revenue_gbp': total_renewal_revenue,
        'expansion_revenue_gbp': total_expansion_revenue,
        'total_mrr_gbp': total_month_revenue,
        'strategic_partner_mrr_gbp': partner_mrr,
        'total_with_partners_mrr_gbp': total_month_revenue + partner_mrr
    })

monthly_rev_df = pd.DataFrame(monthly_revenue_records)

print(f"✓ Enterprise licensing monthly revenue calculated")
print(f"  48-month revenue model")
print(f"  Includes 4 strategic partners")
print(f"  Month 12 total: £{monthly_rev_df[monthly_rev_df['month']==12]['total_with_partners_mrr_gbp'].iloc[0]:,.0f}")
print(f"  Month 48 total: £{monthly_rev_df[monthly_rev_df['month']==48]['total_with_partners_mrr_gbp'].iloc[0]:,.0f}")