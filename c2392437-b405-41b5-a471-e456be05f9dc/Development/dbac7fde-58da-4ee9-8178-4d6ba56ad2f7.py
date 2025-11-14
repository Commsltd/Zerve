"""
Conversion Funnels by Segment and Phase
Source: Schema conversion metrics - tier upgrade rates and timing by segment
"""

conversion_funnels = {
    'free_to_starter': {
        'conversion_rate': 0.12,  # 12% conversion from free to Starter
        'avg_lag_months': 2,  # Average time to convert
        'description': 'Initial paid conversion - trial to first purchase',
        'key_drivers': ['Value demonstration', 'Usage threshold', 'Pain point validation']
    },
    'starter_to_growth': {
        'conversion_rate': 0.18,  # 18% conversion from Starter to Growth
        'avg_lag_months': 6,  # Average time to upgrade
        'description': 'First upsell - expanding usage and value',
        'key_drivers': ['Token usage patterns', 'Feature needs', 'Team expansion']
    },
    'growth_to_scale': {
        'conversion_rate': 0.09,  # 9% conversion from Growth to Scale
        'avg_lag_months': 9,  # Average time to upgrade
        'description': 'High-value conversion - enterprise adoption',
        'key_drivers': ['Volume requirements', 'Multi-team deployment', 'ROI validation']
    },
    'scale_to_enterprise': {
        'conversion_rate': 0.04,  # 4% conversion from Scale to Enterprise
        'avg_lag_months': 9,  # Average time to upgrade (can overlap with Growth→Scale)
        'description': 'Enterprise deal - custom solutions and strategic partnerships',
        'key_drivers': ['Custom requirements', 'Integration needs', 'Strategic value']
    },
    'segment_variations': {
        'micro_small': {
            'free_to_starter_boost': 1.2,  # 20% higher conversion for smaller companies
            'description': 'SMBs convert faster at entry level'
        },
        'large_mnc': {
            'growth_to_scale_boost': 1.5,  # 50% higher conversion for larger companies
            'scale_to_enterprise_boost': 2.0,  # 100% higher conversion to Enterprise
            'description': 'Enterprises more likely to upgrade to higher tiers'
        }
    }
}

print("Conversion Funnel Model Defined")
print("\nConversion Rates by Tier Transition:")
for _funnel_name, funnel_data in conversion_funnels.items():
    if _funnel_name != 'segment_variations' and 'conversion_rate' in funnel_data:
        rate = funnel_data['conversion_rate'] * 100
        lag = funnel_data['avg_lag_months']
        print(f"  {_funnel_name}: {rate}% conversion, {lag} month lag")