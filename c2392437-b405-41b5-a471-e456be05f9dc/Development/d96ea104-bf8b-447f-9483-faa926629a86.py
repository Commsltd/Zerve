"""
Revenue Mix Breakdown - Interactive Pie Chart (Month 60)
"""
import plotly.graph_objects as go
import pandas as pd

# Get Month 60 revenue mix data
revenue_mix_m60 = revenue_mix.iloc[-1]

# Prepare data for pie chart
revenue_labels = ['Subscription', 'Token Overage', 'Token PAYG', 'Invoice Finance', 'Enterprise Licensing']
revenue_percentages = [
    revenue_mix_m60['subscription_pct'] * 100,
    revenue_mix_m60['token_overage_pct'] * 100,
    revenue_mix_m60['token_payg_pct'] * 100,
    revenue_mix_m60['invoice_finance_pct'] * 100,
    revenue_mix_m60['enterprise_licensing_pct'] * 100
]

# Create pie chart
dashboard_fig3 = go.Figure(data=[go.Pie(
    labels=revenue_labels,
    values=revenue_percentages,
    hole=0.3,  # Donut chart
    marker=dict(colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']),
    textinfo='label+percent',
    hovertemplate='<b>%{label}</b><br>Share: %{percent}<br>(%{value:.2f}%)<extra></extra>'
)])

dashboard_fig3.update_layout(
    title={
        'text': 'Revenue Mix at Month 60 (Year 5)',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'color': '#2c3e50'}
    },
    template='plotly_white',
    height=500,
    showlegend=True,
    legend=dict(
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="left",
        x=1.02
    )
)

print("✓ Revenue mix pie chart created (Month 60)")
print(f"  Subscription: {revenue_percentages[0]:.1f}%")
print(f"  Invoice Finance: {revenue_percentages[3]:.1f}%")
print(f"  Enterprise Licensing: {revenue_percentages[4]:.1f}%")
print(f"  Token (Overage + PAYG): {revenue_percentages[1] + revenue_percentages[2]:.1f}%")

dashboard_fig3