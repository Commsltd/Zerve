"""
Strategic Seeding Partnerships
Models 4 strategic partners providing critical mass data with preferred licensing terms
"""

import pandas as pd

# Define strategic seeding partnerships
strategic_partners_data = {
    'baker_ing_international': {
        'company': 'Baker Ing International',
        'type': 'Global debt collection agency',
        'data_contribution_pct': 0.25,  # 25% of critical mass threshold
        'seeding_period': 'Y1',
        'preferred_terms': {
            'discount_y1_y2': 0.50,  # 50% discount Y1-Y2
            'discount_y3': 0.25,      # 25% discount Y3+
            'standard_pricing_y4': True,  # Revert to standard Y4+
            'co_marketing_rights': True
        },
        'estimated_baseline_contract_gbp': 200000,  # What they'd pay at standard rates
        'use_case': 'Global invoice intelligence and debtor monitoring'
    },
    'harley_davidson_fs': {
        'company': 'Harley-Davidson Financial Services',
        'type': 'Captive finance company',
        'data_contribution_pct': 0.25,
        'seeding_period': 'Y1',
        'preferred_terms': {
            'discount_y1_y2': 0.50,
            'discount_y3': 0.25,
            'standard_pricing_y4': True,
            'co_marketing_rights': True
        },
        'estimated_baseline_contract_gbp': 150000,
        'use_case': 'Dealer network credit risk and payment intelligence'
    },
    'tokio_marine': {
        'company': 'Tokio Marine (Trade Credit Division)',
        'type': 'Trade credit insurer',
        'data_contribution_pct': 0.25,
        'seeding_period': 'Y1-Y2',
        'preferred_terms': {
            'discount_y1_y2': 0.50,
            'discount_y3': 0.25,
            'standard_pricing_y4': True,
            'co_marketing_rights': True
        },
        'estimated_baseline_contract_gbp': 300000,
        'use_case': 'RTCI feeds for underwriting and portfolio risk management'
    },
    'fis_atelio': {
        'company': 'FIS/Atelio',
        'type': 'Payment intelligence and embedded finance platform',
        'data_contribution_pct': 0.25,
        'seeding_period': 'Y1-Y2',
        'preferred_terms': {
            'discount_y1_y2': 0.50,
            'discount_y3': 0.25,
            'standard_pricing_y4': True,
            'co_marketing_rights': True
        },
        'estimated_baseline_contract_gbp': 250000,
        'use_case': 'Payment behavior data and embedded credit decisioning'
    }
}

# Calculate actual revenue by year with discounts
partners_revenue_list = []
for partner_key, partner_info in strategic_partners_data.items():
    baseline = partner_info['estimated_baseline_contract_gbp']
    
    partners_revenue_list.append({
        'partner': partner_info['company'],
        'partner_type': partner_info['type'],
        'data_contribution': f"{partner_info['data_contribution_pct']:.0%}",
        'baseline_contract_gbp': baseline,
        'y1_revenue_gbp': baseline * (1 - partner_info['preferred_terms']['discount_y1_y2']),
        'y2_revenue_gbp': baseline * (1 - partner_info['preferred_terms']['discount_y1_y2']),
        'y3_revenue_gbp': baseline * (1 - partner_info['preferred_terms']['discount_y3']),
        'y4_plus_revenue_gbp': baseline,  # Standard pricing
        'co_marketing': partner_info['preferred_terms']['co_marketing_rights']
    })

partners_revenue_df = pd.DataFrame(partners_revenue_list)

# Summary metrics
total_data_contribution = sum([p['data_contribution_pct'] for p in strategic_partners_data.values()])
total_y1_revenue = partners_revenue_df['y1_revenue_gbp'].sum()
total_y4_revenue = partners_revenue_df['y4_plus_revenue_gbp'].sum()
revenue_ramp = (total_y4_revenue - total_y1_revenue) / total_y1_revenue

print("=" * 80)
print("STRATEGIC SEEDING PARTNERSHIPS")
print("=" * 80)
print(f"\nTotal Partners: {len(strategic_partners_data)}")
print(f"Combined Data Contribution: {total_data_contribution:.0%} (critical mass threshold)")
print(f"\nY1 Revenue (50% discount): £{total_y1_revenue:,.0f}")
print(f"Y4+ Revenue (standard pricing): £{total_y4_revenue:,.0f}")
print(f"Revenue Ramp Y1→Y4+: {revenue_ramp:.0%}")
print(f"\nAll partners have co-marketing rights during seeding period")
print("=" * 80)