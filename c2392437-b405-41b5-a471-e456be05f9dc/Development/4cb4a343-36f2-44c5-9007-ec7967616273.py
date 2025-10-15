"""
Calculation Engine: Churn and Cohort Tracking
Tracks customer cohorts and applies churn to calculate active customers
"""
import pandas as pd
import numpy as np

# Build cohort tracking with churn
calc_cohort_records = []

for acq_month in range(1, calc_months + 1):
    acq_row = calc_acquisition_df[calc_acquisition_df['month'] == acq_month].iloc[0]
    
    for current_month in range(acq_month, calc_months + 1):
        months_elapsed = current_month - acq_month
        
        # Apply churn survival rates
        starter_survival = (1 - calc_churn_rates['starter']['monthly_churn_rate']) ** months_elapsed
        growth_survival = (1 - calc_churn_rates['growth']['monthly_churn_rate']) ** months_elapsed
        scale_survival = (1 - calc_churn_rates['scale']['monthly_churn_rate']) ** months_elapsed
        enterprise_survival = (1 - calc_churn_rates['enterprise']['monthly_churn_rate']) ** months_elapsed
        
        calc_cohort_records.append({
            'cohort_month': acq_month,
            'current_month': current_month,
            'months_since_acquisition': months_elapsed,
            'starter_count': acq_row['new_starter'] * starter_survival,
            'growth_count': acq_row['new_growth'] * growth_survival,
            'scale_count': acq_row['new_scale'] * scale_survival,
            'enterprise_count': acq_row['new_enterprise'] * enterprise_survival
        })

calc_cohort_df = pd.DataFrame(calc_cohort_records)

# Calculate active customers per month (sum across cohorts)
calc_active_customers = calc_cohort_df.groupby('current_month').agg({
    'starter_count': 'sum',
    'growth_count': 'sum',
    'scale_count': 'sum',
    'enterprise_count': 'sum'
}).reset_index()

calc_active_customers.rename(columns={
    'current_month': 'month',
    'starter_count': 'active_starter',
    'growth_count': 'active_growth',
    'scale_count': 'active_scale',
    'enterprise_count': 'active_enterprise'
}, inplace=True)

calc_active_customers['total_active'] = (
    calc_active_customers['active_starter'] +
    calc_active_customers['active_growth'] +
    calc_active_customers['active_scale'] +
    calc_active_customers['active_enterprise']
)

print(f"✓ Cohort Tracking Complete: {len(calc_cohort_df)} cohort-month records")
print(f"  Active Customers at Month 12: {int(calc_active_customers[calc_active_customers['month']==12]['total_active'].values[0]):,}")
print(f"  Active Customers at Month 60: {int(calc_active_customers[calc_active_customers['month']==60]['total_active'].values[0]):,}")