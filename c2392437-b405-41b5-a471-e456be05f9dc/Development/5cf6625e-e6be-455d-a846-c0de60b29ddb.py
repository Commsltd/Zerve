"""
Tier Pricing Structure
Source: Schema commercial assumptions - pricing tiers and token allocations
"""

tier_pricing = {
    'Starter': {
        'monthly_price_gbp': 495,
        'included_tokens': 300,
        'target_segment': 'Micro/Small businesses testing platform',
        'description': 'Entry tier for companies exploring platform capabilities'
    },
    'Growth': {
        'monthly_price_gbp': 1895,
        'included_tokens': 1250,
        'target_segment': 'Small/Medium businesses with active usage',
        'description': 'Mid-tier for scaling operations'
    },
    'Scale': {
        'monthly_price_gbp': 4950,
        'included_tokens': 5000,
        'target_segment': 'Large enterprises with significant volume',
        'description': 'High-volume tier for established users'
    },
    'Enterprise': {
        'monthly_price_gbp': 15000,  # Base price, customizable
        'included_tokens': 'custom',
        'target_segment': 'MNC/Complex organizations',
        'description': 'Custom pricing with dedicated support and tailored solutions'
    }
}

print("Tier Pricing Structure Defined")
print(f"Number of tiers: {len(tier_pricing)}")
for _pricing_tier, _tier_details in tier_pricing.items():
    _price = _tier_details['monthly_price_gbp']
    _tokens = _tier_details['included_tokens']
    print(f"  {_pricing_tier}: £{_price:,}/month, {_tokens} tokens")