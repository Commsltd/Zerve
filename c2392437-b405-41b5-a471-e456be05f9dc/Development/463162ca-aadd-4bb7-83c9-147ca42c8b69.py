"""
Token Revenue Consolidation
Aggregates monthly token revenue by consumption type, tier, and customer type
"""
import pandas as pd

# Assume customer base distribution across tiers (for Year 2 baseline)
customer_base = {
    'Starter': 250,
    'Growth': 180,
    'Scale': 65,
    'Enterprise': 25
}

payg_customers = {
    'micro_payg': 80,
    'small_payg': 45
}

# Monthly token revenue calculations
monthly_token_revenue = {}

# 1. Subscription revenue (base pricing)
subscription_revenue = 0
for _tier, _count in customer_base.items():
    _price = tier_segment_mapping[_tier]['monthly_price_gbp']
    subscription_revenue += _price * _count

# 2. Overage revenue by tier
overage_revenue_by_tier = {}
total_overage_revenue = 0
for _tier, _count in customer_base.items():
    _overage_per_customer = tier_overage_analysis[_tier]['overage_revenue_gbp']
    _tier_overage_rev = _overage_per_customer * _count
    overage_revenue_by_tier[_tier] = _tier_overage_rev
    total_overage_revenue += _tier_overage_rev

# 3. PAYG revenue
payg_revenue_total = 0
payg_revenue_breakdown = {}
for _profile, _count in payg_customers.items():
    _rev_per_customer = payg_revenue_model[_profile]['monthly_revenue_per_customer']
    _profile_revenue = _rev_per_customer * _count
    payg_revenue_breakdown[_profile] = _profile_revenue
    payg_revenue_total += _profile_revenue

# 4. Token consumption by type (aggregated across all customers)
total_monitoring_tokens = 0
total_search_tokens = 0
total_report_tokens = 0

for _tier, _count in customer_base.items():
    _segments = tier_segment_mapping[_tier]['segment_split']
    for _seg, _weight in _segments.items():
        _seg_customers = _count * _weight
        _consumption = consumption_by_segment[_seg]
        total_monitoring_tokens += _consumption['tokens_monitoring'] * _seg_customers
        total_search_tokens += _consumption['tokens_search'] * _seg_customers
        total_report_tokens += _consumption['tokens_reports'] * _seg_customers

total_token_consumption = {
    'monitoring_tokens': total_monitoring_tokens,
    'search_tokens': total_search_tokens,
    'report_tokens': total_report_tokens,
    'total_tokens': total_monitoring_tokens + total_search_tokens + total_report_tokens
}

# 5. Total monthly token revenue
total_monthly_revenue = subscription_revenue + total_overage_revenue + payg_revenue_total

# 6. Effective token price (blended across all revenue and consumption)
effective_token_price = total_monthly_revenue / total_token_consumption['total_tokens']

revenue_summary = {
    'subscription_revenue': subscription_revenue,
    'overage_revenue': total_overage_revenue,
    'payg_revenue': payg_revenue_total,
    'total_monthly_revenue': total_monthly_revenue,
    'total_customers': sum(customer_base.values()) + sum(payg_customers.values()),
    'revenue_per_customer': total_monthly_revenue / (sum(customer_base.values()) + sum(payg_customers.values())),
    'effective_token_price': effective_token_price
}

print("Monthly Token Revenue Consolidation")
print("="*70)
print(f"\nCustomer Base: {sum(customer_base.values())} subscription + {sum(payg_customers.values())} PAYG")
print(f"\nRevenue Breakdown:")
print(f"  Subscription Revenue: £{subscription_revenue:,.0f}/month")
print(f"  Overage Revenue:      £{total_overage_revenue:,.0f}/month")
print(f"  PAYG Revenue:         £{payg_revenue_total:,.0f}/month")
print(f"  ───────────────────────────────")
print(f"  Total Monthly Revenue: £{total_monthly_revenue:,.0f}")
print(f"\nToken Consumption by Type:")
print(f"  Monitoring: {total_token_consumption['monitoring_tokens']:,.0f} tokens")
print(f"  Search:     {total_token_consumption['search_tokens']:,.0f} tokens")
print(f"  Reports:    {total_token_consumption['report_tokens']:,.0f} tokens")
print(f"  Total:      {total_token_consumption['total_tokens']:,.0f} tokens/month")
print(f"\nEffective Token Price: £{effective_token_price:.3f}/token")
print(f"Revenue per Customer: £{revenue_summary['revenue_per_customer']:.0f}/month")