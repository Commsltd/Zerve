"""
Load Customer Counts CSV File
Extracts customer count data by tier and segment
"""
import pandas as pd

# Load the customer counts by tier and segment file
customer_counts_df = pd.read_csv('customer_counts_by_tier_segment.csv')

print(f"Customer Counts Data Loaded")
print(f"Shape: {customer_counts_df.shape}")
print(f"Columns: {list(customer_counts_df.columns)}")
print(f"\nFirst few rows:")
print(customer_counts_df.head(3))