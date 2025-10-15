"""
Load Scenario Analysis Excel File
Extracts scenario comparison and sensitivity analysis data
"""
import pandas as pd

# Load the scenario sensitivity analysis Excel file with multiple sheets
scenarios_excel = pd.ExcelFile('scenario_sensitivity_analysis.xlsx')

print(f"Scenario Analysis Excel File Loaded")
print(f"Available sheets: {scenarios_excel.sheet_names}")

# Load each sheet
scenario_sheets = {}
for sheet_name in scenarios_excel.sheet_names:
    scenario_sheets[sheet_name] = pd.read_excel(scenarios_excel, sheet_name=sheet_name)
    print(f"\nSheet '{sheet_name}':")
    print(f"  Shape: {scenario_sheets[sheet_name].shape}")
    print(f"  Columns: {list(scenario_sheets[sheet_name].columns)}")

# Also load the scenario comparison CSV
scenario_comparison_df = pd.read_csv('scenario_comparison_analysis.csv')
print(f"\nScenario Comparison CSV Loaded")
print(f"Shape: {scenario_comparison_df.shape}")
print(scenario_comparison_df)