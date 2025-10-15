"""
Calculation Engine: ARR and MRR Calculation
Calculates Monthly Recurring Revenue (MRR) and Annual Recurring Revenue (ARR) by tier
Includes cumulative metrics, growth rates, and ARPU by tier
"""
import pandas as pd
import numpy as np

# Calculate MRR by tier with cumulative tracking and ARPU
calc_mrr_records = []

for mrr_month_idx in range(1, calc_months + 1):
    tier_row = calc_tier_movement[calc_tier_movement['month'] == mrr_month_idx].iloc[0]
    
    # Base MRR from active customers at each tier
    calc_starter_mrr = tier_row['net_starter'] * calc_pricing_tiers['Starter']['monthly_price_gbp']
    calc_growth_mrr = tier_row['net_growth'] * calc_pricing_tiers['Growth']['monthly_price_gbp']
    calc_scale_mrr = tier_row['net_scale'] * calc_pricing_tiers['Scale']['monthly_price_gbp']
    calc_enterprise_mrr = tier_row['net_enterprise'] * calc_pricing_tiers['Enterprise']['monthly_price_gbp']
    
    calc_total_base_mrr = calc_starter_mrr + calc_growth_mrr + calc_scale_mrr + calc_enterprise_mrr
    
    # Seat expansion (simplified model)
    calc_seat_expansion_mrr = (
        tier_row['net_growth'] * calc_pricing_tiers['Growth']['monthly_price_gbp'] * 0.03 * 0.5 +
        tier_row['net_scale'] * calc_pricing_tiers['Scale']['monthly_price_gbp'] * 0.035 * 2 +
        tier_row['net_enterprise'] * calc_pricing_tiers['Enterprise']['monthly_price_gbp'] * 0.045 * 5
    )
    
    calc_total_mrr = calc_total_base_mrr + calc_seat_expansion_mrr
    calc_arr = calc_total_mrr * 12
    
    # Calculate ARPU by tier (including seat expansion proportionally)
    total_customers = tier_row['net_starter'] + tier_row['net_growth'] + tier_row['net_scale'] + tier_row['net_enterprise']
    
    calc_starter_arpu = (calc_starter_mrr / tier_row['net_starter']) if tier_row['net_starter'] > 0 else 0
    calc_growth_arpu = (calc_growth_mrr / tier_row['net_growth']) if tier_row['net_growth'] > 0 else 0
    calc_scale_arpu = (calc_scale_mrr / tier_row['net_scale']) if tier_row['net_scale'] > 0 else 0
    calc_enterprise_arpu = (calc_enterprise_mrr / tier_row['net_enterprise']) if tier_row['net_enterprise'] > 0 else 0
    calc_blended_arpu = (calc_total_mrr / total_customers) if total_customers > 0 else 0
    
    calc_mrr_records.append({
        'month': mrr_month_idx,
        'starter_mrr': calc_starter_mrr,
        'growth_mrr': calc_growth_mrr,
        'scale_mrr': calc_scale_mrr,
        'enterprise_mrr': calc_enterprise_mrr,
        'base_mrr': calc_total_base_mrr,
        'seat_expansion_mrr': calc_seat_expansion_mrr,
        'total_mrr': calc_total_mrr,
        'arr': calc_arr,
        'starter_arpu': calc_starter_arpu,
        'growth_arpu': calc_growth_arpu,
        'scale_arpu': calc_scale_arpu,
        'enterprise_arpu': calc_enterprise_arpu,
        'blended_arpu': calc_blended_arpu,
        'total_customers': total_customers
    })

calc_subscription_mrr_df = pd.DataFrame(calc_mrr_records)

# Calculate cumulative ARR and MRR
calc_subscription_mrr_df['cumulative_arr'] = calc_subscription_mrr_df['arr'].cumsum()
calc_subscription_mrr_df['cumulative_mrr'] = calc_subscription_mrr_df['total_mrr'].cumsum()

# Calculate growth rates (MoM)
calc_subscription_mrr_df['mrr_growth_rate'] = calc_subscription_mrr_df['total_mrr'].pct_change()
calc_subscription_mrr_df['arr_growth_rate'] = calc_subscription_mrr_df['arr'].pct_change()

# Replace NaN and inf values with 0 for the first month
calc_subscription_mrr_df['mrr_growth_rate'] = calc_subscription_mrr_df['mrr_growth_rate'].replace([np.inf, -np.inf], 0).fillna(0)
calc_subscription_mrr_df['arr_growth_rate'] = calc_subscription_mrr_df['arr_growth_rate'].replace([np.inf, -np.inf], 0).fillna(0)

# Key milestones
calc_arr_m12 = calc_subscription_mrr_df[calc_subscription_mrr_df['month']==12]['arr'].values[0]
calc_arr_m24 = calc_subscription_mrr_df[calc_subscription_mrr_df['month']==24]['arr'].values[0]
calc_arr_m36 = calc_subscription_mrr_df[calc_subscription_mrr_df['month']==36]['arr'].values[0]
calc_arr_m48 = calc_subscription_mrr_df[calc_subscription_mrr_df['month']==48]['arr'].values[0]
calc_arr_m60 = calc_subscription_mrr_df[calc_subscription_mrr_df['month']==60]['arr'].values[0]

# ARPU metrics at key milestones
calc_arpu_m12 = calc_subscription_mrr_df[calc_subscription_mrr_df['month']==12]['blended_arpu'].values[0]
calc_arpu_m60 = calc_subscription_mrr_df[calc_subscription_mrr_df['month']==60]['blended_arpu'].values[0]

print(f"✓ ARR/MRR Calculation Engine: {len(calc_subscription_mrr_df)} months")
print(f"  ARR Milestones:")
print(f"    Year 1 (M12): £{calc_arr_m12:,.0f}")
print(f"    Year 2 (M24): £{calc_arr_m24:,.0f}")
print(f"    Year 3 (M36): £{calc_arr_m36:,.0f}")
print(f"    Year 5 (M60): £{calc_arr_m60:,.0f}")
print(f"  ARPU (Blended):")
print(f"    Year 1 (M12): £{calc_arpu_m12:,.0f}")
print(f"    Year 5 (M60): £{calc_arpu_m60:,.0f}")
