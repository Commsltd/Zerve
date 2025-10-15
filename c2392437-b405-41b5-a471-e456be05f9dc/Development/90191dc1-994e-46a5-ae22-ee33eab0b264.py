"""
COMPREHENSIVE EXECUTIVE DASHBOARD
All key investor metrics in single view
"""
import pandas as pd
import numpy as np

# Extract latest month data
m60_rev = consolidated_revenue[consolidated_revenue['month'] == 60].iloc[0]
m60_cust = tier_movement_df[tier_movement_df['month'] == 60].iloc[0]
m60_ret = retention_metrics_df.iloc[-1]

# Yearly ARR
y_arr = consolidated_revenue.groupby('year')['base_arr'].last()

print("=" * 90)
print("EXECUTIVE DASHBOARD - KEY INVESTOR METRICS")
print("=" * 90)

# ARR/MRR Section
print("\n📊 ARR & MRR TRENDS")
print("-" * 90)
for y in [1, 2, 3, 4, 5]:
    arr_val = y_arr[y]
    if y > 1:
        growth = (y_arr[y] / y_arr[y-1] - 1) * 100
        print(f"Year {y}: £{arr_val:>15,.0f}  |  YoY Growth: {growth:>6.1f}%")
    else:
        print(f"Year {y}: £{arr_val:>15,.0f}")

print(f"\nMonth 60 MRR: £{m60_rev['base_monthly_revenue']:,.0f}")
print(f"Month 60 ARR: £{m60_rev['base_arr']:,.0f}")

# Revenue Mix
print("\n💰 REVENUE MIX (Month 60 - % of Total MRR)")
print("-" * 90)
total_mrr = m60_rev['base_monthly_revenue']
print(f"Subscription:        {m60_rev['subscription_mrr']/total_mrr*100:>5.1f}%  (£{m60_rev['subscription_mrr']:,.0f})")
print(f"Token Overage:       {m60_rev['token_overage_revenue']/total_mrr*100:>5.1f}%  (£{m60_rev['token_overage_revenue']:,.0f})")
print(f"Token PAYG:          {m60_rev['token_payg_revenue']/total_mrr*100:>5.1f}%  (£{m60_rev['token_payg_revenue']:,.0f})")
print(f"Invoice Finance:     {m60_rev['invoice_finance_revenue']/total_mrr*100:>5.1f}%  (£{m60_rev['invoice_finance_revenue']:,.0f})")
print(f"Ent Licensing:       {m60_rev['enterprise_licensing_mrr']/total_mrr*100:>5.1f}%  (£{m60_rev['enterprise_licensing_mrr']:,.0f})")

# Customer Counts
print("\n👥 CUSTOMER COUNTS BY TIER (Month 60)")
print("-" * 90)
print(f"Starter:     {int(m60_cust['net_starter']):>7,}")
print(f"Growth:      {int(m60_cust['net_growth']):>7,}")
print(f"Scale:       {int(m60_cust['net_scale']):>7,}")
print(f"Enterprise:  {int(m60_cust['net_enterprise']):>7,}")
print(f"{'─' * 30}")
print(f"TOTAL:       {int(m60_cust['total_active']):>7,}")

# Retention
print("\n📈 RETENTION METRICS (Latest)")
print("-" * 90)
print(f"GRR (Gross Revenue Retention):  {m60_ret['grr_avg']*100:>5.1f}%")
print(f"NRR (Net Revenue Retention):    {m60_ret['nrr_avg']*100:>5.1f}%")
print(f"\nTarget Benchmarks:")
print(f"  GRR: 92-95% (Enterprise SaaS)")
print(f"  NRR: 110-120% (Best-in-class)")

# LTV by Tier
print("\n💎 LIFETIME VALUE BY TIER")
print("-" * 90)
for tier in ['Starter', 'Growth', 'Scale', 'Enterprise']:
    ltv_val = ltv_by_tier[tier]['ltv_gbp']
    retention_rate = ltv_by_tier[tier]['annual_retention']
    print(f"{tier:12} LTV: £{ltv_val:>12,.0f}  |  Retention: {retention_rate*100:>5.1f}%")
print(f"\nWeighted Avg LTV: £{weighted_ltv:,.0f}")

# CAC Metrics
print("\n💸 CAC & PAYBACK METRICS")
print("-" * 90)
cac_vals = {
    'Stealth/Partnerships': cac_by_channel['stealth_partnerships']['avg_cac_gbp'],
    'Beta/Digital': cac_by_channel['beta_digital']['avg_cac_gbp'],
    'Launch/Mixed': cac_by_channel['launch_mixed']['avg_cac_gbp'],
    'Enterprise/Outbound': cac_by_channel['enterprise_outbound']['avg_cac_gbp']
}
for ch_name, cac_val in cac_vals.items():
    print(f"{ch_name:25} CAC: £{cac_val:>7,.0f}")

# LTV:CAC Ratios
print("\nLTV:CAC RATIOS BY TIER")
starter_ltv_cac = ltv_by_tier['Starter']['ltv_gbp'] / cac_vals['Beta/Digital']
growth_ltv_cac = ltv_by_tier['Growth']['ltv_gbp'] / cac_vals['Launch/Mixed']
scale_ltv_cac = ltv_by_tier['Scale']['ltv_gbp'] / cac_vals['Launch/Mixed']
ent_ltv_cac = ltv_by_tier['Enterprise']['ltv_gbp'] / cac_vals['Enterprise/Outbound']

print(f"Starter:     {starter_ltv_cac:>6.1f}x")
print(f"Growth:      {growth_ltv_cac:>6.1f}x")
print(f"Scale:       {scale_ltv_cac:>6.1f}x")
print(f"Enterprise:  {ent_ltv_cac:>6.1f}x")
print(f"Target: 3-5x for healthy SaaS economics")

# CAC Payback (months)
gm = 0.85
print("\nCAC PAYBACK PERIODS (Months)")
starter_payback = cac_vals['Beta/Digital'] / (ltv_by_tier['Starter']['monthly_price'] * gm)
growth_payback = cac_vals['Launch/Mixed'] / (ltv_by_tier['Growth']['monthly_price'] * gm)
scale_payback = cac_vals['Launch/Mixed'] / (ltv_by_tier['Scale']['monthly_price'] * gm)
ent_payback = cac_vals['Enterprise/Outbound'] / (ltv_by_tier['Enterprise']['monthly_price'] * gm)

print(f"Starter:     {starter_payback:>5.1f} months")
print(f"Growth:      {growth_payback:>5.1f} months")
print(f"Scale:       {scale_payback:>5.1f} months")
print(f"Enterprise:  {ent_payback:>5.1f} months")
print(f"Target: <12 months for efficient growth")

# Rule of 40
y5_growth_pct = (y_arr[5] / y_arr[4] - 1) * 100
rule_40 = y5_growth_pct + (gm * 100)
print("\n⚡ RULE OF 40")
print("-" * 90)
print(f"ARR Growth (Y4→Y5):  {y5_growth_pct:>6.1f}%")
print(f"Gross Margin:        {gm*100:>6.1f}%")
print(f"{'─' * 40}")
print(f"Rule of 40 Score:    {rule_40:>6.1f}")
print(f"Status: {'PASS ✓' if rule_40 >= 40 else 'BELOW TARGET'}")

# Milestones
print("\n🎯 ARR MILESTONES ACHIEVED")
print("-" * 90)
m1_month = consolidated_revenue[consolidated_revenue['base_arr'] >= 1_000_000]['month'].min()
m5_month = consolidated_revenue[consolidated_revenue['base_arr'] >= 5_000_000]['month'].min()
m10_month = consolidated_revenue[consolidated_revenue['base_arr'] >= 10_000_000]['month'].min()
m100_month = consolidated_revenue[consolidated_revenue['base_arr'] >= 100_000_000]['month'].min()

if not pd.isna(m1_month):
    print(f"£1M ARR:    Month {int(m1_month):>3}")
if not pd.isna(m5_month):
    print(f"£5M ARR:    Month {int(m5_month):>3}")
if not pd.isna(m10_month):
    print(f"£10M ARR:   Month {int(m10_month):>3}")
if not pd.isna(m100_month):
    print(f"£100M ARR:  Month {int(m100_month):>3}")

print("\n" + "=" * 90)
print("✅ DASHBOARD COMPLETE")
print("=" * 90)