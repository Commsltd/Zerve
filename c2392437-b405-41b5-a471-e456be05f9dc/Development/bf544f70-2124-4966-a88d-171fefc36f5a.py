"""
Extract Baseline Token Model Parameters
Identifies key baseline parameters from token consumption and pricing model
"""

# Extract token model baseline parameters
baseline_token_model = {
    'consumption_patterns': {
        'micro': {'monthly_tokens': 44, 'customers_per_account': 25},
        'small': {'monthly_tokens': 63, 'customers_per_account': 35},
        'medium': {'monthly_tokens': 362, 'customers_per_account': 210},
        'large': {'monthly_tokens': 1600, 'customers_per_account': 1325},
        'mnc': {'monthly_tokens': 27605, 'customers_per_account': 23000}
    },
    'tier_segment_mapping': {
        'Starter': 'micro',
        'Growth': 'small',
        'Scale': 'medium',
        'Enterprise': 'large/mnc'
    },
    'overage_pricing': {
        'overage_rate_gbp': 1.50,  # £1.50 per token over allocation
        'overage_expectations': {
            'Starter': 0.10,  # 10% of customers exceed allocation
            'Growth': 0.12,   # 12%
            'Scale': 0.15,    # 15%
            'Enterprise': 0.20  # 20%
        }
    },
    'payg_pricing': {
        'payg_rate_gbp': 2.00,  # £2.00 per token
        'customer_profile': {
            'sporadic_users': {'avg_monthly_tokens': 85, 'customers_y5': 500},
            'trial_users': {'avg_monthly_tokens': 15, 'customers_y5': 1200}
        }
    },
    'network_velocity_multiplier': {
        'Y1': 1.0,
        'Y2': 1.2,
        'Y3': 1.4,
        'Y4': 1.6,
        'Y5': 1.8
    },
    'contributor_rewards': {
        'data_contribution_rate_gbp': 0.50,  # £0.50 per validated contribution
        'participation_rate': 0.45  # 45% of customers contribute data
    }
}

print("Baseline Token Model Parameters Extracted")
print(f"\nConsumption by Segment (monthly tokens):")
for _token_segment, _token_info in baseline_token_model['consumption_patterns'].items():
    print(f"  {_token_segment}: {_token_info['monthly_tokens']} tokens ({_token_info['customers_per_account']} customers/account)")

print(f"\nOverage Pricing:")
print(f"  Rate: £{baseline_token_model['overage_pricing']['overage_rate_gbp']:.2f} per token")

print(f"\nPay-As-You-Go Pricing:")
print(f"  Rate: £{baseline_token_model['payg_pricing']['payg_rate_gbp']:.2f} per token")

print(f"\nNetwork Velocity Multiplier:")
for _token_year, _token_multiplier in baseline_token_model['network_velocity_multiplier'].items():
    print(f"  {_token_year}: {_token_multiplier}x")

print(f"\nContributor Rewards:")
print(f"  Contribution Rate: £{baseline_token_model['contributor_rewards']['data_contribution_rate_gbp']:.2f} per contribution")
print(f"  Participation Rate: {baseline_token_model['contributor_rewards']['participation_rate']:.0%}")