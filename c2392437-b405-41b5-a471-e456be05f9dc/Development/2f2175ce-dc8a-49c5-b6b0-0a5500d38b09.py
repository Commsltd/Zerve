"""
Invoice Finance Revenue Summary Output
Consolidated monthly metrics and key performance indicators
"""
import pandas as pd

# Create comprehensive summary dataframe
invoice_finance_summary = pd.DataFrame({
    'month': financed_volume_df['month'],
    'year': financed_volume_df['year'],
    
    # Volume metrics
    'total_invoices_processed': financed_volume_df['invoices_processed'],
    'eligible_invoices': financed_volume_df['invoices_passing_credit_filters'],
    'inst_financed_invoices': financed_volume_df['inst_total_financed'],
    'p2p_financed_invoices': financed_volume_df['p2p_total_financed'],
    'total_financed_invoices': financed_volume_df['total_financed_invoices'],
    
    # Attachment rates
    'inst_attachment_rate': attachment_rates_df['institutional_attachment_rate'],
    'p2p_attachment_rate': attachment_rates_df['p2p_attachment_rate'],
    'total_attachment_rate': attachment_rates_df['total_attachment_rate'],
    
    # Financed values
    'inst_financed_value_gbp': revenue_df['inst_financed_value'],
    'p2p_financed_value_gbp': revenue_df['p2p_financed_value'],
    
    # Revenue
    'inst_gross_revenue_gbp': revenue_df['institutional_revenue'],
    'p2p_gross_revenue_gbp': revenue_df['p2p_revenue'],
    'total_gross_revenue_gbp': revenue_df['total_invoice_finance_revenue'],
    
    # Provisions and costs
    'expected_losses_gbp': loss_provisions_df['total_expected_losses'],
    'partnership_insurance_cost_gbp': loss_provisions_df['partnership_insurance_cost'],
    
    # Net revenue
    'inst_net_revenue_gbp': loss_provisions_df['inst_net_revenue'],
    'p2p_net_revenue_gbp': loss_provisions_df['p2p_net_revenue'],
    'total_net_revenue_gbp': loss_provisions_df['total_net_revenue']
})

# Calculate capital efficiency metrics
invoice_finance_summary['total_financed_value_gbp'] = (
    invoice_finance_summary['inst_financed_value_gbp'] + 
    invoice_finance_summary['p2p_financed_value_gbp']
)

invoice_finance_summary['revenue_as_pct_of_financed'] = (
    invoice_finance_summary['total_gross_revenue_gbp'] / 
    invoice_finance_summary['total_financed_value_gbp'].replace(0, 1)
) * 100

invoice_finance_summary['loss_rate_on_financed'] = (
    invoice_finance_summary['expected_losses_gbp'] / 
    invoice_finance_summary['total_financed_value_gbp'].replace(0, 1)
) * 100

# Annual summaries
annual_summary = invoice_finance_summary.groupby('year').agg({
    'total_financed_invoices': 'sum',
    'total_financed_value_gbp': 'sum',
    'total_gross_revenue_gbp': 'sum',
    'expected_losses_gbp': 'sum',
    'partnership_insurance_cost_gbp': 'sum',
    'total_net_revenue_gbp': 'sum'
}).round(0)

print("Invoice Finance Revenue Model Complete")
print("=" * 70)
print("\nANNUAL SUMMARY (Y1-Y5)")
print("-" * 70)
for yr in range(1, 6):
    if yr in annual_summary.index:
        print(f"\nYear {yr}:")
        print(f"  Financed invoices: {annual_summary.loc[yr, 'total_financed_invoices']:,.0f}")
        print(f"  Financed value: £{annual_summary.loc[yr, 'total_financed_value_gbp']:,.0f}")
        print(f"  Gross revenue: £{annual_summary.loc[yr, 'total_gross_revenue_gbp']:,.0f}")
        print(f"  Expected losses: £{annual_summary.loc[yr, 'expected_losses_gbp']:,.0f}")
        print(f"  Net revenue: £{annual_summary.loc[yr, 'total_net_revenue_gbp']:,.0f}")

print("\n" + "=" * 70)
print("\nKEY MILESTONES")
print("-" * 70)
print(f"Y2 Q3 (Month 18): Institutional pilot launch")
print(f"  Attachment rate: {invoice_finance_summary.loc[17, 'inst_attachment_rate']:.1%}")
print(f"Y3 Q4 (Month 39): P2P crowd pool launch")
print(f"  Combined attachment: {invoice_finance_summary.loc[38, 'total_attachment_rate']:.1%}")
print(f"Y5 End (Month 60): Mature market")
print(f"  Combined attachment: {invoice_finance_summary.loc[59, 'total_attachment_rate']:.1%}")
print(f"  Annual revenue: £{annual_summary.loc[5, 'total_gross_revenue_gbp']:,.0f}")