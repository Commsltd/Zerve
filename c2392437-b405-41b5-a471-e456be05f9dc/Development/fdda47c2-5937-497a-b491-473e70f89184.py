"""
Consolidated Commercial Assumptions Dashboard
Combines all foundational assumptions into a single parameterized structure
"""

import json

# Combine all assumption modules
consolidated_assumptions = {
    'tier_pricing': tier_pricing,
    'token_economics': token_economics,
    'customer_density': customer_density,
    'gtm_phases': gtm_phases,
    'geographic_expansion': geographic_expansion,
    'conversion_funnels': conversion_funnels,
    'churn_rates': churn_rates,
    'cac_by_channel': cac_by_channel,
    'network_effects': network_effects,
    'metadata': {
        'version': '1.0',
        'created_date': '2025-01-13',
        'description': 'Comprehensive commercial assumptions for SaaS financial model',
        'source_schema': 'Commercial assumptions schema v1',
        'ready_for_downstream': True
    }
}

# Summary statistics
summary_stats = {
    'total_assumption_categories': len(consolidated_assumptions) - 1,  # Exclude metadata
    'pricing_tiers': len(tier_pricing),
    'customer_segments': len(customer_density),
    'gtm_phases': len(gtm_phases),
    'geographic_markets': len(geographic_expansion),
    'conversion_pathways': len([k for k in conversion_funnels.keys() if 'segment' not in k]),
    'cac_channels': len(cac_by_channel)
}

print("=" * 60)
print("CONSOLIDATED COMMERCIAL ASSUMPTIONS DASHBOARD")
print("=" * 60)
print(f"\nVersion: {consolidated_assumptions['metadata']['version']}")
print(f"Status: Ready for downstream revenue modeling")
print(f"\nTotal Assumption Categories: {summary_stats['total_assumption_categories']}")
print(f"  • Pricing Tiers: {summary_stats['pricing_tiers']}")
print(f"  • Customer Segments: {summary_stats['customer_segments']}")
print(f"  • GTM Phases: {summary_stats['gtm_phases']}")
print(f"  • Geographic Markets: {summary_stats['geographic_markets']}")
print(f"  • Conversion Pathways: {summary_stats['conversion_pathways']}")
print(f"  • CAC Channels: {summary_stats['cac_channels']}")
print("\n" + "=" * 60)