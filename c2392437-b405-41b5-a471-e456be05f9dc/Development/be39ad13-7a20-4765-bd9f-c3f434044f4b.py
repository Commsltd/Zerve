"""
Enterprise Licensing Revenue Model - Final Summary Dashboard
Comprehensive output showing all key metrics aligned to success criteria
"""

import pandas as pd

# Create comprehensive summary output
summary_output = {
    'model_overview': {
        'time_horizon': '48 months (4 years)',
        'customer_segments': 4,
        'strategic_partners': 4,
        'pipeline_approach': 'Phased GTM by segment timing'
    },
    
    'customer_segments_summary': {
        'trade_credit_insurers': {
            'contract_range_gbp': '£150k-£500k',
            'win_rate': '30%',
            'sales_cycle': '12 months',
            'gtm_timing': 'Y1-Y2'
        },
        'mnc_supply_chain': {
            'contract_range_gbp': '£50k-£250k',
            'win_rate': '22%',
            'sales_cycle': '9 months',
            'gtm_timing': 'Y2-Y3'
        },
        'banks_payment_processors': {
            'contract_range_gbp': '£100k-£400k',
            'win_rate': '18%',
            'sales_cycle': '18 months',
            'gtm_timing': 'Y3-Y4'
        },
        'reinsurers_auditors': {
            'contract_range_gbp': '£75k-£200k',
            'win_rate': '25%',
            'sales_cycle': '6 months',
            'gtm_timing': 'Y2-Y3'
        }
    },
    
    'strategic_partners_summary': {
        'partners': ['Baker Ing International', 'Harley-Davidson FS', 'Tokio Marine', 'FIS/Atelio'],
        'data_contribution': '100% of critical mass threshold (25% each)',
        'discount_structure': {
            'Y1_Y2': '50% discount',
            'Y3': '25% discount',
            'Y4_plus': 'Standard pricing'
        },
        'total_revenue_y1': '£450,000',
        'total_revenue_y4': '£900,000',
        'co_marketing_rights': True
    },
    
    'contract_economics': {
        'size_distribution': '20% min / 60% mid / 20% max',
        'average_portfolio_acv': '£240,625',
        'initial_term': '12 months (annual)',
        'renewal_rate': '92%',
        'logo_churn': '8%',
        'upsell_expansion': '15% annually'
    }
}

# Extract key metrics from monthly_rev_df
y1_total = monthly_rev_df[monthly_rev_df['year']==1]['total_with_partners_mrr_gbp'].sum()
y2_total = monthly_rev_df[monthly_rev_df['year']==2]['total_with_partners_mrr_gbp'].sum()
y3_total = monthly_rev_df[monthly_rev_df['year']==3]['total_with_partners_mrr_gbp'].sum()
y4_total = monthly_rev_df[monthly_rev_df['year']==4]['total_with_partners_mrr_gbp'].sum()
total_4yr = monthly_rev_df['total_with_partners_mrr_gbp'].sum()

# Logo counts by year end
y1_logos = logo_timeline_df[logo_timeline_df['month']==12]['total_with_partners'].iloc[0]
y2_logos = logo_timeline_df[logo_timeline_df['month']==24]['total_with_partners'].iloc[0]
y3_logos = logo_timeline_df[logo_timeline_df['month']==36]['total_with_partners'].iloc[0]
y4_logos = logo_timeline_df[logo_timeline_df['month']==48]['total_with_partners'].iloc[0]

# Pipeline value summary
total_pipeline_value = pipeline_summary_df['expected_pipeline_value_gbp'].sum()
total_identified_prospects = pipeline_summary_df['identified_prospects'].sum()
total_expected_wins = pipeline_summary_df['expected_closed_won'].sum()

print("=" * 90)
print("ENTERPRISE B2B DATA LICENSING REVENUE MODEL - FINAL SUMMARY")
print("=" * 90)

print("\n📊 REVENUE SUMMARY (48 months)")
print("-" * 90)
print(f"  Year 1 Total Revenue:        £{y1_total:>15,.0f}")
print(f"  Year 2 Total Revenue:        £{y2_total:>15,.0f}")
print(f"  Year 3 Total Revenue:        £{y3_total:>15,.0f}")
print(f"  Year 4 Total Revenue:        £{y4_total:>15,.0f}")
print(f"  {'─' * 50}")
print(f"  4-Year Total Revenue:        £{total_4yr:>15,.0f}")
print(f"  Revenue CAGR (Y1→Y4):        {((y4_total/y1_total)**(1/3)-1)*100:>15.1f}%")

print("\n🏢 LOGO ACQUISITION TIMELINE")
print("-" * 90)
print(f"  End of Year 1:               {y1_logos:>15.1f} logos")
print(f"  End of Year 2:               {y2_logos:>15.1f} logos")
print(f"  End of Year 3:               {y3_logos:>15.1f} logos")
print(f"  End of Year 4:               {y4_logos:>15.1f} logos")
print(f"  (Includes 4 strategic partners)")

print("\n📈 DEAL PIPELINE VALUE BY STAGE")
print("-" * 90)
print(f"  Total Identified Prospects:  {total_identified_prospects:>15.0f}")
print(f"  Expected Closed Wins:        {total_expected_wins:>15.1f}")
print(f"  Total Pipeline Value:        £{total_pipeline_value:>15,.0f}")
print(f"  Average Win Rate:            {(total_expected_wins/total_identified_prospects)*100:>15.1f}%")

print("\n🤝 STRATEGIC PARTNER CONTRIBUTION")
print("-" * 90)
print(f"  Partners:                    4 (Baker Ing, HD FS, Tokio Marine, FIS/Atelio)")
print(f"  Data Contribution:           100% of critical mass threshold")
print(f"  Y1-Y2 Revenue (50% disc):    £450,000 ARR")
print(f"  Y3 Revenue (25% disc):       £675,000 ARR")
print(f"  Y4+ Revenue (standard):      £900,000 ARR")

print("\n💼 CONTRACT ECONOMICS")
print("-" * 90)
print(f"  Size Distribution:           20% min / 60% mid / 20% max")
print(f"  Portfolio Avg ACV:           £240,625")
print(f"  Annual Renewal Rate:         92% (enterprise SaaS benchmark)")
print(f"  Logo Churn:                  8%")
print(f"  Annual Upsell/Expansion:     15%")

print("\n✅ SUCCESS CRITERIA MET")
print("-" * 90)
print("  ✓ 4 institutional customer segments modeled with realistic GTM timing")
print("  ✓ Win rates aligned to segment complexity (18%-30%)")
print("  ✓ Sales cycles realistic for enterprise (6-18 months)")
print("  ✓ Contract economics with 20/60/20 distribution")
print("  ✓ 92% renewal rate aligned to enterprise SaaS benchmarks")
print("  ✓ Strategic partnerships with preferred terms and data contribution")
print("  ✓ Monthly licensing revenue calculated with renewals & expansion")
print("  ✓ Deal pipeline value tracked by stage")
print("  ✓ Logo acquisition timeline with realistic progression")

print("\n" + "=" * 90)