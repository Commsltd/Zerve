"""
Enterprise B2B Data Licensing - Customer Segment Definitions
Models 4 institutional customer segments with GTM timing, win rates, and sales cycles
"""

import pandas as pd

# Define the 4 institutional customer segments for B2B data licensing
enterprise_segments = {
    'trade_credit_insurers': {
        'description': 'Trade credit insurers licensing RTCI feeds and risk scores for underwriting',
        'examples': ['Euler Hermes', 'Coface', 'Atradius'],
        'contract_size_gbp': {
            'min': 150000,
            'mid': 325000,  # Midpoint
            'max': 500000
        },
        'gtm_timing': 'Y1-Y2',
        'win_rate': 0.30,
        'sales_cycle_months': 12,
        'use_cases': ['RTCI feed licensing', 'Company risk scoring', 'Underwriting workflows', 'Portfolio monitoring']
    },
    'mnc_supply_chain': {
        'description': 'MNCs and supply chain finance providers licensing real-time debtor intelligence APIs',
        'examples': ['Large corporates', 'SCF providers', 'Working capital platforms'],
        'contract_size_gbp': {
            'min': 50000,
            'mid': 150000,
            'max': 250000
        },
        'gtm_timing': 'Y2-Y3',
        'win_rate': 0.22,
        'sales_cycle_months': 9,
        'use_cases': ['Debtor intelligence APIs', 'Supply chain risk monitoring', 'Working capital optimization', 'Supplier/buyer risk']
    },
    'banks_payment_processors': {
        'description': 'Banks and payment processors integrating PayGauge scoring for credit decisioning',
        'examples': ['Commercial banks', 'Fintech lenders', 'Payment processors', 'Credit decisioning platforms'],
        'contract_size_gbp': {
            'min': 100000,
            'mid': 250000,
            'max': 400000
        },
        'gtm_timing': 'Y3-Y4',
        'win_rate': 0.18,
        'sales_cycle_months': 18,
        'use_cases': ['PayGauge credit scoring integration', 'Credit decisioning engines', 'SME lending workflows', 'Payment risk assessment']
    },
    'reinsurers_auditors': {
        'description': 'Reinsurers and auditors purchasing aggregated sector risk analytics and RTCI feeds',
        'examples': ['Reinsurance companies', 'Big 4 auditors', 'Risk advisory firms', 'Credit rating agencies'],
        'contract_size_gbp': {
            'min': 75000,
            'mid': 137500,
            'max': 200000
        },
        'gtm_timing': 'Y2-Y3',
        'win_rate': 0.25,
        'sales_cycle_months': 6,
        'use_cases': ['Sector risk analytics', 'RTCI data feeds', 'Portfolio exposure analysis', 'Audit data validation']
    }
}

# Convert to DataFrame for easier analysis
segment_summary_df = pd.DataFrame([
    {
        'segment': seg_name,
        'description': seg_data['description'],
        'min_contract_gbp': seg_data['contract_size_gbp']['min'],
        'mid_contract_gbp': seg_data['contract_size_gbp']['mid'],
        'max_contract_gbp': seg_data['contract_size_gbp']['max'],
        'gtm_timing': seg_data['gtm_timing'],
        'win_rate': seg_data['win_rate'],
        'sales_cycle_months': seg_data['sales_cycle_months']
    }
    for seg_name, seg_data in enterprise_segments.items()
])

print("=" * 80)
print("ENTERPRISE B2B DATA LICENSING - CUSTOMER SEGMENTS")
print("=" * 80)
print(f"\nTotal Segments: {len(enterprise_segments)}")
print(f"\nContract Size Range: £{segment_summary_df['min_contract_gbp'].min():,} - £{segment_summary_df['max_contract_gbp'].max():,}")
print(f"Average Mid-Point Contract: £{segment_summary_df['mid_contract_gbp'].mean():,.0f}")
print(f"Average Win Rate: {segment_summary_df['win_rate'].mean():.1%}")
print(f"Average Sales Cycle: {segment_summary_df['sales_cycle_months'].mean():.1f} months")
print("\n" + "=" * 80)