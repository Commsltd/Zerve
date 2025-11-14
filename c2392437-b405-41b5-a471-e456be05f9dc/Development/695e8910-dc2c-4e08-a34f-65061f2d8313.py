"""
Load Revenue Streams CSV File
Extracts monthly revenue data by stream from exported CSV file
"""
import pandas as pd

# Load the monthly revenue by stream file
revenue_streams_df = pd.read_csv('monthly_revenue_by_stream.csv')

print(f"Revenue Streams Data Loaded")
print(f"Shape: {revenue_streams_df.shape}")
print(f"Columns: {list(revenue_streams_df.columns)}")
print(f"\nFirst few rows:")
print(revenue_streams_df.head(3))