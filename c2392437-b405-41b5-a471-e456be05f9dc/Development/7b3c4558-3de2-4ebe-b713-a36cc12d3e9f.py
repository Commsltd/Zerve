"""
Consolidated Revenue Model - All Streams Integrated with Geographic Expansion and Network Effects
Final 60-month P&L top line model
"""
import pandas as pd
import numpy as np

# Import core dataframes from upstream blocks
# Subscription revenue (60 months, includes base token subscription)
sub_rev_df = subscription_mrr_df[['month', 'total_mrr', 'arr']].copy()
sub_rev_df.columns = ['month', 'subscription_mrr', 'subscription_arr']

# Invoice finance revenue (60 months)
inv_fin_df = revenue_df[['month', 'total_invoice_finance_revenue']].copy()

# Enterprise licensing (48 months - extend to 60)
_ent_lic_mrr = np.zeros(60)
_ent_lic_mrr[:48] = monthly_rev_df['total_with_partners_mrr_gbp'].values
_y4_avg = monthly_rev_df[monthly_rev_df['year']==4]['total_with_partners_mrr_gbp'].mean()
_y3_avg = monthly_rev_df[monthly_rev_df['year']==3]['total_with_partners_mrr_gbp'].mean()
_ent_growth = (_y4_avg / _y3_avg) ** (1/12) if _y3_avg > 0 else 1.0
for _idx in range(48, 60):
    _ent_lic_mrr[_idx] = _ent_lic_mrr[_idx-1] * _ent_growth

# Token overage/PAYG (scale with subscription growth)
_sub_growth_factor = sub_rev_df['subscription_mrr'] / sub_rev_df['subscription_mrr'].iloc[0]
_token_overage_base = 42288.75
_token_payg_base = 38220.0

# Build consolidated revenue model
consolidated_revenue = pd.DataFrame({
    'month': timeline_df['month'],
    'date': timeline_df['date'],
    'year': timeline_df['year'],
    'quarter': timeline_df['quarter'],
    'gtm_phase': timeline_df['gtm_phase'],
    'active_regions': timeline_df['active_regions'],
    
    # Revenue streams
    'subscription_mrr': sub_rev_df['subscription_mrr'],
    'subscription_arr': sub_rev_df['subscription_arr'],
    'token_overage_revenue': _token_overage_base * _sub_growth_factor,
    'token_payg_revenue': _token_payg_base * _sub_growth_factor,
    'invoice_finance_revenue': inv_fin_df['total_invoice_finance_revenue'],
    'enterprise_licensing_mrr': _ent_lic_mrr,
    'enterprise_licensing_arr': _ent_lic_mrr * 12
})

# Total monthly revenue before geographic and network effects
consolidated_revenue['base_monthly_revenue'] = (
    consolidated_revenue['subscription_mrr'] +
    consolidated_revenue['token_overage_revenue'] +
    consolidated_revenue['token_payg_revenue'] +
    consolidated_revenue['invoice_finance_revenue'] +
    consolidated_revenue['enterprise_licensing_mrr']
)

consolidated_revenue['base_arr'] = (
    consolidated_revenue['subscription_arr'] +
    (consolidated_revenue['token_overage_revenue'] + consolidated_revenue['token_payg_revenue']) * 12 +
    consolidated_revenue['invoice_finance_revenue'] * 12 +
    consolidated_revenue['enterprise_licensing_arr']
)

print(f"✓ Consolidated 60-month revenue model created")
print(f"  Total months: {len(consolidated_revenue)}")
print(f"  Revenue streams integrated: 5")
print(f"    • Subscription (SaaS + included tokens)")
print(f"    • Token overage")
print(f"    • Token PAYG")
print(f"    • Invoice finance")
print(f"    • Enterprise licensing")