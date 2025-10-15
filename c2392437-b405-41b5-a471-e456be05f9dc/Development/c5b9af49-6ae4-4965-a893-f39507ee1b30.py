"""
Interactive Parameter Input: Regional Expansion Coefficients
Market size multipliers for geographic expansion
"""

# Geographic Market Size Multipliers (relative to UK baseline of 1.0)
input_uk_market_multiplier = 1.0
input_eu_market_multiplier = 2.3
input_us_market_multiplier = 4.1
input_apac_market_multiplier = 1.8

# Geographic Expansion Timing (in years)
input_uk_timing = 1
input_eu_timing = 2
input_us_timing = 3
input_apac_timing_start = 4

# Package all regional expansion parameters
regional_expansion_inputs = {
    'market_multipliers': {
        'uk': input_uk_market_multiplier,
        'eu': input_eu_market_multiplier,
        'us': input_us_market_multiplier,
        'apac': input_apac_market_multiplier
    },
    'timing': {
        'uk': input_uk_timing,
        'eu': input_eu_timing,
        'us': input_us_timing,
        'apac': input_apac_timing_start
    }
}

print("✓ Regional Expansion Inputs Configured")
print(f"  UK: {input_uk_market_multiplier}x (Y{input_uk_timing})")
print(f"  EU: {input_eu_market_multiplier}x (Y{input_eu_timing})")
print(f"  US: {input_us_market_multiplier}x (Y{input_us_timing})")
print(f"  APAC: {input_apac_market_multiplier}x (Y{input_apac_timing_start}+)")