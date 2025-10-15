"""
Calculation Engine: Core Parameter Configuration
Pulls parameters from master_parameters or defaults to baseline values
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Accept master_parameters if provided, otherwise use baseline defaults
if 'master_parameters' in dir():
    # Use master parameters
    params = master_parameters
    
    # Extract specific parameter sets
    calc_pricing_tiers = {
        'Starter': params['pricing']['Standard'],  # Map Standard to Starter for calc
        'Growth': params['pricing']['Professional'],  # Map Professional to Growth
        'Scale': params['pricing']['Scale'],
        'Enterprise': params['pricing']['Enterprise']
    }
    
    # Churn rates (lowercase keys for consistency)
    calc_churn_rates = {
        'starter': {'monthly_churn_rate': params['churn']['Standard']['monthly_churn_rate']},
        'growth': {'monthly_churn_rate': params['churn']['Professional']['monthly_churn_rate']},
        'scale': {'monthly_churn_rate': params['churn']['Scale']['monthly_churn_rate']},
        'enterprise': {'monthly_churn_rate': params['churn']['Enterprise']['monthly_churn_rate']}
    }
    
    # Volume assumptions
    calc_volume_assumptions = {
        'customer_density': params['volume_growth']['customer_density_by_segment'],
        'conversion_rates': {
            'starter_to_growth': params['upgrades_and_expansion']['tier_upgrade_rates']['standard_to_professional']['conversion_rate'],
            'growth_to_scale': params['upgrades_and_expansion']['tier_upgrade_rates']['professional_to_scale']['conversion_rate'],
            'scale_to_enterprise': params['upgrades_and_expansion']['tier_upgrade_rates']['scale_to_enterprise']['conversion_rate']
        }
    }
    
    # Token economics
    calc_token_economics = {
        'pricing': {
            'payg_rate_gbp': params['token_economics']['pricing']['payg_rate_gbp'],
            'overage_rate_gbp': params['token_economics']['pricing']['overage_rate_gbp']
        },
        'parameters': {
            'rollover_days': params['token_economics']['pricing']['rollover_days']
        }
    }
    
    # Invoice finance
    calc_invoice_finance = {
        'institutional_take_rates': params['invoice_finance']['institutional_take_rates'],
        'p2p_platform_fees': params['invoice_finance']['p2p_platform_fees'],
        'avg_invoice_values': params['invoice_finance']['avg_invoice_values'],
        'product_timeline': params['invoice_finance']['product_timeline'],
        'credit_parameters': {
            'max_prob_late_60': params['invoice_finance']['credit_filters']['max_prob_late_60'],
            'expected_loss_rate': params['invoice_finance']['loss_provisioning']['expected_loss_rate']
        }
    }
    
    # Regional expansion
    calc_regional_expansion = {
        'multipliers': {
            'uk': params['regional_expansion']['uk']['market_size_multiplier'],
            'eu': params['regional_expansion']['eu']['market_size_multiplier'],
            'us': params['regional_expansion']['us']['market_size_multiplier'],
            'apac': params['regional_expansion']['apac']['market_size_multiplier']
        },
        'timing': {'uk': 1, 'eu': 13, 'us': 25, 'apac': 37}  # Keep timing consistent
    }
    
    # CAC by segment
    calc_cac_segments = {
        'stealth_partnerships': params['cac']['stealth_partnerships']['avg_cac_gbp'],
        'beta_digital': params['cac']['beta_digital']['avg_cac_gbp'],
        'launch_mixed': params['cac']['launch_mixed']['avg_cac_gbp'],
        'enterprise_outbound': params['cac']['enterprise_outbound']['avg_cac_gbp']
    }

else:
    # Use baseline defaults
    calc_pricing_tiers = {
        'Starter': {'monthly_price_gbp': 495, 'included_tokens': 300},
        'Growth': {'monthly_price_gbp': 1895, 'included_tokens': 1250},
        'Scale': {'monthly_price_gbp': 4950, 'included_tokens': 5000},
        'Enterprise': {'monthly_price_gbp': 15000, 'included_tokens': 'custom'}
    }
    
    calc_churn_rates = {
        'starter': {'monthly_churn_rate': 0.035},
        'growth': {'monthly_churn_rate': 0.022},
        'scale': {'monthly_churn_rate': 0.011},
        'enterprise': {'monthly_churn_rate': 0.006}
    }
    
    calc_volume_assumptions = {
        'customer_density': {'micro': 25, 'small': 35, 'medium': 210, 'large': 1325, 'mnc': 23000},
        'conversion_rates': {'starter_to_growth': 0.18, 'growth_to_scale': 0.09, 'scale_to_enterprise': 0.04}
    }
    
    calc_token_economics = {
        'pricing': {'payg_rate_gbp': 2.0, 'overage_rate_gbp': 1.5},
        'parameters': {'rollover_days': 90}
    }
    
    calc_invoice_finance = {
        'institutional_take_rates': {'low_risk': 0.015, 'mid_risk': 0.022, 'high_risk': 0.03},
        'p2p_platform_fees': {'low_risk': 0.02, 'mid_risk': 0.03, 'high_risk': 0.04},
        'avg_invoice_values': {'institutional': 8500, 'p2p': 3200},
        'product_timeline': {'institutional_pilot_start': 18, 'institutional_scale_start': 24, 'p2p_pilot_start': 39, 'p2p_scale_start': 48},
        'credit_parameters': {'max_prob_late_60': 0.15, 'expected_loss_rate': 0.025}
    }
    
    calc_regional_expansion = {
        'multipliers': {'uk': 1.0, 'eu': 2.3, 'us': 4.1, 'apac': 1.8},
        'timing': {'uk': 1, 'eu': 13, 'us': 25, 'apac': 37}
    }
    
    calc_cac_segments = {
        'stealth_partnerships': 450,
        'beta_digital': 1200,
        'launch_mixed': 3500,
        'enterprise_outbound': 8500
    }

# Timeline setup (60 months / 5 years)
calc_start_date = datetime(2025, 1, 1)
calc_months = 60

calc_timeline = pd.DataFrame({
    'month': range(1, calc_months + 1),
    'date': [calc_start_date + timedelta(days=30*i) for i in range(calc_months)],
    'year': [(i // 12) + 1 for i in range(calc_months)],
    'quarter': [((i % 12) // 3) + 1 for i in range(calc_months)]
})

print("✓ Calculation Engine Initialized")
print(f"  Timeline: {calc_months} months ({calc_timeline['year'].max()} years)")
print(f"  Pricing Tiers: {len(calc_pricing_tiers)} configured")
print(f"  Parameters Source: {'master_parameters' if 'master_parameters' in dir() else 'baseline defaults'}")