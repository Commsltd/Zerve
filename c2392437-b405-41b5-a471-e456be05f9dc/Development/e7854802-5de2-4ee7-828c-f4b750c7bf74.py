"""
Scenario Testing - Run All Three Scenarios and Generate Comparison
Conservative, Base, and Accelerated scenarios with key revenue metrics
"""
import pandas as pd
import numpy as np

# Define scenario multipliers
scenarios_config = {
    'conservative': {
        'desc': 'Conservative: -30% conversion, +50% churn, +12mo geo delay',
        'conv': 0.70, 'churn': 1.50, 'geo_delay': 12,
        'nvm': 0.85, 'inv_attach': 0.80, 'ent_win': 0.85
    },
    'base': {
        'desc': 'Base: Plan assumptions',
        'conv': 1.00, 'churn': 1.00, 'geo_delay': 0,
        'nvm': 1.00, 'inv_attach': 1.00, 'ent_win': 1.00
    },
    'accelerated': {
        'desc': 'Accelerated: +15% conversion, -15% churn, -6mo geo',
        'conv': 1.15, 'churn': 0.85, 'geo_delay': -6,
        'nvm': 1.20, 'inv_attach': 1.50, 'ent_win': 1.15
    }
}

# Get base case revenue from integrated model
base_rev_df = consolidated_revenue.copy()

# Calculate scenario revenues with simplified impact modeling
scenario_results = []

for scenario_name, params in scenarios_config.items():
    _df = base_rev_df.copy()
    
    # Apply conversion/churn impact on subscription revenue (compound effect)
    _conv_churn_impact = params['conv'] / params['churn']
    _df['subscription_mrr_adj'] = _df['subscription_mrr'] * _conv_churn_impact
    _df['subscription_arr_adj'] = _df['subscription_arr'] * _conv_churn_impact
    
    # Apply NVM multiplier to token revenues
    _df['token_overage_adj'] = _df['token_overage_revenue'] * params['nvm']
    _df['token_payg_adj'] = _df['token_payg_revenue'] * params['nvm']
    
    # Apply invoice finance attachment rate
    _df['invoice_finance_adj'] = _df['invoice_finance_revenue'] * params['inv_attach']
    
    # Apply enterprise win rate
    _df['enterprise_mrr_adj'] = _df['enterprise_licensing_mrr'] * params['ent_win']
    _df['enterprise_arr_adj'] = _df['enterprise_licensing_arr'] * params['ent_win']
    
    # Calculate total adjusted revenue
    _df['total_mrr'] = (_df['subscription_mrr_adj'] + _df['token_overage_adj'] + 
                        _df['token_payg_adj'] + _df['invoice_finance_adj'] + 
                        _df['enterprise_mrr_adj'])
    _df['total_arr'] = (_df['subscription_arr_adj'] + 
                        (_df['token_overage_adj'] + _df['token_payg_adj']) * 12 +
                        _df['invoice_finance_adj'] * 12 + _df['enterprise_arr_adj'])
    
    # Extract key metrics
    _y1_arr = _df[_df['year'] == 1]['total_arr'].iloc[-1]
    _y2_arr = _df[_df['year'] == 2]['total_arr'].iloc[-1]
    _y3_arr = _df[_df['year'] == 3]['total_arr'].iloc[-1]
    _y4_arr = _df[_df['year'] == 4]['total_arr'].iloc[-1]
    _y5_arr = _df[_df['year'] == 5]['total_arr'].iloc[-1]
    
    _total_rev_5y = _df['total_mrr'].sum()
    
    # Find breakeven month (when total revenue exceeds a threshold)
    _cumulative_rev = _df['total_mrr'].cumsum()
    _breakeven_months = _df[_cumulative_rev > 1000000]['month'].values
    _breakeven_month = _breakeven_months[0] if len(_breakeven_months) > 0 else None
    
    scenario_results.append({
        'scenario': scenario_name,
        'description': params['desc'],
        'y1_arr': _y1_arr,
        'y2_arr': _y2_arr,
        'y3_arr': _y3_arr,
        'y4_arr': _y4_arr,
        'y5_arr': _y5_arr,
        'total_revenue_60m': _total_rev_5y,
        'breakeven_month': _breakeven_month
    })

scenario_comparison_df = pd.DataFrame(scenario_results)

print("=" * 100)
print("SCENARIO COMPARISON - ARR BY YEAR")
print("=" * 100)
print(f"\n{'Scenario':<15} {'Y1 ARR':>18} {'Y2 ARR':>18} {'Y3 ARR':>18} {'Y4 ARR':>18} {'Y5 ARR':>18}")
print("-" * 100)
for _idx, _row in scenario_comparison_df.iterrows():
    print(f"{_row['scenario']:<15} £{_row['y1_arr']:>16,.0f} £{_row['y2_arr']:>16,.0f} £{_row['y3_arr']:>16,.0f} £{_row['y4_arr']:>16,.0f} £{_row['y5_arr']:>16,.0f}")
print("=" * 100)

print(f"\n{'Scenario':<15} {'Total 5Y Revenue':>20} {'Breakeven (mo)':>15}")
print("-" * 55)
for _idx, _row in scenario_comparison_df.iterrows():
    _breakeven = f"{_row['breakeven_month']}" if _row['breakeven_month'] else "N/A"
    print(f"{_row['scenario']:<15} £{_row['total_revenue_60m']:>18,.0f}  {_breakeven:>14}")
print("=" * 55)