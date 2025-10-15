"""
Interactive Parameter Input: Token Economics
Token pricing, overage rates, and rollover policies
"""

# Token Pricing (in GBP)
input_payg_rate = 2.00  # Pay-as-you-go rate per token
input_overage_rate = 1.50  # Overage rate per token beyond plan allocation
input_rollover_days = 90  # Token rollover period in days

# Token Burn Rates (consumption rates)
input_search_tokens_per_query = 1
input_monitor_tokens_per_entity_month = 1
input_ai_report_tokens = 10

# Package all token economics parameters
token_economics_inputs = {
    'pricing': {
        'payg_rate_gbp': input_payg_rate,
        'overage_rate_gbp': input_overage_rate,
        'rollover_days': input_rollover_days
    },
    'burn_rates': {
        'search_per_query': input_search_tokens_per_query,
        'monitor_per_entity_per_month': input_monitor_tokens_per_entity_month,
        'ai_report_generation': input_ai_report_tokens
    }
}

print("✓ Token Economics Inputs Configured")
print(f"  PAYG Rate: £{input_payg_rate}/token")
print(f"  Overage Rate: £{input_overage_rate}/token")
print(f"  Rollover: {input_rollover_days} days")
print(f"  Burn Rates: Search={input_search_tokens_per_query}, Monitor={input_monitor_tokens_per_entity_month}, Report={input_ai_report_tokens}")