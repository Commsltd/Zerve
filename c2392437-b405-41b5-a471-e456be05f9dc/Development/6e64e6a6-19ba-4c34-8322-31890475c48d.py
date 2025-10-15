"""
Loss Provisioning and Expected Losses
Calculates risk-adjusted loss provisions based on financed volume
"""
import pandas as pd

# Create loss provisioning dataframe
loss_provisions_df = revenue_df[['month', 'year']].copy()

# Calculate expected losses on financed volume
# Expected loss rate: 2.5% on financed pool (from base parameters)
expected_loss_rate_val = loss_provisions['expected_loss_rate']

# Institutional product losses
loss_provisions_df['inst_expected_losses'] = (
    revenue_df['inst_financed_value'] * expected_loss_rate_val
)

# P2P product losses
loss_provisions_df['p2p_expected_losses'] = (
    revenue_df['p2p_financed_value'] * expected_loss_rate_val
)

# Total expected losses
loss_provisions_df['total_expected_losses'] = (
    loss_provisions_df['inst_expected_losses'] + 
    loss_provisions_df['p2p_expected_losses']
)

# Net revenue after provisions
loss_provisions_df['inst_net_revenue'] = (
    revenue_df['institutional_revenue'] - loss_provisions_df['inst_expected_losses']
)

loss_provisions_df['p2p_net_revenue'] = (
    revenue_df['p2p_revenue'] - loss_provisions_df['p2p_expected_losses']
)

loss_provisions_df['total_net_revenue'] = (
    loss_provisions_df['inst_net_revenue'] + 
    loss_provisions_df['p2p_net_revenue']
)

# Partnership cost (first loss insurance: 50 bps on financed volume for Y2-Y3)
loss_provisions_df['partnership_insurance_cost'] = 0.0
loss_provisions_df.loc[(loss_provisions_df['month'] >= 18) & 
                       (loss_provisions_df['month'] <= 36), 
                       'partnership_insurance_cost'] = (
    revenue_df.loc[(revenue_df['month'] >= 18) & (revenue_df['month'] <= 36), 
                   'inst_financed_value'] * 0.005  # 50 bps
)

print("Loss Provisioning Calculated")
print(f"\nMonth 24 (Y2 End):")
print(f"  Expected losses: £{loss_provisions_df.loc[23, 'total_expected_losses']:,.0f}")
print(f"  Partnership insurance cost: £{loss_provisions_df.loc[23, 'partnership_insurance_cost']:,.0f}")
print(f"  Gross revenue: £{revenue_df.loc[23, 'total_invoice_finance_revenue']:,.0f}")
print(f"  Net revenue (after losses): £{loss_provisions_df.loc[23, 'total_net_revenue']:,.0f}")
print(f"\nMonth 60 (Y5 End):")
print(f"  Expected losses: £{loss_provisions_df.loc[59, 'total_expected_losses']:,.0f}")
print(f"  Gross revenue: £{revenue_df.loc[59, 'total_invoice_finance_revenue']:,.0f}")
print(f"  Net revenue: £{loss_provisions_df.loc[59, 'total_net_revenue']:,.0f}")