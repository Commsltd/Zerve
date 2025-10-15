"""
KPI Dashboard: ARR/MRR Trends Over Time
Interactive line chart showing ARR and MRR growth over 60 months with key milestones
"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Create figure
arr_mrr_fig = make_subplots(
    rows=1, cols=1,
    specs=[[{"secondary_y": False}]]
)

# Convert date column to datetime if needed
_date_column = pd.to_datetime(arr_growth_metrics['date'])

# Add ARR trend line
arr_mrr_fig.add_trace(
    go.Scatter(
        x=_date_column,
        y=arr_growth_metrics['arr'] / 1_000_000,
        name='ARR',
        mode='lines',
        line=dict(color='#1f77b4', width=3),
        hovertemplate='<b>ARR</b><br>Date: %{x}<br>Value: £%{y:.1f}M<extra></extra>'
    )
)

# Add MRR trend line
arr_mrr_fig.add_trace(
    go.Scatter(
        x=_date_column,
        y=arr_growth_metrics['mrr'] / 1_000_000,
        name='MRR',
        mode='lines',
        line=dict(color='#ff7f0e', width=2, dash='dash'),
        hovertemplate='<b>MRR</b><br>Date: %{x}<br>Value: £%{y:.1f}M<extra></extra>'
    )
)

# Add milestone markers - check if milestones are found
if milestone_arr_1m is not None:
    _milestones_arr = [
        (pd.to_datetime(str(milestone_arr_1m.iloc[1])), float(milestone_arr_1m.iloc[4]) / 1_000_000, '£1M ARR')
    ]
    
    if milestone_arr_5m is not None:
        _milestones_arr.append((pd.to_datetime(str(milestone_arr_5m.iloc[1])), float(milestone_arr_5m.iloc[4]) / 1_000_000, '£5M ARR'))
    
    if milestone_arr_10m is not None:
        _milestones_arr.append((pd.to_datetime(str(milestone_arr_10m.iloc[1])), float(milestone_arr_10m.iloc[4]) / 1_000_000, '£10M ARR'))
    
    for _milestone_date, _milestone_value, _label in _milestones_arr:
        arr_mrr_fig.add_trace(
            go.Scatter(
                x=[_milestone_date],
                y=[_milestone_value],
                mode='markers+text',
                marker=dict(size=12, color='red', symbol='star'),
                text=[_label],
                textposition='top center',
                showlegend=False,
                hovertemplate=f'<b>{_label}</b><br>Date: %{{x}}<extra></extra>'
            )
        )

# Update layout
arr_mrr_fig.update_layout(
    title='<b>ARR & MRR Growth Trajectory</b><br><sup>5-Year Monthly Progression with Key Milestones</sup>',
    xaxis_title='<b>Date</b>',
    yaxis_title='<b>Revenue (£M)</b>',
    height=500,
    hovermode='x unified',
    template='plotly_white',
    font=dict(size=12),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    )
)

arr_mrr_fig.show()
print(f"✓ ARR/MRR trends chart created: {len(arr_growth_metrics)} months")
print(f"  Final ARR: £{arr_growth_metrics.iloc[-1]['arr']:,.0f}")
print(f"  Final MRR: £{arr_growth_metrics.iloc[-1]['mrr']:,.0f}")