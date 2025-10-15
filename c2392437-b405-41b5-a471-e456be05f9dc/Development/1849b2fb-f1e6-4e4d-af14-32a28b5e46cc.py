import plotly.graph_objects as go

# Use final month data for revenue mix pie chart
final_month_mix = revenue_mix.iloc[-1]

# Create pie chart for revenue breakdown
revenue_streams = ['Subscription', 'Token Overage', 'Token PAYG', 'Invoice Finance', 'Enterprise Licensing']
revenue_percentages = [
    final_month_mix['subscription_pct'] * 100,
    final_month_mix['token_overage_pct'] * 100,
    final_month_mix['token_payg_pct'] * 100,
    final_month_mix['invoice_finance_pct'] * 100,
    final_month_mix['enterprise_licensing_pct'] * 100
]

revenue_pie_fig = go.Figure(data=[go.Pie(
    labels=revenue_streams,
    values=revenue_percentages,
    hole=0.3,
    marker=dict(colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']),
    textinfo='label+percent',
    textposition='auto',
    hovertemplate='<b>%{label}</b><br>%{percent}<extra></extra>'
)])

revenue_pie_fig.update_layout(
    title=f"<b>Revenue Mix Breakdown (Month 60)</b>",
    height=500,
    template='plotly_white',
    font=dict(size=12),
    showlegend=True,
    legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.02)
)

revenue_pie_fig.show()