"""
Extract Baseline Subscription Metrics
Identifies key baseline parameters from subscription revenue model
"""
import pandas as pd

# Extract subscription baseline metrics from loaded data
baseline_subscription = {
    'tier_pricing': {
        'Starter': 495,
        'Growth': 1895,
        'Scale': 4950,
        'Enterprise': 15000
    },
    'token_allocations': {
        'Starter': 300,
        'Growth': 1250,
        'Scale': 5000,
        'Enterprise': 'custom'
    },
    'churn_rates_monthly': {
        'Starter': 0.012,  # 1.2% monthly
        'Growth': 0.008,   # 0.8% monthly
        'Scale': 0.006,    # 0.6% monthly
        'Enterprise': 0.006  # 0.6% monthly
    }
}

# Extract Year 5 metrics from annual data
if 'annual_df' in dir():
    y5_arr = annual_df[annual_df['year'] == 5]['total_arr'].values[0]
    baseline_subscription['year_5_arr'] = y5_arr
    print(f"Year 5 Target ARR: £{y5_arr:,.2f}")

print("Baseline Subscription Metrics Extracted")
print(f"\nTier Pricing (GBP/month):")
for tier_name, price in baseline_subscription['tier_pricing'].items():
    print(f"  {tier_name}: £{price:,}")

print(f"\nMonthly Churn Rates:")
for tier_name, churn in baseline_subscription['churn_rates_monthly'].items():
    print(f"  {tier_name}: {churn:.2%}")