"""
Calculation Engine: Geographic Revenue Allocation
Allocates revenue across geographic regions based on expansion timeline
Distributes customer counts, ARR, and growth rates by region
"""
import pandas as pd
import numpy as np

# Geographic allocation - revenue and customer distribution
geo_records = []

for geo_month in range(1, calc_months + 1):
    # Determine active regions and their weights
    uk_active = geo_month >= calc_regional_expansion['timing']['uk']
    eu_active = geo_month >= calc_regional_expansion['timing']['eu']
    us_active = geo_month >= calc_regional_expansion['timing']['us']
    apac_active = geo_month >= calc_regional_expansion['timing']['apac']
    
    # Calculate total weight from active regions
    total_weight = 0
    if uk_active:
        total_weight += calc_regional_expansion['multipliers']['uk']
    if eu_active:
        total_weight += calc_regional_expansion['multipliers']['eu']
    if us_active:
        total_weight += calc_regional_expansion['multipliers']['us']
    if apac_active:
        total_weight += calc_regional_expansion['multipliers']['apac']
    
    # Calculate allocation percentages
    uk_pct = calc_regional_expansion['multipliers']['uk'] / total_weight if uk_active else 0
    eu_pct = calc_regional_expansion['multipliers']['eu'] / total_weight if eu_active else 0
    us_pct = calc_regional_expansion['multipliers']['us'] / total_weight if us_active else 0
    apac_pct = calc_regional_expansion['multipliers']['apac'] / total_weight if apac_active else 0
    
    # Get total revenue for this month from all streams
    sub_mrr = calc_subscription_mrr_df[calc_subscription_mrr_df['month'] == geo_month]['total_mrr'].values[0]
    sub_arr = calc_subscription_mrr_df[calc_subscription_mrr_df['month'] == geo_month]['arr'].values[0]
    token_rev = calc_token_revenue_df[calc_token_revenue_df['month'] == geo_month]['total_token_revenue'].values[0]
    invoice_rev = calc_invoice_finance_df[calc_invoice_finance_df['month'] == geo_month]['total_invoice_finance_revenue'].values[0]
    
    monthly_total_revenue = sub_mrr + token_rev + invoice_rev
    annual_total_arr = sub_arr + (token_rev * 12) + (invoice_rev * 12)
    
    # Get customer counts by tier for allocation
    customer_row = calc_active_customers[calc_active_customers['month'] == geo_month].iloc[0]
    total_customers = customer_row['total_active']
    
    # Allocate revenue by region
    uk_revenue = monthly_total_revenue * uk_pct
    eu_revenue = monthly_total_revenue * eu_pct
    us_revenue = monthly_total_revenue * us_pct
    apac_revenue = monthly_total_revenue * apac_pct
    
    # Allocate ARR by region
    uk_arr = annual_total_arr * uk_pct
    eu_arr = annual_total_arr * eu_pct
    us_arr = annual_total_arr * us_pct
    apac_arr = annual_total_arr * apac_pct
    
    # Allocate customers by region
    uk_customers = total_customers * uk_pct
    eu_customers = total_customers * eu_pct
    us_customers = total_customers * us_pct
    apac_customers = total_customers * apac_pct
    
    # Calculate month-over-month growth rate for this month
    if geo_month > 1:
        prev_revenue = geo_records[-1]['total_monthly_revenue']
        mom_growth_rate = (monthly_total_revenue - prev_revenue) / prev_revenue if prev_revenue > 0 else 0
    else:
        mom_growth_rate = 0
    
    geo_records.append({
        'month': geo_month,
        'uk_pct': uk_pct,
        'eu_pct': eu_pct,
        'us_pct': us_pct,
        'apac_pct': apac_pct,
        'uk_revenue': uk_revenue,
        'eu_revenue': eu_revenue,
        'us_revenue': us_revenue,
        'apac_revenue': apac_revenue,
        'uk_arr': uk_arr,
        'eu_arr': eu_arr,
        'us_arr': us_arr,
        'apac_arr': apac_arr,
        'uk_customers': uk_customers,
        'eu_customers': eu_customers,
        'us_customers': us_customers,
        'apac_customers': apac_customers,
        'total_monthly_revenue': monthly_total_revenue,
        'total_arr': annual_total_arr,
        'total_customers': total_customers,
        'mom_growth_rate': mom_growth_rate,
        'active_regions': sum([uk_active, eu_active, us_active, apac_active])
    })

calc_geo_allocation_df = pd.DataFrame(geo_records)

print(f"✓ Geographic Allocation: {len(calc_geo_allocation_df)} months")
print(f"  Month 12: {calc_geo_allocation_df[calc_geo_allocation_df['month']==12]['active_regions'].values[0]} regions")
print(f"    UK: {calc_geo_allocation_df[calc_geo_allocation_df['month']==12]['uk_pct'].values[0]:.0%} | £{calc_geo_allocation_df[calc_geo_allocation_df['month']==12]['uk_revenue'].values[0]:,.0f} MRR")
print(f"  Month 60: {calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['active_regions'].values[0]} regions")
print(f"    UK: {calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['uk_pct'].values[0]:.0%}, EU: {calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['eu_pct'].values[0]:.0%}, US: {calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['us_pct'].values[0]:.0%}, APAC: {calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['apac_pct'].values[0]:.0%}")
print(f"    Total ARR: £{calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['total_arr'].values[0]:,.0f}")
print(f"    Total Customers: {calc_geo_allocation_df[calc_geo_allocation_df['month']==60]['total_customers'].values[0]:,.0f}")
