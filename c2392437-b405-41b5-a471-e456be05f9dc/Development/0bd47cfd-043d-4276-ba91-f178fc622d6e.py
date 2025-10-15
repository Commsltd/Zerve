"""
Contract Economics - Size Distribution and Structure
Models 20/60/20 split across contract size ranges
"""

import pandas as pd
import numpy as np

# Contract size distribution: 20% at min, 60% at mid, 20% at max
# Based on enterprise segment contract ranges
contract_distribution_weights = {
    'min': 0.20,  # 20% of deals at minimum
    'mid': 0.60,  # 60% of deals at midpoint  
    'max': 0.20   # 20% of deals at maximum
}

# Segment contract ranges (from enterprise_segments)
segment_contract_ranges = {
    'trade_credit_insurers': {'min': 150000, 'mid': 325000, 'max': 500000},
    'mnc_supply_chain': {'min': 50000, 'mid': 150000, 'max': 250000},
    'banks_payment_processors': {'min': 100000, 'mid': 250000, 'max': 400000},
    'reinsurers_auditors': {'min': 75000, 'mid': 137500, 'max': 200000}
}

# Calculate weighted average contract value (ACV) by segment
segment_acv_list = []
for seg_name, ranges in segment_contract_ranges.items():
    weighted_acv = (
        ranges['min'] * contract_distribution_weights['min'] +
        ranges['mid'] * contract_distribution_weights['mid'] +
        ranges['max'] * contract_distribution_weights['max']
    )
    
    segment_acv_list.append({
        'segment': seg_name,
        'min_contract_gbp': ranges['min'],
        'mid_contract_gbp': ranges['mid'],
        'max_contract_gbp': ranges['max'],
        'weighted_acv_gbp': weighted_acv,
        'distribution': '20% min / 60% mid / 20% max'
    })

segment_acv_df = pd.DataFrame(segment_acv_list)

# Contract terms and structure
contract_terms_structure = {
    'initial_term_months': 12,  # Annual contracts
    'renewal_rate': 0.92,  # 92% institutional renewal rate
    'logo_churn': 0.08,  # 8% annual logo churn
    'upsell_expansion_rate': 0.15,  # 15% annual upsell/expansion
    'payment_terms': 'Annual upfront or quarterly',
    'typical_structure': 'Annual licensing fee + API call limits + data refresh frequency tiers'
}

print("=" * 80)
print("CONTRACT ECONOMICS - SIZE DISTRIBUTION & STRUCTURE")
print("=" * 80)
print("\nContract Size Distribution Model: 20/60/20 Split")
print(f"  • 20% of deals at minimum contract size")
print(f"  • 60% of deals at midpoint contract size")
print(f"  • 20% of deals at maximum contract size")
print(f"\nWeighted Average ACV by Segment:")
for _idx, row in segment_acv_df.iterrows():
    print(f"  • {row['segment']}: £{row['weighted_acv_gbp']:,.0f}")
print(f"\nOverall Portfolio Average ACV: £{segment_acv_df['weighted_acv_gbp'].mean():,.0f}")
print(f"\nContract Terms:")
print(f"  • Initial Term: {contract_terms_structure['initial_term_months']} months (annual)")
print(f"  • Renewal Rate: {contract_terms_structure['renewal_rate']:.0%}")
print(f"  • Logo Churn: {contract_terms_structure['logo_churn']:.0%}")
print(f"  • Upsell/Expansion: {contract_terms_structure['upsell_expansion_rate']:.0%} annually")
print("=" * 80)