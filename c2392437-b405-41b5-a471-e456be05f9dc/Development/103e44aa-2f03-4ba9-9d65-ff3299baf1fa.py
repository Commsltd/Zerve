"""
Interactive Parameter Input: Churn Rates by Tier
Defines the monthly churn rates for each subscription tier
"""

# Monthly Churn Rates by Tier (as decimal percentages)
input_churn_starter = 0.035  # 3.5% monthly
input_churn_growth = 0.022   # 2.2% monthly
input_churn_scale = 0.011    # 1.1% monthly
input_churn_enterprise = 0.006  # 0.6% monthly

# Package all churn rate parameters
churn_rate_inputs = {
    'starter': {
        'monthly_churn_rate': input_churn_starter,
        'annual_retention': round(1 - (1 - input_churn_starter)**12, 2)
    },
    'growth': {
        'monthly_churn_rate': input_churn_growth,
        'annual_retention': round(1 - (1 - input_churn_growth)**12, 2)
    },
    'scale': {
        'monthly_churn_rate': input_churn_scale,
        'annual_retention': round(1 - (1 - input_churn_scale)**12, 2)
    },
    'enterprise': {
        'monthly_churn_rate': input_churn_enterprise,
        'annual_retention': round(1 - (1 - input_churn_enterprise)**12, 2)
    }
}

print("✓ Churn Rate Inputs Configured")
print(f"  Starter: {input_churn_starter:.1%}/month")
print(f"  Growth: {input_churn_growth:.1%}/month")
print(f"  Scale: {input_churn_scale:.1%}/month")
print(f"  Enterprise: {input_churn_enterprise:.1%}/month")