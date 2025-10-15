"""
Load Geographic Breakdown CSV File
Extracts geographic distribution data by region
"""
import pandas as pd

# Load the geographic breakdown file
geographic_df = pd.read_csv('geographic_breakdown.csv')

print(f"Geographic Breakdown Data Loaded")
print(f"Shape: {geographic_df.shape}")
print(f"Columns: {list(geographic_df.columns)}")
print(f"\nFirst few rows:")
print(geographic_df.head(3))