"""
Monthly Churn Rates by Tier
Source: Schema retention metrics - expected monthly churn by subscription tier
"""

churn_rates = {
    'starter': {
        'monthly_churn_rate': 0.035,  # 3.5% monthly churn
        'annual_retention': 0.66,  # ~66% annual retention
        'description': 'Higher churn due to experimentation and budget constraints',
        'churn_drivers': ['Budget sensitivity', 'Unclear value realization', 'Limited usage']
    },
    'growth': {
        'monthly_churn_rate': 0.022,  # 2.2% monthly churn
        'annual_retention': 0.77,  # ~77% annual retention
        'description': 'Moderate churn as customers establish value',
        'churn_drivers': ['Product fit', 'Competitive alternatives', 'Business changes']
    },
    'scale': {
        'monthly_churn_rate': 0.011,  # 1.1% monthly churn
        'annual_retention': 0.88,  # ~88% annual retention
        'description': 'Low churn with high switching costs and deep integration',
        'churn_drivers': ['Strategic pivots', 'M&A activity', 'Rare dissatisfaction']
    },
    'enterprise': {
        'monthly_churn_rate': 0.006,  # 0.6% monthly churn
        'annual_retention': 0.93,  # ~93% annual retention
        'description': 'Very low churn with long-term contracts and strategic relationships',
        'churn_drivers': ['Contract renewals', 'Major org changes', 'Very rare']
    }
}

print("Churn Rate Model Defined")
print("\nMonthly Churn Rates by Tier:")
for _churn_tier, _churn_details in churn_rates.items():
    _monthly_rate = _churn_details['monthly_churn_rate'] * 100
    _annual_retention = _churn_details['annual_retention'] * 100
    print(f"  {_churn_tier.capitalize()}: {_monthly_rate}% monthly churn, {_annual_retention:.0f}% annual retention")