"""
Extract Baseline Invoice Finance Parameters
Identifies key baseline parameters from invoice finance revenue model
"""

# Extract invoice finance baseline parameters
baseline_invoice_finance = {
    'product_timeline': {
        'institutional_pilot_start': 18,  # Month 18 (Y2 Q3)
        'institutional_scale_start': 24,  # Month 24 (Y3)
        'p2p_pilot_start': 39,  # Month 39 (Y3 Q4)
        'p2p_scale_start': 48   # Month 48 (Y4)
    },
    'institutional_take_rates': {
        'low_risk': 0.015,   # 1.5%
        'mid_risk': 0.022,   # 2.2%
        'high_risk': 0.030   # 3.0%
    },
    'p2p_platform_fees': {
        'low_risk': 0.020,   # 2.0%
        'mid_risk': 0.030,   # 3.0%
        'high_risk': 0.040   # 4.0%
    },
    'avg_invoice_values': {
        'institutional': 8500,  # £8,500
        'p2p': 3200  # £3,200
    },
    'credit_filters': {
        'max_prob_late_60': 0.15,  # 15% max late probability
        'min_confidence_score': 0.6,  # 60% min confidence
        'model_hit_rate': 0.78,  # 78% coverage
        'credit_limit_coverage': True
    },
    'risk_tier_distribution': {
        'low_risk': 0.40,   # 40%
        'mid_risk': 0.40,   # 40%
        'high_risk': 0.20   # 20%
    },
    'expected_loss_rate': 0.025  # 2.5%
}

print("Baseline Invoice Finance Parameters Extracted")
print(f"\nProduct Timeline:")
for phase, month in baseline_invoice_finance['product_timeline'].items():
    print(f"  {phase}: Month {month}")

print(f"\nInstitutional Take Rates:")
for risk, take_rate in baseline_invoice_finance['institutional_take_rates'].items():
    print(f"  {risk}: {take_rate:.2%}")

print(f"\nP2P Platform Fees:")
for risk, fee in baseline_invoice_finance['p2p_platform_fees'].items():
    print(f"  {risk}: {fee:.2%}")

print(f"\nAverage Invoice Values:")
for inv_type, value in baseline_invoice_finance['avg_invoice_values'].items():
    print(f"  {inv_type}: £{value:,}")

print(f"\nExpected Loss Rate: {baseline_invoice_finance['expected_loss_rate']:.2%}")