"""
Calculation Engine: Token Revenue (Overage + PAYG)
Calculates token-based revenue from overage fees and pay-as-you-go customers
"""
import pandas as pd
import numpy as np

# Simplified token revenue calculation
calc_token_records = []

for token_month_idx in range(1, calc_months + 1):
    token_tier_row = calc_tier_movement[calc_tier_movement['month'] == token_month_idx].iloc[0]
    
    # Overage revenue by tier (customers exceeding included tokens)
    # Assume 10% of starter, 12% of growth, 15% of scale, 20% of enterprise have overage
    overage_starter = token_tier_row['net_starter'] * 0.10 * 50 * calc_token_economics['pricing']['overage_rate_gbp']
    overage_growth = token_tier_row['net_growth'] * 0.12 * 150 * calc_token_economics['pricing']['overage_rate_gbp']
    overage_scale = token_tier_row['net_scale'] * 0.15 * 500 * calc_token_economics['pricing']['overage_rate_gbp']
    overage_enterprise = token_tier_row['net_enterprise'] * 0.20 * 2000 * calc_token_economics['pricing']['overage_rate_gbp']
    
    calc_total_overage = overage_starter + overage_growth + overage_scale + overage_enterprise
    
    # PAYG revenue (non-subscription customers)
    # Grows from 0 to 500 sporadic + 1200 trial users by month 60
    progress_factor = token_month_idx / calc_months
    sporadic_users = int(500 * progress_factor)
    trial_users = int(1200 * progress_factor)
    
    payg_sporadic_revenue = sporadic_users * 85 * calc_token_economics['pricing']['payg_rate_gbp']
    payg_trial_revenue = trial_users * 15 * calc_token_economics['pricing']['payg_rate_gbp']
    calc_total_payg = payg_sporadic_revenue + payg_trial_revenue
    
    calc_total_token_revenue = calc_total_overage + calc_total_payg
    
    calc_token_records.append({
        'month': token_month_idx,
        'overage_revenue': calc_total_overage,
        'payg_revenue': calc_total_payg,
        'total_token_revenue': calc_total_token_revenue
    })

calc_token_revenue_df = pd.DataFrame(calc_token_records)

print(f"✓ Token Revenue Calculated: {len(calc_token_revenue_df)} months")
print(f"  Month 12 Token Revenue: £{calc_token_revenue_df[calc_token_revenue_df['month']==12]['total_token_revenue'].values[0]:,.0f}")
print(f"  Month 60 Token Revenue: £{calc_token_revenue_df[calc_token_revenue_df['month']==60]['total_token_revenue'].values[0]:,.0f}")
print(f"    (Overage: £{calc_token_revenue_df[calc_token_revenue_df['month']==60]['overage_revenue'].values[0]:,.0f}, PAYG: £{calc_token_revenue_df[calc_token_revenue_df['month']==60]['payg_revenue'].values[0]:,.0f})")