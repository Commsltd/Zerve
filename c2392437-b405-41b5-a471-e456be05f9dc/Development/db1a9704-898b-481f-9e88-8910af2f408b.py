"""
Invoice Pool Trajectory - Growth to Critical Mass
Models addressable invoice pool from contributor base reaching Y2 targets
"""
import pandas as pd
import numpy as np

# Critical mass targets (end of Y2) from network_effects milestones
critical_mass_y2_end = {
    'invoices_processed': 35_800_000,  # 35.8M invoices
    'unique_debtors': 1_800_000,  # 1.8M debtors
    'active_contributors': 4_500,  # 4.5k contributors
    'hit_rate': 0.78  # 78% coverage
}

# Build monthly trajectory from Y1 to Y5 (60 months)
_invoice_months_range = np.arange(1, 61)

# S-curve growth to critical mass by month 24 (end Y2)
# Then continued growth to Y5
def scurve_growth(month, target_at_24, growth_after_24=1.5):
    """S-curve reaching target at month 24, then linear growth"""
    if month <= 24:
        # Logistic curve: slow start, rapid middle, slow end
        _progress = 1 / (1 + np.exp(-0.25 * (month - 12)))
        return target_at_24 * _progress
    else:
        # Post critical mass: continued growth
        _months_after = month - 24
        _growth_factor = 1 + (growth_after_24 - 1) * (_months_after / 36)
        return target_at_24 * _growth_factor

# Generate trajectories
invoice_pool_trajectory = pd.DataFrame({
    'month': _invoice_months_range,
    'year': (_invoice_months_range - 1) // 12 + 1,
    'invoices_processed': [scurve_growth(m, critical_mass_y2_end['invoices_processed'], 2.0) for m in _invoice_months_range],
    'unique_debtors': [scurve_growth(m, critical_mass_y2_end['unique_debtors'], 1.8) for m in _invoice_months_range],
    'active_contributors': [scurve_growth(m, critical_mass_y2_end['active_contributors'], 1.6) for m in _invoice_months_range],
    'hit_rate': [min(0.78, 0.45 + 0.33 * scurve_growth(m, 1.0)) for m in _invoice_months_range]  # Hit rate grows from 45% to 78%
})

# Round to integers where appropriate
invoice_pool_trajectory['invoices_processed'] = invoice_pool_trajectory['invoices_processed'].round(0).astype(int)
invoice_pool_trajectory['unique_debtors'] = invoice_pool_trajectory['unique_debtors'].round(0).astype(int)
invoice_pool_trajectory['active_contributors'] = invoice_pool_trajectory['active_contributors'].round(0).astype(int)

print(f"Invoice Pool Trajectory: {len(invoice_pool_trajectory)} months")
print(f"\nY2 End (Month 24):")
print(f"  Invoices: {invoice_pool_trajectory.loc[23, 'invoices_processed']:,.0f}")
print(f"  Debtors: {invoice_pool_trajectory.loc[23, 'unique_debtors']:,.0f}")
print(f"  Contributors: {invoice_pool_trajectory.loc[23, 'active_contributors']:,.0f}")
print(f"  Hit rate: {invoice_pool_trajectory.loc[23, 'hit_rate']:.1%}")
print(f"\nY5 End (Month 60):")
print(f"  Invoices: {invoice_pool_trajectory.loc[59, 'invoices_processed']:,.0f}")
print(f"  Debtors: {invoice_pool_trajectory.loc[59, 'unique_debtors']:,.0f}")