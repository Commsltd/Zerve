"""
Export 3: Quarterly and Annual Revenue Rollups
Aggregated revenue summaries by quarter and year
"""
import pandas as pd

# Quarterly rollup of monthly revenue data
export_quarterly_revenue = export_monthly_revenue.groupby(['year', 'quarter']).agg({
    'subscription_mrr': 'mean',
    'subscription_arr': 'last',
    'token_overage_revenue': 'sum',
    'token_payg_revenue': 'sum',
    'token_total_revenue': 'sum',
    'invoice_finance_revenue': 'sum',
    'enterprise_licensing_mrr': 'mean',
    'enterprise_licensing_arr': 'last',
    'total_monthly_revenue': 'sum',
    'total_arr': 'last'
}).reset_index()

export_quarterly_revenue.rename(columns={
    'subscription_mrr': 'avg_subscription_mrr',
    'enterprise_licensing_mrr': 'avg_enterprise_licensing_mrr',
    'total_monthly_revenue': 'quarterly_total_revenue'
}, inplace=True)

# Annual rollup of monthly revenue data
export_annual_revenue = export_monthly_revenue.groupby('year').agg({
    'subscription_mrr': 'mean',
    'subscription_arr': 'last',
    'token_overage_revenue': 'sum',
    'token_payg_revenue': 'sum',
    'token_total_revenue': 'sum',
    'invoice_finance_revenue': 'sum',
    'enterprise_licensing_mrr': 'mean',
    'enterprise_licensing_arr': 'last',
    'total_monthly_revenue': 'sum',
    'total_arr': 'last'
}).reset_index()

export_annual_revenue.rename(columns={
    'subscription_mrr': 'avg_subscription_mrr',
    'enterprise_licensing_mrr': 'avg_enterprise_licensing_mrr',
    'total_monthly_revenue': 'annual_total_revenue'
}, inplace=True)

print(f"✓ Quarterly revenue rollup prepared: {len(export_quarterly_revenue)} quarters")
print(f"✓ Annual revenue rollup prepared: {len(export_annual_revenue)} years")
print(f"  Y5 annual revenue: £{export_annual_revenue.iloc[-1]['annual_total_revenue']:,.0f}")
