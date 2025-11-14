import pandas as pd

# Create comprehensive key metrics summary table
final_metrics = arr_growth_metrics.iloc[-1]
final_cac_ltv = cac_ltv_metrics.iloc[-1]
final_customers = export_customers.iloc[-1]

# Build metrics dictionary
key_metrics_data = {
    'Metric': [
        'Total ARR',
        'Total MRR',
        'Total Customers',
        'Customer Growth (MoM)',
        'ARR Growth (YoY)',
        'Weighted LTV',
        'Blended CAC',
        'LTV:CAC Ratio',
        'CAC Payback (Months)',
        'GRR (12M)',
        'NRR (12M)'
    ],
    'Value': [
        f'£{final_metrics["arr"]/1e6:.2f}M',
        f'£{final_metrics["mrr"]/1e6:.2f}M',
        f'{final_customers["total_subscription_customers"]:,.0f}',
        f'{final_metrics["mrr_mom_growth"]*100:.2f}%',
        f'{final_metrics["arr_yoy_growth"]*100:.2f}%',
        f'£{final_cac_ltv["weighted_ltv_gbp"]:,.0f}',
        f'£{final_cac_ltv["blended_cac_gbp"]:,.0f}',
        f'{final_cac_ltv["ltv_cac_ratio"]:.2f}x',
        f'{final_cac_ltv["cac_payback_months"]:.2f}',
        f'{latest_grr*100:.2f}%',
        f'{latest_nrr*100:.2f}%'
    ]
}

metrics_table_df = pd.DataFrame(key_metrics_data)

print("=" * 60)
print("KEY PERFORMANCE INDICATORS (Month 60)")
print("=" * 60)
print(metrics_table_df.to_string(index=False))
print("=" * 60)