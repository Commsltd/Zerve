"""
Executive Dashboard Metrics Export
Comprehensive KPIs for investor reporting including ARR growth, retention, CAC/LTV, Rule of 40, etc.
"""
import pandas as pd
import numpy as np

# ============================================================================
# 1. ARR GROWTH METRICS
# ============================================================================
arr_growth_metrics = pd.DataFrame({
    'month': consolidated_revenue['month'],
    'date': consolidated_revenue['date'],
    'year': consolidated_revenue['year'],
    'quarter': consolidated_revenue['quarter'],
    'arr': consolidated_revenue['base_arr'],
    'mrr': consolidated_revenue['base_monthly_revenue']
})

# Calculate growth rates
arr_growth_metrics['arr_mom_growth'] = arr_growth_metrics['arr'].pct_change()
arr_growth_metrics['mrr_mom_growth'] = arr_growth_metrics['mrr'].pct_change()

# YoY growth (when available)
arr_growth_metrics['arr_yoy_growth'] = arr_growth_metrics['arr'].pct_change(periods=12)

# Key milestones
milestone_arr_1m = arr_growth_metrics[arr_growth_metrics['arr'] >= 1_000_000].iloc[0] if len(arr_growth_metrics[arr_growth_metrics['arr'] >= 1_000_000]) > 0 else None
milestone_arr_5m = arr_growth_metrics[arr_growth_metrics['arr'] >= 5_000_000].iloc[0] if len(arr_growth_metrics[arr_growth_metrics['arr'] >= 5_000_000]) > 0 else None
milestone_arr_10m = arr_growth_metrics[arr_growth_metrics['arr'] >= 10_000_000].iloc[0] if len(arr_growth_metrics[arr_growth_metrics['arr'] >= 10_000_000]) > 0 else None

print("✓ ARR Growth Metrics Calculated")
print(f"  Month 12 ARR: £{arr_growth_metrics.iloc[11]['arr']:,.0f}")
print(f"  Month 24 ARR: £{arr_growth_metrics.iloc[23]['arr']:,.0f}")
print(f"  Month 60 ARR: £{arr_growth_metrics.iloc[59]['arr']:,.0f}")

# ============================================================================
# 2. NRR/GRR BY PERIOD
# ============================================================================
retention_by_period = retention_metrics_df.copy()
retention_by_period['date'] = timeline_df['date'].iloc[1:61]  # retention starts at month 2
retention_by_period['year'] = timeline_df['year'].iloc[1:61]
retention_by_period['quarter'] = timeline_df['quarter'].iloc[1:61]

# Latest metrics
latest_grr = retention_by_period.iloc[-1]['grr_12m']
latest_nrr = retention_by_period.iloc[-1]['nrr_12m']

print("✓ Retention Metrics (NRR/GRR)")
print(f"  Latest 12M GRR: {latest_grr:.1%}")
print(f"  Latest 12M NRR: {latest_nrr:.1%}")

# ============================================================================
# 3. CAC PAYBACK & LTV:CAC RATIOS
# ============================================================================
# Calculate blended CAC based on customer mix
_blended_cac_by_month = []
for _m in range(60):
    _tier_mix = tier_movement_df.iloc[_m]
    _total_customers = _tier_mix['total_active']
    
    if _total_customers > 0:
        # Map tiers to CAC channels (simplified assumptions)
        _starter_cac = cac_by_channel['beta_digital']['avg_cac_gbp']
        _growth_cac = cac_by_channel['launch_mixed']['avg_cac_gbp']
        _scale_cac = cac_by_channel['launch_mixed']['avg_cac_gbp']
        _enterprise_cac = cac_by_channel['enterprise_outbound']['avg_cac_gbp']
        
        _blended = (
            _tier_mix['net_starter'] * _starter_cac +
            _tier_mix['net_growth'] * _growth_cac +
            _tier_mix['net_scale'] * _scale_cac +
            _tier_mix['net_enterprise'] * _enterprise_cac
        ) / _total_customers
    else:
        _blended = 0
    
    _blended_cac_by_month.append(_blended)

cac_ltv_metrics = pd.DataFrame({
    'month': tier_movement_df['month'],
    'blended_cac_gbp': _blended_cac_by_month,
    'total_customers': tier_movement_df['total_active']
})

# Calculate weighted LTV based on customer mix
_weighted_ltv_by_month = []
for _m in range(60):
    _tier_mix = tier_movement_df.iloc[_m]
    _total = _tier_mix['total_active']
    
    if _total > 0:
        _weighted = (
            _tier_mix['net_starter'] / _total * ltv_by_tier['Starter']['ltv_gbp'] +
            _tier_mix['net_growth'] / _total * ltv_by_tier['Growth']['ltv_gbp'] +
            _tier_mix['net_scale'] / _total * ltv_by_tier['Scale']['ltv_gbp'] +
            _tier_mix['net_enterprise'] / _total * ltv_by_tier['Enterprise']['ltv_gbp']
        )
    else:
        _weighted = 0
    
    _weighted_ltv_by_month.append(_weighted)

cac_ltv_metrics['weighted_ltv_gbp'] = _weighted_ltv_by_month
cac_ltv_metrics['ltv_cac_ratio'] = cac_ltv_metrics['weighted_ltv_gbp'] / cac_ltv_metrics['blended_cac_gbp']
cac_ltv_metrics['cac_payback_months'] = cac_ltv_metrics['blended_cac_gbp'] / (arr_growth_metrics['mrr'] / tier_movement_df['total_active'])

print("✓ CAC/LTV Metrics")
print(f"  Latest LTV:CAC Ratio: {cac_ltv_metrics.iloc[-1]['ltv_cac_ratio']:.2f}x")
print(f"  Latest CAC Payback: {cac_ltv_metrics.iloc[-1]['cac_payback_months']:.1f} months")

# ============================================================================
# 4. RULE OF 40
# ============================================================================
rule_of_40_metrics = pd.DataFrame({
    'month': arr_growth_metrics['month'],
    'year': arr_growth_metrics['year'],
    'quarter': arr_growth_metrics['quarter'],
    'arr_growth_rate': arr_growth_metrics['arr_yoy_growth'],
    'ebitda_margin': 0.85  # Using gross margin as proxy (assuming 85% per LTV calc)
})

rule_of_40_metrics['rule_of_40_score'] = (
    rule_of_40_metrics['arr_growth_rate'].fillna(0) + 
    rule_of_40_metrics['ebitda_margin']
)

print("✓ Rule of 40 Tracking")
print(f"  Year 5 Rule of 40 Score: {rule_of_40_metrics.iloc[-1]['rule_of_40_score']:.1%}")

# ============================================================================
# 5. REVENUE MIX PERCENTAGES
# ============================================================================
revenue_mix = pd.DataFrame({
    'month': consolidated_revenue['month'],
    'date': consolidated_revenue['date'],
    'year': consolidated_revenue['year'],
    'subscription_pct': consolidated_revenue['subscription_mrr'] / consolidated_revenue['base_monthly_revenue'],
    'token_overage_pct': consolidated_revenue['token_overage_revenue'] / consolidated_revenue['base_monthly_revenue'],
    'token_payg_pct': consolidated_revenue['token_payg_revenue'] / consolidated_revenue['base_monthly_revenue'],
    'invoice_finance_pct': consolidated_revenue['invoice_finance_revenue'] / consolidated_revenue['base_monthly_revenue'],
    'enterprise_licensing_pct': consolidated_revenue['enterprise_licensing_mrr'] / consolidated_revenue['base_monthly_revenue']
})

print("✓ Revenue Mix (Month 60)")
print(f"  Subscription: {revenue_mix.iloc[-1]['subscription_pct']:.1%}")
print(f"  Invoice Finance: {revenue_mix.iloc[-1]['invoice_finance_pct']:.1%}")
print(f"  Enterprise Licensing: {revenue_mix.iloc[-1]['enterprise_licensing_pct']:.1%}")

print("\n✅ Executive metrics calculated successfully")
print(f"Total metrics exported: {len(arr_growth_metrics)} months")