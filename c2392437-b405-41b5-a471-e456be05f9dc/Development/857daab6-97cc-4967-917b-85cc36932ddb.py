"""
Consolidated Executive Dashboard Export
Combines all metrics into comprehensive export dataframes with documentation
"""
import pandas as pd
import numpy as np

# ============================================================================
# EXECUTIVE SUMMARY METRICS
# ============================================================================
executive_summary = pd.DataFrame({
    'metric': [
        'Month 60 ARR',
        'Month 60 MRR',
        'Year 5 ARR Growth Rate (YoY)',
        'Month 60 GRR (12M)',
        'Month 60 NRR (12M)',
        'Month 60 LTV:CAC Ratio',
        'Month 60 CAC Payback (months)',
        'Month 60 Rule of 40 Score',
        'Month 60 Total Customers',
        'Weighted Average LTV'
    ],
    'value': [
        arr_growth_metrics.iloc[-1]['arr'],
        arr_growth_metrics.iloc[-1]['mrr'],
        arr_growth_metrics.iloc[-1]['arr_yoy_growth'],
        latest_grr,
        latest_nrr,
        cac_ltv_metrics.iloc[-1]['ltv_cac_ratio'],
        cac_ltv_metrics.iloc[-1]['cac_payback_months'],
        rule_of_40_metrics.iloc[-1]['rule_of_40_score'],
        tier_movement_df.iloc[-1]['total_active'],
        weighted_ltv
    ]
})

print("✓ Executive Summary")
print(f"  ARR (Month 60): £{executive_summary.iloc[0]['value']:,.0f}")
print(f"  NRR (12M): {executive_summary.iloc[4]['value']:.1%}")
print(f"  LTV:CAC: {executive_summary.iloc[5]['value']:.2f}x")

# ============================================================================
# CALCULATION DOCUMENTATION
# ============================================================================
calculation_notes = pd.DataFrame({
    'metric_category': [
        'ARR Growth',
        'GRR/NRR',
        'LTV',
        'CAC',
        'CAC Payback',
        'Rule of 40',
        'Cohort Retention',
        'Revenue Mix'
    ],
    'calculation_method': [
        'ARR = MRR * 12; Growth = (Current - Previous) / Previous',
        'GRR = Retained MRR / Beginning MRR; NRR = (Retained + Expansion) / Beginning',
        'LTV = (Monthly Price * Gross Margin) / Monthly Churn Rate',
        'Blended CAC weighted by customer tier mix across channels',
        'CAC Payback = CAC / (MRR per customer)',
        'Rule of 40 = ARR Growth Rate + EBITDA Margin',
        'Cohort retention % = Current customers / Baseline cohort customers',
        'Revenue Mix = Revenue Stream / Total Revenue'
    ],
    'data_source': [
        'consolidated_revenue',
        'retention_metrics_df',
        'ltv_by_tier',
        'cac_by_channel, tier_movement_df',
        'cac_ltv_metrics',
        'arr_growth_metrics',
        'cohort_retention_curves_df',
        'revenue_mix'
    ]
})

print("✓ Calculation Documentation")
print(f"  {len(calculation_notes)} metric categories documented")

# ============================================================================
# KEY EXPORT DATAFRAMES
# ============================================================================
print("\n✓ Key Export Dataframes Available:")
print(f"  • arr_growth_metrics: {arr_growth_metrics.shape}")
print(f"  • retention_by_period: {retention_by_period.shape}")
print(f"  • cac_ltv_metrics: {cac_ltv_metrics.shape}")
print(f"  • rule_of_40_metrics: {rule_of_40_metrics.shape}")
print(f"  • revenue_mix: {revenue_mix.shape}")
print(f"  • milestones_df: {milestones_df.shape}")
print(f"  • cohort_retention_curves_df: {cohort_retention_curves_df.shape}")
print(f"  • ltv_by_tier: {len(ltv_by_tier)} tiers")
print(f"  • executive_summary: {executive_summary.shape}")

print("\n✅ Comprehensive executive dashboard metrics ready for export")