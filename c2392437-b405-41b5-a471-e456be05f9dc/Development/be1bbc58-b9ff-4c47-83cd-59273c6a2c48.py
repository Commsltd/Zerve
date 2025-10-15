import pandas as pd
import numpy as np

# Calculate NRR (Net Revenue Retention) and GRR (Gross Revenue Retention)
# Key SaaS metrics for investor benchmarks

retention_records = []

for month_idx in range(2, 61):  # Start from month 2
    # Get beginning cohort (customers from 12 months ago)
    if month_idx >= 13:
        cohort_start_month = month_idx - 12
        
        # Beginning MRR (12 months ago)
        beginning_mrr = subscription_mrr_df[subscription_mrr_df['month'] == cohort_start_month]['total_base_mrr'].values[0]
        
        # Current cohort's retained MRR
        # Filter cohort_df for customers acquired in cohort_start_month
        cohort_now = cohort_df[
            (cohort_df['cohort_month'] == cohort_start_month) & 
            (cohort_df['current_month'] == month_idx)
        ]
        
        if len(cohort_now) > 0:
            cohort_customers_retained = (
                cohort_now['starter_count'].values[0] +
                cohort_now['growth_count'].values[0] +
                cohort_now['scale_count'].values[0] +
                cohort_now['enterprise_count'].values[0]
            )
            
            # Approximate retained MRR (simplified - using survival rate)
            survival_rate = cohort_customers_retained / (
                acquisition_df[acquisition_df['month'] == cohort_start_month]['new_starter'].values[0] +
                acquisition_df[acquisition_df['month'] == cohort_start_month]['new_growth'].values[0] +
                acquisition_df[acquisition_df['month'] == cohort_start_month]['new_scale'].values[0] +
                acquisition_df[acquisition_df['month'] == cohort_start_month]['new_enterprise'].values[0]
            )
            
            retained_mrr = beginning_mrr * survival_rate
            
            # GRR: retained / beginning (no expansion)
            grr = retained_mrr / beginning_mrr if beginning_mrr > 0 else 0
            
            # NRR: (retained + expansion) / beginning
            # Add expansion from seat growth
            expansion_contribution = seat_expansion_df[seat_expansion_df['month'] == month_idx]['total_expansion_mrr'].values[0] * 0.1  # Approximate 10% from this cohort
            nrr = (retained_mrr + expansion_contribution) / beginning_mrr if beginning_mrr > 0 else 0
            
        else:
            grr = 0
            nrr = 0
    else:
        grr = 1.0  # Not enough history
        nrr = 1.0
    
    retention_records.append({
        'month': month_idx,
        'grr_12m': grr,
        'nrr_12m': nrr
    })

retention_metrics_df = pd.DataFrame(retention_records)

# Calculate rolling averages for benchmarking
retention_metrics_df['grr_avg'] = retention_metrics_df['grr_12m'].rolling(window=6, min_periods=1).mean()
retention_metrics_df['nrr_avg'] = retention_metrics_df['nrr_12m'].rolling(window=6, min_periods=1).mean()

print(f"Retention metrics calculated for {len(retention_metrics_df)} months")
print(f"\nBenchmark Comparison (Latest 6-month avg):")
latest_grr = retention_metrics_df.iloc[-1]['grr_avg']
latest_nrr = retention_metrics_df.iloc[-1]['nrr_avg']
print(f"  GRR: {latest_grr:.1%} (Target: 92-95%)")
print(f"  NRR: {latest_nrr:.1%} (Target: 110-120%)")