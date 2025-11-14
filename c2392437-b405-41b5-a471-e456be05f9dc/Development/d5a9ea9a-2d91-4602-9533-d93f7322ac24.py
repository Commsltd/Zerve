"""
Base Parameters for Invoice Finance Revenue Modeling
Defines take rates, product timelines, partnership economics
"""
import numpy as np
import pandas as pd

# Product launch timelines (in months from start)
product_timeline = {
    'institutional_pilot_start': 18,  # Y2 Q3
    'institutional_scale_start': 24,  # Y3
    'p2p_pilot_start': 39,  # Y3 Q4
    'p2p_scale_start': 48   # Y4
}

# Risk-tiered take rates for institutional factoring
institutional_take_rates = {
    'low_risk': {
        'rate': 0.015,  # 1.5%
        'criteria': 'prob_late_60 < 10%',
        'description': 'Highest quality debtors'
    },
    'mid_risk': {
        'rate': 0.022,  # 2.2%
        'criteria': '10% <= prob_late_60 < 15%',
        'description': 'Medium risk debtors'
    },
    'high_risk': {
        'rate': 0.030,  # 3.0%
        'criteria': '15% <= prob_late_60 < 20%',
        'description': 'Higher risk but acceptable'
    }
}

# Risk-tiered platform fees for P2P crowd pool
p2p_platform_fees = {
    'low_risk': {
        'rate': 0.020,  # 2.0%
        'criteria': 'prob_late_60 < 10%',
        'description': 'Highest quality debtors'
    },
    'mid_risk': {
        'rate': 0.030,  # 3.0%
        'criteria': '10% <= prob_late_60 < 15%',
        'description': 'Medium risk debtors'
    },
    'high_risk': {
        'rate': 0.040,  # 4.0%
        'criteria': '15% <= prob_late_60 < 20%',
        'description': 'Higher risk but acceptable'
    }
}

# Average invoice values by product type
avg_invoice_values = {
    'institutional': 8500,  # £8,500 for supply chain factoring
    'p2p': 3200  # £3,200 for SME crowd pool
}

# Credit quality filters (eligibility criteria)
credit_filters = {
    'max_prob_late_60': 0.15,  # 15% max late probability (excludes >15%)
    'min_confidence_score': 0.6,  # Consensus confidence >0.6
    'model_hit_rate': 0.78,  # 78% coverage
    'credit_limit_coverage': True  # recommended_credit_limit > invoice_amount
}

# Risk tier distribution (% of eligible invoices in each band)
risk_tier_distribution = {
    'low_risk': 0.40,   # 40% in <10% prob_late
    'mid_risk': 0.40,   # 40% in 10-15% range
    'high_risk': 0.20   # 20% in 15-20% range (note: >20% excluded by filters)
}

# Partnership economics (Y2-Y3 institutional product)
partnership_terms = {
    'first_loss_insurance': {
        'provider': 'Trade credit insurers',
        'coverage': 0.10,  # Covers bottom 10% losses
        'cost_bps': 50,  # 50 bps of financed volume
        'timing': 'Y2-Y3'
    },
    'co_investment': {
        'provider': 'Insurance partners',
        'capital_split': 0.50,  # 50/50 capital split
        'timing': 'Y2-Y3'
    }
}

# Expected loss provisioning
loss_provisions = {
    'expected_loss_rate': 0.025,  # 2.5% expected loss on financed pool
    'basis': 'Model calibration on historical data',
    'confidence': 'Based on AUC >0.80, KS >0.40'
}

# FCA Art 36H compliance for P2P
fca_compliance = {
    'regulation': 'FCA Article 36H',
    'pilot_timing': 'Y3 Q4',
    'requirements': 'P2P platform authorization'
}

print("Invoice Finance Base Parameters Loaded")
print(f"Products: Institutional (Y2 Q3), P2P Crowd (Y3 Q4)")
print(f"Institutional rates: {institutional_take_rates['low_risk']['rate']:.1%} - {institutional_take_rates['high_risk']['rate']:.1%}")
print(f"P2P rates: {p2p_platform_fees['low_risk']['rate']:.1%} - {p2p_platform_fees['high_risk']['rate']:.1%}")
print(f"Expected loss provision: {loss_provisions['expected_loss_rate']:.1%}")