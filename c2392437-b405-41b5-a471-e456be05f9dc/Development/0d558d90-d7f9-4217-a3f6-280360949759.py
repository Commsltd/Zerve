"""
Export 2: Customer Counts by Tier and Segment (60 months)
Monthly customer counts with tier and segment breakdowns
"""
import pandas as pd

# Build customer counts export table
export_customers = pd.DataFrame({
    'month': tier_movement_df['month'],
    'date': timeline_df['date'].dt.strftime('%Y-%m-%d'),
    'year': timeline_df['year'],
    'quarter': timeline_df['quarter'],
    
    # Subscription tier customers
    'starter_customers': tier_movement_df['net_starter'],
    'growth_customers': tier_movement_df['net_growth'],
    'scale_customers': tier_movement_df['net_scale'],
    'enterprise_customers': tier_movement_df['net_enterprise'],
    'total_subscription_customers': tier_movement_df['total_active'],
    
    # Enterprise licensing customers (first 48 months, then extend)
    'trade_credit_insurers_logos': 0.0,
    'mnc_supply_chain_logos': 0.0,
    'banks_payment_processors_logos': 0.0,
    'reinsurers_auditors_logos': 0.0,
    'enterprise_licensing_logos': 0.0,
    'strategic_partner_logos': 0
})

# Populate enterprise licensing customer data (48 months available)
for _month_idx in range(min(48, len(export_customers))):
    export_customers.loc[_month_idx, 'trade_credit_insurers_logos'] = logo_timeline_df.iloc[_month_idx]['trade_credit_insurers_logos']
    export_customers.loc[_month_idx, 'mnc_supply_chain_logos'] = logo_timeline_df.iloc[_month_idx]['mnc_supply_chain_logos']
    export_customers.loc[_month_idx, 'banks_payment_processors_logos'] = logo_timeline_df.iloc[_month_idx]['banks_payment_processors_logos']
    export_customers.loc[_month_idx, 'reinsurers_auditors_logos'] = logo_timeline_df.iloc[_month_idx]['reinsurers_auditors_logos']
    export_customers.loc[_month_idx, 'enterprise_licensing_logos'] = logo_timeline_df.iloc[_month_idx]['total_logos']
    export_customers.loc[_month_idx, 'strategic_partner_logos'] = logo_timeline_df.iloc[_month_idx]['strategic_partner_logos']

# Extend to 60 months (keep last value for months 49-60)
if len(logo_timeline_df) == 48:
    _last_row = logo_timeline_df.iloc[-1]
    for _month_idx in range(48, 60):
        export_customers.loc[_month_idx, 'trade_credit_insurers_logos'] = _last_row['trade_credit_insurers_logos']
        export_customers.loc[_month_idx, 'mnc_supply_chain_logos'] = _last_row['mnc_supply_chain_logos']
        export_customers.loc[_month_idx, 'banks_payment_processors_logos'] = _last_row['banks_payment_processors_logos']
        export_customers.loc[_month_idx, 'reinsurers_auditors_logos'] = _last_row['reinsurers_auditors_logos']
        export_customers.loc[_month_idx, 'enterprise_licensing_logos'] = _last_row['total_logos']
        export_customers.loc[_month_idx, 'strategic_partner_logos'] = _last_row['strategic_partner_logos']

print(f"✓ Customer counts by tier and segment table prepared: {len(export_customers)} months")
print(f"  Total subscription customers Y5: {export_customers.iloc[-1]['total_subscription_customers']:,.0f}")
print(f"  Total enterprise licensing logos Y4: {logo_timeline_df.iloc[-1]['total_with_partners']:,.1f}")
