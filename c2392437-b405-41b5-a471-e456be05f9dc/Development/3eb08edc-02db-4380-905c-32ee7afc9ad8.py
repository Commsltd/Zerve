"""
Eligible Invoice Pool Calculation
Applies credit quality filters and model coverage to invoice pool
"""
import pandas as pd
import numpy as np

# Apply eligibility filters to invoice pool
eligible_invoices_df = invoice_pool_trajectory.copy()

# Apply hit rate (78% model coverage at maturity)
eligible_invoices_df['invoices_with_model_coverage'] = (
    eligible_invoices_df['invoices_processed'] * eligible_invoices_df['hit_rate']
).round(0).astype(int)

# Apply credit quality filters
# Assuming 65% of invoices pass credit filters (prob_late_60 <15%, confidence >0.6, credit limit ok)
credit_pass_rate_filter = 0.65

eligible_invoices_df['invoices_passing_credit_filters'] = (
    eligible_invoices_df['invoices_with_model_coverage'] * credit_pass_rate_filter
).round(0).astype(int)

# Split by risk tier distribution (40/40/20)
eligible_invoices_df['eligible_low_risk'] = (
    eligible_invoices_df['invoices_passing_credit_filters'] * risk_tier_distribution['low_risk']
).round(0).astype(int)

eligible_invoices_df['eligible_mid_risk'] = (
    eligible_invoices_df['invoices_passing_credit_filters'] * risk_tier_distribution['mid_risk']
).round(0).astype(int)

eligible_invoices_df['eligible_high_risk'] = (
    eligible_invoices_df['invoices_passing_credit_filters'] * risk_tier_distribution['high_risk']
).round(0).astype(int)

print(f"Eligible Invoice Pool Calculated")
print(f"\nY2 Q3 (Month 18 - Institutional Pilot Start):")
print(f"  Total invoices: {eligible_invoices_df.loc[17, 'invoices_processed']:,.0f}")
print(f"  With model coverage: {eligible_invoices_df.loc[17, 'invoices_with_model_coverage']:,.0f}")
print(f"  Passing credit filters: {eligible_invoices_df.loc[17, 'invoices_passing_credit_filters']:,.0f}")
print(f"    Low risk: {eligible_invoices_df.loc[17, 'eligible_low_risk']:,.0f}")
print(f"    Mid risk: {eligible_invoices_df.loc[17, 'eligible_mid_risk']:,.0f}")
print(f"    High risk: {eligible_invoices_df.loc[17, 'eligible_high_risk']:,.0f}")
print(f"\nY2 End (Month 24):")
print(f"  Passing credit filters: {eligible_invoices_df.loc[23, 'invoices_passing_credit_filters']:,.0f}")