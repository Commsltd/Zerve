"""
Load Consolidated Dashboard Excel File
Extracts comprehensive financial data from the master Excel export
"""
import pandas as pd

# Load the consolidated financial exports Excel file
financial_excel = pd.ExcelFile('financial_exports_complete.xlsx')

print(f"Consolidated Dashboard Excel File Loaded")
print(f"Available sheets: {financial_excel.sheet_names}")
print(f"Total sheets: {len(financial_excel.sheet_names)}")

# Load key sheets for analysis
financial_data = {}
for sheet_name in financial_excel.sheet_names:
    financial_data[sheet_name] = pd.read_excel(financial_excel, sheet_name=sheet_name)
    print(f"\nSheet '{sheet_name}': {financial_data[sheet_name].shape}")