import pandas as pd

# Generate comprehensive summary output for subscription revenue model

print("=" * 70)
print("SUBSCRIPTION REVENUE MODEL - 60-MONTH PROJECTION")
print("=" * 70)

# ARR Milestones
print("\n📊 ARR MILESTONES")
print("-" * 70)
arr_m12 = subscription_mrr_df[subscription_mrr_df['month']==12]['arr'].values[0]
arr_m24 = subscription_mrr_df[subscription_mrr_df['month']==24]['arr'].values[0]
arr_m36 = subscription_mrr_df[subscription_mrr_df['month']==36]['arr'].values[0]
arr_m48 = subscription_mrr_df[subscription_mrr_df['month']==48]['arr'].values[0]
arr_m60 = subscription_mrr_df[subscription_mrr_df['month']==60]['arr'].values[0]

print(f"Year 1 (Month 12): £{arr_m12:,.0f}")
print(f"Year 2 (Month 24): £{arr_m24:,.0f}")
print(f"Year 3 (Month 36): £{arr_m36:,.0f}")
print(f"Year 4 (Month 48): £{arr_m48:,.0f}")
print(f"Year 5 (Month 60): £{arr_m60:,.0f}")

# Key £ Milestones
milestone_1m = subscription_mrr_df[subscription_mrr_df['arr'] >= 1_000_000]['month'].min()
milestone_5m = subscription_mrr_df[subscription_mrr_df['arr'] >= 5_000_000]['month'].min()
milestone_10m = subscription_mrr_df[subscription_mrr_df['arr'] >= 10_000_000]['month'].min()

print(f"\n🎯 Key Milestones Reached:")
if not pd.isna(milestone_1m):
    print(f"  £1M ARR: Month {milestone_1m}")
if not pd.isna(milestone_5m):
    print(f"  £5M ARR: Month {milestone_5m}")
if not pd.isna(milestone_10m):
    print(f"  £10M ARR: Month {milestone_10m}")

# Customer Counts
print(f"\n👥 CUSTOMER COUNTS BY TIER (Year 5)")
print("-" * 70)
y5_data = tier_movement_df[tier_movement_df['month']==60].iloc[0]
print(f"Starter:    {y5_data['net_starter']:,.0f} customers")
print(f"Growth:     {y5_data['net_growth']:,.0f} customers")
print(f"Scale:      {y5_data['net_scale']:,.0f} customers")
print(f"Enterprise: {y5_data['net_enterprise']:,.0f} customers")
print(f"TOTAL:      {y5_data['net_starter'] + y5_data['net_growth'] + y5_data['net_scale'] + y5_data['net_enterprise']:,.0f} customers")

# MRR Breakdown Year 5
print(f"\n💰 MRR BREAKDOWN (Month 60)")
print("-" * 70)
mrr_y5 = subscription_mrr_df[subscription_mrr_df['month']==60].iloc[0]
print(f"Base MRR:      £{mrr_y5['total_base_mrr']:,.0f}")
print(f"Expansion MRR: £{mrr_y5['expansion_mrr']:,.0f}")
print(f"TOTAL MRR:     £{mrr_y5['total_mrr']:,.0f}")

# Retention Metrics
print(f"\n📈 RETENTION METRICS (Latest 6-month avg)")
print("-" * 70)
latest_ret = retention_metrics_df.iloc[-1]
print(f"GRR (Gross Revenue Retention): {latest_ret['grr_avg']:.1%}")
print(f"NRR (Net Revenue Retention):   {latest_ret['nrr_avg']:.1%}")
print(f"\nBenchmarks:")
print(f"  GRR Target: 92-95%")
print(f"  NRR Target: 110-120% (Enterprise)")

# LTV Summary
print(f"\n💎 LIFETIME VALUE BY TIER")
print("-" * 70)
for tier, data in ltv_by_tier.items():
    print(f"{tier:12} LTV: £{data['ltv_gbp']:>10,.0f}  |  Retention: {data['annual_retention']:.0%}")

print(f"\nWeighted Avg LTV (Y5 mix): £{weighted_ltv:,.0f}")

# Upgrade Activity
print(f"\n⬆️  TIER UPGRADE ACTIVITY (Cumulative 60 months)")
print("-" * 70)
total_upgrades = upgrade_df[['starter_to_growth', 'growth_to_scale', 'scale_to_enterprise']].sum()
print(f"Starter → Growth:     {total_upgrades['starter_to_growth']:,.0f} upgrades")
print(f"Growth → Scale:       {total_upgrades['growth_to_scale']:,.0f} upgrades")
print(f"Scale → Enterprise:   {total_upgrades['scale_to_enterprise']:,.0f} upgrades")

print(f"\n{'=' * 70}")
print("✅ Subscription revenue baseline established")
print("=" * 70)