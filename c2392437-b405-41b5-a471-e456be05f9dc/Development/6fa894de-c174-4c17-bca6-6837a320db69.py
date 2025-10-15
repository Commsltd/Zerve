import pandas as pd
import numpy as np

# Build MRR bridge: new bookings, expansion, contraction, churn
# Waterfall components month-over-month

bridge_records = []

for month_idx in range(1, 61):
    prev_month = month_idx - 1
    
    # Current month MRR
    current_mrr = subscription_mrr_df[subscription_mrr_df['month'] == month_idx]['total_mrr'].values[0]
    
    # Previous month MRR (0 for first month)
    if prev_month == 0:
        prev_mrr = 0
        new_bookings_mrr = current_mrr
        expansion_mrr_bridge = 0
        churn_mrr_bridge = 0
        contraction_mrr = 0
    else:
        prev_mrr = subscription_mrr_df[subscription_mrr_df['month'] == prev_month]['total_mrr'].values[0]
        
        # Get new customer acquisitions this month
        acq_row = acquisition_df[acquisition_df['month'] == month_idx].iloc[0]
        new_bookings_mrr = (
            acq_row['new_starter'] * tier_pricing['Starter']['monthly_price_gbp'] +
            acq_row['new_growth'] * tier_pricing['Growth']['monthly_price_gbp'] +
            acq_row['new_scale'] * tier_pricing['Scale']['monthly_price_gbp'] +
            acq_row['new_enterprise'] * tier_pricing['Enterprise']['monthly_price_gbp']
        )
        
        # Expansion MRR (seat additions)
        expansion_row_current = seat_expansion_df[seat_expansion_df['month'] == month_idx].iloc[0]
        expansion_row_prev = seat_expansion_df[seat_expansion_df['month'] == prev_month].iloc[0]
        expansion_mrr_bridge = expansion_row_current['total_expansion_mrr'] - expansion_row_prev['total_expansion_mrr']
        
        # Calculate churn impact
        prev_base_mrr = subscription_mrr_df[subscription_mrr_df['month'] == prev_month]['total_base_mrr'].values[0]
        current_base_mrr = subscription_mrr_df[subscription_mrr_df['month'] == month_idx]['total_base_mrr'].values[0]
        
        # Churn is the loss from base MRR (negative value)
        expected_base_without_churn = prev_base_mrr + new_bookings_mrr
        churn_mrr_bridge = current_base_mrr - expected_base_without_churn
        
        # Contraction (tier downgrades - minimal in this model)
        contraction_mrr = 0
    
    net_change = current_mrr - prev_mrr
    
    bridge_records.append({
        'month': month_idx,
        'beginning_mrr': prev_mrr,
        'new_bookings': new_bookings_mrr,
        'expansion_mrr': expansion_mrr_bridge,
        'contraction_mrr': contraction_mrr,
        'churn_mrr': churn_mrr_bridge,
        'ending_mrr': current_mrr,
        'net_change': net_change
    })

mrr_bridge_df = pd.DataFrame(bridge_records)

print(f"MRR bridge created for {len(mrr_bridge_df)} months")
print(f"\nMonth 60 MRR Bridge:")
m60 = mrr_bridge_df[mrr_bridge_df['month'] == 60].iloc[0]
print(f"  Beginning MRR: £{m60['beginning_mrr']:,.0f}")
print(f"  New Bookings: £{m60['new_bookings']:,.0f}")
print(f"  Expansion: £{m60['expansion_mrr']:,.0f}")
print(f"  Churn: £{m60['churn_mrr']:,.0f}")
print(f"  Ending MRR: £{m60['ending_mrr']:,.0f}")