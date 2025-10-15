"""
Attachment Rate Growth Curve
Models % of eligible invoices financed from 5% (Y2 pilot) to 25% (Y5)
Growth driven by RTCI predictive accuracy proof and institutional trust building
"""
import pandas as pd
import numpy as np

# Attachment rate targets by year
attachment_targets = {
    'y2_pilot': 0.05,   # 5% at institutional pilot start (month 18)
    'y2_end': 0.08,     # 8% by end of Y2
    'y3': 0.12,         # 12% by end of Y3 (product proven)
    'y4': 0.18,         # 18% by end of Y4 (P2P adds volume)
    'y5': 0.25          # 25% by end of Y5 (mature market)
}

# Build attachment rate curve for each month
attachment_rates_df = pd.DataFrame({
    'month': eligible_invoices_df['month'],
    'year': eligible_invoices_df['year']
})

# Define attachment rate by month
def get_attachment_rate_by_month(month_num):
    """Calculate attachment rate for given month"""
    if month_num < product_timeline['institutional_pilot_start']:
        # Before institutional pilot
        return 0.0
    elif month_num < 24:  # Y2
        # Ramp from 5% at month 18 to 8% at month 24
        _months_since_start = month_num - product_timeline['institutional_pilot_start']
        _ramp_months = 24 - product_timeline['institutional_pilot_start']
        _progress = _months_since_start / _ramp_months
        return attachment_targets['y2_pilot'] + (attachment_targets['y2_end'] - attachment_targets['y2_pilot']) * _progress
    elif month_num < 36:  # Y3
        # Ramp from 8% to 12%
        _progress = (month_num - 24) / 12
        return attachment_targets['y2_end'] + (attachment_targets['y3'] - attachment_targets['y2_end']) * _progress
    elif month_num < 48:  # Y4
        # Ramp from 12% to 18% (P2P boost)
        _progress = (month_num - 36) / 12
        return attachment_targets['y3'] + (attachment_targets['y4'] - attachment_targets['y3']) * _progress
    else:  # Y5
        # Ramp from 18% to 25%
        _progress = (month_num - 48) / 12
        return attachment_targets['y4'] + (attachment_targets['y5'] - attachment_targets['y4']) * _progress

attachment_rates_df['institutional_attachment_rate'] = [
    get_attachment_rate_by_month(m) for m in attachment_rates_df['month']
]

# P2P attachment rate (starts at month 39, Y3 Q4)
def get_p2p_attachment_rate(month_num):
    """P2P product attachment rate"""
    if month_num < product_timeline['p2p_pilot_start']:
        return 0.0
    elif month_num < product_timeline['p2p_scale_start']:
        # Pilot phase: 3% attachment
        return 0.03
    else:
        # Scale phase: ramp from 3% to 8% by Y5 end
        _months_since_scale = month_num - product_timeline['p2p_scale_start']
        _progress = min(1.0, _months_since_scale / 12)
        return 0.03 + (0.08 - 0.03) * _progress

attachment_rates_df['p2p_attachment_rate'] = [
    get_p2p_attachment_rate(m) for m in attachment_rates_df['month']
]

# Combined attachment rate
attachment_rates_df['total_attachment_rate'] = (
    attachment_rates_df['institutional_attachment_rate'] + 
    attachment_rates_df['p2p_attachment_rate']
)

print("Attachment Rate Curves Built")
print(f"\nMonth 18 (Y2 Q3 - Institutional Pilot): {attachment_rates_df.loc[17, 'institutional_attachment_rate']:.1%}")
print(f"Month 24 (Y2 End): {attachment_rates_df.loc[23, 'total_attachment_rate']:.1%}")
print(f"Month 36 (Y3 End): {attachment_rates_df.loc[35, 'total_attachment_rate']:.1%}")
print(f"Month 39 (Y3 Q4 - P2P Pilot): Inst {attachment_rates_df.loc[38, 'institutional_attachment_rate']:.1%} + P2P {attachment_rates_df.loc[38, 'p2p_attachment_rate']:.1%}")
print(f"Month 48 (Y4 End): {attachment_rates_df.loc[47, 'total_attachment_rate']:.1%}")
print(f"Month 60 (Y5 End): {attachment_rates_df.loc[59, 'total_attachment_rate']:.1%}")