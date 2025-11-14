import pandas as pd
import numpy as np

# Build cohort-based customer tracking with churn
# Track each cohort (acquisition month) through its lifecycle

cohort_records = []

for acq_month in range(1, 61):
    # Get new customers acquired in this month
    acq_row = acquisition_df[acquisition_df['month'] == acq_month].iloc[0]
    
    cohort_data = {
        'cohort_month': acq_month,
        'starter_acquired': acq_row['new_starter'],
        'growth_acquired': acq_row['new_growth'],
        'scale_acquired': acq_row['new_scale'],
        'enterprise_acquired': acq_row['new_enterprise']
    }
    
    # Track this cohort forward through all subsequent months
    for current_month in range(acq_month, 61):
        months_since_acq = current_month - acq_month
        
        # Apply monthly churn rates to calculate surviving customers
        starter_survival = (1 - churn_rates['starter']['monthly_churn_rate']) ** months_since_acq
        growth_survival = (1 - churn_rates['growth']['monthly_churn_rate']) ** months_since_acq
        scale_survival = (1 - churn_rates['scale']['monthly_churn_rate']) ** months_since_acq
        enterprise_survival = (1 - churn_rates['enterprise']['monthly_churn_rate']) ** months_since_acq
        
        cohort_records.append({
            'cohort_month': acq_month,
            'current_month': current_month,
            'months_since_acquisition': months_since_acq,
            'starter_count': cohort_data['starter_acquired'] * starter_survival,
            'growth_count': cohort_data['growth_acquired'] * growth_survival,
            'scale_count': cohort_data['scale_acquired'] * scale_survival,
            'enterprise_count': cohort_data['enterprise_acquired'] * enterprise_survival
        })

cohort_df = pd.DataFrame(cohort_records)

# Calculate total active customers by month by tier
active_customers_df = cohort_df.groupby('current_month').agg({
    'starter_count': 'sum',
    'growth_count': 'sum',
    'scale_count': 'sum',
    'enterprise_count': 'sum'
}).reset_index()

active_customers_df.columns = ['month', 'active_starter', 'active_growth', 'active_scale', 'active_enterprise']
active_customers_df['total_active'] = (
    active_customers_df['active_starter'] + 
    active_customers_df['active_growth'] + 
    active_customers_df['active_scale'] + 
    active_customers_df['active_enterprise']
)

print(f"Cohort tracking created: {len(cohort_df)} cohort-month records")
print(f"\nActive customers by end of Year 1: {int(active_customers_df[active_customers_df['month']==12]['total_active'].values[0]):,}")
print(f"Active customers by end of Year 3: {int(active_customers_df[active_customers_df['month']==36]['total_active'].values[0]):,}")
print(f"Active customers by end of Year 5: {int(active_customers_df[active_customers_df['month']==60]['total_active'].values[0]):,}")