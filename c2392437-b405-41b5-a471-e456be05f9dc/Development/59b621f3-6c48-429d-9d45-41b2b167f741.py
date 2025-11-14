import plotly.graph_objects as go

# Create bar chart for geographic distribution by active regions
geographic_data = export_geographic.groupby('num_regions').agg({
    'total_monthly_revenue': 'sum'
}).reset_index()

# Map region counts to region names for better labeling
region_labels = {
    1: 'UK Only',
    2: 'UK + EU',
    3: 'UK + EU + US',
    4: 'UK + EU + US + APAC'
}

geographic_data['region_label'] = geographic_data['num_regions'].map(region_labels)

geo_fig = go.Figure(data=[
    go.Bar(
        x=geographic_data['region_label'],
        y=geographic_data['total_monthly_revenue'] / 1e9,  # Convert to billions
        marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
        text=geographic_data['total_monthly_revenue'].apply(lambda x: f'£{x/1e9:.2f}B'),
        textposition='outside'
    )
])

geo_fig.update_layout(
    title="<b>Cumulative Revenue by Geographic Expansion</b>",
    xaxis_title="<b>Active Regions</b>",
    yaxis_title="<b>Cumulative Revenue (£B)</b>",
    height=500,
    template='plotly_white',
    font=dict(size=12),
    showlegend=False
)

geo_fig.show()