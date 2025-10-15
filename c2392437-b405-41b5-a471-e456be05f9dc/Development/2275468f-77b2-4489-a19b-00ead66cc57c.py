import pandas as pd
import numpy as np

# Calculate Monthly Recurring Revenue (MRR) by tier
# Base MRR + Tier upgrade MRR + Seat expansion MRR

mrr_records = []

for month_idx in range(1, 61):
    # Get tier counts
    tier_row = tier_movement_df[tier_movement_df['month'] == month_idx].iloc[0]
    
    # Base MRR from active customers
    base_starter_mrr = tier_row['net_starter'] * tier_pricing['Starter']['monthly_price_gbp']
    base_growth_mrr = tier_row['net_growth'] * tier_pricing['Growth']['monthly_price_gbp']
    base_scale_mrr = tier_row['net_scale'] * tier_pricing['Scale']['monthly_price_gbp']
    base_enterprise_mrr = tier_row['net_enterprise'] * tier_pricing['Enterprise']['monthly_price_gbp']
    
    total_base_mrr = base_starter_mrr + base_growth_mrr + base_scale_mrr + base_enterprise_mrr
    
    # Get seat expansion MRR
    expansion_row = seat_expansion_df[seat_expansion_df['month'] == month_idx].iloc[0]
    expansion_mrr = expansion_row['total_expansion_mrr']
    
    # Total MRR
    total_mrr = total_base_mrr + expansion_mrr
    
    mrr_records.append({
        'month': month_idx,
        'base_starter_mrr': base_starter_mrr,
        'base_growth_mrr': base_growth_mrr,
        'base_scale_mrr': base_scale_mrr,
        'base_enterprise_mrr': base_enterprise_mrr,
        'total_base_mrr': total_base_mrr,
        'expansion_mrr': expansion_mrr,
        'total_mrr': total_mrr,
        'arr': total_mrr * 12
    })

subscription_mrr_df = pd.DataFrame(mrr_records)

print(f"MRR model created for {len(subscription_mrr_df)} months")
print(f"\nKey Milestones:")
print(f"  Month 12 ARR: £{subscription_mrr_df[subscription_mrr_df['month']==12]['arr'].values[0]:,.0f}")
print(f"  Month 36 ARR: £{subscription_mrr_df[subscription_mrr_df['month']==36]['arr'].values[0]:,.0f}")
print(f"  Month 60 ARR: £{subscription_mrr_df[subscription_mrr_df['month']==60]['arr'].values[0]:,.0f}")