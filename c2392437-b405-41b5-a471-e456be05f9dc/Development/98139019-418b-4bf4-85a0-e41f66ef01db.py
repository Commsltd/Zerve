"""
Calculation Engine: Tier Upgrades
Calculates customer movements between tiers based on conversion rates
"""
import pandas as pd
import numpy as np

# Calculate tier upgrades
calc_upgrade_records = []

for month_idx in range(1, calc_months + 1):
    active_row = calc_active_customers[calc_active_customers['month'] == month_idx].iloc[0]
    
    # Eligible customers for upgrade (active for at least 3 months)
    eligible_starter = active_row['active_starter'] * 0.5  # Assume 50% are eligible
    eligible_growth = active_row['active_growth'] * 0.4
    eligible_scale = active_row['active_scale'] * 0.3
    
    # Apply conversion rates
    starter_to_growth_upgrades = eligible_starter * calc_volume_assumptions['conversion_rates']['starter_to_growth'] / 12
    growth_to_scale_upgrades = eligible_growth * calc_volume_assumptions['conversion_rates']['growth_to_scale'] / 12
    scale_to_enterprise_upgrades = eligible_scale * calc_volume_assumptions['conversion_rates']['scale_to_enterprise'] / 12
    
    calc_upgrade_records.append({
        'month': month_idx,
        'starter_to_growth': starter_to_growth_upgrades,
        'growth_to_scale': growth_to_scale_upgrades,
        'scale_to_enterprise': scale_to_enterprise_upgrades
    })

calc_upgrade_df = pd.DataFrame(calc_upgrade_records)

# Calculate net tier counts after upgrades
calc_tier_movement = calc_active_customers.merge(calc_upgrade_df, on='month')

calc_tier_movement['net_starter'] = (
    calc_tier_movement['active_starter'] - 
    calc_tier_movement['starter_to_growth']
)

calc_tier_movement['net_growth'] = (
    calc_tier_movement['active_growth'] + 
    calc_tier_movement['starter_to_growth'] - 
    calc_tier_movement['growth_to_scale']
)

calc_tier_movement['net_scale'] = (
    calc_tier_movement['active_scale'] + 
    calc_tier_movement['growth_to_scale'] - 
    calc_tier_movement['scale_to_enterprise']
)

calc_tier_movement['net_enterprise'] = (
    calc_tier_movement['active_enterprise'] + 
    calc_tier_movement['scale_to_enterprise']
)

# Ensure no negative values
for col in ['net_starter', 'net_growth', 'net_scale', 'net_enterprise']:
    calc_tier_movement[col] = calc_tier_movement[col].clip(lower=0)

print(f"✓ Tier Upgrades Calculated: {len(calc_upgrade_df)} months")
print(f"  Total Upgrades over 60 months:")
print(f"    Starter→Growth: {int(calc_upgrade_df['starter_to_growth'].sum()):,}")
print(f"    Growth→Scale: {int(calc_upgrade_df['growth_to_scale'].sum()):,}")
print(f"    Scale→Enterprise: {int(calc_upgrade_df['scale_to_enterprise'].sum()):,}")