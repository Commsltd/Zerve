"""
Load Sensitivity Analysis Drivers CSV
Extracts driver sensitivity data
"""
import pandas as pd

# Load the sensitivity analysis drivers file
sensitivity_drivers_df = pd.read_csv('sensitivity_analysis_drivers.csv')

print(f"Sensitivity Analysis Drivers Loaded")
print(f"Shape: {sensitivity_drivers_df.shape}")
print(sensitivity_drivers_df)