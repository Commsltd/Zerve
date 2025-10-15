"""
Token Economics Model
Source: Schema commercial assumptions - token pricing, overage, rollover, and burn rates
"""

token_economics = {
    'pricing': {
        'payg_rate_gbp': 2.00,  # Pay-as-you-go rate per token
        'overage_rate_gbp': 1.50,  # Rate for tokens beyond plan allocation
        'rollover_days': 90,  # Token rollover period
        'rollover_policy': 'Unused tokens roll over for 90 days'
    },
    'burn_rates': {
        'search_per_query': 1,  # Tokens consumed per search query
        'monitor_per_entity_per_month': 1,  # Monthly token cost per monitored entity
        'ai_report_generation': 10,  # Tokens consumed per AI-generated report
        'description': 'Token consumption rates by activity type'
    },
    'usage_patterns': {
        'typical_starter_monthly': 250,  # Typical usage for Starter tier
        'typical_growth_monthly': 1100,  # Typical usage for Growth tier
        'typical_scale_monthly': 4500,  # Typical usage for Scale tier
        'description': 'Expected monthly token consumption by tier'
    }
}

print("Token Economics Model Defined")
print(f"PAYG Rate: £{token_economics['pricing']['payg_rate_gbp']}/token")
print(f"Overage Rate: £{token_economics['pricing']['overage_rate_gbp']}/token")
print(f"Rollover Period: {token_economics['pricing']['rollover_days']} days")
print("\nToken Burn Rates:")
print(f"  Search: {token_economics['burn_rates']['search_per_query']} token/query")
print(f"  Monitor: {token_economics['burn_rates']['monitor_per_entity_per_month']} token/entity/month")
print(f"  AI Report: {token_economics['burn_rates']['ai_report_generation']} tokens/report")