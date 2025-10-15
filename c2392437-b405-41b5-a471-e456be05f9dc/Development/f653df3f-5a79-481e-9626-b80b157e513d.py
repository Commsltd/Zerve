import pandas as pd
import numpy as np

# Calculate Lifetime Value (LTV) by tier
# LTV = ARPU * (1 / churn_rate) * gross_margin

# Assume 85% gross margin for SaaS
gross_margin = 0.85

ltv_by_tier = {}

for tier_name, tier_info in tier_pricing.items():
    monthly_price = tier_info['monthly_price_gbp']
    churn_rate_monthly = churn_rates[tier_name.lower()]['monthly_churn_rate']
    
    # LTV = Monthly Price * Gross Margin / Monthly Churn
    ltv = (monthly_price * gross_margin) / churn_rate_monthly
    
    ltv_by_tier[tier_name] = {
        'monthly_price': monthly_price,
        'monthly_churn': churn_rate_monthly,
        'annual_retention': churn_rates[tier_name.lower()]['annual_retention'],
        'ltv_gbp': ltv,
        'gross_margin': gross_margin
    }

# Calculate weighted average LTV based on Year 5 customer mix
y5_customers = tier_movement_df[tier_movement_df['month'] == 60].iloc[0]
total_y5_customers = (
    y5_customers['net_starter'] + 
    y5_customers['net_growth'] + 
    y5_customers['net_scale'] + 
    y5_customers['net_enterprise']
)

weighted_ltv = (
    (y5_customers['net_starter'] / total_y5_customers * ltv_by_tier['Starter']['ltv_gbp']) +
    (y5_customers['net_growth'] / total_y5_customers * ltv_by_tier['Growth']['ltv_gbp']) +
    (y5_customers['net_scale'] / total_y5_customers * ltv_by_tier['Scale']['ltv_gbp']) +
    (y5_customers['net_enterprise'] / total_y5_customers * ltv_by_tier['Enterprise']['ltv_gbp'])
)

print("Lifetime Value (LTV) by Tier:")
print("=" * 60)
for tier_name, tier_data in ltv_by_tier.items():
    print(f"\n{tier_name}:")
    print(f"  Monthly Price: £{tier_data['monthly_price']:,.0f}")
    print(f"  Monthly Churn: {tier_data['monthly_churn']:.1%}")
    print(f"  Annual Retention: {tier_data['annual_retention']:.1%}")
    print(f"  LTV: £{tier_data['ltv_gbp']:,.0f}")

print(f"\n{'='*60}")
print(f"Weighted Average LTV (Year 5 mix): £{weighted_ltv:,.0f}")