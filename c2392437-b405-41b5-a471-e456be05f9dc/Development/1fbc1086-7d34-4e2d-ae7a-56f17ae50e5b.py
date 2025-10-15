"""
Interactive Parameter Input: Volume Assumptions
Customer density and conversion funnel rates
"""

# Customer Density (average customers/debtors per account by company size)
input_density_micro = 25
input_density_small = 35
input_density_medium = 210
input_density_large = 1325
input_density_mnc = 23000

# Conversion Funnel Rates (as decimal percentages)
input_conv_free_to_starter = 0.12  # 12%
input_conv_starter_to_growth = 0.18  # 18%
input_conv_growth_to_scale = 0.09  # 9%
input_conv_scale_to_enterprise = 0.04  # 4%

# Package all volume parameters
volume_assumption_inputs = {
    'customer_density': {
        'micro': input_density_micro,
        'small': input_density_small,
        'medium': input_density_medium,
        'large': input_density_large,
        'mnc': input_density_mnc
    },
    'conversion_rates': {
        'free_to_starter': input_conv_free_to_starter,
        'starter_to_growth': input_conv_starter_to_growth,
        'growth_to_scale': input_conv_growth_to_scale,
        'scale_to_enterprise': input_conv_scale_to_enterprise
    }
}

print("✓ Volume Assumption Inputs Configured")
print(f"Customer Density: Micro={input_density_micro}, Large={input_density_large}, MNC={input_density_mnc}")
print(f"Conversions: S→G={input_conv_starter_to_growth:.0%}, G→S={input_conv_growth_to_scale:.0%}")