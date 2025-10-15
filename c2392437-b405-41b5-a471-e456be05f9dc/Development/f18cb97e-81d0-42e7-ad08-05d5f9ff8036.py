"""
Interactive Parameter Input: Customer Acquisition Cost (CAC) by Segment
Defines the average CAC for different customer acquisition channels/segments
"""

# CAC by Customer Acquisition Channel/Segment (in GBP)
input_cac_stealth_partnerships = 450
input_cac_beta_digital = 1200
input_cac_launch_mixed = 3500
input_cac_enterprise_outbound = 8500

# Package all CAC parameters
cac_segment_inputs = {
    'stealth_partnerships': {
        'avg_cac_gbp': input_cac_stealth_partnerships,
        'description': 'Early-stage warm introductions and partnerships'
    },
    'beta_digital': {
        'avg_cac_gbp': input_cac_beta_digital,
        'description': 'Digital marketing and PLG motion'
    },
    'launch_mixed': {
        'avg_cac_gbp': input_cac_launch_mixed,
        'description': 'Mid-market inside sales and marketing'
    },
    'enterprise_outbound': {
        'avg_cac_gbp': input_cac_enterprise_outbound,
        'description': 'Strategic enterprise field sales'
    }
}

print("✓ CAC by Segment Inputs Configured")
print(f"  Stealth Partnerships: £{input_cac_stealth_partnerships}")
print(f"  Beta Digital: £{input_cac_beta_digital}")
print(f"  Launch Mixed: £{input_cac_launch_mixed}")
print(f"  Enterprise Outbound: £{input_cac_enterprise_outbound}")