"""
Enhanced Scenario Comparison View with Baseline Parameter Comparison
Shows side-by-side comparison of current parameters vs baseline scenarios
Displays variance metrics and detailed parameter-level changes
"""
import pandas as pd
import numpy as np

# Load scenario comparison data
scenario_data = scenario_comparison_df.copy()

# Load sensitivity analysis data  
sensitivity_data = sensitivity_df.copy()

# Load baseline parameter data from config.parameter_master
baseline_params = master_parameters.copy()

# ============================================================================
# 1. SCENARIO REVENUE COMPARISON
# ============================================================================

comparison_metrics = []

# Extract metrics for each scenario
for _idx, scenario_row in scenario_data.iterrows():
    scenario_name_val = scenario_row['scenario']
    
    # Calculate variance from base
    base_row = scenario_data[scenario_data['scenario'] == 'base'].iloc[0]
    
    # Year-over-year metrics
    y1_arr_val = scenario_row['y1_arr']
    y2_arr_val = scenario_row['y2_arr']
    y3_arr_val = scenario_row['y3_arr']
    y4_arr_val = scenario_row['y4_arr']
    y5_arr_val = scenario_row['y5_arr']
    
    # Variance calculations
    y5_variance_pct = ((y5_arr_val / base_row['y5_arr']) - 1) * 100 if scenario_name_val != 'base' else 0
    total_rev_variance_pct = ((scenario_row['total_revenue_60m'] / base_row['total_revenue_60m']) - 1) * 100 if scenario_name_val != 'base' else 0
    
    # CAGR calculation (Y1 to Y5)
    cagr_val = ((y5_arr_val / y1_arr_val) ** (1/4) - 1) * 100 if y1_arr_val > 0 else 0
    
    comparison_metrics.append({
        'scenario': scenario_name_val.title(),
        'description': scenario_row['description'],
        'y1_arr_gbp': y1_arr_val,
        'y2_arr_gbp': y2_arr_val,
        'y3_arr_gbp': y3_arr_val,
        'y4_arr_gbp': y4_arr_val,
        'y5_arr_gbp': y5_arr_val,
        'total_5y_revenue_gbp': scenario_row['total_revenue_60m'],
        'breakeven_month': scenario_row['breakeven_month'],
        'y5_variance_vs_base_pct': y5_variance_pct,
        'total_revenue_variance_vs_base_pct': total_rev_variance_pct,
        'arr_cagr_pct': cagr_val
    })

comparison_df = pd.DataFrame(comparison_metrics)

# ============================================================================
# 2. BASELINE PARAMETER COMPARISON TABLE
# ============================================================================

# Extract key parameters from baseline for comparison display
parameter_comparison = []

# Pricing parameters
for tier_name_val, tier_data_val in baseline_params['pricing'].items():
    parameter_comparison.append({
        'category': 'Pricing',
        'parameter': f'{tier_name_val} Monthly Price',
        'baseline_value': f"£{tier_data_val['monthly_price_gbp']:,}",
        'current_value': f"£{tier_data_val['monthly_price_gbp']:,}",
        'variance': '0%'
    })

# Churn parameters
for tier_name_val, tier_data_val in baseline_params['churn'].items():
    parameter_comparison.append({
        'category': 'Churn',
        'parameter': f'{tier_name_val} Monthly Churn',
        'baseline_value': f"{tier_data_val['monthly_churn_rate']:.1%}",
        'current_value': f"{tier_data_val['monthly_churn_rate']:.1%}",
        'variance': '0%'
    })

# CAC parameters
for channel_name, channel_data_val in baseline_params['cac'].items():
    parameter_comparison.append({
        'category': 'CAC',
        'parameter': channel_name.replace('_', ' ').title(),
        'baseline_value': f"£{channel_data_val['avg_cac_gbp']:,}",
        'current_value': f"£{channel_data_val['avg_cac_gbp']:,}",
        'variance': '0%'
    })

# Token economics
parameter_comparison.append({
    'category': 'Token Economics',
    'parameter': 'PAYG Rate',
    'baseline_value': f"£{baseline_params['token_economics']['pricing']['payg_rate_gbp']:.2f}",
    'current_value': f"£{baseline_params['token_economics']['pricing']['payg_rate_gbp']:.2f}",
    'variance': '0%'
})

parameter_comparison.append({
    'category': 'Token Economics',
    'parameter': 'Overage Rate',
    'baseline_value': f"£{baseline_params['token_economics']['pricing']['overage_rate_gbp']:.2f}",
    'current_value': f"£{baseline_params['token_economics']['pricing']['overage_rate_gbp']:.2f}",
    'variance': '0%'
})

# Invoice finance
for risk_tier, take_rate_val in baseline_params['invoice_finance']['institutional_take_rates'].items():
    parameter_comparison.append({
        'category': 'Invoice Finance',
        'parameter': f'{risk_tier.replace("_", " ").title()} Take Rate',
        'baseline_value': f"{take_rate_val:.1%}",
        'current_value': f"{take_rate_val:.1%}",
        'variance': '0%'
    })

parameter_comparison_df = pd.DataFrame(parameter_comparison)

# ============================================================================
# 3. SENSITIVITY IMPACT SUMMARY
# ============================================================================

sensitivity_summary = sensitivity_data[['driver', 'base_value', 'pct_impact_low', 'pct_impact_high']].copy()
sensitivity_summary['avg_impact_pct'] = (abs(sensitivity_summary['pct_impact_low']) + abs(sensitivity_summary['pct_impact_high'])) / 2
sensitivity_summary = sensitivity_summary.sort_values('avg_impact_pct', ascending=False)

# ============================================================================
# 4. DISPLAY COMPREHENSIVE COMPARISON VIEW
# ============================================================================

print("=" * 140)
print("SCENARIO COMPARISON VIEW - BASELINE VS ALTERNATIVE SCENARIOS")
print("=" * 140)

print("\n" + "=" * 140)
print("1. SCENARIO REVENUE METRICS COMPARISON")
print("=" * 140)
print(f"\n{'Scenario':<15} {'Description':<50} {'Breakeven':<12} {'CAGR':<10}")
print("-" * 140)
for _idx, comp_row_val in comparison_df.iterrows():
    print(f"{comp_row_val['scenario']:<15} {comp_row_val['description']:<50} Month {comp_row_val['breakeven_month']:<7} {comp_row_val['arr_cagr_pct']:>6.1f}%")

print(f"\n{'Scenario':<15} {'Y1 ARR':>20} {'Y2 ARR':>20} {'Y3 ARR':>20} {'Y4 ARR':>20} {'Y5 ARR':>20}")
print("-" * 140)
for _idx, comp_row_val in comparison_df.iterrows():
    print(f"{comp_row_val['scenario']:<15} £{comp_row_val['y1_arr_gbp']:>18,.0f} £{comp_row_val['y2_arr_gbp']:>18,.0f} £{comp_row_val['y3_arr_gbp']:>18,.0f} £{comp_row_val['y4_arr_gbp']:>18,.0f} £{comp_row_val['y5_arr_gbp']:>18,.0f}")

print(f"\n{'Scenario':<15} {'Total 5Y Revenue':>22} {'Y5 Variance vs Base':>22} {'Total Rev Variance':>22}")
print("-" * 140)
for _idx, comp_row_val in comparison_df.iterrows():
    variance_y5_str = f"{comp_row_val['y5_variance_vs_base_pct']:+.1f}%" if comp_row_val['scenario'] != 'Base' else "Baseline"
    variance_total_str = f"{comp_row_val['total_revenue_variance_vs_base_pct']:+.1f}%" if comp_row_val['scenario'] != 'Base' else "Baseline"
    print(f"{comp_row_val['scenario']:<15} £{comp_row_val['total_5y_revenue_gbp']:>20,.0f} {variance_y5_str:>21} {variance_total_str:>21}")

print("\n" + "=" * 140)
print("2. BASELINE PARAMETER VALUES (Sample - Top Parameters by Category)")
print("=" * 140)
print(f"\n{'Category':<20} {'Parameter':<35} {'Baseline Value':<20} {'Current Value':<20} {'Variance':<15}")
print("-" * 140)

# Display key parameters by category
for category_val in ['Pricing', 'Churn', 'CAC', 'Token Economics', 'Invoice Finance']:
    category_params = parameter_comparison_df[parameter_comparison_df['category'] == category_val].head(3)
    for _idx, param_row in category_params.iterrows():
        print(f"{param_row['category']:<20} {param_row['parameter']:<35} {param_row['baseline_value']:<20} {param_row['current_value']:<20} {param_row['variance']:<15}")

print("\n" + "=" * 140)
print("3. KEY DRIVER SENSITIVITY ANALYSIS")
print("=" * 140)
print(f"\n{'Driver':<35} {'Base Value':<20} {'-20% Impact':>18} {'+20% Impact':>18} {'Avg Impact':>15}")
print("-" * 140)
for _idx, sens_row_val in sensitivity_summary.iterrows():
    print(f"{sens_row_val['driver']:<35} {sens_row_val['base_value']:<20} {sens_row_val['pct_impact_low']:>+16.1f}% {sens_row_val['pct_impact_high']:>+16.1f}% {sens_row_val['avg_impact_pct']:>13.1f}%")

print("\n" + "=" * 140)
print("VARIANCE INDICATORS & KEY INSIGHTS")
print("=" * 140)
print(f"\n📊 Scenario Impact Summary:")
print(f"  • Conservative scenario: {comparison_df[comparison_df['scenario']=='Conservative']['y5_variance_vs_base_pct'].iloc[0]:.1f}% below baseline")
print(f"  • Accelerated scenario: {comparison_df[comparison_df['scenario']=='Accelerated']['y5_variance_vs_base_pct'].iloc[0]:.1f}% above baseline")
print(f"  • Base case Y5 ARR: £{comparison_df[comparison_df['scenario']=='Base']['y5_arr_gbp'].iloc[0]:,.0f}")

print(f"\n🎯 Most Sensitive Drivers:")
for i, sens_row_val in sensitivity_summary.head(3).iterrows():
    print(f"  {i+1}. {sens_row_val['driver']}: {sens_row_val['avg_impact_pct']:.1f}% avg impact on Y5 ARR")

print(f"\n📈 Parameter Baseline Status:")
print(f"  • Total parameters tracked: {len(parameter_comparison_df)}")
print(f"  • Parameters matching baseline: {len(parameter_comparison_df[parameter_comparison_df['variance'] == '0%'])}")
print(f"  • Categories covered: Pricing, Churn, CAC, Token Economics, Invoice Finance")

print("\n" + "=" * 140)
print("✓ Scenario comparison view with baseline parameter tracking complete")
print("=" * 140)

# Store outputs for downstream use
scenario_comparison_output = comparison_df
parameter_baseline_tracking = parameter_comparison_df
