"""
Calculate Token Overage by Tier
Determines monthly overage tokens and revenue based on consumption vs allocation
"""
import pandas as pd

# Token overage pricing
overage_rate_gbp = 1.50  # £1.50 per overage token

# Calculate overage for each tier based on typical consumption
tier_overage_analysis = {}

for _tier, _tier_info in tier_segment_mapping.items():
    _included = _tier_info['included_tokens']
    _segments = _tier_info['segment_split']
    
    # Calculate weighted average consumption for this tier
    _weighted_consumption = 0
    for _seg, _weight in _segments.items():
        _seg_consumption = consumption_by_segment[_seg]['total_monthly_tokens']
        _weighted_consumption += _seg_consumption * _weight
    
    # Calculate overage
    _overage_tokens = max(0, _weighted_consumption - _included)
    _overage_revenue = _overage_tokens * overage_rate_gbp
    
    tier_overage_analysis[_tier] = {
        'included_tokens': _included,
        'avg_consumption': _weighted_consumption,
        'overage_tokens': _overage_tokens,
        'overage_revenue_gbp': _overage_revenue,
        'total_token_cost_gbp': _tier_info['monthly_price_gbp'] + _overage_revenue,
        'effective_token_price': (_tier_info['monthly_price_gbp'] + _overage_revenue) / _weighted_consumption if _weighted_consumption > 0 else 0
    }

overage_df = pd.DataFrame.from_dict(tier_overage_analysis, orient='index')

print("Token Overage Analysis by Tier")
print("="*70)
for _tier in overage_df.index:
    _row = overage_df.loc[_tier]
    print(f"\n{_tier}:")
    print(f"  Included: {_row['included_tokens']:.0f} tokens")
    print(f"  Avg Consumption: {_row['avg_consumption']:.0f} tokens/month")
    print(f"  Overage: {_row['overage_tokens']:.0f} tokens @ £{overage_rate_gbp:.2f}/token")
    print(f"  Overage Revenue: £{_row['overage_revenue_gbp']:.2f}/month")
    print(f"  Effective Token Price: £{_row['effective_token_price']:.3f}/token")