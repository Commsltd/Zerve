"""
Key Metrics Summary Table - Final KPI Dashboard
"""
import plotly.graph_objects as go
import pandas as pd

# Compile key metrics from available data at Month 60
metrics_data = {
    'Metric': [
        'Total ARR',
        'Total MRR',
        'Total Customers',
        'ARPU (per customer)',
        'LTV:CAC Ratio',
        'NRR (12M)',
        'GRR (12M)',
        'Revenue Mix - Subscription',
        'Revenue Mix - Invoice Finance',
        'Revenue Mix - Enterprise Licensing',
        'Active Regions'
    ],
    'Value': [
        f"£{arr_growth_metrics.iloc[-1]['arr']/1e6:.1f}M",
        f"£{arr_growth_metrics.iloc[-1]['mrr']/1e6:.1f}M",
        f"{export_customers.iloc[-1]['total_subscription_customers']:,.0f}",
        f"£{arr_growth_metrics.iloc[-1]['arr']/export_customers.iloc[-1]['total_subscription_customers']:,.0f}",
        f"{cac_ltv_metrics.iloc[-1]['ltv_cac_ratio']:.2f}x",
        f"{retention_by_period.iloc[-1]['nrr_12m']:.1%}",
        f"{retention_by_period.iloc[-1]['grr_12m']:.1%}",
        f"{revenue_mix.iloc[-1]['subscription_pct']:.1%}",
        f"{revenue_mix.iloc[-1]['invoice_finance_pct']:.1%}",
        f"{revenue_mix.iloc[-1]['enterprise_licensing_pct']:.1%}",
        f"{export_geographic.iloc[-1]['num_regions']} (UK, EU, US, APAC)"
    ]
}

metrics_table_df = pd.DataFrame(metrics_data)

# Create table visualization using Plotly
dashboard_fig5 = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>Key Performance Indicator</b>', '<b>Value at Month 60</b>'],
        fill_color='#1f77b4',
        align='left',
        font=dict(color='white', size=14, family='Arial')
    ),
    cells=dict(
        values=[metrics_table_df['Metric'], metrics_table_df['Value']],
        fill_color=[['#f0f0f0', 'white'] * 6],  # Alternating colors
        align='left',
        font=dict(color='#2c3e50', size=12, family='Arial'),
        height=30
    )
)])

dashboard_fig5.update_layout(
    title={
        'text': 'Executive KPI Summary (Month 60 - Year 5)',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'color': '#2c3e50'}
    },
    height=500,
    margin=dict(l=20, r=20, t=60, b=20)
)

print("✓ Key metrics summary table created")
print(f"  Total metrics displayed: {len(metrics_table_df)}")
print(f"  ARR at M60: £{arr_growth_metrics.iloc[-1]['arr']/1e6:.1f}M")
print(f"  Customer count at M60: {export_customers.iloc[-1]['total_subscription_customers']:,.0f}")
print(f"  LTV:CAC ratio: {cac_ltv_metrics.iloc[-1]['ltv_cac_ratio']:.2f}x")

dashboard_fig5