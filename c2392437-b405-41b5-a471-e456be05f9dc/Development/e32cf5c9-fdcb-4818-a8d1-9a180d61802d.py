import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create ARR/MRR trend line chart with dual axis
arr_mrr_fig = make_subplots(
    rows=1, cols=1,
    specs=[[{"secondary_y": True}]]
)

# Add ARR trace
arr_mrr_fig.add_trace(
    go.Scatter(
        x=arr_growth_metrics['date'],
        y=arr_growth_metrics['arr'] / 1e6,  # Convert to millions
        name='ARR',
        mode='lines+markers',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=6)
    ),
    secondary_y=False
)

# Add MRR trace
arr_mrr_fig.add_trace(
    go.Scatter(
        x=arr_growth_metrics['date'],
        y=arr_growth_metrics['mrr'] / 1e6,  # Convert to millions
        name='MRR',
        mode='lines+markers',
        line=dict(color='#ff7f0e', width=3),
        marker=dict(size=6)
    ),
    secondary_y=False
)

# Add MoM growth rate on secondary axis
arr_mrr_fig.add_trace(
    go.Scatter(
        x=arr_growth_metrics['date'],
        y=arr_growth_metrics['mrr_mom_growth'] * 100,  # Convert to percentage
        name='MoM Growth %',
        mode='lines',
        line=dict(color='#2ca02c', width=2, dash='dash'),
        opacity=0.7
    ),
    secondary_y=True
)

arr_mrr_fig.update_xaxes(title_text="Date")
arr_mrr_fig.update_yaxes(title_text="<b>ARR/MRR (£M)</b>", secondary_y=False)
arr_mrr_fig.update_yaxes(title_text="<b>MoM Growth (%)</b>", secondary_y=True)

arr_mrr_fig.update_layout(
    title="<b>ARR & MRR Growth Trends Over Time</b>",
    hovermode='x unified',
    height=500,
    template='plotly_white',
    font=dict(size=12),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

arr_mrr_fig.show()