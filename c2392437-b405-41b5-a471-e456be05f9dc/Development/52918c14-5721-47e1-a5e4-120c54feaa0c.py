"""
Export 1: Monthly Revenue by Stream (60 months)
Detailed monthly breakdown of all revenue streams
"""
import pandas as pd

# Build comprehensive monthly revenue table
export_monthly_revenue = pd.DataFrame({
    'month': consolidated_revenue['month'],
    'date': consolidated_revenue['date'],
    'year': consolidated_revenue['year'],
    'quarter': consolidated_revenue['quarter'],
    'gtm_phase': consolidated_revenue['gtm_phase'],
    
    # Subscription revenue
    'subscription_mrr': consolidated_revenue['subscription_mrr'],
    'subscription_arr': consolidated_revenue['subscription_arr'],
    
    # Token revenue
    'token_overage_revenue': consolidated_revenue['token_overage_revenue'],
    'token_payg_revenue': consolidated_revenue['token_payg_revenue'],
    'token_total_revenue': (consolidated_revenue['token_overage_revenue'] + 
                           consolidated_revenue['token_payg_revenue']),
    
    # Invoice finance revenue
    'invoice_finance_revenue': consolidated_revenue['invoice_finance_revenue'],
    
    # Enterprise licensing revenue
    'enterprise_licensing_mrr': consolidated_revenue['enterprise_licensing_mrr'],
    'enterprise_licensing_arr': consolidated_revenue['enterprise_licensing_arr'],
    
    # Total revenue
    'total_monthly_revenue': consolidated_revenue['base_monthly_revenue'],
    'total_arr': consolidated_revenue['base_arr']
})

# Format date column
export_monthly_revenue['date'] = export_monthly_revenue['date'].dt.strftime('%Y-%m-%d')

print(f"✓ Monthly revenue by stream table prepared: {len(export_monthly_revenue)} months")
print(f"  Columns: {len(export_monthly_revenue.columns)}")
print(f"  Total revenue Y5 (Month 60): £{export_monthly_revenue.iloc[-1]['total_monthly_revenue']:,.0f}")
