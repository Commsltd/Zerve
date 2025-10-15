"""
Interactive Toggle Between Scenarios
Allows users to instantly switch between different parameter sets and see impacts
"""
import pandas as pd

# Create scenario selector function
def show_scenario_details(scenario_name='base'):
    """Display detailed breakdown for a selected scenario"""
    selected = comparison_df[comparison_df['scenario'] == scenario_name.title()].iloc[0]
    
    print("=" * 100)
    print(f"SCENARIO: {selected['scenario'].upper()}")
    print("=" * 100)
    print(f"\nDescription: {selected['description']}")
    print(f"\nBreakeven: Month {selected['breakeven_month']}")
    print(f"ARR CAGR (Y1-Y5): {selected['arr_cagr_pct']:.1f}%")
    print(f"\nAnnual ARR Progression:")
    print(f"  Year 1: £{selected['y1_arr_gbp']:>18,.0f}")
    print(f"  Year 2: £{selected['y2_arr_gbp']:>18,.0f}")
    print(f"  Year 3: £{selected['y3_arr_gbp']:>18,.0f}")
    print(f"  Year 4: £{selected['y4_arr_gbp']:>18,.0f}")
    print(f"  Year 5: £{selected['y5_arr_gbp']:>18,.0f}")
    print(f"\nTotal 5-Year Revenue: £{selected['total_5y_revenue_gbp']:,.0f}")
    
    if selected['scenario'] != 'Base':
        print(f"\nVariance vs Base Case:")
        print(f"  Y5 ARR: {selected['y5_variance_vs_base_pct']:+.1f}%")
        print(f"  Total Revenue: {selected['total_revenue_variance_vs_base_pct']:+.1f}%")
    
    print("=" * 100)

# Display all three scenarios for comparison
print("INTERACTIVE SCENARIO TOGGLE VIEW\n")
print("Toggle between scenarios to see instant impact:")
print("\n" + "─" * 100)

# Show Conservative
show_scenario_details('conservative')
print("\n")

# Show Base
show_scenario_details('base')
print("\n")

# Show Accelerated
show_scenario_details('accelerated')

# Create quick comparison table
print("\n\n" + "=" * 100)
print("QUICK SCENARIO TOGGLE - KEY METRICS")
print("=" * 100)
print(f"\n{'Metric':<30} {'Conservative':>20} {'Base':>20} {'Accelerated':>20}")
print("─" * 100)

conservative_data = comparison_df[comparison_df['scenario'] == 'Conservative'].iloc[0]
base_data = comparison_df[comparison_df['scenario'] == 'Base'].iloc[0]
accelerated_data = comparison_df[comparison_df['scenario'] == 'Accelerated'].iloc[0]

print(f"{'Y5 ARR':<30} £{conservative_data['y5_arr_gbp']:>18,.0f} £{base_data['y5_arr_gbp']:>18,.0f} £{accelerated_data['y5_arr_gbp']:>18,.0f}")
print(f"{'Total 5Y Revenue':<30} £{conservative_data['total_5y_revenue_gbp']:>18,.0f} £{base_data['total_5y_revenue_gbp']:>18,.0f} £{accelerated_data['total_5y_revenue_gbp']:>18,.0f}")
print(f"{'Breakeven Month':<30} {conservative_data['breakeven_month']:>20} {base_data['breakeven_month']:>20} {accelerated_data['breakeven_month']:>20}")
print(f"{'ARR CAGR (Y1-Y5)':<30} {conservative_data['arr_cagr_pct']:>18.1f}% {base_data['arr_cagr_pct']:>18.1f}% {accelerated_data['arr_cagr_pct']:>18.1f}%")
print(f"{'Y5 Variance vs Base':<30} {conservative_data['y5_variance_vs_base_pct']:>18.1f}% {'Baseline':>20} {accelerated_data['y5_variance_vs_base_pct']:>18.1f}%")

print("=" * 100)
print("\n✓ Interactive scenario toggle view ready")
print("  Users can instantly compare parameter impacts across all three scenarios")
