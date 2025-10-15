"""
Calculation Engine: Invoice Finance Revenue
Calculates revenue from institutional and P2P invoice financing
"""
import pandas as pd
import numpy as np

# S-curve growth function
def scurve_growth(month, start_month, max_value, steepness=0.15):
    if month < start_month:
        return 0
    months_since_start = month - start_month
    return max_value / (1 + np.exp(-steepness * (months_since_start - 10)))

# Invoice finance revenue calculation
calc_invoice_finance_records = []

for invoice_month_idx in range(1, calc_months + 1):
    inst_pilot_start = calc_invoice_finance['product_timeline']['institutional_pilot_start']
    inst_scale_start = calc_invoice_finance['product_timeline']['institutional_scale_start']
    p2p_pilot_start = calc_invoice_finance['product_timeline']['p2p_pilot_start']
    p2p_scale_start = calc_invoice_finance['product_timeline']['p2p_scale_start']
    
    # Invoice pool trajectory (grows with customer base)
    active_customers = calc_active_customers[calc_active_customers['month'] == invoice_month_idx]['total_active'].values[0]
    invoices_processed = int(active_customers * 15)  # ~15 invoices per customer per month
    
    # Institutional financing
    if invoice_month_idx >= inst_pilot_start:
        max_inst_volume = invoices_processed * 0.5  # Up to 50% attachment
        inst_financed_volume = scurve_growth(invoice_month_idx, inst_pilot_start, max_inst_volume)
        
        # Apply risk tier distribution
        inst_low_risk = inst_financed_volume * 0.4
        inst_mid_risk = inst_financed_volume * 0.4
        inst_high_risk = inst_financed_volume * 0.2
        
        # Calculate revenue
        inst_rev_low = inst_low_risk * calc_invoice_finance['avg_invoice_values']['institutional'] * calc_invoice_finance['institutional_take_rates']['low_risk']
        inst_rev_mid = inst_mid_risk * calc_invoice_finance['avg_invoice_values']['institutional'] * calc_invoice_finance['institutional_take_rates']['mid_risk']
        inst_rev_high = inst_high_risk * calc_invoice_finance['avg_invoice_values']['institutional'] * calc_invoice_finance['institutional_take_rates']['high_risk']
        
        institutional_revenue = inst_rev_low + inst_rev_mid + inst_rev_high
    else:
        institutional_revenue = 0
        inst_financed_volume = 0
    
    # P2P financing
    if invoice_month_idx >= p2p_pilot_start:
        max_p2p_volume = invoices_processed * 0.3  # Up to 30% attachment
        p2p_financed_volume = scurve_growth(invoice_month_idx, p2p_pilot_start, max_p2p_volume)
        
        # Apply risk tier distribution
        p2p_low_risk = p2p_financed_volume * 0.4
        p2p_mid_risk = p2p_financed_volume * 0.4
        p2p_high_risk = p2p_financed_volume * 0.2
        
        # Calculate revenue
        p2p_rev_low = p2p_low_risk * calc_invoice_finance['avg_invoice_values']['p2p'] * calc_invoice_finance['p2p_platform_fees']['low_risk']
        p2p_rev_mid = p2p_mid_risk * calc_invoice_finance['avg_invoice_values']['p2p'] * calc_invoice_finance['p2p_platform_fees']['mid_risk']
        p2p_rev_high = p2p_high_risk * calc_invoice_finance['avg_invoice_values']['p2p'] * calc_invoice_finance['p2p_platform_fees']['high_risk']
        
        p2p_revenue = p2p_rev_low + p2p_rev_mid + p2p_rev_high
    else:
        p2p_revenue = 0
        p2p_financed_volume = 0
    
    calc_total_invoice_finance_revenue = institutional_revenue + p2p_revenue
    
    calc_invoice_finance_records.append({
        'month': invoice_month_idx,
        'invoices_processed': invoices_processed,
        'inst_financed_volume': int(inst_financed_volume),
        'p2p_financed_volume': int(p2p_financed_volume),
        'institutional_revenue': institutional_revenue,
        'p2p_revenue': p2p_revenue,
        'total_invoice_finance_revenue': calc_total_invoice_finance_revenue
    })

calc_invoice_finance_df = pd.DataFrame(calc_invoice_finance_records)

print(f"✓ Invoice Finance Revenue Calculated: {len(calc_invoice_finance_df)} months")
print(f"  Month 18 (Inst Pilot): £{calc_invoice_finance_df[calc_invoice_finance_df['month']==18]['institutional_revenue'].values[0]:,.0f}")
print(f"  Month 39 (P2P Launch): £{calc_invoice_finance_df[calc_invoice_finance_df['month']==39]['total_invoice_finance_revenue'].values[0]:,.0f}")
print(f"  Month 60: £{calc_invoice_finance_df[calc_invoice_finance_df['month']==60]['total_invoice_finance_revenue'].values[0]:,.0f}")