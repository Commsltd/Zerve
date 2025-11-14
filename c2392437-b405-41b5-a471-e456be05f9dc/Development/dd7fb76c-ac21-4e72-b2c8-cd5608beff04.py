import pandas as pd
import numpy as np

# Create customer acquisition model by tier and month
# Based on GTM phases, conversion funnels, and time lags

acquisition_records = []

for _, month_row in timeline_df.iterrows():
    month_num = month_row['month']
    phase = month_row['gtm_phase']
    
    # Define target new customers per phase per month
    if phase == 'stealth':
        # 120 accounts over 6 months
        new_starters = 20 * (1 + month_num * 0.1)  # Ramp up
        new_growth = 0
        new_scale = 0
        new_enterprise = 0
    elif phase == 'beta':
        # 850 accounts over 12 months (months 7-18)
        months_in_beta = month_num - 6
        new_starters = 40 + months_in_beta * 3
        new_growth = 10 + months_in_beta * 1.5
        new_scale = 2 + months_in_beta * 0.3
        new_enterprise = 0
    else:  # launch
        # Scale to 4200 total by month 60
        months_in_launch = month_num - 18
        # Accelerating growth pattern
        growth_factor = 1 + (months_in_launch / 42) * 2
        new_starters = 60 * growth_factor
        new_growth = 25 * growth_factor
        new_scale = 8 * growth_factor
        new_enterprise = 2 * growth_factor
    
    acquisition_records.append({
        'month': month_num,
        'gtm_phase': phase,
        'new_starter': int(new_starters),
        'new_growth': int(new_growth),
        'new_scale': int(new_scale),
        'new_enterprise': int(new_enterprise)
    })

acquisition_df = pd.DataFrame(acquisition_records)

# Calculate geographic multipliers
acquisition_df['geo_multiplier'] = acquisition_df['month'].apply(
    lambda m: 1.0 if m < 13 else 
              (1.0 + geographic_expansion['eu']['market_size_multiplier']) if m < 25 else
              (1.0 + geographic_expansion['eu']['market_size_multiplier'] + geographic_expansion['us']['market_size_multiplier']) if m < 37 else
              (1.0 + geographic_expansion['eu']['market_size_multiplier'] + geographic_expansion['us']['market_size_multiplier'] + geographic_expansion['apac']['market_size_multiplier'])
)

# Apply geographic multipliers
for tier_col in ['new_starter', 'new_growth', 'new_scale', 'new_enterprise']:
    acquisition_df[tier_col] = (acquisition_df[tier_col] * acquisition_df['geo_multiplier']).astype(int)

print(f"Acquisition model created: {len(acquisition_df)} months")
print(f"\nTotal new customers by tier over 60 months:")
print(f"  Starter: {acquisition_df['new_starter'].sum():,}")
print(f"  Growth: {acquisition_df['new_growth'].sum():,}")
print(f"  Scale: {acquisition_df['new_scale'].sum():,}")
print(f"  Enterprise: {acquisition_df['new_enterprise'].sum():,}")