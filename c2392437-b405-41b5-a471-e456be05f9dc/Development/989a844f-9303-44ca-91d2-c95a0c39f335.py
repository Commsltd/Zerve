"""
Monthly Financed Invoice Volume
Calculates invoices financed by product type and risk tier
"""
import pandas as pd

# Merge eligible invoices with attachment rates
financed_volume_df = eligible_invoices_df.copy()
financed_volume_df = financed_volume_df.merge(
    attachment_rates_df[['month', 'institutional_attachment_rate', 'p2p_attachment_rate']], 
    on='month'
)

# Calculate financed invoices by product and risk tier
# Institutional product (uses institutional attachment rate)
financed_volume_df['inst_financed_low_risk'] = (
    financed_volume_df['eligible_low_risk'] * financed_volume_df['institutional_attachment_rate']
).round(0).astype(int)

financed_volume_df['inst_financed_mid_risk'] = (
    financed_volume_df['eligible_mid_risk'] * financed_volume_df['institutional_attachment_rate']
).round(0).astype(int)

financed_volume_df['inst_financed_high_risk'] = (
    financed_volume_df['eligible_high_risk'] * financed_volume_df['institutional_attachment_rate']
).round(0).astype(int)

financed_volume_df['inst_total_financed'] = (
    financed_volume_df['inst_financed_low_risk'] + 
    financed_volume_df['inst_financed_mid_risk'] + 
    financed_volume_df['inst_financed_high_risk']
)

# P2P product (uses p2p attachment rate on same eligible pool)
financed_volume_df['p2p_financed_low_risk'] = (
    financed_volume_df['eligible_low_risk'] * financed_volume_df['p2p_attachment_rate']
).round(0).astype(int)

financed_volume_df['p2p_financed_mid_risk'] = (
    financed_volume_df['eligible_mid_risk'] * financed_volume_df['p2p_attachment_rate']
).round(0).astype(int)

financed_volume_df['p2p_financed_high_risk'] = (
    financed_volume_df['eligible_high_risk'] * financed_volume_df['p2p_attachment_rate']
).round(0).astype(int)

financed_volume_df['p2p_total_financed'] = (
    financed_volume_df['p2p_financed_low_risk'] + 
    financed_volume_df['p2p_financed_mid_risk'] + 
    financed_volume_df['p2p_financed_high_risk']
)

# Total financed across products
financed_volume_df['total_financed_invoices'] = (
    financed_volume_df['inst_total_financed'] + 
    financed_volume_df['p2p_total_financed']
)

print("Financed Volume Calculated")
print(f"\nMonth 18 (Y2 Q3 - Institutional Pilot):")
print(f"  Institutional: {financed_volume_df.loc[17, 'inst_total_financed']:,} invoices")
print(f"\nMonth 24 (Y2 End):")
print(f"  Institutional: {financed_volume_df.loc[23, 'inst_total_financed']:,} invoices")
print(f"\nMonth 39 (Y3 Q4 - P2P Pilot Start):")
print(f"  Institutional: {financed_volume_df.loc[38, 'inst_total_financed']:,} invoices")
print(f"  P2P: {financed_volume_df.loc[38, 'p2p_total_financed']:,} invoices")
print(f"\nMonth 60 (Y5 End):")
print(f"  Total financed: {financed_volume_df.loc[59, 'total_financed_invoices']:,} invoices")