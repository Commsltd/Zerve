import pandas as pd
import numpy as np

# Model tier upgrades/downgrades with time lags
# Apply conversion funnel rates to existing customers

upgrade_records = []

for current_month in range(1, 61):
    # Get active customers in current month
    active_row = active_customers_df[active_customers_df['month'] == current_month].iloc[0]
    
    # Calculate upgrades based on conversion rates and lag times
    # Starter -> Growth (18% conversion, 6 month lag)
    starter_to_growth = 0
    if current_month >= 7:  # Need at least 6 months of lag
        # Look at customers who've been Starter for ~6 months
        eligible_starters = active_row['active_starter'] * 0.25  # Rough estimate of eligible cohort
        starter_to_growth = eligible_starters * conversion_funnels['starter_to_growth']['conversion_rate'] / 6
    
    # Growth -> Scale (9% conversion, 9 month lag)
    growth_to_scale = 0
    if current_month >= 10:
        eligible_growth = active_row['active_growth'] * 0.2
        growth_to_scale = eligible_growth * conversion_funnels['growth_to_scale']['conversion_rate'] / 9
    
    # Scale -> Enterprise (4% conversion, 9 month lag)
    scale_to_enterprise = 0
    if current_month >= 10:
        eligible_scale = active_row['active_scale'] * 0.15
        scale_to_enterprise = eligible_scale * conversion_funnels['scale_to_enterprise']['conversion_rate'] / 9
    
    upgrade_records.append({
        'month': current_month,
        'starter_to_growth': starter_to_growth,
        'growth_to_scale': growth_to_scale,
        'scale_to_enterprise': scale_to_enterprise
    })

upgrade_df = pd.DataFrame(upgrade_records)

# Calculate net tier counts after upgrades
tier_movement_df = active_customers_df.copy()
tier_movement_df = tier_movement_df.merge(upgrade_df, on='month')

# Adjust counts for tier movements
tier_movement_df['net_starter'] = (
    tier_movement_df['active_starter'] - tier_movement_df['starter_to_growth']
)
tier_movement_df['net_growth'] = (
    tier_movement_df['active_growth'] + tier_movement_df['starter_to_growth'] - tier_movement_df['growth_to_scale']
)
tier_movement_df['net_scale'] = (
    tier_movement_df['active_scale'] + tier_movement_df['growth_to_scale'] - tier_movement_df['scale_to_enterprise']
)
tier_movement_df['net_enterprise'] = (
    tier_movement_df['active_enterprise'] + tier_movement_df['scale_to_enterprise']
)

print(f"Tier upgrade model created for {len(upgrade_df)} months")
print(f"\nTotal upgrades over 60 months:")
print(f"  Starter → Growth: {int(upgrade_df['starter_to_growth'].sum()):,}")
print(f"  Growth → Scale: {int(upgrade_df['growth_to_scale'].sum()):,}")
print(f"  Scale → Enterprise: {int(upgrade_df['scale_to_enterprise'].sum()):,}")