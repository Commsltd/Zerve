"""
Calculation Engine: Output Summary
Consolidates all calculated outputs for easy access and validation
"""
import pandas as pd
import numpy as np

# Consolidate all outputs
calc_engine_output = {
    'parameters_used': {
        'pricing_tiers': calc_pricing_tiers,
        'churn_rates': calc_churn_rates,
        'token_economics': calc_token_economics,
        'invoice_finance_timeline': calc_invoice_finance['product_timeline'],
        'regional_expansion': calc_regional_expansion
    },
    'subscription_revenue': {
        'arr_m12': calc_arr_m12,
        'arr_m24': calc_arr_m24,
        'arr_m36': calc_arr_m36,
        'arr_m60': calc_arr_m60,
        'mrr_dataframe': calc_subscription_mrr_df
    },
    'customer_metrics': {
        'total_new_customers': calc_acquisition_df[['new_starter', 'new_growth', 'new_scale', 'new_enterprise']].sum().sum(),
        'active_customers_m60': calc_active_customers[calc_active_customers['month']==60]['total_active'].values[0],
        'active_customers_dataframe': calc_active_customers,
        'cohort_dataframe': calc_cohort_df
    },
    'token_revenue': {
        'month_60_total': calc_token_revenue_df[calc_token_revenue_df['month']==60]['total_token_revenue'].values[0],
        'month_60_overage': calc_token_revenue_df[calc_token_revenue_df['month']==60]['overage_revenue'].values[0],
        'month_60_payg': calc_token_revenue_df[calc_token_revenue_df['month']==60]['payg_revenue'].values[0],
        'token_revenue_dataframe': calc_token_revenue_df
    },
    'invoice_finance_revenue': {
        'month_18_institutional': calc_invoice_finance_df[calc_invoice_finance_df['month']==18]['institutional_revenue'].values[0],
        'month_60_total': calc_invoice_finance_df[calc_invoice_finance_df['month']==60]['total_invoice_finance_revenue'].values[0],
        'invoice_finance_dataframe': calc_invoice_finance_df
    },
    'geographic_allocation': {
        'month_60_uk_pct': calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['uk_pct'].values[0],
        'month_60_eu_pct': calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['eu_pct'].values[0],
        'month_60_us_pct': calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['us_pct'].values[0],
        'month_60_apac_pct': calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['apac_pct'].values[0],
        'geographic_dataframe': calc_geo_allocation_df
    }
}

print("=" * 70)
print("CALCULATION ENGINE - OUTPUT SUMMARY")
print("=" * 70)
print(f"\n✓ Subscription ARR Milestones:")
print(f"  Year 1 (M12): £{calc_engine_output['subscription_revenue']['arr_m12']:,.0f}")
print(f"  Year 2 (M24): £{calc_engine_output['subscription_revenue']['arr_m24']:,.0f}")
print(f"  Year 3 (M36): £{calc_engine_output['subscription_revenue']['arr_m36']:,.0f}")
print(f"  Year 5 (M60): £{calc_engine_output['subscription_revenue']['arr_m60']:,.0f}")

print(f"\n✓ Customer Projections:")
print(f"  Total New Customers (60 months): {int(calc_engine_output['customer_metrics']['total_new_customers']):,}")
print(f"  Active Customers at Month 60: {int(calc_engine_output['customer_metrics']['active_customers_m60']):,}")

print(f"\n✓ Token Revenue (Month 60):")
print(f"  Total: £{calc_engine_output['token_revenue']['month_60_total']:,.0f}")
print(f"  Overage: £{calc_engine_output['token_revenue']['month_60_overage']:,.0f}")
print(f"  PAYG: £{calc_engine_output['token_revenue']['month_60_payg']:,.0f}")

print(f"\n✓ Invoice Finance Revenue:")
print(f"  Month 18 (Inst Launch): £{calc_engine_output['invoice_finance_revenue']['month_18_institutional']:,.0f}")
print(f"  Month 60 (Total): £{calc_engine_output['invoice_finance_revenue']['month_60_total']:,.0f}")

print(f"\n✓ Geographic Allocation (Month 60):")
print(f"  UK: {calc_engine_output['geographic_allocation']['month_60_uk_pct']:.1%}")
print(f"  EU: {calc_engine_output['geographic_allocation']['month_60_eu_pct']:.1%}")
print(f"  US: {calc_engine_output['geographic_allocation']['month_60_us_pct']:.1%}")
print(f"  APAC: {calc_engine_output['geographic_allocation']['month_60_apac_pct']:.1%}")

print(f"\n" + "=" * 70)
print("✓ Calculation Engine Complete - All Financial Metrics Calculated")
print("=" * 70)