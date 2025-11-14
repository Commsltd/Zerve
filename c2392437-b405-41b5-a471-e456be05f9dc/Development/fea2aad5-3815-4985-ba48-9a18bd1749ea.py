"""
Sensitivity Analysis: Key Driver Impact Assessment
Test ±20% changes in conversion rates, churn, NVM, attachment rates, and win rates
"""
import pandas as pd
import numpy as np

# Define base assumptions from validation block
base_assumptions = {
    'conversion_starter_to_growth': 0.18,
    'conversion_growth_to_scale': 0.09,
    'churn_starter': 0.035,
    'churn_growth': 0.022,
    'churn_scale': 0.011,
    'churn_enterprise': 0.006,
    'nvm_multiplier_y5': 2.34,
    'invoice_attachment_rate': 0.25,  # Average across phases
    'enterprise_win_rate': 0.25
}

# Define sensitivity test: ±20% variation
sensitivity_tests = []

# Test each driver independently
drivers_to_test = [
    ('conversion_rates', ['conversion_starter_to_growth', 'conversion_growth_to_scale'], 'Conversion Rates'),
    ('churn_rates', ['churn_starter', 'churn_growth', 'churn_scale', 'churn_enterprise'], 'Churn Rates'),
    ('nvm', ['nvm_multiplier_y5'], 'Network Value Multiplier'),
    ('invoice_attachment', ['invoice_attachment_rate'], 'Invoice Finance Attachment'),
    ('enterprise_win_rate', ['enterprise_win_rate'], 'Enterprise Win Rate')
]

# Get base case scenario results
base_scenario_arr = scenario_comparison_df[scenario_comparison_df['scenario'] == 'base'].iloc[0]
base_y5_arr = base_scenario_arr['y5_arr']
base_total_rev = base_scenario_arr['total_revenue_60m']

# Calculate sensitivity for each driver
for driver_name, driver_keys, driver_label in drivers_to_test:
    # Test -20% impact
    _sensitivity_factor_low = 0.80
    _sensitivity_factor_high = 1.20
    
    # For churn, inverse relationship (lower churn = better outcomes)
    if driver_name == 'churn_rates':
        _conv_churn_impact_low = 1.0 / _sensitivity_factor_low  # -20% churn = better
        _conv_churn_impact_high = 1.0 / _sensitivity_factor_high  # +20% churn = worse
    else:
        _conv_churn_impact_low = _sensitivity_factor_low
        _conv_churn_impact_high = _sensitivity_factor_high
    
    # Simplified impact on revenue (apply to subscription base)
    if driver_name in ['conversion_rates', 'churn_rates']:
        # Impact subscription revenue
        _revenue_impact_low = base_total_rev * _conv_churn_impact_low * 0.65  # 65% subscription weight
        _revenue_impact_high = base_total_rev * _conv_churn_impact_high * 0.65
        _y5_arr_low = base_y5_arr * _conv_churn_impact_low * 0.65
        _y5_arr_high = base_y5_arr * _conv_churn_impact_high * 0.65
    elif driver_name == 'nvm':
        # Impact token revenues (~8% of total)
        _revenue_impact_low = base_total_rev * (0.92 + 0.08 * _sensitivity_factor_low)
        _revenue_impact_high = base_total_rev * (0.92 + 0.08 * _sensitivity_factor_high)
        _y5_arr_low = base_y5_arr * (0.92 + 0.08 * _sensitivity_factor_low)
        _y5_arr_high = base_y5_arr * (0.92 + 0.08 * _sensitivity_factor_high)
    elif driver_name == 'invoice_attachment':
        # Impact invoice finance (~20% of total)
        _revenue_impact_low = base_total_rev * (0.80 + 0.20 * _sensitivity_factor_low)
        _revenue_impact_high = base_total_rev * (0.80 + 0.20 * _sensitivity_factor_high)
        _y5_arr_low = base_y5_arr * (0.80 + 0.20 * _sensitivity_factor_low)
        _y5_arr_high = base_y5_arr * (0.80 + 0.20 * _sensitivity_factor_high)
    elif driver_name == 'enterprise_win_rate':
        # Impact enterprise licensing (~7% of total)
        _revenue_impact_low = base_total_rev * (0.93 + 0.07 * _sensitivity_factor_low)
        _revenue_impact_high = base_total_rev * (0.93 + 0.07 * _sensitivity_factor_high)
        _y5_arr_low = base_y5_arr * (0.93 + 0.07 * _sensitivity_factor_low)
        _y5_arr_high = base_y5_arr * (0.93 + 0.07 * _sensitivity_factor_high)
    
    # Calculate % impact
    _pct_impact_low = (_revenue_impact_low / base_total_rev - 1) * 100
    _pct_impact_high = (_revenue_impact_high / base_total_rev - 1) * 100
    
    sensitivity_tests.append({
        'driver': driver_label,
        'base_value': ', '.join([f"{base_assumptions[k]:.1%}" if k in base_assumptions else "N/A" for k in driver_keys]),
        'change_low': '-20%',
        'y5_arr_low': _y5_arr_low,
        'total_revenue_low': _revenue_impact_low,
        'pct_impact_low': _pct_impact_low,
        'change_high': '+20%',
        'y5_arr_high': _y5_arr_high,
        'total_revenue_high': _revenue_impact_high,
        'pct_impact_high': _pct_impact_high
    })

sensitivity_df = pd.DataFrame(sensitivity_tests)

print("=" * 120)
print("SENSITIVITY ANALYSIS: KEY DRIVER IMPACT (±20% CHANGE)")
print("=" * 120)
print(f"\nBase Case: Y5 ARR = £{base_y5_arr:,.0f}, Total 5Y Revenue = £{base_total_rev:,.0f}")
print("\n" + "-" * 120)
print(f"{'Driver':<30} {'Base Value':<20} {'-20% Impact':>25} {'+20% Impact':>25}")
print("-" * 120)

for _idx, _row in sensitivity_df.iterrows():
    print(f"{_row['driver']:<30} {_row['base_value']:<20} {_row['pct_impact_low']:>+23.1f}% {_row['pct_impact_high']:>+23.1f}%")

print("=" * 120)
print("\nDetailed Results (Y5 ARR):")
print("-" * 120)
for _idx, _row in sensitivity_df.iterrows():
    print(f"{_row['driver']:<30} -20%: £{_row['y5_arr_low']:>18,.0f}  |  +20%: £{_row['y5_arr_high']:>18,.0f}")
print("=" * 120)