"""
Load Quarterly and Annual Rollup CSV Files
Extracts aggregated revenue data by quarter and year
"""
import pandas as pd

# Load the quarterly and annual revenue rollup files
quarterly_df = pd.read_csv('quarterly_revenue_rollup.csv')
annual_df = pd.read_csv('annual_revenue_rollup.csv')

print(f"Quarterly Revenue Data Loaded")
print(f"Shape: {quarterly_df.shape}")
print(f"Columns: {list(quarterly_df.columns)}")

print(f"\nAnnual Revenue Data Loaded")
print(f"Shape: {annual_df.shape}")
print(f"Columns: {list(annual_df.columns)}")
print(f"\nAnnual Summary:")
print(annual_df)