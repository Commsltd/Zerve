"""
PAYG (Pay-As-You-Go) Token Revenue Model
Models customers purchasing tokens without subscription
"""
import pandas as pd

# PAYG pricing
payg_rate_gbp = 2.00  # £2.00 per token

# PAYG customer assumptions
# Assume 20% of micro and 10% of small customers use PAYG instead of subscription
payg_customer_profile = {
    'micro_payg': {
        'segment': 'micro',
        'avg_monthly_tokens': 150,  # Lower usage than subscription customers
        'seasonality_factor': 0.85,  # More sporadic usage
    },
    'small_payg': {
        'segment': 'small',
        'avg_monthly_tokens': 220,
        'seasonality_factor': 0.90,
    }
}

payg_revenue_model = {}

for _profile_name, _profile in payg_customer_profile.items():
    _tokens = _profile['avg_monthly_tokens']
    _seasonal = _profile['seasonality_factor']
    _effective_tokens = _tokens * _seasonal
    
    payg_revenue_model[_profile_name] = {
        'segment': _profile['segment'],
        'base_monthly_tokens': _tokens,
        'seasonality_factor': _seasonal,
        'effective_monthly_tokens': _effective_tokens,
        'monthly_revenue_per_customer': _effective_tokens * payg_rate_gbp,
        'annual_revenue_per_customer': _effective_tokens * payg_rate_gbp * 12
    }

payg_df = pd.DataFrame.from_dict(payg_revenue_model, orient='index')

print("PAYG Token Revenue Model")
print("="*60)
print(f"PAYG Rate: £{payg_rate_gbp:.2f}/token")
print("\nPer Customer Economics:")
for _profile in payg_df.index:
    _row = payg_df.loc[_profile]
    print(f"\n{_profile.replace('_', ' ').title()} ({_row['segment']} segment):")
    print(f"  Monthly tokens: {_row['effective_monthly_tokens']:.0f} tokens")
    print(f"  Monthly revenue: £{_row['monthly_revenue_per_customer']:.2f}")
    print(f"  Annual revenue: £{_row['annual_revenue_per_customer']:.2f}")