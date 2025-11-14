"""
Export 5: Write All Export Tables to CSV and Excel
Final step: write all prepared export tables to files
"""
import pandas as pd

# Export to CSV files
export_monthly_revenue.to_csv('monthly_revenue_by_stream.csv', index=False)
export_customers.to_csv('customer_counts_by_tier_segment.csv', index=False)
export_quarterly_revenue.to_csv('quarterly_revenue_rollup.csv', index=False)
export_annual_revenue.to_csv('annual_revenue_rollup.csv', index=False)
export_geographic.to_csv('geographic_breakdown.csv', index=False)

# Also create an Excel workbook with all tables as separate sheets
with pd.ExcelWriter('financial_exports_complete.xlsx', engine='openpyxl') as _writer:
    export_monthly_revenue.to_excel(_writer, sheet_name='Monthly Revenue', index=False)
    export_customers.to_excel(_writer, sheet_name='Customer Counts', index=False)
    export_quarterly_revenue.to_excel(_writer, sheet_name='Quarterly Rollup', index=False)
    export_annual_revenue.to_excel(_writer, sheet_name='Annual Rollup', index=False)
    export_geographic.to_excel(_writer, sheet_name='Geographic Breakdown', index=False)

print("=" * 70)
print("FINANCIAL DATA EXPORT COMPLETE")
print("=" * 70)
print("\n📊 CSV Files Created:")
print("  • monthly_revenue_by_stream.csv (60 months)")
print("  • customer_counts_by_tier_segment.csv (60 months)")
print("  • quarterly_revenue_rollup.csv (20 quarters)")
print("  • annual_revenue_rollup.csv (5 years)")
print("  • geographic_breakdown.csv (60 months)")
print("\n📁 Excel File Created:")
print("  • financial_exports_complete.xlsx (5 sheets)")
print("\n✓ All revenue tables exported successfully")
print(f"  60-month P&L summary included in all exports")
print("=" * 70)
