"""
Customer Counts by Tier - Stacked Bar Chart
"""
import plotly.graph_objects as go
import pandas as pd

# Create stacked bar chart for customer counts by tier
dashboard_fig2 = go.Figure()

# Add traces for each tier (in stacking order from bottom to top)
dashboard_fig2.add_trace(go.Bar(
    x=export_customers['date'],
    y=export_customers['starter_customers'],
    name='Starter',
    marker_color='#e6f2ff',
    hovertemplate='<b>Starter</b><br>Date: %{x}<br>Count: %{y:,.0f}<extra></extra>'
))

dashboard_fig2.add_trace(go.Bar(
    x=export_customers['date'],
    y=export_customers['growth_customers'],
    name='Growth',
    marker_color='#99ccff',
    hovertemplate='<b>Growth</b><br>Date: %{x}<br>Count: %{y:,.0f}<extra></extra>'
))

dashboard_fig2.add_trace(go.Bar(
    x=export_customers['date'],
    y=export_customers['scale_customers'],
    name='Scale',
    marker_color='#3399ff',
    hovertemplate='<b>Scale</b><br>Date: %{x}<br>Count: %{y:,.0f}<extra></extra>'
))

dashboard_fig2.add_trace(go.Bar(
    x=export_customers['date'],
    y=export_customers['enterprise_customers'],
    name='Enterprise',
    marker_color='#0066cc',
    hovertemplate='<b>Enterprise</b><br>Date: %{x}<br>Count: %{y:,.0f}<extra></extra>'
))

# Update layout
dashboard_fig2.update_layout(
    title={
        'text': 'Customer Growth by Subscription Tier',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'color': '#2c3e50'}
    },
    xaxis_title='Date',
    yaxis_title='Customer Count',
    barmode='stack',
    hovermode='x unified',
    template='plotly_white',
    height=500,
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

print("✓ Customer tier stacked bar chart created")
print(f"  Total customers at month 60: {export_customers.iloc[-1]['total_subscription_customers']:,.0f}")
print(f"  Starter: {export_customers.iloc[-1]['starter_customers']:,.0f}")
print(f"  Growth: {export_customers.iloc[-1]['growth_customers']:,.0f}")
print(f"  Scale: {export_customers.iloc[-1]['scale_customers']:,.0f}")
print(f"  Enterprise: {export_customers.iloc[-1]['enterprise_customers']:,.0f}")

dashboard_fig2