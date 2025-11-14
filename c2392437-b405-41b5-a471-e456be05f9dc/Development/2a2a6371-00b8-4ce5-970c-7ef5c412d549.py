"""
Interactive Parameter Input: Invoice Finance Metrics
Discount rates, advance rates, platform fees, and loss provisions
"""

# Institutional Factoring Take Rates (as decimal percentages)
input_inst_low_risk_rate = 0.015  # 1.5%
input_inst_mid_risk_rate = 0.022  # 2.2%
input_inst_high_risk_rate = 0.030  # 3.0%

# P2P Crowd Pool Platform Fees (as decimal percentages)
input_p2p_low_risk_rate = 0.020  # 2.0%
input_p2p_mid_risk_rate = 0.030  # 3.0%
input_p2p_high_risk_rate = 0.040  # 4.0%

# Credit Filters and Risk Parameters
input_max_prob_late_60 = 0.15  # 15% maximum late probability
input_expected_loss_rate = 0.025  # 2.5% expected loss on financed pool

# Average Invoice Values (in GBP)
input_avg_invoice_institutional = 8500
input_avg_invoice_p2p = 3200

# Product Launch Timing (months from start)
input_institutional_pilot_start = 18  # Y2 Q3
input_institutional_scale_start = 24  # Y3
input_p2p_pilot_start = 39  # Y3 Q4
input_p2p_scale_start = 48  # Y4

# Package all invoice finance parameters
invoice_finance_inputs = {
    'institutional_take_rates': {
        'low_risk': input_inst_low_risk_rate,
        'mid_risk': input_inst_mid_risk_rate,
        'high_risk': input_inst_high_risk_rate
    },
    'p2p_platform_fees': {
        'low_risk': input_p2p_low_risk_rate,
        'mid_risk': input_p2p_mid_risk_rate,
        'high_risk': input_p2p_high_risk_rate
    },
    'credit_parameters': {
        'max_prob_late_60': input_max_prob_late_60,
        'expected_loss_rate': input_expected_loss_rate
    },
    'avg_invoice_values': {
        'institutional': input_avg_invoice_institutional,
        'p2p': input_avg_invoice_p2p
    },
    'product_timeline': {
        'institutional_pilot_start': input_institutional_pilot_start,
        'institutional_scale_start': input_institutional_scale_start,
        'p2p_pilot_start': input_p2p_pilot_start,
        'p2p_scale_start': input_p2p_scale_start
    }
}

print("✓ Invoice Finance Inputs Configured")
print(f"  Institutional: {input_inst_low_risk_rate:.1%}-{input_inst_high_risk_rate:.1%}")
print(f"  P2P: {input_p2p_low_risk_rate:.1%}-{input_p2p_high_risk_rate:.1%}")
print(f"  Expected Loss: {input_expected_loss_rate:.1%}")
print(f"  Launch: Inst Y2 Q3 (M{input_institutional_pilot_start}), P2P Y3 Q4 (M{input_p2p_pilot_start})")