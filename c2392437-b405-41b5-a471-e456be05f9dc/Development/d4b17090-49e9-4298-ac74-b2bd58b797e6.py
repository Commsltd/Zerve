"""
Calculation Engine: Customer Acquisition by Tier
Calculates new customer additions by tier and month
"""
import pandas as pd
import numpy as np

# Define GTM phases
def get_gtm_phase(month_num):
    if month_num <= 6:
        return 'stealth'
    elif month_num <= 18:
        return 'beta'
    else:
        return 'launch'

# Calculate geographic multiplier
def get_geo_multiplier(month_num):
    multiplier = calc_regional_expansion['multipliers']['uk']
    if month_num >= calc_regional_expansion['timing']['eu']:
        multiplier += calc_regional_expansion['multipliers']['eu'] - 1.0
    if month_num >= calc_regional_expansion['timing']['us']:
        multiplier += calc_regional_expansion['multipliers']['us'] - 1.0
    if month_num >= calc_regional_expansion['timing']['apac']:
        multiplier += calc_regional_expansion['multipliers']['apac'] - 1.0
    return multiplier

# Customer acquisition model
calc_acquisition_records = []

for _, row in calc_timeline.iterrows():
    month_num = row['month']
    gtm_phase = get_gtm_phase(month_num)
    
    # Base acquisition by phase
    if gtm_phase == 'stealth':
        base_starter = 20 * (1 + month_num * 0.1)
        base_growth = 0
        base_scale = 0
        base_enterprise = 0
    elif gtm_phase == 'beta':
        months_in_beta = month_num - 6
        base_starter = 40 + months_in_beta * 3
        base_growth = 10 + months_in_beta * 1.5
        base_scale = 2 + months_in_beta * 0.3
        base_enterprise = 0
    else:  # launch
        months_in_launch = month_num - 18
        growth_factor = 1 + (months_in_launch / 42) * 2
        base_starter = 60 * growth_factor
        base_growth = 25 * growth_factor
        base_scale = 8 * growth_factor
        base_enterprise = 2 * growth_factor
    
    # Apply geographic multiplier
    geo_mult = get_geo_multiplier(month_num)
    
    calc_acquisition_records.append({
        'month': month_num,
        'gtm_phase': gtm_phase,
        'geo_multiplier': geo_mult,
        'new_starter': int(base_starter * geo_mult),
        'new_growth': int(base_growth * geo_mult),
        'new_scale': int(base_scale * geo_mult),
        'new_enterprise': int(base_enterprise * geo_mult)
    })

calc_acquisition_df = pd.DataFrame(calc_acquisition_records)

print(f"✓ Customer Acquisition Calculated: {len(calc_acquisition_df)} months")
print(f"  Total New Customers: {calc_acquisition_df[['new_starter', 'new_growth', 'new_scale', 'new_enterprise']].sum().sum():,}")
print(f"  By Tier: Starter={calc_acquisition_df['new_starter'].sum():,}, Growth={calc_acquisition_df['new_growth'].sum():,}, Scale={calc_acquisition_df['new_scale'].sum():,}, Enterprise={calc_acquisition_df['new_enterprise'].sum():,}")