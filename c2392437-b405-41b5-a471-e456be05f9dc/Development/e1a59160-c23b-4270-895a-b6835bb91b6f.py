"""
ARR/MRR Trends Over Time - Interactive Line Chart
"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Create dual-axis chart with ARR and MRR
dashboard_fig1 = make_subplots(
    specs=[[{"secondary_y": True}]],
    subplot_titles=("ARR & MRR Growth Trajectory",)
)

# ARR line
dashboard_fig1.add_trace(
    go.Scatter(
        x=arr_growth_metrics['date'],
        y=arr_growth_metrics['arr'] / 1_000_000,  # Convert to millions
        name='ARR',
        line=dict(color='#1f77b4', width=3),
        hovertemplate='<b>ARR</b><br>Date: %{x}<br>Value: £%{y:.1f}M<extra></extra>'
    ),
    secondary_y=False
)

# MRR line
dashboard_fig1.add_trace(
    go.Scatter(
        x=arr_growth_metrics['date'],
        y=arr_growth_metrics['mrr'] / 1_000_000,  # Convert to millions
        name='MRR',
        line=dict(color='#ff7f0e', width=2, dash='dash'),
        hovertemplate='<b>MRR</b><br>Date: %{x}<br>Value: £%{y:.1f}M<extra></extra>'
    ),
    secondary_y=False
)

# Update layout
dashboard_fig1.update_xaxes(title_text="Date", showgrid=True)
dashboard_fig1.update_yaxes(
    title_text="Revenue (£M)", 
    secondary_y=False,
    showgrid=True
)

dashboard_fig1.update_layout(
    title={
        'text': 'ARR & MRR Growth Over Time',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'color': '#2c3e50'}
    },
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

print("✓ ARR/MRR line chart created")
print(f"  ARR range: £{arr_growth_metrics['arr'].min()/1e6:.1f}M to £{arr_growth_metrics['arr'].max()/1e6:.1f}M")
print(f"  MRR range: £{arr_growth_metrics['mrr'].min()/1e6:.1f}M to £{arr_growth_metrics['mrr'].max()/1e6:.1f}M")

dashboard_fig1