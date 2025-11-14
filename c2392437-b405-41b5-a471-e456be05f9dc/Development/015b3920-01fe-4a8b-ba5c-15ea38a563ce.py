"""
Revenue Integration Validation
Validates all revenue streams consolidate correctly and reconcile to expected totals
"""

import pandas as pd
import numpy as np

print("="*80)
print("REVENUE STREAM INTEGRATION VALIDATION")
print("="*80)

# 1. Validate consolidated_revenue dataframe structure
print("\n✓ Data Structure Validation:")
print(f"  Months covered: {len(consolidated_revenue)}")
print(f"  Expected: 60 months")
print(f"  Status: {'PASS' if len(consolidated_revenue) == 60 else 'FAIL'}")

# 2. Validate individual revenue streams present
print("\n✓ Revenue Streams Present:")
expected_streams = ['subscription_mrr', 'token_overage_revenue', 'token_payg_revenue', 
                    'invoice_finance_revenue', 'enterprise_licensing_mrr']
for stream in expected_streams:
    has_stream = stream in consolidated_revenue.columns
    print(f"  {stream}: {'PASS' if has_stream else 'FAIL'}")

# 3. Validate revenue consolidation logic
print("\n✓ Revenue Consolidation Reconciliation:")
_reconciliation_check = consolidated_revenue[['month', 'subscription_mrr', 'token_overage_revenue', 
                                              'token_payg_revenue', 'invoice_finance_revenue', 
                                              'enterprise_licensing_mrr', 'base_monthly_revenue']].copy()

_reconciliation_check['calculated_total'] = (
    _reconciliation_check['subscription_mrr'] +
    _reconciliation_check['token_overage_revenue'] +
    _reconciliation_check['token_payg_revenue'] +
    _reconciliation_check['invoice_finance_revenue'] +
    _reconciliation_check['enterprise_licensing_mrr']
)

_reconciliation_check['diff'] = _reconciliation_check['base_monthly_revenue'] - _reconciliation_check['calculated_total']
max_diff = _reconciliation_check['diff'].abs().max()

print(f"  Max reconciliation difference: £{max_diff:.2f}")
print(f"  Status: {'PASS' if max_diff < 0.01 else 'FAIL'}")

# 4. Validate ARR calculations
print("\n✓ ARR Calculation Validation:")
_arr_check = consolidated_revenue[['month', 'subscription_arr', 'enterprise_licensing_arr', 'base_arr']].copy()
_arr_check['monthly_to_arr'] = (
    consolidated_revenue['subscription_arr'] +
    (consolidated_revenue['token_overage_revenue'] + consolidated_revenue['token_payg_revenue']) * 12 +
    consolidated_revenue['invoice_finance_revenue'] * 12 +
    consolidated_revenue['enterprise_licensing_arr']
)
_arr_check['arr_diff'] = _arr_check['base_arr'] - _arr_check['monthly_to_arr']
max_arr_diff = _arr_check['arr_diff'].abs().max()

print(f"  Max ARR difference: £{max_arr_diff:.2f}")
print(f"  Status: {'PASS' if max_arr_diff < 0.01 else 'FAIL'}")

# 5. Validate specific milestones
print("\n✓ Key Milestone Validation:")
print(f"\n  Month 12 (Year 1 End):")
_m12 = consolidated_revenue[consolidated_revenue['month']==12].iloc[0]
print(f"    Subscription MRR: £{_m12['subscription_mrr']:,.0f}")
print(f"    Enterprise Licensing MRR: £{_m12['enterprise_licensing_mrr']:,.0f}")
print(f"    Invoice Finance: £{_m12['invoice_finance_revenue']:,.0f}")
print(f"    Total Monthly Revenue: £{_m12['base_monthly_revenue']:,.0f}")
print(f"    Base ARR: £{_m12['base_arr']:,.0f}")

print(f"\n  Month 60 (Year 5 End):")
_m60 = consolidated_revenue[consolidated_revenue['month']==60].iloc[0]
print(f"    Subscription MRR: £{_m60['subscription_mrr']:,.0f}")
print(f"    Enterprise Licensing MRR: £{_m60['enterprise_licensing_mrr']:,.0f}")
print(f"    Invoice Finance: £{_m60['invoice_finance_revenue']:,.0f}")
print(f"    Token Overage: £{_m60['token_overage_revenue']:,.0f}")
print(f"    Token PAYG: £{_m60['token_payg_revenue']:,.0f}")
print(f"    Total Monthly Revenue: £{_m60['base_monthly_revenue']:,.0f}")
print(f"    Base ARR: £{_m60['base_arr']:,.0f}")

# 6. Revenue growth validation
print("\n✓ Revenue Growth Patterns:")
_m1_rev = consolidated_revenue[consolidated_revenue['month']==1].iloc[0]['base_monthly_revenue']
_m60_rev = consolidated_revenue[consolidated_revenue['month']==60].iloc[0]['base_monthly_revenue']
_growth_rate = ((_m60_rev / _m1_rev) ** (1/59)) - 1

print(f"  Month 1 Revenue: £{_m1_rev:,.0f}")
print(f"  Month 60 Revenue: £{_m60_rev:,.0f}")
print(f"  60x Multiple: {_m60_rev / _m1_rev:.1f}x")
print(f"  Monthly Growth Rate: {_growth_rate*100:.2f}%")
print(f"  Status: {'PASS' if _m60_rev > _m1_rev else 'FAIL'}")

# 7. No negative revenue validation
print("\n✓ Data Quality Checks:")
_negative_check = (consolidated_revenue[expected_streams] < 0).any().any()
print(f"  No negative revenue values: {'PASS' if not _negative_check else 'FAIL'}")

_null_check = consolidated_revenue[expected_streams].isnull().any().any()
print(f"  No null values: {'PASS' if not _null_check else 'FAIL'}")

print("\n" + "="*80)
print("✅ VALIDATION COMPLETE")
print("="*80)