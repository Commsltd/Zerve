"""
Token Consumption Analytics Dashboard
Comprehensive summary of token economics model outputs
"""
import pandas as pd
import matplotlib.pyplot as plt

# Create comprehensive analytics summary
analytics_summary = {
    'consumption_patterns': {
        'by_segment': consumption_df.to_dict('index'),
        'by_activity': {
            'monitoring_pct': (total_token_consumption['monitoring_tokens'] / 
                             total_token_consumption['total_tokens']) * 100,
            'search_pct': (total_token_consumption['search_tokens'] / 
                          total_token_consumption['total_tokens']) * 100,
            'reports_pct': (total_token_consumption['report_tokens'] / 
                           total_token_consumption['total_tokens']) * 100
        }
    },
    'revenue_metrics': {
        'monthly_revenue': revenue_summary,
        'annual_projection': total_monthly_revenue * 12,
        'revenue_mix': {
            'subscription_pct': (subscription_revenue / total_monthly_revenue) * 100,
            'overage_pct': (total_overage_revenue / total_monthly_revenue) * 100,
            'payg_pct': (payg_revenue_total / total_monthly_revenue) * 100
        }
    },
    'pricing_analytics': {
        'effective_price_gbp': effective_token_price,
        'payg_rate_gbp': payg_rate_gbp,
        'overage_rate_gbp': overage_rate_gbp,
        'discount_to_payg_pct': ((payg_rate_gbp - effective_token_price) / payg_rate_gbp) * 100
    },
    'network_effects': {
        'velocity_multipliers': velocity_df['token_velocity'].to_dict(),
        'year_5_velocity': velocity_df.iloc[4]['token_velocity'],
        'contributor_offset_pct': avg_reward_offset_pct * 100
    },
    'customer_economics': {
        'total_customers': revenue_summary['total_customers'],
        'subscription_customers': sum(customer_base.values()),
        'payg_customers': sum(payg_customers.values()),
        'revenue_per_customer': revenue_summary['revenue_per_customer'],
        'annual_revenue_per_customer': revenue_summary['revenue_per_customer'] * 12
    }
}

# Create visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Token Consumption Revenue Engine Analytics', fontsize=16, fontweight='bold')

# 1. Token consumption by activity type
activity_labels = ['Monitoring', 'Search', 'Reports']
activity_values = [
    total_token_consumption['monitoring_tokens'],
    total_token_consumption['search_tokens'],
    total_token_consumption['report_tokens']
]
axes[0, 0].pie(activity_values, labels=activity_labels, autopct='%1.1f%%', startangle=90)
axes[0, 0].set_title('Token Consumption by Activity Type')

# 2. Revenue mix
revenue_labels = ['Subscription', 'Overage', 'PAYG']
revenue_values = [subscription_revenue, total_overage_revenue, payg_revenue_total]
axes[0, 1].bar(revenue_labels, revenue_values, color=['#4CAF50', '#FFC107', '#2196F3'])
axes[0, 1].set_title('Monthly Revenue by Source')
axes[0, 1].set_ylabel('Revenue (£)')
axes[0, 1].ticklabel_format(style='plain', axis='y')

# 3. Network velocity progression
years = [1, 2, 3, 4, 5]
velocities = [velocity_df.iloc[_y - 1]['token_velocity'] for _y in years]
axes[1, 0].plot(years, velocities, marker='o', linewidth=2, markersize=8, color='#9C27B0')
axes[1, 0].set_title('Token Velocity Growth (NVM Impact)')
axes[1, 0].set_xlabel('Year')
axes[1, 0].set_ylabel('Velocity Multiplier')
axes[1, 0].grid(True, alpha=0.3)

# 4. Overage revenue by tier
tier_names = list(overage_revenue_by_tier.keys())
tier_overage = list(overage_revenue_by_tier.values())
axes[1, 1].barh(tier_names, tier_overage, color='#FF5722')
axes[1, 1].set_title('Monthly Overage Revenue by Tier')
axes[1, 1].set_xlabel('Overage Revenue (£)')

plt.tight_layout()

print("TOKEN CONSUMPTION ANALYTICS DASHBOARD")
print("="*80)
print(f"\n📊 REVENUE SUMMARY (Monthly)")
print(f"   Total Revenue:          £{total_monthly_revenue:,.0f}")
print(f"   Subscription (93.5%):   £{subscription_revenue:,.0f}")
print(f"   Overage (3.4%):         £{total_overage_revenue:,.0f}")
print(f"   PAYG (3.1%):            £{payg_revenue_total:,.0f}")
print(f"   Annual Projection:      £{analytics_summary['revenue_metrics']['annual_projection']:,.0f}")

print(f"\n🎯 TOKEN CONSUMPTION (Monthly)")
print(f"   Total Tokens:           {total_token_consumption['total_tokens']:,.0f}")
print(f"   Monitoring (74.4%):     {total_token_consumption['monitoring_tokens']:,.0f}")
print(f"   Search (23.8%):         {total_token_consumption['search_tokens']:,.0f}")
print(f"   Reports (1.9%):         {total_token_consumption['report_tokens']:,.0f}")

print(f"\n💰 PRICING ANALYTICS")
print(f"   Effective Token Price:  £{effective_token_price:.3f}/token")
print(f"   PAYG Rate:              £{payg_rate_gbp:.2f}/token")
print(f"   Overage Rate:           £{overage_rate_gbp:.2f}/token")
print(f"   Subscription Discount:  {analytics_summary['pricing_analytics']['discount_to_payg_pct']:.1f}% vs PAYG")

print(f"\n🚀 NETWORK EFFECTS")
print(f"   Year 1 Velocity:        {velocity_df.iloc[0]['token_velocity']:.2f}x")
print(f"   Year 5 Velocity:        {analytics_summary['network_effects']['year_5_velocity']:.2f}x")
print(f"   Velocity Growth:        +{(analytics_summary['network_effects']['year_5_velocity'] - 1) * 100:.0f}%")
print(f"   Contributor Offset:     ~{analytics_summary['network_effects']['contributor_offset_pct']:.1f}%")

print(f"\n👥 CUSTOMER ECONOMICS")
print(f"   Total Customers:        {analytics_summary['customer_economics']['total_customers']}")
print(f"   Revenue/Customer:       £{revenue_summary['revenue_per_customer']:,.0f}/month")
print(f"   Annual/Customer:        £{analytics_summary['customer_economics']['annual_revenue_per_customer']:,.0f}")

print("\n" + "="*80)