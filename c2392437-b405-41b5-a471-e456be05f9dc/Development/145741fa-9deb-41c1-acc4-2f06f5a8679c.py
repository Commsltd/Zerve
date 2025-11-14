"""
Export Scenario Comparison and Sensitivity Analysis Tables
Creates CSV and Excel exports for decision-making
"""
import pandas as pd
import numpy as np

# SCENARIO COMPARISON EXPORT
scenario_export = scenario_comparison_df[['scenario', 'description', 'y1_arr', 'y2_arr', 'y3_arr', 
                                          'y4_arr', 'y5_arr', 'total_revenue_60m', 'breakeven_month']].copy()

# Format for readability
scenario_export_formatted = scenario_export.copy()
scenario_export_formatted.columns = ['Scenario', 'Description', 'Y1 ARR (£)', 'Y2 ARR (£)', 'Y3 ARR (£)', 
                                     'Y4 ARR (£)', 'Y5 ARR (£)', 'Total 5Y Revenue (£)', 'Breakeven Month']

# Calculate variance from base case
base_y5_arr_val = scenario_comparison_df[scenario_comparison_df['scenario'] == 'base']['y5_arr'].iloc[0]
base_total_rev_val = scenario_comparison_df[scenario_comparison_df['scenario'] == 'base']['total_revenue_60m'].iloc[0]

scenario_export_formatted['Y5 ARR vs Base (%)'] = (
    (scenario_export['y5_arr'] / base_y5_arr_val - 1) * 100
).round(1)
scenario_export_formatted['Total Revenue vs Base (%)'] = (
    (scenario_export['total_revenue_60m'] / base_total_rev_val - 1) * 100
).round(1)

# SENSITIVITY ANALYSIS EXPORT
sensitivity_export = sensitivity_df[['driver', 'base_value', 'pct_impact_low', 'pct_impact_high']].copy()
sensitivity_export.columns = ['Driver', 'Base Value', 'Impact at -20% (%)', 'Impact at +20% (%)']
sensitivity_export['Sensitivity Score'] = (
    (abs(sensitivity_export['Impact at -20% (%)']) + abs(sensitivity_export['Impact at +20% (%)'])) / 2
).round(1)

# Sort by sensitivity (most impactful first)
sensitivity_export = sensitivity_export.sort_values('Sensitivity Score', ascending=False)

# Write to CSV files
scenario_export_formatted.to_csv('scenario_comparison_analysis.csv', index=False)
sensitivity_export.to_csv('sensitivity_analysis_drivers.csv', index=False)

# Create combined Excel export with multiple sheets
with pd.ExcelWriter('scenario_sensitivity_analysis.xlsx', engine='openpyxl') as writer:
    scenario_export_formatted.to_excel(writer, sheet_name='Scenarios', index=False)
    sensitivity_export.to_excel(writer, sheet_name='Sensitivity', index=False)
    
    # Add detailed sensitivity results
    sensitivity_detailed = sensitivity_df.copy()
    sensitivity_detailed.columns = ['Driver', 'Base Value', 'Change Low', 'Y5 ARR Low (£)', 
                                    'Total Rev Low (£)', 'Impact Low (%)', 'Change High', 
                                    'Y5 ARR High (£)', 'Total Rev High (£)', 'Impact High (%)']
    sensitivity_detailed.to_excel(writer, sheet_name='Sensitivity Detail', index=False)

print("✓ Scenario and sensitivity analysis exports created successfully")
print(f"\nFiles created:")
print("  • scenario_comparison_analysis.csv")
print("  • sensitivity_analysis_drivers.csv")
print("  • scenario_sensitivity_analysis.xlsx (3 sheets)")
print(f"\nScenario Summary:")
print(f"  Conservative Y5 ARR: £{scenario_export['y5_arr'].iloc[0]:,.0f}")
print(f"  Base Y5 ARR:         £{scenario_export['y5_arr'].iloc[1]:,.0f}")
print(f"  Accelerated Y5 ARR:  £{scenario_export['y5_arr'].iloc[2]:,.0f}")
print(f"\nTop 3 Most Sensitive Drivers:")
for _idx, _row in sensitivity_export.head(3).iterrows():
    print(f"  {_idx+1}. {_row['Driver']}: {_row['Sensitivity Score']:.1f}% avg impact")