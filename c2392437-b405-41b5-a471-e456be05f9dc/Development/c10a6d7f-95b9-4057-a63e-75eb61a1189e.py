"""
Extract Baseline Enterprise Licensing Parameters
Identifies key baseline parameters from enterprise B2B licensing model
"""

# Extract enterprise licensing baseline parameters
baseline_enterprise_licensing = {
    'customer_segments': {
        'trade_credit_insurers': {
            'contract_size_range': (150000, 500000),
            'midpoint': 325000,
            'win_rate': 0.30,
            'sales_cycle_months': 12,
            'gtm_timing': 'Y1-Y2'
        },
        'mnc_supply_chain': {
            'contract_size_range': (50000, 250000),
            'midpoint': 150000,
            'win_rate': 0.22,
            'sales_cycle_months': 9,
            'gtm_timing': 'Y2-Y3'
        },
        'banks_payment_processors': {
            'contract_size_range': (100000, 400000),
            'midpoint': 250000,
            'win_rate': 0.18,
            'sales_cycle_months': 18,
            'gtm_timing': 'Y3-Y4'
        },
        'reinsurers_auditors': {
            'contract_size_range': (75000, 200000),
            'midpoint': 137500,
            'win_rate': 0.25,
            'sales_cycle_months': 6,
            'gtm_timing': 'Y2-Y3'
        }
    },
    'strategic_partners': {
        'credit_bureau': {'baseline_acv': 100000, 'y4_potential': 500000},
        'erp_platform': {'baseline_acv': 75000, 'y4_potential': 300000},
        'insurance_consortium': {'baseline_acv': 250000, 'y4_potential': 1000000},
        'fintech_aggregator': {'baseline_acv': 25000, 'y4_potential': 150000}
    },
    'contract_economics': {
        'annual_renewal_rate': 0.92,  # 92% annual renewal
        'monthly_churn': 0.006924,  # ~0.7% monthly
        'annual_expansion': 0.15  # 15% annual expansion/upsell
    }
}

print("Baseline Enterprise Licensing Parameters Extracted")
print(f"\nCustomer Segments:")
for _ent_segment, _ent_params in baseline_enterprise_licensing['customer_segments'].items():
    print(f"\n  {_ent_segment}:")
    print(f"    Contract Range: £{_ent_params['contract_size_range'][0]:,} - £{_ent_params['contract_size_range'][1]:,}")
    print(f"    Midpoint: £{_ent_params['midpoint']:,}")
    print(f"    Win Rate: {_ent_params['win_rate']:.0%}")
    print(f"    Sales Cycle: {_ent_params['sales_cycle_months']} months")
    print(f"    GTM Timing: {_ent_params['gtm_timing']}")

print(f"\nStrategic Partners:")
for _ent_partner, _ent_details in baseline_enterprise_licensing['strategic_partners'].items():
    print(f"  {_ent_partner}: £{_ent_details['baseline_acv']:,} → £{_ent_details['y4_potential']:,}")

print(f"\nContract Economics:")
print(f"  Annual Renewal Rate: {baseline_enterprise_licensing['contract_economics']['annual_renewal_rate']:.1%}")
print(f"  Monthly Churn: {baseline_enterprise_licensing['contract_economics']['monthly_churn']:.3%}")
print(f"  Annual Expansion: {baseline_enterprise_licensing['contract_economics']['annual_expansion']:.0%}")