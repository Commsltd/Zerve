import pandas as pd
import numpy as np

# Model seat-based expansion revenue
# Growth: 3 seats avg, Scale: 10 seats avg, Enterprise: per-seat pricing

seat_expansion_records = []

for _, tier_row in tier_movement_df.iterrows():
    month_num = int(tier_row['month'])
    
    # Growth tier: 3 seats on average, assume 30% add seats over time
    growth_base_customers = tier_row['net_growth']
    growth_seat_expansion_rate = 0.02 if month_num < 12 else 0.03  # Monthly seat addition rate
    growth_expansion_customers = growth_base_customers * growth_seat_expansion_rate
    growth_avg_extra_seats = 0.5  # Average extra seats per expanding customer
    growth_expansion_mrr = growth_expansion_customers * growth_avg_extra_seats * (tier_pricing['Growth']['monthly_price_gbp'] / 3)
    
    # Scale tier: 10 seats on average, assume 40% add seats over time
    scale_base_customers = tier_row['net_scale']
    scale_seat_expansion_rate = 0.025 if month_num < 12 else 0.035
    scale_expansion_customers = scale_base_customers * scale_seat_expansion_rate
    scale_avg_extra_seats = 2.0
    scale_expansion_mrr = scale_expansion_customers * scale_avg_extra_seats * (tier_pricing['Scale']['monthly_price_gbp'] / 10)
    
    # Enterprise tier: custom per-seat pricing
    enterprise_base_customers = tier_row['net_enterprise']
    enterprise_seat_expansion_rate = 0.03 if month_num < 12 else 0.045
    enterprise_expansion_customers = enterprise_base_customers * enterprise_seat_expansion_rate
    enterprise_avg_extra_seats = 5.0
    # Enterprise per-seat: ~£500/seat/month
    enterprise_expansion_mrr = enterprise_expansion_customers * enterprise_avg_extra_seats * 500
    
    total_expansion_mrr = growth_expansion_mrr + scale_expansion_mrr + enterprise_expansion_mrr
    
    seat_expansion_records.append({
        'month': month_num,
        'growth_expansion_mrr': growth_expansion_mrr,
        'scale_expansion_mrr': scale_expansion_mrr,
        'enterprise_expansion_mrr': enterprise_expansion_mrr,
        'total_expansion_mrr': total_expansion_mrr
    })

seat_expansion_df = pd.DataFrame(seat_expansion_records)

print(f"Seat expansion model created for {len(seat_expansion_df)} months")
print(f"\nTotal expansion MRR by Year 5: £{seat_expansion_df[seat_expansion_df['month']==60]['total_expansion_mrr'].values[0]:,.0f}")
print(f"Cumulative expansion ARR over 60 months: £{seat_expansion_df['total_expansion_mrr'].sum() * 12 / 60:,.0f}")