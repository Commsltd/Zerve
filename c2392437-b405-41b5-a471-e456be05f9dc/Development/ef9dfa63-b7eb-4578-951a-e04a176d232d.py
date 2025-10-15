"""
Monthly Revenue Calculation
Calculates revenue by product, risk tier using take rates and avg invoice values
"""
import pandas as pd

# Create revenue dataframe (no global months variable - use financed_volume_df directly)
revenue_df = financed_volume_df[['month', 'year']].copy()

# Calculate institutional revenue by risk tier
# Revenue = financed_invoices * avg_invoice_value * take_rate
revenue_df['inst_rev_low_risk'] = (
    financed_volume_df['inst_financed_low_risk'] * 
    avg_invoice_values['institutional'] * 
    institutional_take_rates['low_risk']['rate']
)

revenue_df['inst_rev_mid_risk'] = (
    financed_volume_df['inst_financed_mid_risk'] * 
    avg_invoice_values['institutional'] * 
    institutional_take_rates['mid_risk']['rate']
)

revenue_df['inst_rev_high_risk'] = (
    financed_volume_df['inst_financed_high_risk'] * 
    avg_invoice_values['institutional'] * 
    institutional_take_rates['high_risk']['rate']
)

revenue_df['institutional_revenue'] = (
    revenue_df['inst_rev_low_risk'] + 
    revenue_df['inst_rev_mid_risk'] + 
    revenue_df['inst_rev_high_risk']
)

# Calculate P2P revenue by risk tier
revenue_df['p2p_rev_low_risk'] = (
    financed_volume_df['p2p_financed_low_risk'] * 
    avg_invoice_values['p2p'] * 
    p2p_platform_fees['low_risk']['rate']
)

revenue_df['p2p_rev_mid_risk'] = (
    financed_volume_df['p2p_financed_mid_risk'] * 
    avg_invoice_values['p2p'] * 
    p2p_platform_fees['mid_risk']['rate']
)

revenue_df['p2p_rev_high_risk'] = (
    financed_volume_df['p2p_financed_high_risk'] * 
    avg_invoice_values['p2p'] * 
    p2p_platform_fees['high_risk']['rate']
)

revenue_df['p2p_revenue'] = (
    revenue_df['p2p_rev_low_risk'] + 
    revenue_df['p2p_rev_mid_risk'] + 
    revenue_df['p2p_rev_high_risk']
)

# Total invoice finance revenue
revenue_df['total_invoice_finance_revenue'] = (
    revenue_df['institutional_revenue'] + 
    revenue_df['p2p_revenue']
)

# Calculate financed value (invoice count * avg value)
revenue_df['inst_financed_value'] = (
    financed_volume_df['inst_total_financed'] * avg_invoice_values['institutional']
)

revenue_df['p2p_financed_value'] = (
    financed_volume_df['p2p_total_financed'] * avg_invoice_values['p2p']
)

print("Invoice Finance Revenue Calculated")
print(f"\nMonth 18 (Y2 Q3 - Institutional Pilot):")
print(f"  Institutional revenue: £{revenue_df.loc[17, 'institutional_revenue']:,.0f}")
print(f"  Financed value: £{revenue_df.loc[17, 'inst_financed_value']:,.0f}")
print(f"\nMonth 24 (Y2 End):")
print(f"  Institutional revenue: £{revenue_df.loc[23, 'institutional_revenue']:,.0f}")
print(f"\nMonth 39 (Y3 Q4 - P2P Launch):")
print(f"  Total revenue: £{revenue_df.loc[38, 'total_invoice_finance_revenue']:,.0f}")
print(f"  (Inst: £{revenue_df.loc[38, 'institutional_revenue']:,.0f}, P2P: £{revenue_df.loc[38, 'p2p_revenue']:,.0f})")
print(f"\nMonth 60 (Y5 End):")
print(f"  Total revenue: £{revenue_df.loc[59, 'total_invoice_finance_revenue']:,.0f}")