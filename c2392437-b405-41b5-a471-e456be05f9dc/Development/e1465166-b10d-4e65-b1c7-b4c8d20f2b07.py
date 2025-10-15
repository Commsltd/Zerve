"""
Map Customer Segments to Subscription Tiers
Defines typical tier distribution across segments
"""

# Tier mapping: which segments typically use which tiers
# Based on token consumption needs vs included allowances
tier_segment_mapping = {
    'Starter': {
        'primary_segments': ['micro', 'small'],
        'included_tokens': 300,
        'monthly_price_gbp': 495,
        'segment_split': {'micro': 0.65, 'small': 0.35}  # % of Starter tier customers
    },
    'Growth': {
        'primary_segments': ['small', 'medium'],
        'included_tokens': 1250,
        'monthly_price_gbp': 1895,
        'segment_split': {'small': 0.40, 'medium': 0.60}
    },
    'Scale': {
        'primary_segments': ['medium', 'large'],
        'included_tokens': 5000,
        'monthly_price_gbp': 4950,
        'segment_split': {'medium': 0.30, 'large': 0.70}
    },
    'Enterprise': {
        'primary_segments': ['large', 'mnc'],
        'included_tokens': 20000,  # Custom, using 20k as baseline
        'monthly_price_gbp': 15000,
        'segment_split': {'large': 0.45, 'mnc': 0.55}
    }
}

print("Tier → Segment Mapping")
print("="*60)
for _tier_name, _tier_map in tier_segment_mapping.items():
    print(f"\n{_tier_name}: £{_tier_map['monthly_price_gbp']:,}/mo ({_tier_map['included_tokens']} tokens)")
    print(f"  Primary segments: {', '.join(_tier_map['primary_segments'])}")
    for _seg, _pct in _tier_map['segment_split'].items():
        print(f"    {_seg}: {_pct:.0%}")