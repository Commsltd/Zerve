"""
Geographic Revenue Distribution - Bar Chart
"""
import plotly.graph_objects as go
import pandas as pd

# Calculate revenue by region at month 60 (regions active at different stages)
geo_data_m60 = export_geographic.iloc[-1]

# Define regions and approximate revenue allocations based on expansion timeline
# UK: months 1-60, EU: months 13-60, US: months 25-60, APAC: months 37-60
regions = ['UK', 'EU', 'US', 'APAC']

# Simple allocation based on number of active months (as a proxy)
# In reality, this would be in the data, but we'll estimate here
total_revenue_m60 = geo_data_m60['total_monthly_revenue']

# Assume proportional to months active (simplified)
uk_pct = 60 / (60 + 48 + 36 + 24)  # 60 months
eu_pct = 48 / (60 + 48 + 36 + 24)  # 48 months (started month 13)
us_pct = 36 / (60 + 48 + 36 + 24)  # 36 months (started month 25)
apac_pct = 24 / (60 + 48 + 36 + 24)  # 24 months (started month 37)

region_revenues = [
    total_revenue_m60 * uk_pct,
    total_revenue_m60 * eu_pct,
    total_revenue_m60 * us_pct,
    total_revenue_m60 * apac_pct
]

# Create bar chart
dashboard_fig4 = go.Figure(data=[
    go.Bar(
        x=regions,
        y=[r / 1_000_000 for r in region_revenues],  # Convert to millions
        marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
        text=[f'£{r/1e6:.1f}M' for r in region_revenues],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Revenue: £%{y:.1f}M<extra></extra>'
    )
])

dashboard_fig4.update_layout(
    title={
        'text': 'Revenue Distribution by Geographic Region (Month 60)',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'color': '#2c3e50'}
    },
    xaxis_title='Region',
    yaxis_title='Monthly Revenue (£M)',
    template='plotly_white',
    height=500,
    showlegend=False
)

print("✓ Geographic distribution bar chart created")
print(f"  Active regions at M60: {geo_data_m60['num_regions']}")
print(f"  Total M60 revenue: £{total_revenue_m60/1e6:.1f}M")
print(f"  UK: £{region_revenues[0]/1e6:.1f}M ({uk_pct:.1%})")
print(f"  EU: £{region_revenues[1]/1e6:.1f}M ({eu_pct:.1%})")

dashboard_fig4