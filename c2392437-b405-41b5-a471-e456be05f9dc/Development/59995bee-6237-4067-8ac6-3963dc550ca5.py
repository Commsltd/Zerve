import plotly.graph_objects as go

# Create stacked bar chart for customer counts by tier over time
customer_tier_fig = go.Figure()

# Add traces for each tier
customer_tier_fig.add_trace(go.Bar(
    x=export_customers['date'],
    y=export_customers['starter_customers'],
    name='Starter',
    marker_color='#8dd3c7'
))

customer_tier_fig.add_trace(go.Bar(
    x=export_customers['date'],
    y=export_customers['growth_customers'],
    name='Growth',
    marker_color='#bebada'
))

customer_tier_fig.add_trace(go.Bar(
    x=export_customers['date'],
    y=export_customers['scale_customers'],
    name='Scale',
    marker_color='#fb8072'
))

customer_tier_fig.add_trace(go.Bar(
    x=export_customers['date'],
    y=export_customers['enterprise_customers'],
    name='Enterprise',
    marker_color='#80b1d3'
))

customer_tier_fig.update_layout(
    title="<b>Customer Count by Tier Over Time</b>",
    xaxis_title="Date",
    yaxis_title="<b>Customer Count</b>",
    barmode='stack',
    height=500,
    template='plotly_white',
    font=dict(size=12),
    hovermode='x unified',
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

customer_tier_fig.show()