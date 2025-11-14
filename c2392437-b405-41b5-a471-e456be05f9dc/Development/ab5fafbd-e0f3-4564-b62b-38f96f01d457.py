"""
Interactive Parameter Input: Pricing Tiers
Defines the monthly prices and token allocations for all subscription tiers
"""

# Pricing Tier Parameters (Monthly Prices in GBP)
input_starter_price = 495
input_growth_price = 1895
input_scale_price = 4950
input_enterprise_price = 15000

# Token Allocations per Tier
input_starter_tokens = 300
input_growth_tokens = 1250
input_scale_tokens = 5000
input_enterprise_tokens_custom = True  # Enterprise has custom allocations

# Package all pricing parameters
pricing_tier_inputs = {
    'Starter': {
        'monthly_price_gbp': input_starter_price,
        'included_tokens': input_starter_tokens
    },
    'Growth': {
        'monthly_price_gbp': input_growth_price,
        'included_tokens': input_growth_tokens
    },
    'Scale': {
        'monthly_price_gbp': input_scale_price,
        'included_tokens': input_scale_tokens
    },
    'Enterprise': {
        'monthly_price_gbp': input_enterprise_price,
        'included_tokens': 'custom' if input_enterprise_tokens_custom else 20000
    }
}

print("✓ Pricing Tier Inputs Configured")
print(f"  Starter: £{input_starter_price}/mo, {input_starter_tokens} tokens")
print(f"  Growth: £{input_growth_price}/mo, {input_growth_tokens} tokens")
print(f"  Scale: £{input_scale_price}/mo, {input_scale_tokens} tokens")
print(f"  Enterprise: £{input_enterprise_price}/mo, custom tokens")